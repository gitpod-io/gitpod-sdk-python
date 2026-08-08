import os
import asyncio
import logging

import mcp.types as types
import mcp.server.stdio
from mcp.server import Server, NotificationOptions
from mcp.server.models import InitializationOptions

import gitpod.lib as util
from gitpod import AsyncGitpod
from gitpod.types.environment_spec_param import EnvironmentSpecParam
from gitpod.types.environment_initializer_param import Spec

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
        self.client = self._setup_client()

    def _setup_client(self) -> AsyncGitpod:
        """Initialize the Gitpod client with API key from environment."""
        api_key = os.environ.get('GITPOD_API_KEY')
        if not api_key:
            raise ValueError("GITPOD_API_KEY environment variable is required")

        return AsyncGitpod(bearer_token=api_key)

    async def close(self):
        """Cleanup method to properly close the client"""
        if self.client:
            await self.client.close()

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
        raise ValueError(f"Unknown tool: {name}")

    gitpod = GitpodMCPServer()
    try:
        if name == "get-identity":
            response = await gitpod.client.identity.get_authenticated_identity()
            return [
                types.TextContent(
                    type="text",
                    text=f"Organization ID: {response.organization_id}"
                )
            ]

        elif name in ["create-environment", "create-environment-with-command"]:
            repo_url = arguments.get("repository_url", "https://github.com/gitpod-io/empty")

            # Get environment class
            env_class = await util.find_most_used_environment_class(gitpod.client)
            if not env_class:
                return [types.TextContent(
                    type="text",
                    text="Error: No environment class found. Please create one first."
                )]

            # Create environment
            spec: EnvironmentSpecParam = {
                "desired_phase": "ENVIRONMENT_PHASE_RUNNING",
                "machine": {"class": env_class.id},
                "content": {
                    "initializer": {"specs": [Spec(
                        context_url={"url": repo_url}
                    )]}
                }
            }

            environment = (await gitpod.client.environments.create(spec=spec)).environment
            if not environment or not environment.id:
                raise ValueError("Failed to create environment")

            await util.wait_for_environment_ready(gitpod.client, environment.id)

            # Handle command execution if needed
            if name == "create-environment-with-command" and arguments.get("command"):
                try:
                    async with asyncio.timeout(300):  # 5 minute timeout
                        command_output = []
                        async for line in await util.run_command(
                            gitpod.client,
                            environment.id,
                            arguments["command"]
                        ):
                            command_output.append(line)
                            if len(command_output) % 10 == 0:
                                await asyncio.sleep(0.1)

                        return [types.TextContent(
                            type="text",
                            text=f"Environment created and command executed:\nID: {environment.id}\nCommand output:\n{''.join(command_output)}"
                        )]
                except asyncio.TimeoutError:
                    return [types.TextContent(
                        type="text",
                        text=f"Environment created but command timed out after 5 minutes.\nEnvironment ID: {environment.id}"
                    )]

            return [types.TextContent(
                type="text",
                text=f"Environment created successfully:\nID: {environment.id}\nRepository: {repo_url}"
            )]

    except Exception as e:
        logger.error(f"Error in {name}: {str(e)}", exc_info=True)
        return [types.TextContent(type="text", text=f"Error: {str(e)}")]
    finally:
        await gitpod.close()

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
