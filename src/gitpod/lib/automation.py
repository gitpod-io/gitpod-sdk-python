import asyncio
from typing import Callable, Optional, Awaitable, AsyncIterator

import httpx

from gitpod._client import AsyncGitpod
from gitpod.types.environments.automations import service_create_params

TASK_REFERENCE = "gitpod-python-sdk"

async def run_service(
    client: AsyncGitpod,
    environment_id: str,
    metadata: service_create_params.ServiceMetadataParam,
    spec: service_create_params.ServiceSpecParam
) -> AsyncIterator[str]:
    reference = metadata.get("reference")
    if not reference:
        raise ValueError("metadata.reference is required")
    
    services = (await client.environments.automations.services.list(
        filter={
            "references": [reference],
            "environment_ids": [environment_id]
        }
    )).services

    if not services:
        service = (await client.environments.automations.services.create(   
            environment_id=environment_id,
            spec=spec,
            metadata=metadata
        )).service
    else:
        service = services[0]

    await client.environments.automations.services.start(id=service.id)
    log_url = await wait_for_service_log_url(client, environment_id, service.id)
    return stream_logs(client, environment_id, log_url)

async def run_command(client: AsyncGitpod, environment_id: str, command: str) -> AsyncIterator[str]:
    tasks = (await client.environments.automations.tasks.list(
        filter={
            "references": [TASK_REFERENCE],
            "environment_ids": [environment_id]
        }
    )).tasks

    if not tasks:
        task = (await client.environments.automations.tasks.create(
            spec={
                "command": command,
            },
            environment_id=environment_id,
            metadata={
                "name": "Gitpod Python SDK Task",
                "description": "Gitpod Python SDK Task",
                "reference": TASK_REFERENCE,
            },
        )).task
    else:
        task = tasks[0]
        await client.environments.automations.tasks.update(
            id=task.id,
            spec={
                "command": command,
            },
        )

    task_execution = (await client.environments.automations.tasks.start(id=task.id)).task_execution
    log_url = await wait_for_task_log_url(client, environment_id, task_execution.id)
    return stream_logs(client, environment_id, log_url)

async def wait_for_task_log_url(client: AsyncGitpod, environment_id: str, task_execution_id: str) -> str:
    async def get_log_url() -> Optional[str]:
        execution = (await client.environments.automations.tasks.executions.retrieve(id=task_execution_id)).task_execution
        if not execution or not execution.status:
            return None
        return execution.status.log_url
    
    return await wait_for_log_url(client, environment_id, task_execution_id, get_log_url, "RESOURCE_TYPE_TASK_EXECUTION")

async def wait_for_service_log_url(client: AsyncGitpod, environment_id: str, service_id: str) -> str:
    async def get_log_url() -> Optional[str]:
        service = (await client.environments.automations.services.retrieve(id=service_id)).service
        if not service or not service.status:
            return None
        if service.status.phase != "SERVICE_PHASE_RUNNING":
            return None
        return service.status.log_url
    
    return await wait_for_log_url(client, environment_id, service_id, get_log_url, "RESOURCE_TYPE_SERVICE")

async def wait_for_log_url(client: AsyncGitpod, environment_id: str, resource_id: str, get_log_url_fn: Callable[[], Awaitable[Optional[str]]], resource_type: str) -> str:
    log_url = await get_log_url_fn()
    if log_url:
        return log_url

    event_stream = await client.events.watch(environment_id=environment_id, timeout=None)
    try:
        log_url = await get_log_url_fn()
        if log_url:
            return log_url

        async for event in event_stream:
            if event.resource_type == resource_type and event.resource_id == resource_id:
                log_url = await get_log_url_fn()
                if log_url is not None:
                    return log_url
    finally:
        await event_stream.http_response.aclose()

    raise Exception("Failed to get log URL")

async def stream_logs(client: AsyncGitpod, environment_id: str, log_url: str) -> AsyncIterator[str]:
    logs_access_token = (await client.environments.create_logs_token(environment_id=environment_id)).access_token
    async with httpx.AsyncClient() as http_client:
        retries = 3
        while retries > 0:
            try:
                async with http_client.stream("GET", log_url, headers={"Authorization": f"Bearer {logs_access_token}"}, timeout=None) as response:
                    if response.status_code == 502:  # Bad Gateway
                        retries -= 1
                        if retries == 0:
                            raise Exception("Failed to stream logs after 3 retries")
                        await asyncio.sleep(1)  # Wait before retrying
                        continue
                        
                    buffer = ""
                    async for chunk in response.aiter_text():
                        buffer += chunk
                        while "\n" in buffer:
                            line, buffer = buffer.split("\n", 1)
                            if line:
                                yield line
                    if buffer:
                        yield buffer
                    break  # Success - exit retry loop
                    
            except httpx.HTTPError as e:
                if retries > 0 and (isinstance(e, httpx.HTTPStatusError) and e.response.status_code == 502):
                    retries -= 1
                    await asyncio.sleep(1)  # Wait before retrying
                    continue
                raise  # Re-raise if not a 502 or out of retries