# export ANTHROPIC_API_KEY=...
# python -m examples.anthropic_tool_use

from __future__ import annotations

from typing import cast

from anthropic import Anthropic
from anthropic.types import ToolParam, MessageParam

import gitpod.lib as util
from gitpod import AsyncGitpod
from gitpod.types.environment_initializer_param import Spec

from .scm_auth import verify_context_url  # type: ignore

gpclient = AsyncGitpod()
llmclient = Anthropic()

user_message: MessageParam = {
    "role": "user",
    "content": "What is the test coverage for this repository: https://github.com/gitpod-io/gitpod-sdk-go",
}
tools: list[ToolParam] = [
    {
        "name": "create_environment",
        "description": "Create a new environment for a given context URL. This will create a new environment and return the ID of the environment.",
        "input_schema": {
            "type": "object",
            "properties": {"context_url": {"type": "string"}},
        },
    },
    {
        "name": "execute_command",
        "description": "Execute a command in a given environment ID. This will execute the command in the given environment and return the output of the command.",
        "input_schema": {
            "type": "object",
            "properties": {"environment_id": {"type": "string"}, "command": {"type": "string"}},
        },
    },
]

async def create_environment(args: dict[str, str], cleanup: util.Disposables) -> str:
    env_class = await util.find_most_used_environment_class(gpclient)
    if not env_class:
        raise Exception("No environment class found. Please create one first.")
    await verify_context_url(gpclient, args["context_url"], env_class.runner_id)

    environment = (await gpclient.environments.create(
        spec={
            "desired_phase": "ENVIRONMENT_PHASE_RUNNING",
            "content": {
                "initializer": {"specs": [Spec(
                    context_url={
                        "url": args["context_url"]
                    }
                )]},
            },
            "machine": {"class": env_class.id},
        }
    )).environment
    cleanup.adda(lambda: gpclient.environments.delete(environment_id=environment.id))
    
    print(f"\nCreated environment: {environment.id} - waiting for it to be ready...")
    await util.wait_for_environment_running(gpclient, environment.id)
    print(f"\nEnvironment is ready: {environment.id}")
    return environment.id

async def execute_command(args: dict[str, str]) -> str:
    lines_iter = await util.run_command(gpclient, args["environment_id"], args["command"])
    lines: list[str] = []
    async for line in lines_iter:
        lines.append(line)
    return "\n".join(lines)

async def main(cleanup: util.Disposables) -> None:
    messages = [user_message]
    while True:
        message = llmclient.messages.create(
            model="claude-3-5-sonnet-latest",
            max_tokens=1024,
            messages=messages,
            tools=tools,
        )
        print(f"\nResponse: {message.model_dump_json(indent=2)}")
        
        if message.stop_reason != "tool_use":
            print(f"\nFinal response reached! {message.model_dump_json(indent=2)}")
            break
        
        messages.extend([
            {"role": message.role, "content": message.content}
        ])
        
        # Handle all tool calls in this response
        for tool in (c for c in message.content if c.type == "tool_use"):
            try:
                if tool.name == "create_environment":
                    args = cast(dict[str, str], tool.input)
                    environment_id = await create_environment(args, cleanup)
                    messages.append({
                        "role": "user",
                        "content": [{
                                "type": "tool_result",
                                "tool_use_id": tool.id,
                                "content": [{"type": "text", "text": f"The environment ID is {environment_id}"}],
                        }],
                    })
                elif tool.name == "execute_command":
                    args = cast(dict[str, str], tool.input)
                    output = await execute_command(args)
                    messages.append({
                        "role": "user",
                        "content": [{
                            "type": "tool_result",
                            "tool_use_id": tool.id,
                            "content": [{"type": "text", "text": output}],
                        }],
                    })
                else:
                    raise Exception(f"Unknown tool: {tool.name}")
            except Exception as e:
                messages.append({
                    "role": "user",
                    "content": [{
                        "type": "tool_result",
                        "tool_use_id": tool.id,
                        "is_error": True,
                        "content": [{"type": "text", "text": f"Error: {e}"}],
                    }],
                })

    print("\nFinal response reached!")

if __name__ == "__main__":
    import asyncio
    asyncio.run(util.with_disposables(main))
