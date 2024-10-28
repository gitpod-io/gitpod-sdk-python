# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import environment_automation_update_task_execution_status_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    is_given,
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options

__all__ = ["EnvironmentAutomationResource", "AsyncEnvironmentAutomationResource"]


class EnvironmentAutomationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EnvironmentAutomationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return EnvironmentAutomationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EnvironmentAutomationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return EnvironmentAutomationResourceWithStreamingResponse(self)

    def update_task_execution_status(
        self,
        *,
        body: environment_automation_update_task_execution_status_params.Body,
        connect_protocol_version: Literal[1],
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """UpdateTaskExecutionStatus updates the status of a task execution.

        Only the
        environment executing a task execution is expected to call this function.

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          connect_timeout_ms: Define the timeout, in ms

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Connect-Protocol-Version": str(connect_protocol_version),
                    "Connect-Timeout-Ms": str(connect_timeout_ms) if is_given(connect_timeout_ms) else NOT_GIVEN,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            "/gitpod.v1.EnvironmentAutomationService/UpdateTaskExecutionStatus",
            body=maybe_transform(
                body,
                environment_automation_update_task_execution_status_params.EnvironmentAutomationUpdateTaskExecutionStatusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncEnvironmentAutomationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEnvironmentAutomationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEnvironmentAutomationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEnvironmentAutomationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return AsyncEnvironmentAutomationResourceWithStreamingResponse(self)

    async def update_task_execution_status(
        self,
        *,
        body: environment_automation_update_task_execution_status_params.Body,
        connect_protocol_version: Literal[1],
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """UpdateTaskExecutionStatus updates the status of a task execution.

        Only the
        environment executing a task execution is expected to call this function.

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          connect_timeout_ms: Define the timeout, in ms

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Connect-Protocol-Version": str(connect_protocol_version),
                    "Connect-Timeout-Ms": str(connect_timeout_ms) if is_given(connect_timeout_ms) else NOT_GIVEN,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            "/gitpod.v1.EnvironmentAutomationService/UpdateTaskExecutionStatus",
            body=await async_maybe_transform(
                body,
                environment_automation_update_task_execution_status_params.EnvironmentAutomationUpdateTaskExecutionStatusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class EnvironmentAutomationResourceWithRawResponse:
    def __init__(self, environment_automation: EnvironmentAutomationResource) -> None:
        self._environment_automation = environment_automation

        self.update_task_execution_status = to_raw_response_wrapper(
            environment_automation.update_task_execution_status,
        )


class AsyncEnvironmentAutomationResourceWithRawResponse:
    def __init__(self, environment_automation: AsyncEnvironmentAutomationResource) -> None:
        self._environment_automation = environment_automation

        self.update_task_execution_status = async_to_raw_response_wrapper(
            environment_automation.update_task_execution_status,
        )


class EnvironmentAutomationResourceWithStreamingResponse:
    def __init__(self, environment_automation: EnvironmentAutomationResource) -> None:
        self._environment_automation = environment_automation

        self.update_task_execution_status = to_streamed_response_wrapper(
            environment_automation.update_task_execution_status,
        )


class AsyncEnvironmentAutomationResourceWithStreamingResponse:
    def __init__(self, environment_automation: AsyncEnvironmentAutomationResource) -> None:
        self._environment_automation = environment_automation

        self.update_task_execution_status = async_to_streamed_response_wrapper(
            environment_automation.update_task_execution_status,
        )
