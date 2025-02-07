#!/usr/bin/env python

import sys
import asyncio
from io import StringIO

import paramiko

import gitpod.lib as util
from gitpod import AsyncGitpod
from gitpod.types.environment_spec_param import EnvironmentSpecParam
from gitpod.types.environment_initializer_param import Spec


# Examples:
# - ./examples/fs_access.py
# - ./examples/fs_access.py https://github.com/gitpod-io/empty
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
    
    print("Generating SSH key pair")
    key = paramiko.RSAKey.generate(2048)
    private_key_file = StringIO()
    key.write_private_key(private_key_file)
    private_key_file.seek(0)  # Reset position to start
    public_key = f"{key.get_name()} {key.get_base64()}"

    print("Creating environment with SSH access")
    key_id = "fs-access-example"
    spec: EnvironmentSpecParam = {
        "desired_phase": "ENVIRONMENT_PHASE_RUNNING",
        "machine": {"class": env_class_id},
        "ssh_public_keys": [{
            "id": key_id,
            "value": public_key
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

    env = util.EnvironmentState(client, environment_id)
    cleanup.add(lambda: asyncio.run(env.close()))

    print("Waiting for environment to be running")
    await env.wait_until_running()

    print("Waiting for SSH key to be applied")
    await env.wait_for_ssh_key_applied(key_id=key_id, key_value=public_key)

    print("Waiting for SSH URL")
    ssh_url = await env.wait_for_ssh_url()

    print(f"Setting up SSH connection to {ssh_url}")
    # Parse ssh://username@host:port format
    url_parts = ssh_url.split('://')[-1]
    username, rest = url_parts.split('@')
    host, port_str = rest.split(':')
    port = int(port_str)

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(
        hostname=host,
        port=port,
        username=username,
        pkey=key
    )
    cleanup.add(lambda: ssh.close())

    print("Creating SFTP client")
    sftp = ssh.open_sftp()
    cleanup.add(lambda: sftp.close())

    print("Writing test file")
    test_content = "Hello from Gitpod Python SDK!"
    with sftp.file('test.txt', 'w') as f:
        f.write(test_content)

    with sftp.file('test.txt', 'r') as f:
        content = f.read()
        print(f"File content: {content.decode()}")

if __name__ == "__main__":
    disposables = util.Disposables()
    with disposables:
        asyncio.run(main(disposables))