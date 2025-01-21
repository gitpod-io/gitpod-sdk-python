# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
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
from ...types.runner_interactions import (
    environment_list_params,
    environment_retrieve_params,
    environment_update_status_params,
)
from ...types.runner_interactions.environment_list_response import EnvironmentListResponse
from ...types.runner_interactions.environment_retrieve_response import EnvironmentRetrieveResponse

__all__ = ["EnvironmentsResource", "AsyncEnvironmentsResource"]


class EnvironmentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EnvironmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return EnvironmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EnvironmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return EnvironmentsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        connect_protocol_version: Literal[1],
        environment_id: str | NotGiven = NOT_GIVEN,
        runner_id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnvironmentRetrieveResponse:
        """
        GetRunnerEnvironment returns the environment given it is owned by the runner.

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          environment_id: The environment's ID

          runner_id: The runner's identity

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
            "/gitpod.v1.RunnerInteractionService/GetRunnerEnvironment",
            body=maybe_transform(
                {
                    "environment_id": environment_id,
                    "runner_id": runner_id,
                },
                environment_retrieve_params.EnvironmentRetrieveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvironmentRetrieveResponse,
        )

    def list(
        self,
        *,
        connect_protocol_version: Literal[1],
        environment_ids: List[str] | NotGiven = NOT_GIVEN,
        pagination: environment_list_params.Pagination | NotGiven = NOT_GIVEN,
        runner_id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnvironmentListResponse:
        """
        ListRunnerEnvironments returns the environments this runner is responsible for.

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          environment_ids: An optional list of environment IDs to fetch. If this list is empty/not provided
              all environments that ought to run on the runner are returned.

          pagination: pagination contains the pagination options for listing environments

          runner_id: The runner's identifier

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
            "/gitpod.v1.RunnerInteractionService/ListRunnerEnvironments",
            body=maybe_transform(
                {
                    "environment_ids": environment_ids,
                    "pagination": pagination,
                    "runner_id": runner_id,
                },
                environment_list_params.EnvironmentListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvironmentListResponse,
        )

    def update_status(
        self,
        *,
        connect_protocol_version: Literal[1],
        environment_id: str | NotGiven = NOT_GIVEN,
        runner_id: str | NotGiven = NOT_GIVEN,
        status: environment_update_status_params.Status | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        UpdateRunnerEnvironmentStatus updates the status of an environment this runner
        is responsible for.

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          environment_id: The environment's ID

          runner_id: The runner's identity

          status: EnvironmentStatus describes an environment status

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
            "/gitpod.v1.RunnerInteractionService/UpdateRunnerEnvironmentStatus",
            body=maybe_transform(
                {
                    "environment_id": environment_id,
                    "runner_id": runner_id,
                    "status": status,
                },
                environment_update_status_params.EnvironmentUpdateStatusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncEnvironmentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEnvironmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEnvironmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEnvironmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return AsyncEnvironmentsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        connect_protocol_version: Literal[1],
        environment_id: str | NotGiven = NOT_GIVEN,
        runner_id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnvironmentRetrieveResponse:
        """
        GetRunnerEnvironment returns the environment given it is owned by the runner.

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          environment_id: The environment's ID

          runner_id: The runner's identity

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
            "/gitpod.v1.RunnerInteractionService/GetRunnerEnvironment",
            body=await async_maybe_transform(
                {
                    "environment_id": environment_id,
                    "runner_id": runner_id,
                },
                environment_retrieve_params.EnvironmentRetrieveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvironmentRetrieveResponse,
        )

    async def list(
        self,
        *,
        connect_protocol_version: Literal[1],
        environment_ids: List[str] | NotGiven = NOT_GIVEN,
        pagination: environment_list_params.Pagination | NotGiven = NOT_GIVEN,
        runner_id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnvironmentListResponse:
        """
        ListRunnerEnvironments returns the environments this runner is responsible for.

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          environment_ids: An optional list of environment IDs to fetch. If this list is empty/not provided
              all environments that ought to run on the runner are returned.

          pagination: pagination contains the pagination options for listing environments

          runner_id: The runner's identifier

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
            "/gitpod.v1.RunnerInteractionService/ListRunnerEnvironments",
            body=await async_maybe_transform(
                {
                    "environment_ids": environment_ids,
                    "pagination": pagination,
                    "runner_id": runner_id,
                },
                environment_list_params.EnvironmentListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvironmentListResponse,
        )

    async def update_status(
        self,
        *,
        connect_protocol_version: Literal[1],
        environment_id: str | NotGiven = NOT_GIVEN,
        runner_id: str | NotGiven = NOT_GIVEN,
        status: environment_update_status_params.Status | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        UpdateRunnerEnvironmentStatus updates the status of an environment this runner
        is responsible for.

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          environment_id: The environment's ID

          runner_id: The runner's identity

          status: EnvironmentStatus describes an environment status

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
            "/gitpod.v1.RunnerInteractionService/UpdateRunnerEnvironmentStatus",
            body=await async_maybe_transform(
                {
                    "environment_id": environment_id,
                    "runner_id": runner_id,
                    "status": status,
                },
                environment_update_status_params.EnvironmentUpdateStatusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class EnvironmentsResourceWithRawResponse:
    def __init__(self, environments: EnvironmentsResource) -> None:
        self._environments = environments

        self.retrieve = to_raw_response_wrapper(
            environments.retrieve,
        )
        self.list = to_raw_response_wrapper(
            environments.list,
        )
        self.update_status = to_raw_response_wrapper(
            environments.update_status,
        )


class AsyncEnvironmentsResourceWithRawResponse:
    def __init__(self, environments: AsyncEnvironmentsResource) -> None:
        self._environments = environments

        self.retrieve = async_to_raw_response_wrapper(
            environments.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            environments.list,
        )
        self.update_status = async_to_raw_response_wrapper(
            environments.update_status,
        )


class EnvironmentsResourceWithStreamingResponse:
    def __init__(self, environments: EnvironmentsResource) -> None:
        self._environments = environments

        self.retrieve = to_streamed_response_wrapper(
            environments.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            environments.list,
        )
        self.update_status = to_streamed_response_wrapper(
            environments.update_status,
        )


class AsyncEnvironmentsResourceWithStreamingResponse:
    def __init__(self, environments: AsyncEnvironmentsResource) -> None:
        self._environments = environments

        self.retrieve = async_to_streamed_response_wrapper(
            environments.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            environments.list,
        )
        self.update_status = async_to_streamed_response_wrapper(
            environments.update_status,
        )
