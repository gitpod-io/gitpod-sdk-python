# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import usage_list_environment_sessions_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncSessionsPage, AsyncSessionsPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.environment_session import EnvironmentSession

__all__ = ["UsageResource", "AsyncUsageResource"]


class UsageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UsageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return UsageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return UsageResourceWithStreamingResponse(self)

    def list_environment_sessions(
        self,
        *,
        token: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        filter: usage_list_environment_sessions_params.Filter | NotGiven = NOT_GIVEN,
        pagination: usage_list_environment_sessions_params.Pagination | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSessionsPage[EnvironmentSession]:
        """
        Lists environment sessions within a specified date range.

        Returns a list of environment sessions that were active within the specified
        date range.

        Args:
          filter: Filter options.

          pagination: Pagination options.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.UsageService/ListEnvironmentSessions",
            page=SyncSessionsPage[EnvironmentSession],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                usage_list_environment_sessions_params.UsageListEnvironmentSessionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "token": token,
                        "page_size": page_size,
                    },
                    usage_list_environment_sessions_params.UsageListEnvironmentSessionsParams,
                ),
            ),
            model=EnvironmentSession,
            method="post",
        )


class AsyncUsageResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUsageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return AsyncUsageResourceWithStreamingResponse(self)

    def list_environment_sessions(
        self,
        *,
        token: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        filter: usage_list_environment_sessions_params.Filter | NotGiven = NOT_GIVEN,
        pagination: usage_list_environment_sessions_params.Pagination | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[EnvironmentSession, AsyncSessionsPage[EnvironmentSession]]:
        """
        Lists environment sessions within a specified date range.

        Returns a list of environment sessions that were active within the specified
        date range.

        Args:
          filter: Filter options.

          pagination: Pagination options.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.UsageService/ListEnvironmentSessions",
            page=AsyncSessionsPage[EnvironmentSession],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                usage_list_environment_sessions_params.UsageListEnvironmentSessionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "token": token,
                        "page_size": page_size,
                    },
                    usage_list_environment_sessions_params.UsageListEnvironmentSessionsParams,
                ),
            ),
            model=EnvironmentSession,
            method="post",
        )


class UsageResourceWithRawResponse:
    def __init__(self, usage: UsageResource) -> None:
        self._usage = usage

        self.list_environment_sessions = to_raw_response_wrapper(
            usage.list_environment_sessions,
        )


class AsyncUsageResourceWithRawResponse:
    def __init__(self, usage: AsyncUsageResource) -> None:
        self._usage = usage

        self.list_environment_sessions = async_to_raw_response_wrapper(
            usage.list_environment_sessions,
        )


class UsageResourceWithStreamingResponse:
    def __init__(self, usage: UsageResource) -> None:
        self._usage = usage

        self.list_environment_sessions = to_streamed_response_wrapper(
            usage.list_environment_sessions,
        )


class AsyncUsageResourceWithStreamingResponse:
    def __init__(self, usage: AsyncUsageResource) -> None:
        self._usage = usage

        self.list_environment_sessions = async_to_streamed_response_wrapper(
            usage.list_environment_sessions,
        )
