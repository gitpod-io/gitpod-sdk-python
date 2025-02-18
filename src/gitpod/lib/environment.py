import asyncio
import logging
from typing import List, TypeVar, Callable, Optional

from gitpod import AsyncGitpod
from gitpod.types.shared import EnvironmentClass
from gitpod.types.environment import Environment

T = TypeVar('T')

log = logging.getLogger(__name__)

class EnvironmentState:
    """
    Maintains the current state of an environment and updates it via event stream.
    Uses simple threading and callbacks for state updates.
    """
    def __init__(self, client: AsyncGitpod, environment_id: str):
        self.client = client
        self.environment_id = environment_id
        self._ready = asyncio.Event()
        self._environment: Optional[Environment] = None

        # State management
        self._listeners: List[Callable[[Environment], None]] = []
        self._should_stop = False
        self.mutex = asyncio.Lock()
        
        # Start background task
        loop = asyncio.get_event_loop()
        self._update_task: asyncio.Task[None] = loop.create_task(self._start_update_loop())

    async def get_environment(self) -> Environment:
        await self._ready.wait()
        assert self._environment is not None
        return self._environment
    
    async def _update_environment(self) -> None:
        try:
            resp = await self.client.environments.retrieve(environment_id=self.environment_id)
            env = resp.environment
            self._environment = env
            self._ready.set()
            for listener in list(self._listeners):
                try:
                    listener(env)
                except Exception:
                    log.exception("failed to call listener")
        except BaseException:
            log.exception("failed to update environment")

    async def _start_update_loop(self) -> None:
        """Background coroutine that maintains the event stream"""
        retry_delay = 1.0  # Initial retry delay in seconds
        max_delay = 32.0   # Maximum retry delay

        await self._update_environment()
        
        while not self._should_stop:
            try:
                async with self.mutex:
                    if self._should_stop:
                        return # type: ignore[unreachable]

                    event_stream = await self.client.events.watch(environment_id=self.environment_id, timeout=None)
                    self.event_stream = event_stream

                retry_delay = 1.0  # Reset delay on successful connection
                if self._should_stop:
                    return # type: ignore[unreachable]
                
                # Immediately do one update so we don't miss changes
                await self._update_environment()
                if self._should_stop:
                    return # type: ignore[unreachable]
                
                try: 
                    async for event in event_stream:
                        if self._should_stop:
                            return # type: ignore[unreachable]
                        
                        if event.resource_type == "RESOURCE_TYPE_ENVIRONMENT" and event.resource_id == self.environment_id:
                            await self._update_environment()
                finally:
                    await event_stream.http_response.aclose()

            except BaseException as e:
                if self._should_stop or isinstance(e, asyncio.CancelledError):
                    return
                
                log.exception("error in event stream, retrying in %s seconds", retry_delay)
                await asyncio.sleep(retry_delay)
                retry_delay = min(retry_delay * 2, max_delay)

    async def close(self) -> None:
        """Stop the update loop and clean up resources"""
        async with self.mutex:
            if self._should_stop:
                return
            self._should_stop = True

        if self.event_stream:
            await self.event_stream.http_response.aclose()

        await self._update_task

    async def wait_until(self, check_fn: Callable[[Environment], Optional[T]]) -> T:
        """Wait until check function returns a value
        
        Args:
            check_fn: Function that checks the environment and returns a value when condition is met
            
        Returns:
            The value returned by check_fn
        """
        # Check current state first        
        initial_env = await self.get_environment()
        initial_check = check_fn(initial_env)
        if initial_check is not None:
            return initial_check

        event = asyncio.Event()
        result: Optional[T] = None

        def listener(env: Environment) -> None:
            nonlocal result
            check_result = check_fn(env)
            if check_result is not None:
                result = check_result
                event.set()

        self._listeners.append(listener)
        try:
            await event.wait()
            if result is None:
                raise RuntimeError("wait_until completed but result is None")
            return result # type: ignore[unreachable] 
        finally:
            self._listeners.remove(listener)

    def is_running(self, env: Environment) -> bool:
        """Check if environment is ready"""
        if not env.status:
            return False
            
        if env.status.failure_message:
            raise RuntimeError(f"Environment {env.id} failed: {'; '.join(env.status.failure_message)}")
        elif env.status.phase in ["ENVIRONMENT_PHASE_STOPPING", "ENVIRONMENT_PHASE_STOPPED", 
                              "ENVIRONMENT_PHASE_DELETING", "ENVIRONMENT_PHASE_DELETED"]:
            raise RuntimeError(f"Environment {env.id} is in unexpected phase: {env.status.phase}")
        
        return env.status.phase == "ENVIRONMENT_PHASE_RUNNING"

    def get_ssh_url(self, env: Environment) -> Optional[str]:
        """Get SSH URL if available"""
        if not env.status or not env.status.environment_urls or not env.status.environment_urls.ssh:
            return None
        return env.status.environment_urls.ssh.url

    def get_port_url(self, env: Environment, port: int) -> Optional[str]:
        """Get port URL if available"""
        if not env.status or not env.status.environment_urls or not env.status.environment_urls.ports:
            return None
        
        for p in env.status.environment_urls.ports:
            if p.port == port:
                return p.url
        return None

    def check_ssh_key_applied(self, env: Environment, key_id: str, key_value: str) -> bool:
        """Check if SSH key is applied"""
        if not env.spec or not env.spec.ssh_public_keys:
            return False
            
        key = next((k for k in env.spec.ssh_public_keys if k.id == key_id), None)
        if not key:
            raise RuntimeError(f"SSH key '{key_id}' not found in environment spec")
        
        if key.value != key_value:
            raise RuntimeError(f"SSH key '{key_id}' has incorrect value")

        if not env.status or not env.status.ssh_public_keys:
            return False
        
        key_status = next((ks for ks in env.status.ssh_public_keys if ks.id == key_id), None)  
        if not key_status:
            return False
        
        if key_status.phase == "CONTENT_PHASE_FAILED":
            raise RuntimeError(f"SSH key '{key_id}' failed to apply")
        
        return key_status.phase == "CONTENT_PHASE_READY"
    
    async def wait_until_running(self) -> None:
        def check_running(env: Environment) -> Optional[bool]:
            return True if self.is_running(env) else None
        await self.wait_until(check_running)

    async def wait_for_ssh_url(self) -> str:
        def get_url(env: Environment) -> Optional[str]:
            return self.get_ssh_url(env)
        return await self.wait_until(get_url)

    async def wait_for_port_url(self, port: int) -> str:
        def check_port(env: Environment) -> Optional[str]:
            return self.get_port_url(env, port)
        return await self.wait_until(check_port)

    async def wait_for_ssh_key_applied(self, key_id: str, key_value: str) -> None:
        def check_key(env: Environment) -> Optional[bool]:
            return True if self.check_ssh_key_applied(env, key_id, key_value) else None
        await self.wait_until(check_key)

