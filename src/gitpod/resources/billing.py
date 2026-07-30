# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from ..types import (
    CreditUsageExportGroupBy,
    billing_get_credit_usage_export_params,
    billing_get_credit_usage_report_params,
    billing_get_cumulative_credit_usage_params,
    billing_list_enterprise_ai_team_usage_params,
    billing_list_enterprise_ai_user_usage_params,
    billing_get_enterprise_ai_usage_summary_params,
    billing_list_enterprise_user_credit_usage_params,
    billing_get_enterprise_ai_usage_time_series_params,
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
from ..pagination import SyncTeamUsagePage, SyncUserUsagePage, AsyncTeamUsagePage, AsyncUserUsagePage
from .._base_client import AsyncPaginator, make_request_options
from ..types.user_cost_budget_usage import UserCostBudgetUsage
from ..types.shared_params.date_range import DateRange
from ..types.team_enterprise_ai_usage import TeamEnterpriseAIUsage
from ..types.user_credit_budget_usage import UserCreditBudgetUsage
from ..types.credit_usage_export_group_by import CreditUsageExportGroupBy
from ..types.credit_usage_report_filter_param import CreditUsageReportFilterParam
from ..types.billing_get_credit_usage_export_response import BillingGetCreditUsageExportResponse
from ..types.billing_get_credit_usage_report_response import BillingGetCreditUsageReportResponse
from ..types.billing_get_cumulative_credit_usage_response import BillingGetCumulativeCreditUsageResponse
from ..types.enterprise_ai_usage_time_series_filter_param import EnterpriseAIUsageTimeSeriesFilterParam
from ..types.billing_get_enterprise_ai_usage_summary_response import BillingGetEnterpriseAIUsageSummaryResponse
from ..types.billing_get_enterprise_ai_usage_time_series_response import BillingGetEnterpriseAIUsageTimeSeriesResponse

__all__ = ["BillingResource", "AsyncBillingResource"]


