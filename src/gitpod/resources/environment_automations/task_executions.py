# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    is_given,
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.environment_automations import (
    task_execution_list_params,
    task_execution_stop_params,
    task_execution_retrieve_params,
    task_execution_create_list_params,
    task_execution_create_retrieve_params,
)
from ...types.environment_automations.task_execution_list_response import TaskExecutionListResponse
from ...types.environment_automations.task_execution_retrieve_response import TaskExecutionRetrieveResponse
from ...types.environment_automations.task_execution_create_list_response import TaskExecutionCreateListResponse
from ...types.environment_automations.task_execution_create_retrieve_response import TaskExecutionCreateRetrieveResponse

__all__ = ["TaskExecutionsResource", "AsyncTaskExecutionsResource"]


class TaskExecutionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TaskExecutionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return TaskExecutionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TaskExecutionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return TaskExecutionsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        connect_protocol_version: Literal[1],
        base64: str | NotGiven = NOT_GIVEN,
        compression: str | NotGiven = NOT_GIVEN,
        connect: str | NotGiven = NOT_GIVEN,
        encoding: str | NotGiven = NOT_GIVEN,
        message: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskExecutionRetrieveResponse:
        """
        GetTaskExecution

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
        return self._get(
            "/gitpod.v1.EnvironmentAutomationService/GetTaskExecution",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "base64": base64,
                        "compression": compression,
                        "connect": connect,
                        "encoding": encoding,
                        "message": message,
                    },
                    task_execution_retrieve_params.TaskExecutionRetrieveParams,
                ),
            ),
            cast_to=TaskExecutionRetrieveResponse,
        )

    def list(
        self,
        *,
        connect_protocol_version: Literal[1],
        base64: str | NotGiven = NOT_GIVEN,
        compression: str | NotGiven = NOT_GIVEN,
        connect: str | NotGiven = NOT_GIVEN,
        encoding: str | NotGiven = NOT_GIVEN,
        message: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskExecutionListResponse:
        """
        ListTaskExecutions

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
        return self._get(
            "/gitpod.v1.EnvironmentAutomationService/ListTaskExecutions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "base64": base64,
                        "compression": compression,
                        "connect": connect,
                        "encoding": encoding,
                        "message": message,
                    },
                    task_execution_list_params.TaskExecutionListParams,
                ),
            ),
            cast_to=TaskExecutionListResponse,
        )

    def create_list(
        self,
        *,
        connect_protocol_version: Literal[1],
        filter: task_execution_create_list_params.Filter | NotGiven = NOT_GIVEN,
        pagination: task_execution_create_list_params.Pagination | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskExecutionCreateListResponse:
        """
        ListTaskExecutions

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          filter: filter contains the filter options for listing task runs

          pagination: pagination contains the pagination options for listing task runs

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
            "/gitpod.v1.EnvironmentAutomationService/ListTaskExecutions",
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                task_execution_create_list_params.TaskExecutionCreateListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskExecutionCreateListResponse,
        )

    def create_retrieve(
        self,
        *,
        connect_protocol_version: Literal[1],
        id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskExecutionCreateRetrieveResponse:
        """
        GetTaskExecution

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
            "/gitpod.v1.EnvironmentAutomationService/GetTaskExecution",
            body=maybe_transform({"id": id}, task_execution_create_retrieve_params.TaskExecutionCreateRetrieveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskExecutionCreateRetrieveResponse,
        )

    def stop(
        self,
        *,
        connect_protocol_version: Literal[1],
        id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        StopTaskExecution

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
            "/gitpod.v1.EnvironmentAutomationService/StopTaskExecution",
            body=maybe_transform({"id": id}, task_execution_stop_params.TaskExecutionStopParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncTaskExecutionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTaskExecutionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTaskExecutionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTaskExecutionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return AsyncTaskExecutionsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        connect_protocol_version: Literal[1],
        base64: str | NotGiven = NOT_GIVEN,
        compression: str | NotGiven = NOT_GIVEN,
        connect: str | NotGiven = NOT_GIVEN,
        encoding: str | NotGiven = NOT_GIVEN,
        message: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskExecutionRetrieveResponse:
        """
        GetTaskExecution

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
        return await self._get(
            "/gitpod.v1.EnvironmentAutomationService/GetTaskExecution",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "base64": base64,
                        "compression": compression,
                        "connect": connect,
                        "encoding": encoding,
                        "message": message,
                    },
                    task_execution_retrieve_params.TaskExecutionRetrieveParams,
                ),
            ),
            cast_to=TaskExecutionRetrieveResponse,
        )

    async def list(
        self,
        *,
        connect_protocol_version: Literal[1],
        base64: str | NotGiven = NOT_GIVEN,
        compression: str | NotGiven = NOT_GIVEN,
        connect: str | NotGiven = NOT_GIVEN,
        encoding: str | NotGiven = NOT_GIVEN,
        message: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskExecutionListResponse:
        """
        ListTaskExecutions

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
        return await self._get(
            "/gitpod.v1.EnvironmentAutomationService/ListTaskExecutions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "base64": base64,
                        "compression": compression,
                        "connect": connect,
                        "encoding": encoding,
                        "message": message,
                    },
                    task_execution_list_params.TaskExecutionListParams,
                ),
            ),
            cast_to=TaskExecutionListResponse,
        )

    async def create_list(
        self,
        *,
        connect_protocol_version: Literal[1],
        filter: task_execution_create_list_params.Filter | NotGiven = NOT_GIVEN,
        pagination: task_execution_create_list_params.Pagination | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskExecutionCreateListResponse:
        """
        ListTaskExecutions

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          filter: filter contains the filter options for listing task runs

          pagination: pagination contains the pagination options for listing task runs

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
            "/gitpod.v1.EnvironmentAutomationService/ListTaskExecutions",
            body=await async_maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                task_execution_create_list_params.TaskExecutionCreateListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskExecutionCreateListResponse,
        )

    async def create_retrieve(
        self,
        *,
        connect_protocol_version: Literal[1],
        id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskExecutionCreateRetrieveResponse:
        """
        GetTaskExecution

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
            "/gitpod.v1.EnvironmentAutomationService/GetTaskExecution",
            body=await async_maybe_transform(
                {"id": id}, task_execution_create_retrieve_params.TaskExecutionCreateRetrieveParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskExecutionCreateRetrieveResponse,
        )

    async def stop(
        self,
        *,
        connect_protocol_version: Literal[1],
        id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        StopTaskExecution

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
            "/gitpod.v1.EnvironmentAutomationService/StopTaskExecution",
            body=await async_maybe_transform({"id": id}, task_execution_stop_params.TaskExecutionStopParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class TaskExecutionsResourceWithRawResponse:
    def __init__(self, task_executions: TaskExecutionsResource) -> None:
        self._task_executions = task_executions

        self.retrieve = to_raw_response_wrapper(
            task_executions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            task_executions.list,
        )
        self.create_list = to_raw_response_wrapper(
            task_executions.create_list,
        )
        self.create_retrieve = to_raw_response_wrapper(
            task_executions.create_retrieve,
        )
        self.stop = to_raw_response_wrapper(
            task_executions.stop,
        )


class AsyncTaskExecutionsResourceWithRawResponse:
    def __init__(self, task_executions: AsyncTaskExecutionsResource) -> None:
        self._task_executions = task_executions

        self.retrieve = async_to_raw_response_wrapper(
            task_executions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            task_executions.list,
        )
        self.create_list = async_to_raw_response_wrapper(
            task_executions.create_list,
        )
        self.create_retrieve = async_to_raw_response_wrapper(
            task_executions.create_retrieve,
        )
        self.stop = async_to_raw_response_wrapper(
            task_executions.stop,
        )


class TaskExecutionsResourceWithStreamingResponse:
    def __init__(self, task_executions: TaskExecutionsResource) -> None:
        self._task_executions = task_executions

        self.retrieve = to_streamed_response_wrapper(
            task_executions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            task_executions.list,
        )
        self.create_list = to_streamed_response_wrapper(
            task_executions.create_list,
        )
        self.create_retrieve = to_streamed_response_wrapper(
            task_executions.create_retrieve,
        )
        self.stop = to_streamed_response_wrapper(
            task_executions.stop,
        )


class AsyncTaskExecutionsResourceWithStreamingResponse:
    def __init__(self, task_executions: AsyncTaskExecutionsResource) -> None:
        self._task_executions = task_executions

        self.retrieve = async_to_streamed_response_wrapper(
            task_executions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            task_executions.list,
        )
        self.create_list = async_to_streamed_response_wrapper(
            task_executions.create_list,
        )
        self.create_retrieve = async_to_streamed_response_wrapper(
            task_executions.create_retrieve,
        )
        self.stop = async_to_streamed_response_wrapper(
            task_executions.stop,
        )
