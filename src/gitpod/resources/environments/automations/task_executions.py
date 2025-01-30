# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import overload

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    required_args,
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.environments.automations import (
    task_execution_list_params,
    task_execution_stop_params,
    task_execution_retrieve_params,
    task_execution_update_task_execution_status_params,
)
from ....types.environments.automations.task_execution_list_response import TaskExecutionListResponse
from ....types.environments.automations.task_execution_retrieve_response import TaskExecutionRetrieveResponse

__all__ = ["TaskExecutionsResource", "AsyncTaskExecutionsResource"]


class TaskExecutionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TaskExecutionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
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
        id: str | NotGiven = NOT_GIVEN,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.EnvironmentAutomationService/GetTaskExecution",
            body=maybe_transform({"id": id}, task_execution_retrieve_params.TaskExecutionRetrieveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskExecutionRetrieveResponse,
        )

    def list(
        self,
        *,
        filter: task_execution_list_params.Filter | NotGiven = NOT_GIVEN,
        pagination: task_execution_list_params.Pagination | NotGiven = NOT_GIVEN,
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
          filter: filter contains the filter options for listing task runs

          pagination: pagination contains the pagination options for listing task runs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.EnvironmentAutomationService/ListTaskExecutions",
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                task_execution_list_params.TaskExecutionListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskExecutionListResponse,
        )

    def stop(
        self,
        *,
        id: str | NotGiven = NOT_GIVEN,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.EnvironmentAutomationService/StopTaskExecution",
            body=maybe_transform({"id": id}, task_execution_stop_params.TaskExecutionStopParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    @overload
    def update_task_execution_status(
        self,
        *,
        failure_message: str,
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
          failure_message: failure_message marks the task execution as failed and provides a message
              explaining the failure.

              If an individual step has failed, callers are NOT expected to set this message;
              only if the task execution as a whole has failed/cannot be started.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update_task_execution_status(
        self,
        *,
        log_url: str,
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
          log_url: log_url is the URL to the logs of the task's steps. If this is empty, the task
              either has no logs or has not yet started.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["failure_message"], ["log_url"])
    def update_task_execution_status(
        self,
        *,
        failure_message: str | NotGiven = NOT_GIVEN,
        log_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        return self._post(
            "/gitpod.v1.EnvironmentAutomationService/UpdateTaskExecutionStatus",
            body=maybe_transform(
                {
                    "failure_message": failure_message,
                    "log_url": log_url,
                },
                task_execution_update_task_execution_status_params.TaskExecutionUpdateTaskExecutionStatusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncTaskExecutionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTaskExecutionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
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
        id: str | NotGiven = NOT_GIVEN,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.EnvironmentAutomationService/GetTaskExecution",
            body=await async_maybe_transform({"id": id}, task_execution_retrieve_params.TaskExecutionRetrieveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskExecutionRetrieveResponse,
        )

    async def list(
        self,
        *,
        filter: task_execution_list_params.Filter | NotGiven = NOT_GIVEN,
        pagination: task_execution_list_params.Pagination | NotGiven = NOT_GIVEN,
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
          filter: filter contains the filter options for listing task runs

          pagination: pagination contains the pagination options for listing task runs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.EnvironmentAutomationService/ListTaskExecutions",
            body=await async_maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                task_execution_list_params.TaskExecutionListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskExecutionListResponse,
        )

    async def stop(
        self,
        *,
        id: str | NotGiven = NOT_GIVEN,
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.EnvironmentAutomationService/StopTaskExecution",
            body=await async_maybe_transform({"id": id}, task_execution_stop_params.TaskExecutionStopParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    @overload
    async def update_task_execution_status(
        self,
        *,
        failure_message: str,
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
          failure_message: failure_message marks the task execution as failed and provides a message
              explaining the failure.

              If an individual step has failed, callers are NOT expected to set this message;
              only if the task execution as a whole has failed/cannot be started.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update_task_execution_status(
        self,
        *,
        log_url: str,
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
          log_url: log_url is the URL to the logs of the task's steps. If this is empty, the task
              either has no logs or has not yet started.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["failure_message"], ["log_url"])
    async def update_task_execution_status(
        self,
        *,
        failure_message: str | NotGiven = NOT_GIVEN,
        log_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        return await self._post(
            "/gitpod.v1.EnvironmentAutomationService/UpdateTaskExecutionStatus",
            body=await async_maybe_transform(
                {
                    "failure_message": failure_message,
                    "log_url": log_url,
                },
                task_execution_update_task_execution_status_params.TaskExecutionUpdateTaskExecutionStatusParams,
            ),
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
        self.stop = to_raw_response_wrapper(
            task_executions.stop,
        )
        self.update_task_execution_status = to_raw_response_wrapper(
            task_executions.update_task_execution_status,
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
        self.stop = async_to_raw_response_wrapper(
            task_executions.stop,
        )
        self.update_task_execution_status = async_to_raw_response_wrapper(
            task_executions.update_task_execution_status,
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
        self.stop = to_streamed_response_wrapper(
            task_executions.stop,
        )
        self.update_task_execution_status = to_streamed_response_wrapper(
            task_executions.update_task_execution_status,
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
        self.stop = async_to_streamed_response_wrapper(
            task_executions.stop,
        )
        self.update_task_execution_status = async_to_streamed_response_wrapper(
            task_executions.update_task_execution_status,
        )
