import os
import sys
import asyncio
import logging
import threading
from typing import Optional

from gitpod import Gitpod, AsyncGitpod
import gitpod.lib as util
from gitpod.types.environment_spec_param import EnvironmentSpecParam
from gitpod.types.environment_initializer_param import Spec
import mcp.server.stdio
import mcp.types as types
from mcp.server import NotificationOptions, Server
from mcp.server.models import InitializationOptions

# Configure logging with more detailed format
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - [%(threadName)s] %(message)s',
    handlers=[
        logging.FileHandler("gitpod_mcp.log", mode='a'),  # 'a' for append mode
        logging.StreamHandler()
    ]
)

# Add a logger instance for the module
logger = logging.getLogger(__name__)

# Define available tools
tools = [
    "get-identity",
    "create-environment",
    "create-environment-with-command"
]

# Create the server instance
server = Server("gitpod-mcp")

class GitpodMCPServer:
    def __init__(self):
        self.client = None
        self._setup_client()

    def _setup_client(self):
        # Get API key from environment variables
        self.gitpod_api_key = os.environ.get('GITPOD_API_KEY')

        # Log environment variables (excluding sensitive data)
        env_vars = {k: '***' if 'API_KEY' in k else v for k, v in dict(os.environ).items()}
        logger.info(f"Environment variables: {env_vars}")

        if not self.gitpod_api_key:
            # Try to load from claude_desktop_config.json as fallback
            config_path = os.path.expanduser("~/Library/Application Support/Claude/claude_desktop_config.json")
            try:
                import json
                with open(config_path) as f:
                    config = json.load(f)
                    self.gitpod_api_key = config["mcpServers"]["gitpod-mcp"]["env"]["GITPOD_API_KEY"]
                    logger.info("Successfully loaded API key from claude_desktop_config.json")
            except FileNotFoundError:
                logger.error(f"Config file not found at {config_path}")
                raise ValueError("GITPOD_API_KEY not found in environment or config file")
            except KeyError as e:
                logger.error(f"Missing key in config file: {e}")
                raise ValueError(f"Invalid config structure: {e}")
            except Exception as e:
                logger.error(f"Unexpected error loading config: {str(e)}", exc_info=True)
                raise ValueError("Failed to load GITPOD_API_KEY from config")

        # Initialize Gitpod client
        try:
            self.client = AsyncGitpod(bearer_token=self.gitpod_api_key)
            logger.info("Successfully initialized AsyncGitpod client")
        except Exception as e:
            logger.error(f"Failed to initialize AsyncGitpod client: {str(e)}", exc_info=True)
            raise

    async def close(self):
        """Cleanup method to properly close the client"""
        if self.client:
            try:
                await self.client.close()
                self.client = None
                logger.info("Successfully closed Gitpod client")
            except Exception as e:
                logger.error(f"Error closing Gitpod client: {str(e)}", exc_info=True)
                raise

@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    """List available tools that can be called."""
    logger.debug("Listing available tools")
    return [
        types.Tool(
            name="get-identity",
            description="Get authenticated identity from Gitpod",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            },
        ),
        types.Tool(
            name="create-environment",
            description="Create a new Gitpod environment from a repository URL",
            inputSchema={
                "type": "object",
                "properties": {
                    "repository_url": {
                        "type": "string",
                        "description": "Repository URL (defaults to https://github.com/gitpod-io/empty)"
                    }
                }
            },
        ),
        types.Tool(
            name="create-environment-with-command",
            description="Create a new Gitpod environment and run a command",
            inputSchema={
                "type": "object",
                "properties": {
                    "repository_url": {
                        "type": "string",
                        "description": "Repository URL (defaults to https://github.com/gitpod-io/empty)"
                    },
                    "command": {
                        "type": "string",
                        "description": "Command to run in the environment"
                    }
                },
                "required": ["command"]
            },
        )
    ]

