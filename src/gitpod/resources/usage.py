# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import usage_list_environment_runtime_records_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncRecordsPage, AsyncRecordsPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.environment_usage_record import EnvironmentUsageRecord

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

    def list_environment_runtime_records(
        self,
        *,
        token: str | Omit = omit,
        page_size: int | Omit = omit,
        filter: usage_list_environment_runtime_records_params.Filter | Omit = omit,
        pagination: usage_list_environment_runtime_records_params.Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncRecordsPage[EnvironmentUsageRecord]:
        """
        Lists completed environment runtime records within a specified date range.

        Returns a list of environment runtime records that were completed within the
        specified date range. Records of currently running environments are not
        included.

        Use this method to:

        - View environment runtime records
        - Filter by project
        - Create custom usage reports

        ### Example

        ```yaml
        filter:
          projectId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          dateRange:
            startTime: "2024-01-01T00:00:00Z"
            endTime: "2024-01-02T00:00:00Z"
        pagination:
          pageSize: 100
        ```

        Args:
          filter: Filter options.

          pagination: Pagination options.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.UsageService/ListEnvironmentUsageRecords",
            page=SyncRecordsPage[EnvironmentUsageRecord],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                usage_list_environment_runtime_records_params.UsageListEnvironmentRuntimeRecordsParams,
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
                    usage_list_environment_runtime_records_params.UsageListEnvironmentRuntimeRecordsParams,
                ),
            ),
            model=EnvironmentUsageRecord,
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

    def list_environment_runtime_records(
        self,
        *,
        token: str | Omit = omit,
        page_size: int | Omit = omit,
        filter: usage_list_environment_runtime_records_params.Filter | Omit = omit,
        pagination: usage_list_environment_runtime_records_params.Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[EnvironmentUsageRecord, AsyncRecordsPage[EnvironmentUsageRecord]]:
        """
        Lists completed environment runtime records within a specified date range.

        Returns a list of environment runtime records that were completed within the
        specified date range. Records of currently running environments are not
        included.

        Use this method to:

        - View environment runtime records
        - Filter by project
        - Create custom usage reports

        ### Example

        ```yaml
        filter:
          projectId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          dateRange:
            startTime: "2024-01-01T00:00:00Z"
            endTime: "2024-01-02T00:00:00Z"
        pagination:
          pageSize: 100
        ```

        Args:
          filter: Filter options.

          pagination: Pagination options.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.UsageService/ListEnvironmentUsageRecords",
            page=AsyncRecordsPage[EnvironmentUsageRecord],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                usage_list_environment_runtime_records_params.UsageListEnvironmentRuntimeRecordsParams,
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
                    usage_list_environment_runtime_records_params.UsageListEnvironmentRuntimeRecordsParams,
                ),
            ),
            model=EnvironmentUsageRecord,
            method="post",
        )


class UsageResourceWithRawResponse:
    def __init__(self, usage: UsageResource) -> None:
        self._usage = usage

        self.list_environment_runtime_records = to_raw_response_wrapper(
            usage.list_environment_runtime_records,
        )


class AsyncUsageResourceWithRawResponse:
    def __init__(self, usage: AsyncUsageResource) -> None:
        self._usage = usage

        self.list_environment_runtime_records = async_to_raw_response_wrapper(
            usage.list_environment_runtime_records,
        )


class UsageResourceWithStreamingResponse:
    def __init__(self, usage: UsageResource) -> None:
        self._usage = usage

        self.list_environment_runtime_records = to_streamed_response_wrapper(
            usage.list_environment_runtime_records,
        )


class AsyncUsageResourceWithStreamingResponse:
    def __init__(self, usage: AsyncUsageResource) -> None:
        self._usage = usage

        self.list_environment_runtime_records = async_to_streamed_response_wrapper(
            usage.list_environment_runtime_records,
        )
