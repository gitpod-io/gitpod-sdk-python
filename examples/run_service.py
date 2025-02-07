#!/usr/bin/env python

import sys
import asyncio

import gitpod.lib as util
from gitpod import AsyncGitpod
from gitpod.types.environment_spec_param import EnvironmentSpecParam
from gitpod.types.environment_initializer_param import Spec


# Examples:
# - ./examples/run_service.py
# - ./examples/run_service.py https://github.com/gitpod-io/empty
async def main(cleanup: util.Disposables) -> None:
    client = AsyncGitpod()

    context_url = sys.argv[1] if len(sys.argv) > 1 else None

    env_class = await util.find_most_used_environment_class(client)
    if not env_class:
        print("Error: No environment class found. Please create one first.")
        sys.exit(1)
    print(f"Found environment class: {env_class.display_name} ({env_class.description})")
    env_class_id = env_class.id
    assert env_class_id is not None
    
    port = 8888
    spec: EnvironmentSpecParam = {
        "desired_phase": "ENVIRONMENT_PHASE_RUNNING",
        "machine": {"class": env_class_id},
        "ports": [{
            "name": "Lama Service",
            "port": port,
            "admission": "ADMISSION_LEVEL_EVERYONE"
        }]
    }
    if context_url:
        spec["content"] = {
            "initializer": {"specs": [Spec(
             context_url={
                 "url": context_url
             }
        )]}
    }

    print("Creating environment")
    environment = (await client.environments.create(spec=spec)).environment
    assert environment is not None
    environment_id = environment.id
    assert environment_id is not None
    cleanup.add(lambda: asyncio.run(client.environments.delete(environment_id=environment_id)))
    
    print("Waiting for environment to be ready")
    env = util.EnvironmentState(client, environment_id)
    cleanup.add(lambda: asyncio.run(env.close()))
    await env.wait_until_running()

    print("Starting Lama Service")
    lines = await util.run_service(client, environment_id, {
        "name":"Lama Service",
        "description":"Lama Service", 
        "reference":"lama-service"
    }, {
        "commands": {
            "start":f"curl lama.sh | LAMA_PORT={port} sh",
            "ready":f"curl -s http://localhost:{port}"
        }
    })

    port_url = await env.wait_for_port_url(port)
    print(f"Lama Service is running at {port_url}")

    async for line in lines:
        print(line)

if __name__ == "__main__":
    disposables = util.Disposables()
    with disposables:
        asyncio.run(main(disposables))
