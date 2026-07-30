# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    Resolution,
    usage_get_pr_summary_params,
    usage_get_pr_time_series_params,
    usage_get_co_author_summary_params,
    usage_get_agent_trace_summary_params,
    usage_get_co_author_time_series_params,
    usage_get_adoption_usage_summary_params,
    usage_get_agent_trace_time_series_params,
    usage_list_environment_runtime_records_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
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
from ..types.resolution import Resolution
from ..types.environment_usage_record import EnvironmentUsageRecord
from ..types.shared_params.date_range import DateRange
from ..types.usage_get_pr_summary_response import UsageGetPrSummaryResponse
from ..types.usage_get_pr_time_series_response import UsageGetPrTimeSeriesResponse
from ..types.usage_get_co_author_summary_response import UsageGetCoAuthorSummaryResponse
from ..types.usage_get_agent_trace_summary_response import UsageGetAgentTraceSummaryResponse
from ..types.usage_get_co_author_time_series_response import UsageGetCoAuthorTimeSeriesResponse
from ..types.usage_get_adoption_usage_summary_response import UsageGetAdoptionUsageSummaryResponse
from ..types.usage_get_agent_trace_time_series_response import UsageGetAgentTraceTimeSeriesResponse

__all__ = ["UsageResource", "AsyncUsageResource"]


