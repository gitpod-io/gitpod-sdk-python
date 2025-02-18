import logging
from typing import Any, List, Callable, Awaitable

log = logging.getLogger(__name__)

class Disposables:
    """A utility class to manage cleanup actions (disposables) in a LIFO order.
    
    Example:
        ```python
        with Disposables() as disposables:
            # Add cleanup actions
            disposables.add(lambda: cleanup_something())
            disposables.add(lambda: cleanup_something_else())
            
            # Do work that needs cleanup
            do_something()
            do_something_else()
        # Cleanup actions will be executed in reverse order when exiting the context
        ```
    """
    
    def __init__(self) -> None:
        self._actions: List[Callable[[], Awaitable[Any]]] = []

    def adda(self, action: Callable[[], Awaitable[Any]]) -> None:
        """Add an async cleanup action to be executed when the context exits.
        
        Args:
            action: An async callable that performs cleanup when called
        """
        self._actions.append(action)

    def add(self, action: Callable[[], Any]) -> None:
        """Add a cleanup action to be executed when the context exits.
        
        Args:
            action: A callable that performs cleanup when called
        """
        async def wrapper() -> Any:
            return action()
        self._actions.append(wrapper)
    
    async def cleanup(self) -> None:
        """Execute all cleanup actions in reverse order.
        
        If any cleanup action raises an exception, it will be logged but won't prevent
        other cleanup actions from executing.
        """
        for action in reversed(self._actions):
            try:
                await action()
            except BaseException:
                log.exception("cleanup action failed")

async def with_disposables(fn: Callable[['Disposables'], Awaitable[Any]]) -> Any:
    disposables = Disposables()
    try:
        return await fn(disposables)
    finally:
        await disposables.cleanup()
