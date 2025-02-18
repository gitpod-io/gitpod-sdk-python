import sys
import asyncio

import gitpod.lib as util
from gitpod import AsyncGitpod
from gitpod.types.environment_spec_param import EnvironmentSpecParam
from gitpod.types.environment_initializer_param import Spec

from .scm_auth import verify_context_url  # type: ignore


# Examples:
# - python -m examples.run_command 'echo "Hello World!"'
# - python -m examples.run_command 'echo "Hello World!"' https://github.com/gitpod-io/empty
async def main(cleanup: util.Disposables) -> None:
    client = AsyncGitpod()

    if len(sys.argv) < 2:
        print("Usage: ./examples/run_command.py '<COMMAND>' [CONTEXT_URL]")
        sys.exit(1)

    command = sys.argv[1]
    context_url = sys.argv[2] if len(sys.argv) > 2 else None

    env_class = await util.find_most_used_environment_class(client)
    if not env_class:
        print("Error: No environment class found. Please create one first.")
        sys.exit(1)
    print(f"Found environment class: {env_class.display_name} ({env_class.description})")
    
    spec: EnvironmentSpecParam = {
        "desired_phase": "ENVIRONMENT_PHASE_RUNNING",
        "machine": {"class": env_class.id},
    }
    if context_url:
        await verify_context_url(client, context_url, env_class.runner_id)
        spec["content"] = {
            "initializer": {"specs": [Spec(
                context_url={
                    "url": context_url
                }
            )]}
        }

    print("Creating environment")
    environment = (await client.environments.create(spec=spec)).environment
    cleanup.adda(lambda: client.environments.delete(environment_id=environment.id))

    print("Waiting for environment to be ready")
    await util.wait_for_environment_running(client, environment.id)

    print("Running command")
    lines = await util.run_command(client, environment.id, command)
    async for line in lines:
        print(line)

if __name__ == "__main__":
    asyncio.run(util.with_disposables(main))
