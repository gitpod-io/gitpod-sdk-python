# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .tasks import (
    TasksResource,
    AsyncTasksResource,
    TasksResourceWithRawResponse,
    AsyncTasksResourceWithRawResponse,
    TasksResourceWithStreamingResponse,
    AsyncTasksResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .task_executions import (
    TaskExecutionsResource,
    AsyncTaskExecutionsResource,
    TaskExecutionsResourceWithRawResponse,
    AsyncTaskExecutionsResourceWithRawResponse,
    TaskExecutionsResourceWithStreamingResponse,
    AsyncTaskExecutionsResourceWithStreamingResponse,
)

__all__ = ["EnvironmentAutomationsResource", "AsyncEnvironmentAutomationsResource"]


class EnvironmentAutomationsResource(SyncAPIResource):
    @cached_property
    def tasks(self) -> TasksResource:
        return TasksResource(self._client)

    @cached_property
    def task_executions(self) -> TaskExecutionsResource:
        return TaskExecutionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> EnvironmentAutomationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return EnvironmentAutomationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EnvironmentAutomationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return EnvironmentAutomationsResourceWithStreamingResponse(self)


class AsyncEnvironmentAutomationsResource(AsyncAPIResource):
    @cached_property
    def tasks(self) -> AsyncTasksResource:
        return AsyncTasksResource(self._client)

    @cached_property
    def task_executions(self) -> AsyncTaskExecutionsResource:
        return AsyncTaskExecutionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEnvironmentAutomationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEnvironmentAutomationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEnvironmentAutomationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return AsyncEnvironmentAutomationsResourceWithStreamingResponse(self)


class EnvironmentAutomationsResourceWithRawResponse:
    def __init__(self, environment_automations: EnvironmentAutomationsResource) -> None:
        self._environment_automations = environment_automations

    @cached_property
    def tasks(self) -> TasksResourceWithRawResponse:
        return TasksResourceWithRawResponse(self._environment_automations.tasks)

    @cached_property
    def task_executions(self) -> TaskExecutionsResourceWithRawResponse:
        return TaskExecutionsResourceWithRawResponse(self._environment_automations.task_executions)


class AsyncEnvironmentAutomationsResourceWithRawResponse:
    def __init__(self, environment_automations: AsyncEnvironmentAutomationsResource) -> None:
        self._environment_automations = environment_automations

    @cached_property
    def tasks(self) -> AsyncTasksResourceWithRawResponse:
        return AsyncTasksResourceWithRawResponse(self._environment_automations.tasks)

    @cached_property
    def task_executions(self) -> AsyncTaskExecutionsResourceWithRawResponse:
        return AsyncTaskExecutionsResourceWithRawResponse(self._environment_automations.task_executions)


class EnvironmentAutomationsResourceWithStreamingResponse:
    def __init__(self, environment_automations: EnvironmentAutomationsResource) -> None:
        self._environment_automations = environment_automations

    @cached_property
    def tasks(self) -> TasksResourceWithStreamingResponse:
        return TasksResourceWithStreamingResponse(self._environment_automations.tasks)

    @cached_property
    def task_executions(self) -> TaskExecutionsResourceWithStreamingResponse:
        return TaskExecutionsResourceWithStreamingResponse(self._environment_automations.task_executions)


class AsyncEnvironmentAutomationsResourceWithStreamingResponse:
    def __init__(self, environment_automations: AsyncEnvironmentAutomationsResource) -> None:
        self._environment_automations = environment_automations

    @cached_property
    def tasks(self) -> AsyncTasksResourceWithStreamingResponse:
        return AsyncTasksResourceWithStreamingResponse(self._environment_automations.tasks)

    @cached_property
    def task_executions(self) -> AsyncTaskExecutionsResourceWithStreamingResponse:
        return AsyncTaskExecutionsResourceWithStreamingResponse(self._environment_automations.task_executions)
