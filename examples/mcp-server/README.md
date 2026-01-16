# Gitpod MCP Server Example

A Modal Context Protocol (MCP) server that enables Claude Desktop to interact with Gitpod's API. This integration allows Claude to create Gitpod environments, check identity information, and perform other Gitpod-related tasks directly through natural language commands.

## 🌟 Features

- 🔐 **Secure Authentication**: Uses Gitpod API tokens for secure access
- 🔄 **Real-time Integration**: Direct integration with Gitpod's API
- 🤖 **Natural Language Interface**: Interact with Gitpod using natural language through Claude
- 📝 **Comprehensive Logging**: Detailed logging for debugging and monitoring
- 🚀 **Environment Management**: Create and manage Gitpod environments easily
- ⚡ **Command Execution**: Run commands in your environments directly

## 🚀 Available Tools

1. **get-identity**
   - Get authenticated identity information from Gitpod
   - No additional parameters required

2. **create-environment**
   - Create a new Gitpod environment from a repository URL
   - Optional parameter: `repository_url` (defaults to https://github.com/gitpod-io/empty)

3. **create-environment-with-command**
   - Create a new Gitpod environment and run a command in it
   - Required parameter: `command` (command to run in the environment)
   - Optional parameter: `repository_url` (defaults to https://github.com/gitpod-io/empty)

## Prerequisites

- Python 3.8 or higher
- Claude Desktop application
- Gitpod flex account and API token

## Installation

1. Clone the repository and install dependencies:
```bash
git clone https://github.com/gitpod-io/gitpod-sdk-python
cd gitpod-sdk-python
./scripts/bootstrap
```

## Configuration

1. Get your Gitpod API token from [Gitpod Flex Dashboard](https://app.gitpod.io/settings/personal-access-tokens)

2. Configure Claude Desktop:
   Create or update `~/Library/Application\ Support/Claude/claude_desktop_config.json`:

   ```json
   {
     "mcpServers": {
       "gitpod-mcp": {
         "command": "python",
         "args": [
           "/path/to/gitpod-sdk-python/examples/mcp-server/server.py"
         ],
         "env": {
           "GITPOD_LOG": "info",
           "GITPOD_API_KEY": "your-gitpod-api-token-here"
         }
       }
     }
   }
   ```

## 🎯 Usage Examples

Here are some ways you can interact with the MCP server through Claude Desktop:

1. Check your Gitpod identity:
   ```
   "Get my Gitpod identity"
   ```

2. Create a new environment:
   ```
   "Create a Gitpod environment"
   "Create a Gitpod environment for https://github.com/my/repo"
   ```

3. Create an environment and run a command:
   ```
   "Create a Gitpod environment and run 'echo Hello World'"
   "Create an environment from https://github.com/my/repo and run 'npm install'"
   ```

## 🔍 Troubleshooting

The server logs all activities to `gitpod_mcp.log` in the project directory. Common issues:

1. **Authentication Errors**
   - Verify your Gitpod API token is valid
   - Check if the token has the required scopes
   - Look for authentication errors in the log

2. **Environment Creation Issues**
   - Ensure the repository URL is accessible
   - Check if you have an environment class available
   - Verify your Gitpod account has available resources

3. **Command Execution Problems**
   - Make sure the command is valid for the environment
   - Check if the environment is fully initialized
   - Look for command execution errors in the logs