@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict | None
) -> list[types.TextContent | types.ImageContent]:
    """Handle tool execution requests."""
    logger.info(f"Tool called: {name} with arguments: {arguments}")

    if name not in tools:
        logger.error(f"Unknown tool requested: {name}")
        raise ValueError(f"Unknown tool: {name}")

    try:
        gitpod = GitpodMCPServer()
    except Exception as e:
        logger.error(f"Failed to initialize GitpodMCPServer: {str(e)}", exc_info=True)
        return [
            types.TextContent(
                type="text",
                text=f"Server initialization error: {str(e)}"
            )
        ]

    if name == "get-identity":
        try:
            logger.debug("Fetching authenticated identity")
            response = gitpod.client.identity.get_authenticated_identity()
            logger.info(f"Successfully retrieved identity for org: {response.organization_id}")
            return [
                types.TextContent(
                    type="text",
                    text=f"Organization ID: {response.organization_id}"
                )
            ]
        except Exception as e:
            logger.error(f"Error getting identity: {str(e)}", exc_info=True)
            return [
                types.TextContent(
                    type="text",
                    text=f"Error getting identity: {str(e)}"
                )
            ]

    elif name in ["create-environment", "create-environment-with-command"]:
        try:
            # Get repository URL or use default
            repo_url = arguments.get("repository_url") if arguments else None
            if not repo_url:
                repo_url = "https://github.com/gitpod-io/empty"
                logger.info(f"Using default repository: {repo_url}")

            # Find most used environment class
            env_class = await util.find_most_used_environment_class(gitpod.client)
            if not env_class:
                logger.error("No environment class found")
                return [
                    types.TextContent(
                        type="text",
                        text="Error: No environment class found. Please create one first."
                    )
                ]

            logger.info(f"Using environment class: {env_class.display_name}")
            env_class_id = env_class.id

            # Prepare environment spec
            spec: EnvironmentSpecParam = {
                "desired_phase": "ENVIRONMENT_PHASE_RUNNING",
                "machine": {"class": env_class_id},
                "content": {
                    "initializer": {"specs": [Spec(
                        context_url={
                            "url": repo_url
                        }
                    )]}
                }
            }

            # Create environment
            logger.info("Creating environment")
            environment = (await gitpod.client.environments.create(spec=spec)).environment
            if not environment or not environment.id:
                raise ValueError("Failed to create environment")

            environment_id = environment.id
            logger.info(f"Environment created with ID: {environment_id}")

            # Wait for environment to be ready
            logger.info("Waiting for environment to be ready")
            await util.wait_for_environment_ready(gitpod.client, environment_id)

            # If command was provided, run it
            if name == "create-environment-with-command":
                command = arguments.get("command")
                if command:
                    try:
                        logger.info(f"Running command: {command}")
                        lines = await util.run_command(gitpod.client, environment_id, command)
                        command_output = []

                        # Use asyncio.TimeoutError to handle long-running commands
                        async with asyncio.timeout(300):  # 5 minute timeout
                            async for line in lines:
                                command_output.append(line)
                                # Yield partial results to keep connection alive
                                if len(command_output) % 10 == 0:  # Every 10 lines
                                    await asyncio.sleep(0.1)

                        logger.info("Command execution completed successfully")
                        return [
                            types.TextContent(
                                type="text",
                                text=f"Environment created and command executed:\nID: {environment_id}\nCommand output:\n{''.join(command_output)}"
                            )
                        ]
                    except asyncio.TimeoutError:
                        logger.warning(f"Command execution timed out after 5 minutes: {command}")
                        return [
                            types.TextContent(
                                type="text",
                                text=f"Environment created but command execution timed out after 5 minutes.\nEnvironment ID: {environment_id}\nPartial output:\n{''.join(command_output)}"
                            )
                        ]
                    except Exception as cmd_error:
                        logger.error(f"Error executing command: {str(cmd_error)}", exc_info=True)
                        return [
                            types.TextContent(
                                type="text",
                                text=f"Environment created but command execution failed:\nID: {environment_id}\nError: {str(cmd_error)}"
                            )
                        ]
                    finally:
                        # Ensure we close any open connections
                        try:
                            await gitpod.client.close()
                        except Exception as close_error:
                            logger.warning(f"Error closing client: {str(close_error)}")

            logger.info("Environment creation completed successfully")
            return [
                types.TextContent(
                    type="text",
                    text=f"Environment created successfully:\nID: {environment_id}\nRepository: {repo_url}"
                )
            ]

        except Exception as e:
            logger.error(f"Error creating environment: {str(e)}", exc_info=True)
            return [
                types.TextContent(
                    type="text",
                    text=f"Error creating environment: {str(e)}"
                )
            ]
        finally:
            # Ensure we close the client in all cases
            try:
                await gitpod.client.close()
            except Exception as close_error:
                logger.warning(f"Error closing client: {str(close_error)}")

async def main():
    logger.info("Starting Gitpod MCP server")
    try:
        # Run the server using stdin/stdout streams
        async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
            await server.run(
                read_stream,
                write_stream,
                InitializationOptions(
                    server_name="gitpod-mcp",
                    server_version="0.1.0",
                    capabilities=server.get_capabilities(
                        notification_options=NotificationOptions(),
                        experimental_capabilities={},
                    ),
                ),
            )
    except Exception as e:
        logger.critical(f"Critical error in MCP server: {str(e)}", exc_info=True)
        raise

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Server shutdown requested by user")
    except Exception as e:
        logger.critical(f"Unhandled exception during server runtime: {str(e)}", exc_info=True)