class BillingResource(SyncAPIResource):
    """BillingService provides billing and subscription management functionality."""

    @cached_property
    def with_raw_response(self) -> BillingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return BillingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BillingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return BillingResourceWithStreamingResponse(self)

    def get_credit_usage_export(
        self,
        *,
        date_range: DateRange,
        organization_id: str,
        group_by: CreditUsageExportGroupBy | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingGetCreditUsageExportResponse:
        """
        Returns a signed download URL for a CSV export of credit usage.

        The URL points to an HTTP endpoint that streams gzip-compressed CSV and is valid
        for five minutes. The download must be made by the same principal that requested
        it, carrying its own bearer token. The export range may cover up to a year.

        For organizations without enterprise credit usage enabled (no billing contract
        start date), the export instead contains BYOK cost usage with a different column
        set, and groupBy=RESOURCE is rejected.

        Use this method to:

        - Export per-user daily credit usage for external reporting
        - Export a per-environment and per-conversation resource breakdown

        ### Examples

        - Export January's daily summary:

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          dateRange:
            startTime: "2024-01-01T00:00:00Z"
            endTime: "2024-01-31T00:00:00Z"
          groupBy: CREDIT_USAGE_EXPORT_GROUP_BY_DAILY_SUMMARY
          ```

        ### Authorization

        Requires `billing:read_usage` permission on the organization.

        Args:
          date_range: Date range to export. Both start and end dates are inclusive; time-of-day is
              ignored. Unlike GetCreditUsageReport, the range may cover up to a year.

          group_by: How to group the export data. Defaults to DAILY_SUMMARY.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.BillingService/GetCreditUsageExport",
            body=maybe_transform(
                {
                    "date_range": date_range,
                    "organization_id": organization_id,
                    "group_by": group_by,
                },
                billing_get_credit_usage_export_params.BillingGetCreditUsageExportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingGetCreditUsageExportResponse,
        )

    def get_credit_usage_report(
        self,
        *,
        date_range: DateRange,
        organization_id: str,
        filter: CreditUsageReportFilterParam | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingGetCreditUsageReportResponse:
        """
        Returns a daily credit usage report for an enterprise organization.

        Each day reports org-wide credits by usage type, plus per-user, per-team,
        per-environment, and per-conversation breakdowns (top consumers with the
        remainder aggregated into an "Others" bucket) and a per-model breakdown of
        intelligence usage.

        Use this method to:

        - Chart daily credit consumption over a date range
        - Attribute credit usage to users, teams, environments, and conversations
        - Restrict the report to a single user or service account

        ### Examples

        - Get the report for January:

          Both dates are inclusive and the range must not exceed 31 days.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          dateRange:
            startTime: "2024-01-01T00:00:00Z"
            endTime: "2024-01-31T00:00:00Z"
          ```

        ### Authorization

        Requires `billing:read_usage` permission on the organization. A user without it
        can read their own usage by setting filter.subject to their own user identity;
        this self-access path is not available to service accounts.

        Args:
          date_range: Date range for the report. Both start and end dates are inclusive. Time-of-day
              is ignored; dates are truncated to midnight in the specified timezone. The range
              must not exceed 31 days.

          filter: Optional filter narrowing the returned data. When unset or empty, the response
              preserves the default behavior (top-N users + "Others"). See
              CreditUsageReportFilter for per-field response-scoping semantics.

          timezone: IANA timezone name (e.g. "America/New_York", "Europe/Berlin") used to bucket
              daily usage. When empty, defaults to "UTC".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.BillingService/GetCreditUsageReport",
            body=maybe_transform(
                {
                    "date_range": date_range,
                    "organization_id": organization_id,
                    "filter": filter,
                    "timezone": timezone,
                },
                billing_get_credit_usage_report_params.BillingGetCreditUsageReportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingGetCreditUsageReportResponse,
        )

    def get_cumulative_credit_usage(
        self,
        *,
        organization_id: str,
        as_of: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingGetCumulativeCreditUsageResponse:
        """
        Returns cumulative credit usage for an organization and its teams.

        Use this method to:

        - Get the total cumulative credit consumption as of a point in time
        - Get per-team cumulative usage with credit allocation (budget) comparison
        - Display team credit summaries on the usage page and team detail page
        - Display user budget utilization when user budgets are enabled

        ### Examples

        - Get current cumulative usage:

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          ```

        - Get cumulative usage as of a specific date:

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          asOf: "2026-03-31T23:59:59Z"
          ```

        ### Authorization

        Requires `billing:read_usage` permission on the organization.

        Args:
          organization_id: organization_id is the ID of the organization to get cumulative usage for.

          as_of: as_of is the point in time to compute cumulative usage up to. Defaults to now if
              not set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.BillingService/GetCumulativeCreditUsage",
            body=maybe_transform(
                {
                    "organization_id": organization_id,
                    "as_of": as_of,
                },
                billing_get_cumulative_credit_usage_params.BillingGetCumulativeCreditUsageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingGetCumulativeCreditUsageResponse,
        )

    def get_enterprise_ai_usage_summary(
        self,
        *,
        date_range: DateRange,
        organization_id: str,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingGetEnterpriseAIUsageSummaryResponse:
        """
        Returns organization-level enterprise AI usage totals for reporting.

        Reports BYOK (bring-your-own-key) token spend: cost in the organization's
        billing currency plus token counts, with a per-model breakdown. Credit-based
        usage from managed models is not included and the credits field is not populated
        by this endpoint.

        Use this method to:

        - Report total BYOK AI spend (cost and tokens) for a date range
        - Break down organization usage by model

        Only available for enterprise organizations.

        ### Examples

        - Get usage totals for January:

          Returns organization-wide BYOK spend for the month. Both dates are inclusive
          and the range must not exceed 31 days.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          dateRange:
            startTime: "2024-01-01T00:00:00Z"
            endTime: "2024-01-31T00:00:00Z"
          ```

        ### Authorization

        Requires `billing:read_usage` permission on the organization.

        Args:
          date_range: Date range for the summary. Both start and end dates are inclusive. Time-of-day
              is ignored; dates are truncated to midnight in the specified timezone.

          timezone: IANA timezone name used to bucket usage. When empty, defaults to "UTC".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.BillingService/GetEnterpriseAIUsageSummary",
            body=maybe_transform(
                {
                    "date_range": date_range,
                    "organization_id": organization_id,
                    "timezone": timezone,
                },
                billing_get_enterprise_ai_usage_summary_params.BillingGetEnterpriseAIUsageSummaryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingGetEnterpriseAIUsageSummaryResponse,
        )

    def get_enterprise_ai_usage_time_series(
        self,
        *,
        date_range: DateRange,
        organization_id: str,
        filter: EnterpriseAIUsageTimeSeriesFilterParam | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingGetEnterpriseAIUsageTimeSeriesResponse:
        """
        Returns daily enterprise AI usage totals for the organization.

        Each day reports BYOK token spend (cost and tokens) with per-user, per-team, and
        per-model breakdowns. Per-user entries cover the top spenders with the remainder
        aggregated into an "Others" bucket; usage not attributed to a user or service
        account appears only in the daily totals. The credits field is not populated by
        this endpoint.

        When filter.subject is set the response contains only that subject's usage:
        daily totals and the team breakdown are omitted, and the model breakdown covers
        the subject only.

        Use this method to:

        - Chart daily BYOK AI spend over a date range
        - Feed daily per-user usage into external dashboards
        - Restrict the response to a single user or service account

        Only available for enterprise organizations.

        ### Examples

        - Get daily usage for January:

          Returns one entry per day with per-user, per-team, and per-model breakdowns.
          Both dates are inclusive and the range must not exceed 31 days.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          dateRange:
            startTime: "2024-01-01T00:00:00Z"
            endTime: "2024-01-31T00:00:00Z"
          ```

        ### Authorization

        Requires `billing:read_usage` permission on the organization.

        Args:
          date_range: Date range for the daily usage series. Both start and end dates are inclusive.
              Time-of-day is ignored; dates are truncated to midnight in the specified
              timezone.

          timezone: IANA timezone name used to bucket daily usage. When empty, defaults to "UTC".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.BillingService/GetEnterpriseAIUsageTimeSeries",
            body=maybe_transform(
                {
                    "date_range": date_range,
                    "organization_id": organization_id,
                    "filter": filter,
                    "timezone": timezone,
                },
                billing_get_enterprise_ai_usage_time_series_params.BillingGetEnterpriseAIUsageTimeSeriesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingGetEnterpriseAIUsageTimeSeriesResponse,
        )

    def list_enterprise_ai_team_usage(
        self,
        *,
        date_range: DateRange,
        organization_id: str,
        token: str | Omit = omit,
        page_size: int | Omit = omit,
        filter: billing_list_enterprise_ai_team_usage_params.Filter | Omit = omit,
        pagination: billing_list_enterprise_ai_team_usage_params.Pagination | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncTeamUsagePage[TeamEnterpriseAIUsage]:
        """
        Lists enterprise AI usage grouped by team.

        Reports BYOK token spend per team (cost and tokens) with each team's monthly
        budget when one applies. The credits field is not populated by this endpoint.

        Use this method to:

        - Compare BYOK AI spend across teams
        - Track team budget utilization
        - Filter usage to specific teams

        Only available for enterprise organizations.

        ### Examples

        - List team usage for January:

          Returns BYOK spend per team with monthly budgets. Both dates are inclusive and
          the range must not exceed 31 days.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          dateRange:
            startTime: "2024-01-01T00:00:00Z"
            endTime: "2024-01-31T00:00:00Z"
          ```

        ### Authorization

        Requires `billing:read_usage` permission on the organization.

        Args:
          date_range: Date range for the team usage list. Both start and end dates are inclusive.
              Time-of-day is ignored; dates are truncated to midnight in the specified
              timezone.

          timezone: IANA timezone name used to bucket usage. When empty, defaults to "UTC".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.BillingService/ListEnterpriseAITeamUsage",
            page=SyncTeamUsagePage[TeamEnterpriseAIUsage],
            body=maybe_transform(
                {
                    "date_range": date_range,
                    "organization_id": organization_id,
                    "filter": filter,
                    "pagination": pagination,
                    "timezone": timezone,
                },
                billing_list_enterprise_ai_team_usage_params.BillingListEnterpriseAITeamUsageParams,
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
                    billing_list_enterprise_ai_team_usage_params.BillingListEnterpriseAITeamUsageParams,
                ),
            ),
            model=TeamEnterpriseAIUsage,
            method="post",
        )

    def list_enterprise_ai_user_usage(
        self,
        *,
        date_range: DateRange,
        organization_id: str,
        token: str | Omit = omit,
        page_size: int | Omit = omit,
        filter: billing_list_enterprise_ai_user_usage_params.Filter | Omit = omit,
        pagination: billing_list_enterprise_ai_user_usage_params.Pagination | Omit = omit,
        sort: billing_list_enterprise_ai_user_usage_params.Sort | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncUserUsagePage[UserCostBudgetUsage]:
        """
        Lists enterprise AI usage grouped by user with effective monthly budget data.

        Reports BYOK token spend (cost and tokens) for each user and service account
        with attributed usage in the date range, including each subject's effective
        monthly budget. Usage not attributed to a user or service account is excluded,
        so the sum across subjects can be less than the organization totals from
        GetEnterpriseAIUsageSummary. The credits field is not populated by this
        endpoint.

        Budget fields (month_to_date_usage, utilization_percent, over_budget) are
        computed from usage inside the requested date range measured against the monthly
        limit. Send a range that starts on the first day of the month for true
        month-to-date figures.

        Use this method to:

        - Export per-user BYOK AI spend to external reporting
        - Identify the highest spenders in the organization
        - Track per-user budget utilization and over-budget users

        Only available for enterprise organizations.

        ### Examples

        - List user usage for January:

          Returns per-user BYOK spend with effective budgets, highest spend first. Both
          dates are inclusive and the range must not exceed 31 days.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          dateRange:
            startTime: "2024-01-01T00:00:00Z"
            endTime: "2024-01-31T00:00:00Z"
          ```

        ### Authorization

        Requires `billing:read_usage` permission on the organization. Callers without it
        can read their own usage by setting filter.subject to themselves.

        Args:
          date_range: Date range for the user usage list. Both start and end dates are inclusive.
              Time-of-day is ignored; dates are truncated to midnight in the specified
              timezone.

          filter: Optional filter narrowing the returned user usage. When set to a subject, the
              response contains only usage for that user or service account.

          sort: sort controls the ordering of results. Defaults to total spend descending.

          timezone: IANA timezone name used to bucket usage. When empty, defaults to "UTC".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.BillingService/ListEnterpriseAIUserUsage",
            page=SyncUserUsagePage[UserCostBudgetUsage],
            body=maybe_transform(
                {
                    "date_range": date_range,
                    "organization_id": organization_id,
                    "filter": filter,
                    "pagination": pagination,
                    "sort": sort,
                    "timezone": timezone,
                },
                billing_list_enterprise_ai_user_usage_params.BillingListEnterpriseAIUserUsageParams,
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
                    billing_list_enterprise_ai_user_usage_params.BillingListEnterpriseAIUserUsageParams,
                ),
            ),
            model=UserCostBudgetUsage,
            method="post",
        )

    def list_enterprise_user_credit_usage(
        self,
        *,
        organization_id: str,
        token: str | Omit = omit,
        page_size: int | Omit = omit,
        as_of: Union[str, datetime, None] | Omit = omit,
        pagination: billing_list_enterprise_user_credit_usage_params.Pagination | Omit = omit,
        sort: billing_list_enterprise_user_credit_usage_params.Sort | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncUserUsagePage[UserCreditBudgetUsage]:
        """
        Lists per-user month-to-date credit usage with effective monthly budgets.

        Results are ordered by total credits descending so the highest spenders appear
        first, with user_id as a stable tiebreaker. Use cursor pagination to walk the
        full set for large organizations.

        The default SORT_FIELD_USAGE ordering supports cursor pagination over any number
        of users. Sorting by display name, budget, or budget utilization computes the
        order in memory and is limited to organizations with at most 10,000 users;
        beyond that, use SORT_FIELD_USAGE. Because month-to-date figures are recomputed
        per request, hold a date range stable across a paginated walk to keep page
        tokens valid.

        Use this method to:

        - Export per-user credit usage to external reporting
        - Identify the highest spenders in the organization
        - Track per-user budget utilization and over-budget users

        ### Examples

        - List user usage for the current month:

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          pagination:
            pageSize: 50
          ```

        ### Authorization

        Requires `billing:read_usage` permission on the organization.

        Args:
          organization_id: organization_id is the ID of the organization to list user credit usage for.

          as_of: as_of is the point in time to compute month-to-date usage up to. Defaults to now
              if not set.

          sort: sort controls the ordering of results. Defaults to total credits descending.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.BillingService/ListEnterpriseUserCreditUsage",
            page=SyncUserUsagePage[UserCreditBudgetUsage],
            body=maybe_transform(
                {
                    "organization_id": organization_id,
                    "as_of": as_of,
                    "pagination": pagination,
                    "sort": sort,
                },
                billing_list_enterprise_user_credit_usage_params.BillingListEnterpriseUserCreditUsageParams,
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
                    billing_list_enterprise_user_credit_usage_params.BillingListEnterpriseUserCreditUsageParams,
                ),
            ),
            model=UserCreditBudgetUsage,
            method="post",
        )


class AsyncBillingResource(AsyncAPIResource):
    """BillingService provides billing and subscription management functionality."""

    @cached_property
    def with_raw_response(self) -> AsyncBillingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBillingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBillingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return AsyncBillingResourceWithStreamingResponse(self)

    async def get_credit_usage_export(
        self,
        *,
        date_range: DateRange,
        organization_id: str,
        group_by: CreditUsageExportGroupBy | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingGetCreditUsageExportResponse:
        """
        Returns a signed download URL for a CSV export of credit usage.

        The URL points to an HTTP endpoint that streams gzip-compressed CSV and is valid
        for five minutes. The download must be made by the same principal that requested
        it, carrying its own bearer token. The export range may cover up to a year.

        For organizations without enterprise credit usage enabled (no billing contract
        start date), the export instead contains BYOK cost usage with a different column
        set, and groupBy=RESOURCE is rejected.

        Use this method to:

        - Export per-user daily credit usage for external reporting
        - Export a per-environment and per-conversation resource breakdown

        ### Examples

        - Export January's daily summary:

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          dateRange:
            startTime: "2024-01-01T00:00:00Z"
            endTime: "2024-01-31T00:00:00Z"
          groupBy: CREDIT_USAGE_EXPORT_GROUP_BY_DAILY_SUMMARY
          ```

        ### Authorization

        Requires `billing:read_usage` permission on the organization.

        Args:
          date_range: Date range to export. Both start and end dates are inclusive; time-of-day is
              ignored. Unlike GetCreditUsageReport, the range may cover up to a year.

          group_by: How to group the export data. Defaults to DAILY_SUMMARY.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.BillingService/GetCreditUsageExport",
            body=await async_maybe_transform(
                {
                    "date_range": date_range,
                    "organization_id": organization_id,
                    "group_by": group_by,
                },
                billing_get_credit_usage_export_params.BillingGetCreditUsageExportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingGetCreditUsageExportResponse,
        )

    async def get_credit_usage_report(
        self,
        *,
        date_range: DateRange,
        organization_id: str,
        filter: CreditUsageReportFilterParam | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingGetCreditUsageReportResponse:
        """
        Returns a daily credit usage report for an enterprise organization.

        Each day reports org-wide credits by usage type, plus per-user, per-team,
        per-environment, and per-conversation breakdowns (top consumers with the
        remainder aggregated into an "Others" bucket) and a per-model breakdown of
        intelligence usage.

        Use this method to:

        - Chart daily credit consumption over a date range
        - Attribute credit usage to users, teams, environments, and conversations
        - Restrict the report to a single user or service account

        ### Examples

        - Get the report for January:

          Both dates are inclusive and the range must not exceed 31 days.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          dateRange:
            startTime: "2024-01-01T00:00:00Z"
            endTime: "2024-01-31T00:00:00Z"
          ```

        ### Authorization

        Requires `billing:read_usage` permission on the organization. A user without it
        can read their own usage by setting filter.subject to their own user identity;
        this self-access path is not available to service accounts.

        Args:
          date_range: Date range for the report. Both start and end dates are inclusive. Time-of-day
              is ignored; dates are truncated to midnight in the specified timezone. The range
              must not exceed 31 days.

          filter: Optional filter narrowing the returned data. When unset or empty, the response
              preserves the default behavior (top-N users + "Others"). See
              CreditUsageReportFilter for per-field response-scoping semantics.

          timezone: IANA timezone name (e.g. "America/New_York", "Europe/Berlin") used to bucket
              daily usage. When empty, defaults to "UTC".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.BillingService/GetCreditUsageReport",
            body=await async_maybe_transform(
                {
                    "date_range": date_range,
                    "organization_id": organization_id,
                    "filter": filter,
                    "timezone": timezone,
                },
                billing_get_credit_usage_report_params.BillingGetCreditUsageReportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingGetCreditUsageReportResponse,
        )

    async def get_cumulative_credit_usage(
        self,
        *,
        organization_id: str,
        as_of: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingGetCumulativeCreditUsageResponse:
        """
        Returns cumulative credit usage for an organization and its teams.

        Use this method to:

        - Get the total cumulative credit consumption as of a point in time
        - Get per-team cumulative usage with credit allocation (budget) comparison
        - Display team credit summaries on the usage page and team detail page
        - Display user budget utilization when user budgets are enabled

        ### Examples

        - Get current cumulative usage:

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          ```

        - Get cumulative usage as of a specific date:

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          asOf: "2026-03-31T23:59:59Z"
          ```

        ### Authorization

        Requires `billing:read_usage` permission on the organization.

        Args:
          organization_id: organization_id is the ID of the organization to get cumulative usage for.

          as_of: as_of is the point in time to compute cumulative usage up to. Defaults to now if
              not set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.BillingService/GetCumulativeCreditUsage",
            body=await async_maybe_transform(
                {
                    "organization_id": organization_id,
                    "as_of": as_of,
                },
                billing_get_cumulative_credit_usage_params.BillingGetCumulativeCreditUsageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingGetCumulativeCreditUsageResponse,
        )

    async def get_enterprise_ai_usage_summary(
        self,
        *,
        date_range: DateRange,
        organization_id: str,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingGetEnterpriseAIUsageSummaryResponse:
        """
        Returns organization-level enterprise AI usage totals for reporting.

        Reports BYOK (bring-your-own-key) token spend: cost in the organization's
        billing currency plus token counts, with a per-model breakdown. Credit-based
        usage from managed models is not included and the credits field is not populated
        by this endpoint.

        Use this method to:

        - Report total BYOK AI spend (cost and tokens) for a date range
        - Break down organization usage by model

        Only available for enterprise organizations.

        ### Examples

        - Get usage totals for January:

          Returns organization-wide BYOK spend for the month. Both dates are inclusive
          and the range must not exceed 31 days.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          dateRange:
            startTime: "2024-01-01T00:00:00Z"
            endTime: "2024-01-31T00:00:00Z"
          ```

        ### Authorization

        Requires `billing:read_usage` permission on the organization.

        Args:
          date_range: Date range for the summary. Both start and end dates are inclusive. Time-of-day
              is ignored; dates are truncated to midnight in the specified timezone.

          timezone: IANA timezone name used to bucket usage. When empty, defaults to "UTC".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.BillingService/GetEnterpriseAIUsageSummary",
            body=await async_maybe_transform(
                {
                    "date_range": date_range,
                    "organization_id": organization_id,
                    "timezone": timezone,
                },
                billing_get_enterprise_ai_usage_summary_params.BillingGetEnterpriseAIUsageSummaryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingGetEnterpriseAIUsageSummaryResponse,
        )

    async def get_enterprise_ai_usage_time_series(
        self,
        *,
        date_range: DateRange,
        organization_id: str,
        filter: EnterpriseAIUsageTimeSeriesFilterParam | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingGetEnterpriseAIUsageTimeSeriesResponse:
        """
        Returns daily enterprise AI usage totals for the organization.

        Each day reports BYOK token spend (cost and tokens) with per-user, per-team, and
        per-model breakdowns. Per-user entries cover the top spenders with the remainder
        aggregated into an "Others" bucket; usage not attributed to a user or service
        account appears only in the daily totals. The credits field is not populated by
        this endpoint.

        When filter.subject is set the response contains only that subject's usage:
        daily totals and the team breakdown are omitted, and the model breakdown covers
        the subject only.

        Use this method to:

        - Chart daily BYOK AI spend over a date range
        - Feed daily per-user usage into external dashboards
        - Restrict the response to a single user or service account

        Only available for enterprise organizations.

        ### Examples

        - Get daily usage for January:

          Returns one entry per day with per-user, per-team, and per-model breakdowns.
          Both dates are inclusive and the range must not exceed 31 days.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          dateRange:
            startTime: "2024-01-01T00:00:00Z"
            endTime: "2024-01-31T00:00:00Z"
          ```

        ### Authorization

        Requires `billing:read_usage` permission on the organization.

        Args:
          date_range: Date range for the daily usage series. Both start and end dates are inclusive.
              Time-of-day is ignored; dates are truncated to midnight in the specified
              timezone.

          timezone: IANA timezone name used to bucket daily usage. When empty, defaults to "UTC".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.BillingService/GetEnterpriseAIUsageTimeSeries",
            body=await async_maybe_transform(
                {
                    "date_range": date_range,
                    "organization_id": organization_id,
                    "filter": filter,
                    "timezone": timezone,
                },
                billing_get_enterprise_ai_usage_time_series_params.BillingGetEnterpriseAIUsageTimeSeriesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingGetEnterpriseAIUsageTimeSeriesResponse,
        )

    def list_enterprise_ai_team_usage(
        self,
        *,
        date_range: DateRange,
        organization_id: str,
        token: str | Omit = omit,
        page_size: int | Omit = omit,
        filter: billing_list_enterprise_ai_team_usage_params.Filter | Omit = omit,
        pagination: billing_list_enterprise_ai_team_usage_params.Pagination | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[TeamEnterpriseAIUsage, AsyncTeamUsagePage[TeamEnterpriseAIUsage]]:
        """
        Lists enterprise AI usage grouped by team.

        Reports BYOK token spend per team (cost and tokens) with each team's monthly
        budget when one applies. The credits field is not populated by this endpoint.

        Use this method to:

        - Compare BYOK AI spend across teams
        - Track team budget utilization
        - Filter usage to specific teams

        Only available for enterprise organizations.

        ### Examples

        - List team usage for January:

          Returns BYOK spend per team with monthly budgets. Both dates are inclusive and
          the range must not exceed 31 days.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          dateRange:
            startTime: "2024-01-01T00:00:00Z"
            endTime: "2024-01-31T00:00:00Z"
          ```

        ### Authorization

        Requires `billing:read_usage` permission on the organization.

        Args:
          date_range: Date range for the team usage list. Both start and end dates are inclusive.
              Time-of-day is ignored; dates are truncated to midnight in the specified
              timezone.

          timezone: IANA timezone name used to bucket usage. When empty, defaults to "UTC".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.BillingService/ListEnterpriseAITeamUsage",
            page=AsyncTeamUsagePage[TeamEnterpriseAIUsage],
            body=maybe_transform(
                {
                    "date_range": date_range,
                    "organization_id": organization_id,
                    "filter": filter,
                    "pagination": pagination,
                    "timezone": timezone,
                },
                billing_list_enterprise_ai_team_usage_params.BillingListEnterpriseAITeamUsageParams,
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
                    billing_list_enterprise_ai_team_usage_params.BillingListEnterpriseAITeamUsageParams,
                ),
            ),
            model=TeamEnterpriseAIUsage,
            method="post",
        )

    def list_enterprise_ai_user_usage(
        self,
        *,
        date_range: DateRange,
        organization_id: str,
        token: str | Omit = omit,
        page_size: int | Omit = omit,
        filter: billing_list_enterprise_ai_user_usage_params.Filter | Omit = omit,
        pagination: billing_list_enterprise_ai_user_usage_params.Pagination | Omit = omit,
        sort: billing_list_enterprise_ai_user_usage_params.Sort | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[UserCostBudgetUsage, AsyncUserUsagePage[UserCostBudgetUsage]]:
        """
        Lists enterprise AI usage grouped by user with effective monthly budget data.

        Reports BYOK token spend (cost and tokens) for each user and service account
        with attributed usage in the date range, including each subject's effective
        monthly budget. Usage not attributed to a user or service account is excluded,
        so the sum across subjects can be less than the organization totals from
        GetEnterpriseAIUsageSummary. The credits field is not populated by this
        endpoint.

        Budget fields (month_to_date_usage, utilization_percent, over_budget) are
        computed from usage inside the requested date range measured against the monthly
        limit. Send a range that starts on the first day of the month for true
        month-to-date figures.

        Use this method to:

        - Export per-user BYOK AI spend to external reporting
        - Identify the highest spenders in the organization
        - Track per-user budget utilization and over-budget users

        Only available for enterprise organizations.

        ### Examples

        - List user usage for January:

          Returns per-user BYOK spend with effective budgets, highest spend first. Both
          dates are inclusive and the range must not exceed 31 days.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          dateRange:
            startTime: "2024-01-01T00:00:00Z"
            endTime: "2024-01-31T00:00:00Z"
          ```

        ### Authorization

        Requires `billing:read_usage` permission on the organization. Callers without it
        can read their own usage by setting filter.subject to themselves.

        Args:
          date_range: Date range for the user usage list. Both start and end dates are inclusive.
              Time-of-day is ignored; dates are truncated to midnight in the specified
              timezone.

          filter: Optional filter narrowing the returned user usage. When set to a subject, the
              response contains only usage for that user or service account.

          sort: sort controls the ordering of results. Defaults to total spend descending.

          timezone: IANA timezone name used to bucket usage. When empty, defaults to "UTC".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.BillingService/ListEnterpriseAIUserUsage",
            page=AsyncUserUsagePage[UserCostBudgetUsage],
            body=maybe_transform(
                {
                    "date_range": date_range,
                    "organization_id": organization_id,
                    "filter": filter,
                    "pagination": pagination,
                    "sort": sort,
                    "timezone": timezone,
                },
                billing_list_enterprise_ai_user_usage_params.BillingListEnterpriseAIUserUsageParams,
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
                    billing_list_enterprise_ai_user_usage_params.BillingListEnterpriseAIUserUsageParams,
                ),
            ),
            model=UserCostBudgetUsage,
            method="post",
        )

    def list_enterprise_user_credit_usage(
        self,
        *,
        organization_id: str,
        token: str | Omit = omit,
        page_size: int | Omit = omit,
        as_of: Union[str, datetime, None] | Omit = omit,
        pagination: billing_list_enterprise_user_credit_usage_params.Pagination | Omit = omit,
        sort: billing_list_enterprise_user_credit_usage_params.Sort | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[UserCreditBudgetUsage, AsyncUserUsagePage[UserCreditBudgetUsage]]:
        """
        Lists per-user month-to-date credit usage with effective monthly budgets.

        Results are ordered by total credits descending so the highest spenders appear
        first, with user_id as a stable tiebreaker. Use cursor pagination to walk the
        full set for large organizations.

        The default SORT_FIELD_USAGE ordering supports cursor pagination over any number
        of users. Sorting by display name, budget, or budget utilization computes the
        order in memory and is limited to organizations with at most 10,000 users;
        beyond that, use SORT_FIELD_USAGE. Because month-to-date figures are recomputed
        per request, hold a date range stable across a paginated walk to keep page
        tokens valid.

        Use this method to:

        - Export per-user credit usage to external reporting
        - Identify the highest spenders in the organization
        - Track per-user budget utilization and over-budget users

        ### Examples

        - List user usage for the current month:

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          pagination:
            pageSize: 50
          ```

        ### Authorization

        Requires `billing:read_usage` permission on the organization.

        Args:
          organization_id: organization_id is the ID of the organization to list user credit usage for.

          as_of: as_of is the point in time to compute month-to-date usage up to. Defaults to now
              if not set.

          sort: sort controls the ordering of results. Defaults to total credits descending.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.BillingService/ListEnterpriseUserCreditUsage",
            page=AsyncUserUsagePage[UserCreditBudgetUsage],
            body=maybe_transform(
                {
                    "organization_id": organization_id,
                    "as_of": as_of,
                    "pagination": pagination,
                    "sort": sort,
                },
                billing_list_enterprise_user_credit_usage_params.BillingListEnterpriseUserCreditUsageParams,
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
                    billing_list_enterprise_user_credit_usage_params.BillingListEnterpriseUserCreditUsageParams,
                ),
            ),
            model=UserCreditBudgetUsage,
            method="post",
        )


class BillingResourceWithRawResponse:
    def __init__(self, billing: BillingResource) -> None:
        self._billing = billing

        self.get_credit_usage_export = to_raw_response_wrapper(
            billing.get_credit_usage_export,
        )
        self.get_credit_usage_report = to_raw_response_wrapper(
            billing.get_credit_usage_report,
        )
        self.get_cumulative_credit_usage = to_raw_response_wrapper(
            billing.get_cumulative_credit_usage,
        )
        self.get_enterprise_ai_usage_summary = to_raw_response_wrapper(
            billing.get_enterprise_ai_usage_summary,
        )
        self.get_enterprise_ai_usage_time_series = to_raw_response_wrapper(
            billing.get_enterprise_ai_usage_time_series,
        )
        self.list_enterprise_ai_team_usage = to_raw_response_wrapper(
            billing.list_enterprise_ai_team_usage,
        )
        self.list_enterprise_ai_user_usage = to_raw_response_wrapper(
            billing.list_enterprise_ai_user_usage,
        )
        self.list_enterprise_user_credit_usage = to_raw_response_wrapper(
            billing.list_enterprise_user_credit_usage,
        )


class AsyncBillingResourceWithRawResponse:
    def __init__(self, billing: AsyncBillingResource) -> None:
        self._billing = billing

        self.get_credit_usage_export = async_to_raw_response_wrapper(
            billing.get_credit_usage_export,
        )
        self.get_credit_usage_report = async_to_raw_response_wrapper(
            billing.get_credit_usage_report,
        )
        self.get_cumulative_credit_usage = async_to_raw_response_wrapper(
            billing.get_cumulative_credit_usage,
        )
        self.get_enterprise_ai_usage_summary = async_to_raw_response_wrapper(
            billing.get_enterprise_ai_usage_summary,
        )
        self.get_enterprise_ai_usage_time_series = async_to_raw_response_wrapper(
            billing.get_enterprise_ai_usage_time_series,
        )
        self.list_enterprise_ai_team_usage = async_to_raw_response_wrapper(
            billing.list_enterprise_ai_team_usage,
        )
        self.list_enterprise_ai_user_usage = async_to_raw_response_wrapper(
            billing.list_enterprise_ai_user_usage,
        )
        self.list_enterprise_user_credit_usage = async_to_raw_response_wrapper(
            billing.list_enterprise_user_credit_usage,
        )


class BillingResourceWithStreamingResponse:
    def __init__(self, billing: BillingResource) -> None:
        self._billing = billing

        self.get_credit_usage_export = to_streamed_response_wrapper(
            billing.get_credit_usage_export,
        )
        self.get_credit_usage_report = to_streamed_response_wrapper(
            billing.get_credit_usage_report,
        )
        self.get_cumulative_credit_usage = to_streamed_response_wrapper(
            billing.get_cumulative_credit_usage,
        )
        self.get_enterprise_ai_usage_summary = to_streamed_response_wrapper(
            billing.get_enterprise_ai_usage_summary,
        )
        self.get_enterprise_ai_usage_time_series = to_streamed_response_wrapper(
            billing.get_enterprise_ai_usage_time_series,
        )
        self.list_enterprise_ai_team_usage = to_streamed_response_wrapper(
            billing.list_enterprise_ai_team_usage,
        )
        self.list_enterprise_ai_user_usage = to_streamed_response_wrapper(
            billing.list_enterprise_ai_user_usage,
        )
        self.list_enterprise_user_credit_usage = to_streamed_response_wrapper(
            billing.list_enterprise_user_credit_usage,
        )


class AsyncBillingResourceWithStreamingResponse:
    def __init__(self, billing: AsyncBillingResource) -> None:
        self._billing = billing

        self.get_credit_usage_export = async_to_streamed_response_wrapper(
            billing.get_credit_usage_export,
        )
        self.get_credit_usage_report = async_to_streamed_response_wrapper(
            billing.get_credit_usage_report,
        )
        self.get_cumulative_credit_usage = async_to_streamed_response_wrapper(
            billing.get_cumulative_credit_usage,
        )
        self.get_enterprise_ai_usage_summary = async_to_streamed_response_wrapper(
            billing.get_enterprise_ai_usage_summary,
        )
        self.get_enterprise_ai_usage_time_series = async_to_streamed_response_wrapper(
            billing.get_enterprise_ai_usage_time_series,
        )
        self.list_enterprise_ai_team_usage = async_to_streamed_response_wrapper(
            billing.list_enterprise_ai_team_usage,
        )
        self.list_enterprise_ai_user_usage = async_to_streamed_response_wrapper(
            billing.list_enterprise_ai_user_usage,
        )
        self.list_enterprise_user_credit_usage = async_to_streamed_response_wrapper(
            billing.list_enterprise_user_credit_usage,
        )