async def wait_for_environment_running(client: AsyncGitpod, environment_id: str) -> None:
    env = EnvironmentState(client, environment_id)
    try: 
        await env.wait_until_running()
    finally:
        await env.close()

async def find_most_used_environment_class(client: AsyncGitpod) -> Optional[EnvironmentClass]:
    """
    Find the most used environment class.
    """
    class_usage: dict[str, int] = {}
    envs_resp = await client.environments.list()
    while envs_resp:
        for env in envs_resp.environments:
            if env.spec and env.spec.machine and env.spec.machine.class_:
                env_class = env.spec.machine.class_
                class_usage[env_class] = class_usage.get(env_class, 0) + 1
        if envs_resp.pagination and envs_resp.pagination.next_token:
            envs_resp = await client.environments.list(token=envs_resp.pagination.next_token)
        else:
            break

    sorted_classes = sorted(class_usage.items(), key=lambda item: -item[1])
    environment_class_id: Optional[str] = sorted_classes[0][0] if sorted_classes else None
    if not environment_class_id:
        return None
    
    return await find_environment_class_by_id(client, environment_class_id)

async def find_environment_class_by_id(client: AsyncGitpod, environment_class_id: str) -> Optional[EnvironmentClass]:
    classes_resp = await client.environments.classes.list(filter={"can_create_environments": True})
    while classes_resp:
        for cls in classes_resp.environment_classes:
            if cls.id == environment_class_id:
                return cls
        if classes_resp.pagination and classes_resp.pagination.next_token:
            classes_resp = await client.environments.classes.list(token=classes_resp.pagination.next_token)
        else:
            break
    return None