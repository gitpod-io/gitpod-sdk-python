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
from .services import (
    ServicesResource,
    AsyncServicesResource,
    ServicesResourceWithRawResponse,
    AsyncServicesResourceWithRawResponse,
    ServicesResourceWithStreamingResponse,
    AsyncServicesResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["AutomationsResource", "AsyncAutomationsResource"]


class AutomationsResource(SyncAPIResource):
    @cached_property
    def tasks(self) -> TasksResource:
        return TasksResource(self._client)

    @cached_property
    def services(self) -> ServicesResource:
        return ServicesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AutomationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return AutomationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AutomationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return AutomationsResourceWithStreamingResponse(self)


class AsyncAutomationsResource(AsyncAPIResource):
    @cached_property
    def tasks(self) -> AsyncTasksResource:
        return AsyncTasksResource(self._client)

    @cached_property
    def services(self) -> AsyncServicesResource:
        return AsyncServicesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAutomationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAutomationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAutomationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return AsyncAutomationsResourceWithStreamingResponse(self)


class AutomationsResourceWithRawResponse:
    def __init__(self, automations: AutomationsResource) -> None:
        self._automations = automations

    @cached_property
    def tasks(self) -> TasksResourceWithRawResponse:
        return TasksResourceWithRawResponse(self._automations.tasks)

    @cached_property
    def services(self) -> ServicesResourceWithRawResponse:
        return ServicesResourceWithRawResponse(self._automations.services)


class AsyncAutomationsResourceWithRawResponse:
    def __init__(self, automations: AsyncAutomationsResource) -> None:
        self._automations = automations

    @cached_property
    def tasks(self) -> AsyncTasksResourceWithRawResponse:
        return AsyncTasksResourceWithRawResponse(self._automations.tasks)

    @cached_property
    def services(self) -> AsyncServicesResourceWithRawResponse:
        return AsyncServicesResourceWithRawResponse(self._automations.services)


class AutomationsResourceWithStreamingResponse:
    def __init__(self, automations: AutomationsResource) -> None:
        self._automations = automations

    @cached_property
    def tasks(self) -> TasksResourceWithStreamingResponse:
        return TasksResourceWithStreamingResponse(self._automations.tasks)

    @cached_property
    def services(self) -> ServicesResourceWithStreamingResponse:
        return ServicesResourceWithStreamingResponse(self._automations.services)


class AsyncAutomationsResourceWithStreamingResponse:
    def __init__(self, automations: AsyncAutomationsResource) -> None:
        self._automations = automations

    @cached_property
    def tasks(self) -> AsyncTasksResourceWithStreamingResponse:
        return AsyncTasksResourceWithStreamingResponse(self._automations.tasks)

    @cached_property
    def services(self) -> AsyncServicesResourceWithStreamingResponse:
        return AsyncServicesResourceWithStreamingResponse(self._automations.services)