class UsageResource(SyncAPIResource):
    """
    UsageService provides usage information about environments, users, and projects.
    """

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

    def get_adoption_usage_summary(
        self,
        *,
        date_range: DateRange,
        project_id: str | Omit = omit,
        team_id: str | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageGetAdoptionUsageSummaryResponse:
        """
        Gets a summary of adoption and usage metrics.

        Returns all scalar values, trends, and a sparkline for the Adoption & Usage
        insight category. For full-resolution time series, use the individual time
        series RPCs.

        Use this method to:

        - Build adoption and usage insight cards
        - Filter adoption metrics by project, user, or team
        - Compare the requested date range against the previous period

        ### Example

        ```yaml
        dateRange:
          startTime: "2024-01-01T00:00:00Z"
          endTime: "2024-02-01T00:00:00Z"
        projectId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
        ```

        Args:
          date_range: Date range to query metrics within.

          project_id: Optional project ID to filter metrics by.

          team_id: Optional team ID to scope results to members of a specific team.

          user_id: Optional user ID to filter metrics for a specific user (personal insights view).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.UsageService/GetAdoptionUsageSummary",
            body=maybe_transform(
                {
                    "date_range": date_range,
                    "project_id": project_id,
                    "team_id": team_id,
                    "user_id": user_id,
                },
                usage_get_adoption_usage_summary_params.UsageGetAdoptionUsageSummaryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsageGetAdoptionUsageSummaryResponse,
        )

    def get_agent_trace_summary(
        self,
        *,
        date_range: DateRange,
        project_id: str | Omit = omit,
        team_id: str | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageGetAgentTraceSummaryResponse:
        """
        Gets aggregated agent trace summary for the organization or a specific project.

        Use this method to:

        - Measure agent sessions and line changes
        - Break down agent activity by model
        - Scope agent trace insights to a project, user, or team

        ### Example

        ```yaml
        dateRange:
          startTime: "2024-01-01T00:00:00Z"
          endTime: "2024-02-01T00:00:00Z"
        projectId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
        ```

        Args:
          date_range: Date range to query within.

          project_id: Optional project ID to scope results.

          team_id: Optional team ID to scope results to a specific team. Mutually exclusive with
              user_id.

          user_id: Optional user ID to scope results to a specific user. Mutually exclusive with
              team_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.UsageService/GetAgentTraceSummary",
            body=maybe_transform(
                {
                    "date_range": date_range,
                    "project_id": project_id,
                    "team_id": team_id,
                    "user_id": user_id,
                },
                usage_get_agent_trace_summary_params.UsageGetAgentTraceSummaryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsageGetAgentTraceSummaryResponse,
        )

    def get_agent_trace_time_series(
        self,
        *,
        date_range: DateRange,
        project_id: str | Omit = omit,
        resolution: Resolution | Omit = omit,
        team_id: str | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageGetAgentTraceTimeSeriesResponse:
        """
        Gets agent trace data as a time series.

        Use this method to:

        - Chart agent sessions and line changes over time
        - Select hourly, daily, weekly, or monthly buckets
        - Scope agent trace insights to a project, user, or team

        ### Example

        ```yaml
        dateRange:
          startTime: "2024-01-01T00:00:00Z"
          endTime: "2024-02-01T00:00:00Z"
        resolution: RESOLUTION_WEEKLY
        projectId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
        ```

        Args:
          date_range: Date range to query within.

          project_id: Optional project ID to scope results.

          resolution: Time resolution for the series data.

          team_id: Optional team ID to scope results to a specific team. Mutually exclusive with
              user_id.

          user_id: Optional user ID to scope results to a specific user. Mutually exclusive with
              team_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.UsageService/GetAgentTraceTimeSeries",
            body=maybe_transform(
                {
                    "date_range": date_range,
                    "project_id": project_id,
                    "resolution": resolution,
                    "team_id": team_id,
                    "user_id": user_id,
                },
                usage_get_agent_trace_time_series_params.UsageGetAgentTraceTimeSeriesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsageGetAgentTraceTimeSeriesResponse,
        )

    def get_co_author_summary(
        self,
        *,
        date_range: DateRange,
        project_id: str | Omit = omit,
        team_id: str | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageGetCoAuthorSummaryResponse:
        """
        Gets aggregated co-author summary for the organization or a specific project.

        Use this method to:

        - Measure AI-assisted commits and line changes
        - Scope co-author insights to a project, user, or team
        - Compare the requested date range against the previous period

        ### Example

        ```yaml
        dateRange:
          startTime: "2024-01-01T00:00:00Z"
          endTime: "2024-02-01T00:00:00Z"
        projectId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
        ```

        Args:
          date_range: Date range to query within.

          project_id: Optional project ID to scope results.

          team_id: Optional team ID to scope results to a specific team. Mutually exclusive with
              user_id.

          user_id: Optional user ID to scope results to a specific user. Mutually exclusive with
              team_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.UsageService/GetCoAuthorSummary",
            body=maybe_transform(
                {
                    "date_range": date_range,
                    "project_id": project_id,
                    "team_id": team_id,
                    "user_id": user_id,
                },
                usage_get_co_author_summary_params.UsageGetCoAuthorSummaryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsageGetCoAuthorSummaryResponse,
        )

    def get_co_author_time_series(
        self,
        *,
        date_range: DateRange,
        project_id: str | Omit = omit,
        resolution: Resolution | Omit = omit,
        team_id: str | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageGetCoAuthorTimeSeriesResponse:
        """
        Gets co-author contribution data as a time series.

        Use this method to:

        - Chart AI-assisted commits and line changes over time
        - Select hourly, daily, weekly, or monthly buckets
        - Scope co-author insights to a project, user, or team

        ### Example

        ```yaml
        dateRange:
          startTime: "2024-01-01T00:00:00Z"
          endTime: "2024-02-01T00:00:00Z"
        resolution: RESOLUTION_WEEKLY
        projectId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
        ```

        Args:
          date_range: Date range to query within.

          project_id: Optional project ID to scope results.

          resolution: Time resolution for the series data.

          team_id: Optional team ID to scope results to a specific team. Mutually exclusive with
              user_id.

          user_id: Optional user ID to scope results to a specific user. Mutually exclusive with
              team_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.UsageService/GetCoAuthorTimeSeries",
            body=maybe_transform(
                {
                    "date_range": date_range,
                    "project_id": project_id,
                    "resolution": resolution,
                    "team_id": team_id,
                    "user_id": user_id,
                },
                usage_get_co_author_time_series_params.UsageGetCoAuthorTimeSeriesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsageGetCoAuthorTimeSeriesResponse,
        )

    def get_pr_summary(
        self,
        *,
        date_range: DateRange,
        project_id: str | Omit = omit,
        team_id: str | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageGetPrSummaryResponse:
        """
        Gets aggregated PR speed summary for the organization or a specific project.

        Use this method to:

        - Measure pull request lead time and review latency
        - Calculate deployment frequency from merged pull requests
        - Scope PR speed insights to a project, user, or team

        ### Example

        ```yaml
        dateRange:
          startTime: "2024-01-01T00:00:00Z"
          endTime: "2024-02-01T00:00:00Z"
        projectId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
        ```

        Args:
          date_range: Date range to query within.

          project_id: Optional project ID to scope results.

          team_id: Optional team ID to scope results to a specific team. Mutually exclusive with
              user_id.

          user_id: Optional user ID to scope results to a specific user. Mutually exclusive with
              team_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.UsageService/GetPrSummary",
            body=maybe_transform(
                {
                    "date_range": date_range,
                    "project_id": project_id,
                    "team_id": team_id,
                    "user_id": user_id,
                },
                usage_get_pr_summary_params.UsageGetPrSummaryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsageGetPrSummaryResponse,
        )

    def get_pr_time_series(
        self,
        *,
        date_range: DateRange,
        project_id: str | Omit = omit,
        resolution: Resolution | Omit = omit,
        team_id: str | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageGetPrTimeSeriesResponse:
        """
        Gets PR speed metrics as a time series.

        Use this method to:

        - Chart pull request lead time, review latency, and deploy counts
        - Select hourly, daily, weekly, or monthly buckets
        - Scope PR speed insights to a project, user, or team

        ### Example

        ```yaml
        dateRange:
          startTime: "2024-01-01T00:00:00Z"
          endTime: "2024-02-01T00:00:00Z"
        resolution: RESOLUTION_WEEKLY
        projectId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
        ```

        Args:
          date_range: Date range to query within.

          project_id: Optional project ID to scope results.

          resolution: Time resolution for the series data.

          team_id: Optional team ID to scope results to a specific team. Mutually exclusive with
              user_id.

          user_id: Optional user ID to scope results to a specific user. Mutually exclusive with
              team_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.UsageService/GetPrTimeSeries",
            body=maybe_transform(
                {
                    "date_range": date_range,
                    "project_id": project_id,
                    "resolution": resolution,
                    "team_id": team_id,
                    "user_id": user_id,
                },
                usage_get_pr_time_series_params.UsageGetPrTimeSeriesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsageGetPrTimeSeriesResponse,
        )

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
    """
    UsageService provides usage information about environments, users, and projects.
    """

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

    async def get_adoption_usage_summary(
        self,
        *,
        date_range: DateRange,
        project_id: str | Omit = omit,
        team_id: str | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageGetAdoptionUsageSummaryResponse:
        """
        Gets a summary of adoption and usage metrics.

        Returns all scalar values, trends, and a sparkline for the Adoption & Usage
        insight category. For full-resolution time series, use the individual time
        series RPCs.

        Use this method to:

        - Build adoption and usage insight cards
        - Filter adoption metrics by project, user, or team
        - Compare the requested date range against the previous period

        ### Example

        ```yaml
        dateRange:
          startTime: "2024-01-01T00:00:00Z"
          endTime: "2024-02-01T00:00:00Z"
        projectId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
        ```

        Args:
          date_range: Date range to query metrics within.

          project_id: Optional project ID to filter metrics by.

          team_id: Optional team ID to scope results to members of a specific team.

          user_id: Optional user ID to filter metrics for a specific user (personal insights view).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.UsageService/GetAdoptionUsageSummary",
            body=await async_maybe_transform(
                {
                    "date_range": date_range,
                    "project_id": project_id,
                    "team_id": team_id,
                    "user_id": user_id,
                },
                usage_get_adoption_usage_summary_params.UsageGetAdoptionUsageSummaryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsageGetAdoptionUsageSummaryResponse,
        )

    async def get_agent_trace_summary(
        self,
        *,
        date_range: DateRange,
        project_id: str | Omit = omit,
        team_id: str | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageGetAgentTraceSummaryResponse:
        """
        Gets aggregated agent trace summary for the organization or a specific project.

        Use this method to:

        - Measure agent sessions and line changes
        - Break down agent activity by model
        - Scope agent trace insights to a project, user, or team

        ### Example

        ```yaml
        dateRange:
          startTime: "2024-01-01T00:00:00Z"
          endTime: "2024-02-01T00:00:00Z"
        projectId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
        ```

        Args:
          date_range: Date range to query within.

          project_id: Optional project ID to scope results.

          team_id: Optional team ID to scope results to a specific team. Mutually exclusive with
              user_id.

          user_id: Optional user ID to scope results to a specific user. Mutually exclusive with
              team_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.UsageService/GetAgentTraceSummary",
            body=await async_maybe_transform(
                {
                    "date_range": date_range,
                    "project_id": project_id,
                    "team_id": team_id,
                    "user_id": user_id,
                },
                usage_get_agent_trace_summary_params.UsageGetAgentTraceSummaryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsageGetAgentTraceSummaryResponse,
        )

    async def get_agent_trace_time_series(
        self,
        *,
        date_range: DateRange,
        project_id: str | Omit = omit,
        resolution: Resolution | Omit = omit,
        team_id: str | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageGetAgentTraceTimeSeriesResponse:
        """
        Gets agent trace data as a time series.

        Use this method to:

        - Chart agent sessions and line changes over time
        - Select hourly, daily, weekly, or monthly buckets
        - Scope agent trace insights to a project, user, or team

        ### Example

        ```yaml
        dateRange:
          startTime: "2024-01-01T00:00:00Z"
          endTime: "2024-02-01T00:00:00Z"
        resolution: RESOLUTION_WEEKLY
        projectId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
        ```

        Args:
          date_range: Date range to query within.

          project_id: Optional project ID to scope results.

          resolution: Time resolution for the series data.

          team_id: Optional team ID to scope results to a specific team. Mutually exclusive with
              user_id.

          user_id: Optional user ID to scope results to a specific user. Mutually exclusive with
              team_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.UsageService/GetAgentTraceTimeSeries",
            body=await async_maybe_transform(
                {
                    "date_range": date_range,
                    "project_id": project_id,
                    "resolution": resolution,
                    "team_id": team_id,
                    "user_id": user_id,
                },
                usage_get_agent_trace_time_series_params.UsageGetAgentTraceTimeSeriesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsageGetAgentTraceTimeSeriesResponse,
        )

    async def get_co_author_summary(
        self,
        *,
        date_range: DateRange,
        project_id: str | Omit = omit,
        team_id: str | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageGetCoAuthorSummaryResponse:
        """
        Gets aggregated co-author summary for the organization or a specific project.

        Use this method to:

        - Measure AI-assisted commits and line changes
        - Scope co-author insights to a project, user, or team
        - Compare the requested date range against the previous period

        ### Example

        ```yaml
        dateRange:
          startTime: "2024-01-01T00:00:00Z"
          endTime: "2024-02-01T00:00:00Z"
        projectId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
        ```

        Args:
          date_range: Date range to query within.

          project_id: Optional project ID to scope results.

          team_id: Optional team ID to scope results to a specific team. Mutually exclusive with
              user_id.

          user_id: Optional user ID to scope results to a specific user. Mutually exclusive with
              team_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.UsageService/GetCoAuthorSummary",
            body=await async_maybe_transform(
                {
                    "date_range": date_range,
                    "project_id": project_id,
                    "team_id": team_id,
                    "user_id": user_id,
                },
                usage_get_co_author_summary_params.UsageGetCoAuthorSummaryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsageGetCoAuthorSummaryResponse,
        )

    async def get_co_author_time_series(
        self,
        *,
        date_range: DateRange,
        project_id: str | Omit = omit,
        resolution: Resolution | Omit = omit,
        team_id: str | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageGetCoAuthorTimeSeriesResponse:
        """
        Gets co-author contribution data as a time series.

        Use this method to:

        - Chart AI-assisted commits and line changes over time
        - Select hourly, daily, weekly, or monthly buckets
        - Scope co-author insights to a project, user, or team

        ### Example

        ```yaml
        dateRange:
          startTime: "2024-01-01T00:00:00Z"
          endTime: "2024-02-01T00:00:00Z"
        resolution: RESOLUTION_WEEKLY
        projectId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
        ```

        Args:
          date_range: Date range to query within.

          project_id: Optional project ID to scope results.

          resolution: Time resolution for the series data.

          team_id: Optional team ID to scope results to a specific team. Mutually exclusive with
              user_id.

          user_id: Optional user ID to scope results to a specific user. Mutually exclusive with
              team_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.UsageService/GetCoAuthorTimeSeries",
            body=await async_maybe_transform(
                {
                    "date_range": date_range,
                    "project_id": project_id,
                    "resolution": resolution,
                    "team_id": team_id,
                    "user_id": user_id,
                },
                usage_get_co_author_time_series_params.UsageGetCoAuthorTimeSeriesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsageGetCoAuthorTimeSeriesResponse,
        )

    async def get_pr_summary(
        self,
        *,
        date_range: DateRange,
        project_id: str | Omit = omit,
        team_id: str | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageGetPrSummaryResponse:
        """
        Gets aggregated PR speed summary for the organization or a specific project.

        Use this method to:

        - Measure pull request lead time and review latency
        - Calculate deployment frequency from merged pull requests
        - Scope PR speed insights to a project, user, or team

        ### Example

        ```yaml
        dateRange:
          startTime: "2024-01-01T00:00:00Z"
          endTime: "2024-02-01T00:00:00Z"
        projectId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
        ```

        Args:
          date_range: Date range to query within.

          project_id: Optional project ID to scope results.

          team_id: Optional team ID to scope results to a specific team. Mutually exclusive with
              user_id.

          user_id: Optional user ID to scope results to a specific user. Mutually exclusive with
              team_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.UsageService/GetPrSummary",
            body=await async_maybe_transform(
                {
                    "date_range": date_range,
                    "project_id": project_id,
                    "team_id": team_id,
                    "user_id": user_id,
                },
                usage_get_pr_summary_params.UsageGetPrSummaryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsageGetPrSummaryResponse,
        )

    async def get_pr_time_series(
        self,
        *,
        date_range: DateRange,
        project_id: str | Omit = omit,
        resolution: Resolution | Omit = omit,
        team_id: str | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageGetPrTimeSeriesResponse:
        """
        Gets PR speed metrics as a time series.

        Use this method to:

        - Chart pull request lead time, review latency, and deploy counts
        - Select hourly, daily, weekly, or monthly buckets
        - Scope PR speed insights to a project, user, or team

        ### Example

        ```yaml
        dateRange:
          startTime: "2024-01-01T00:00:00Z"
          endTime: "2024-02-01T00:00:00Z"
        resolution: RESOLUTION_WEEKLY
        projectId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
        ```

        Args:
          date_range: Date range to query within.

          project_id: Optional project ID to scope results.

          resolution: Time resolution for the series data.

          team_id: Optional team ID to scope results to a specific team. Mutually exclusive with
              user_id.

          user_id: Optional user ID to scope results to a specific user. Mutually exclusive with
              team_id.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.UsageService/GetPrTimeSeries",
            body=await async_maybe_transform(
                {
                    "date_range": date_range,
                    "project_id": project_id,
                    "resolution": resolution,
                    "team_id": team_id,
                    "user_id": user_id,
                },
                usage_get_pr_time_series_params.UsageGetPrTimeSeriesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsageGetPrTimeSeriesResponse,
        )

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

        self.get_adoption_usage_summary = to_raw_response_wrapper(
            usage.get_adoption_usage_summary,
        )
        self.get_agent_trace_summary = to_raw_response_wrapper(
            usage.get_agent_trace_summary,
        )
        self.get_agent_trace_time_series = to_raw_response_wrapper(
            usage.get_agent_trace_time_series,
        )
        self.get_co_author_summary = to_raw_response_wrapper(
            usage.get_co_author_summary,
        )
        self.get_co_author_time_series = to_raw_response_wrapper(
            usage.get_co_author_time_series,
        )
        self.get_pr_summary = to_raw_response_wrapper(
            usage.get_pr_summary,
        )
        self.get_pr_time_series = to_raw_response_wrapper(
            usage.get_pr_time_series,
        )
        self.list_environment_runtime_records = to_raw_response_wrapper(
            usage.list_environment_runtime_records,
        )


class AsyncUsageResourceWithRawResponse:
    def __init__(self, usage: AsyncUsageResource) -> None:
        self._usage = usage

        self.get_adoption_usage_summary = async_to_raw_response_wrapper(
            usage.get_adoption_usage_summary,
        )
        self.get_agent_trace_summary = async_to_raw_response_wrapper(
            usage.get_agent_trace_summary,
        )
        self.get_agent_trace_time_series = async_to_raw_response_wrapper(
            usage.get_agent_trace_time_series,
        )
        self.get_co_author_summary = async_to_raw_response_wrapper(
            usage.get_co_author_summary,
        )
        self.get_co_author_time_series = async_to_raw_response_wrapper(
            usage.get_co_author_time_series,
        )
        self.get_pr_summary = async_to_raw_response_wrapper(
            usage.get_pr_summary,
        )
        self.get_pr_time_series = async_to_raw_response_wrapper(
            usage.get_pr_time_series,
        )
        self.list_environment_runtime_records = async_to_raw_response_wrapper(
            usage.list_environment_runtime_records,
        )


class UsageResourceWithStreamingResponse:
    def __init__(self, usage: UsageResource) -> None:
        self._usage = usage

        self.get_adoption_usage_summary = to_streamed_response_wrapper(
            usage.get_adoption_usage_summary,
        )
        self.get_agent_trace_summary = to_streamed_response_wrapper(
            usage.get_agent_trace_summary,
        )
        self.get_agent_trace_time_series = to_streamed_response_wrapper(
            usage.get_agent_trace_time_series,
        )
        self.get_co_author_summary = to_streamed_response_wrapper(
            usage.get_co_author_summary,
        )
        self.get_co_author_time_series = to_streamed_response_wrapper(
            usage.get_co_author_time_series,
        )
        self.get_pr_summary = to_streamed_response_wrapper(
            usage.get_pr_summary,
        )
        self.get_pr_time_series = to_streamed_response_wrapper(
            usage.get_pr_time_series,
        )
        self.list_environment_runtime_records = to_streamed_response_wrapper(
            usage.list_environment_runtime_records,
        )


class AsyncUsageResourceWithStreamingResponse:
    def __init__(self, usage: AsyncUsageResource) -> None:
        self._usage = usage

        self.get_adoption_usage_summary = async_to_streamed_response_wrapper(
            usage.get_adoption_usage_summary,
        )
        self.get_agent_trace_summary = async_to_streamed_response_wrapper(
            usage.get_agent_trace_summary,
        )
        self.get_agent_trace_time_series = async_to_streamed_response_wrapper(
            usage.get_agent_trace_time_series,
        )
        self.get_co_author_summary = async_to_streamed_response_wrapper(
            usage.get_co_author_summary,
        )
        self.get_co_author_time_series = async_to_streamed_response_wrapper(
            usage.get_co_author_time_series,
        )
        self.get_pr_summary = async_to_streamed_response_wrapper(
            usage.get_pr_summary,
        )
        self.get_pr_time_series = async_to_streamed_response_wrapper(
            usage.get_pr_time_series,
        )
        self.list_environment_runtime_records = async_to_streamed_response_wrapper(
            usage.list_environment_runtime_records,
        )
