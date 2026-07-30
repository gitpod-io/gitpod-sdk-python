# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.types import (
    UserCostBudgetUsage,
    TeamEnterpriseAIUsage,
    UserCreditBudgetUsage,
    BillingGetCreditUsageExportResponse,
    BillingGetCreditUsageReportResponse,
    BillingGetCumulativeCreditUsageResponse,
    BillingGetEnterpriseAIUsageSummaryResponse,
    BillingGetEnterpriseAIUsageTimeSeriesResponse,
)
from gitpod._utils import parse_datetime
from gitpod.pagination import SyncTeamUsagePage, SyncUserUsagePage, AsyncTeamUsagePage, AsyncUserUsagePage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBilling:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_credit_usage_export(self, client: Gitpod) -> None:
        billing = client.billing.get_credit_usage_export(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(BillingGetCreditUsageExportResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_credit_usage_export_with_all_params(self, client: Gitpod) -> None:
        billing = client.billing.get_credit_usage_export(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            group_by="CREDIT_USAGE_EXPORT_GROUP_BY_DAILY_SUMMARY",
        )
        assert_matches_type(BillingGetCreditUsageExportResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_credit_usage_export(self, client: Gitpod) -> None:
        response = client.billing.with_raw_response.get_credit_usage_export(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = response.parse()
        assert_matches_type(BillingGetCreditUsageExportResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_credit_usage_export(self, client: Gitpod) -> None:
        with client.billing.with_streaming_response.get_credit_usage_export(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = response.parse()
            assert_matches_type(BillingGetCreditUsageExportResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_credit_usage_report(self, client: Gitpod) -> None:
        billing = client.billing.get_credit_usage_report(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(BillingGetCreditUsageReportResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_credit_usage_report_with_all_params(self, client: Gitpod) -> None:
        billing = client.billing.get_credit_usage_report(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            filter={
                "subject": {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "principal": "PRINCIPAL_UNSPECIFIED",
                }
            },
            timezone="timezone",
        )
        assert_matches_type(BillingGetCreditUsageReportResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_credit_usage_report(self, client: Gitpod) -> None:
        response = client.billing.with_raw_response.get_credit_usage_report(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = response.parse()
        assert_matches_type(BillingGetCreditUsageReportResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_credit_usage_report(self, client: Gitpod) -> None:
        with client.billing.with_streaming_response.get_credit_usage_report(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = response.parse()
            assert_matches_type(BillingGetCreditUsageReportResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_cumulative_credit_usage(self, client: Gitpod) -> None:
        billing = client.billing.get_cumulative_credit_usage(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(BillingGetCumulativeCreditUsageResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_cumulative_credit_usage_with_all_params(self, client: Gitpod) -> None:
        billing = client.billing.get_cumulative_credit_usage(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            as_of=parse_datetime("2026-03-31T23:59:59Z"),
        )
        assert_matches_type(BillingGetCumulativeCreditUsageResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_cumulative_credit_usage(self, client: Gitpod) -> None:
        response = client.billing.with_raw_response.get_cumulative_credit_usage(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = response.parse()
        assert_matches_type(BillingGetCumulativeCreditUsageResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_cumulative_credit_usage(self, client: Gitpod) -> None:
        with client.billing.with_streaming_response.get_cumulative_credit_usage(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = response.parse()
            assert_matches_type(BillingGetCumulativeCreditUsageResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_enterprise_ai_usage_summary(self, client: Gitpod) -> None:
        billing = client.billing.get_enterprise_ai_usage_summary(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(BillingGetEnterpriseAIUsageSummaryResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_enterprise_ai_usage_summary_with_all_params(self, client: Gitpod) -> None:
        billing = client.billing.get_enterprise_ai_usage_summary(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            timezone="timezone",
        )
        assert_matches_type(BillingGetEnterpriseAIUsageSummaryResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_enterprise_ai_usage_summary(self, client: Gitpod) -> None:
        response = client.billing.with_raw_response.get_enterprise_ai_usage_summary(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = response.parse()
        assert_matches_type(BillingGetEnterpriseAIUsageSummaryResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_enterprise_ai_usage_summary(self, client: Gitpod) -> None:
        with client.billing.with_streaming_response.get_enterprise_ai_usage_summary(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = response.parse()
            assert_matches_type(BillingGetEnterpriseAIUsageSummaryResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_enterprise_ai_usage_time_series(self, client: Gitpod) -> None:
        billing = client.billing.get_enterprise_ai_usage_time_series(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(BillingGetEnterpriseAIUsageTimeSeriesResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_enterprise_ai_usage_time_series_with_all_params(self, client: Gitpod) -> None:
        billing = client.billing.get_enterprise_ai_usage_time_series(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            filter={
                "subject": {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "principal": "PRINCIPAL_UNSPECIFIED",
                }
            },
            timezone="timezone",
        )
        assert_matches_type(BillingGetEnterpriseAIUsageTimeSeriesResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_enterprise_ai_usage_time_series(self, client: Gitpod) -> None:
        response = client.billing.with_raw_response.get_enterprise_ai_usage_time_series(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = response.parse()
        assert_matches_type(BillingGetEnterpriseAIUsageTimeSeriesResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_enterprise_ai_usage_time_series(self, client: Gitpod) -> None:
        with client.billing.with_streaming_response.get_enterprise_ai_usage_time_series(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = response.parse()
            assert_matches_type(BillingGetEnterpriseAIUsageTimeSeriesResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_enterprise_ai_team_usage(self, client: Gitpod) -> None:
        billing = client.billing.list_enterprise_ai_team_usage(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(SyncTeamUsagePage[TeamEnterpriseAIUsage], billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_enterprise_ai_team_usage_with_all_params(self, client: Gitpod) -> None:
        billing = client.billing.list_enterprise_ai_team_usage(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            token="token",
            page_size=0,
            filter={"team_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"]},
            pagination={
                "token": "token",
                "page_size": 100,
            },
            timezone="timezone",
        )
        assert_matches_type(SyncTeamUsagePage[TeamEnterpriseAIUsage], billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_enterprise_ai_team_usage(self, client: Gitpod) -> None:
        response = client.billing.with_raw_response.list_enterprise_ai_team_usage(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = response.parse()
        assert_matches_type(SyncTeamUsagePage[TeamEnterpriseAIUsage], billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_enterprise_ai_team_usage(self, client: Gitpod) -> None:
        with client.billing.with_streaming_response.list_enterprise_ai_team_usage(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = response.parse()
            assert_matches_type(SyncTeamUsagePage[TeamEnterpriseAIUsage], billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_enterprise_ai_user_usage(self, client: Gitpod) -> None:
        billing = client.billing.list_enterprise_ai_user_usage(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(SyncUserUsagePage[UserCostBudgetUsage], billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_enterprise_ai_user_usage_with_all_params(self, client: Gitpod) -> None:
        billing = client.billing.list_enterprise_ai_user_usage(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            token="token",
            page_size=0,
            filter={
                "subject": {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "principal": "PRINCIPAL_UNSPECIFIED",
                }
            },
            pagination={
                "token": "token",
                "page_size": 100,
            },
            sort={
                "field": "SORT_FIELD_UNSPECIFIED",
                "order": "SORT_ORDER_UNSPECIFIED",
            },
            timezone="timezone",
        )
        assert_matches_type(SyncUserUsagePage[UserCostBudgetUsage], billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_enterprise_ai_user_usage(self, client: Gitpod) -> None:
        response = client.billing.with_raw_response.list_enterprise_ai_user_usage(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = response.parse()
        assert_matches_type(SyncUserUsagePage[UserCostBudgetUsage], billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_enterprise_ai_user_usage(self, client: Gitpod) -> None:
        with client.billing.with_streaming_response.list_enterprise_ai_user_usage(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = response.parse()
            assert_matches_type(SyncUserUsagePage[UserCostBudgetUsage], billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_enterprise_user_credit_usage(self, client: Gitpod) -> None:
        billing = client.billing.list_enterprise_user_credit_usage(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(SyncUserUsagePage[UserCreditBudgetUsage], billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_enterprise_user_credit_usage_with_all_params(self, client: Gitpod) -> None:
        billing = client.billing.list_enterprise_user_credit_usage(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            token="token",
            page_size=0,
            as_of=parse_datetime("2019-12-27T18:11:19.117Z"),
            pagination={
                "token": "token",
                "page_size": 50,
            },
            sort={
                "field": "SORT_FIELD_UNSPECIFIED",
                "order": "SORT_ORDER_UNSPECIFIED",
            },
        )
        assert_matches_type(SyncUserUsagePage[UserCreditBudgetUsage], billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_enterprise_user_credit_usage(self, client: Gitpod) -> None:
        response = client.billing.with_raw_response.list_enterprise_user_credit_usage(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = response.parse()
        assert_matches_type(SyncUserUsagePage[UserCreditBudgetUsage], billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_enterprise_user_credit_usage(self, client: Gitpod) -> None:
        with client.billing.with_streaming_response.list_enterprise_user_credit_usage(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = response.parse()
            assert_matches_type(SyncUserUsagePage[UserCreditBudgetUsage], billing, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBilling:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_credit_usage_export(self, async_client: AsyncGitpod) -> None:
        billing = await async_client.billing.get_credit_usage_export(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(BillingGetCreditUsageExportResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_credit_usage_export_with_all_params(self, async_client: AsyncGitpod) -> None:
        billing = await async_client.billing.get_credit_usage_export(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            group_by="CREDIT_USAGE_EXPORT_GROUP_BY_DAILY_SUMMARY",
        )
        assert_matches_type(BillingGetCreditUsageExportResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_credit_usage_export(self, async_client: AsyncGitpod) -> None:
        response = await async_client.billing.with_raw_response.get_credit_usage_export(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = await response.parse()
        assert_matches_type(BillingGetCreditUsageExportResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_credit_usage_export(self, async_client: AsyncGitpod) -> None:
        async with async_client.billing.with_streaming_response.get_credit_usage_export(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = await response.parse()
            assert_matches_type(BillingGetCreditUsageExportResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_credit_usage_report(self, async_client: AsyncGitpod) -> None:
        billing = await async_client.billing.get_credit_usage_report(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(BillingGetCreditUsageReportResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_credit_usage_report_with_all_params(self, async_client: AsyncGitpod) -> None:
        billing = await async_client.billing.get_credit_usage_report(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            filter={
                "subject": {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "principal": "PRINCIPAL_UNSPECIFIED",
                }
            },
            timezone="timezone",
        )
        assert_matches_type(BillingGetCreditUsageReportResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_credit_usage_report(self, async_client: AsyncGitpod) -> None:
        response = await async_client.billing.with_raw_response.get_credit_usage_report(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = await response.parse()
        assert_matches_type(BillingGetCreditUsageReportResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_credit_usage_report(self, async_client: AsyncGitpod) -> None:
        async with async_client.billing.with_streaming_response.get_credit_usage_report(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = await response.parse()
            assert_matches_type(BillingGetCreditUsageReportResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_cumulative_credit_usage(self, async_client: AsyncGitpod) -> None:
        billing = await async_client.billing.get_cumulative_credit_usage(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(BillingGetCumulativeCreditUsageResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_cumulative_credit_usage_with_all_params(self, async_client: AsyncGitpod) -> None:
        billing = await async_client.billing.get_cumulative_credit_usage(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            as_of=parse_datetime("2026-03-31T23:59:59Z"),
        )
        assert_matches_type(BillingGetCumulativeCreditUsageResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_cumulative_credit_usage(self, async_client: AsyncGitpod) -> None:
        response = await async_client.billing.with_raw_response.get_cumulative_credit_usage(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = await response.parse()
        assert_matches_type(BillingGetCumulativeCreditUsageResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_cumulative_credit_usage(self, async_client: AsyncGitpod) -> None:
        async with async_client.billing.with_streaming_response.get_cumulative_credit_usage(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = await response.parse()
            assert_matches_type(BillingGetCumulativeCreditUsageResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_enterprise_ai_usage_summary(self, async_client: AsyncGitpod) -> None:
        billing = await async_client.billing.get_enterprise_ai_usage_summary(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(BillingGetEnterpriseAIUsageSummaryResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_enterprise_ai_usage_summary_with_all_params(self, async_client: AsyncGitpod) -> None:
        billing = await async_client.billing.get_enterprise_ai_usage_summary(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            timezone="timezone",
        )
        assert_matches_type(BillingGetEnterpriseAIUsageSummaryResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_enterprise_ai_usage_summary(self, async_client: AsyncGitpod) -> None:
        response = await async_client.billing.with_raw_response.get_enterprise_ai_usage_summary(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = await response.parse()
        assert_matches_type(BillingGetEnterpriseAIUsageSummaryResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_enterprise_ai_usage_summary(self, async_client: AsyncGitpod) -> None:
        async with async_client.billing.with_streaming_response.get_enterprise_ai_usage_summary(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = await response.parse()
            assert_matches_type(BillingGetEnterpriseAIUsageSummaryResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_enterprise_ai_usage_time_series(self, async_client: AsyncGitpod) -> None:
        billing = await async_client.billing.get_enterprise_ai_usage_time_series(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(BillingGetEnterpriseAIUsageTimeSeriesResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_enterprise_ai_usage_time_series_with_all_params(self, async_client: AsyncGitpod) -> None:
        billing = await async_client.billing.get_enterprise_ai_usage_time_series(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            filter={
                "subject": {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "principal": "PRINCIPAL_UNSPECIFIED",
                }
            },
            timezone="timezone",
        )
        assert_matches_type(BillingGetEnterpriseAIUsageTimeSeriesResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_enterprise_ai_usage_time_series(self, async_client: AsyncGitpod) -> None:
        response = await async_client.billing.with_raw_response.get_enterprise_ai_usage_time_series(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = await response.parse()
        assert_matches_type(BillingGetEnterpriseAIUsageTimeSeriesResponse, billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_enterprise_ai_usage_time_series(self, async_client: AsyncGitpod) -> None:
        async with async_client.billing.with_streaming_response.get_enterprise_ai_usage_time_series(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = await response.parse()
            assert_matches_type(BillingGetEnterpriseAIUsageTimeSeriesResponse, billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_enterprise_ai_team_usage(self, async_client: AsyncGitpod) -> None:
        billing = await async_client.billing.list_enterprise_ai_team_usage(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(AsyncTeamUsagePage[TeamEnterpriseAIUsage], billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_enterprise_ai_team_usage_with_all_params(self, async_client: AsyncGitpod) -> None:
        billing = await async_client.billing.list_enterprise_ai_team_usage(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            token="token",
            page_size=0,
            filter={"team_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"]},
            pagination={
                "token": "token",
                "page_size": 100,
            },
            timezone="timezone",
        )
        assert_matches_type(AsyncTeamUsagePage[TeamEnterpriseAIUsage], billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_enterprise_ai_team_usage(self, async_client: AsyncGitpod) -> None:
        response = await async_client.billing.with_raw_response.list_enterprise_ai_team_usage(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = await response.parse()
        assert_matches_type(AsyncTeamUsagePage[TeamEnterpriseAIUsage], billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_enterprise_ai_team_usage(self, async_client: AsyncGitpod) -> None:
        async with async_client.billing.with_streaming_response.list_enterprise_ai_team_usage(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = await response.parse()
            assert_matches_type(AsyncTeamUsagePage[TeamEnterpriseAIUsage], billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_enterprise_ai_user_usage(self, async_client: AsyncGitpod) -> None:
        billing = await async_client.billing.list_enterprise_ai_user_usage(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(AsyncUserUsagePage[UserCostBudgetUsage], billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_enterprise_ai_user_usage_with_all_params(self, async_client: AsyncGitpod) -> None:
        billing = await async_client.billing.list_enterprise_ai_user_usage(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            token="token",
            page_size=0,
            filter={
                "subject": {
                    "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "principal": "PRINCIPAL_UNSPECIFIED",
                }
            },
            pagination={
                "token": "token",
                "page_size": 100,
            },
            sort={
                "field": "SORT_FIELD_UNSPECIFIED",
                "order": "SORT_ORDER_UNSPECIFIED",
            },
            timezone="timezone",
        )
        assert_matches_type(AsyncUserUsagePage[UserCostBudgetUsage], billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_enterprise_ai_user_usage(self, async_client: AsyncGitpod) -> None:
        response = await async_client.billing.with_raw_response.list_enterprise_ai_user_usage(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = await response.parse()
        assert_matches_type(AsyncUserUsagePage[UserCostBudgetUsage], billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_enterprise_ai_user_usage(self, async_client: AsyncGitpod) -> None:
        async with async_client.billing.with_streaming_response.list_enterprise_ai_user_usage(
            date_range={
                "end_time": parse_datetime("2024-01-31T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = await response.parse()
            assert_matches_type(AsyncUserUsagePage[UserCostBudgetUsage], billing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_enterprise_user_credit_usage(self, async_client: AsyncGitpod) -> None:
        billing = await async_client.billing.list_enterprise_user_credit_usage(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(AsyncUserUsagePage[UserCreditBudgetUsage], billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_enterprise_user_credit_usage_with_all_params(self, async_client: AsyncGitpod) -> None:
        billing = await async_client.billing.list_enterprise_user_credit_usage(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            token="token",
            page_size=0,
            as_of=parse_datetime("2019-12-27T18:11:19.117Z"),
            pagination={
                "token": "token",
                "page_size": 50,
            },
            sort={
                "field": "SORT_FIELD_UNSPECIFIED",
                "order": "SORT_ORDER_UNSPECIFIED",
            },
        )
        assert_matches_type(AsyncUserUsagePage[UserCreditBudgetUsage], billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_enterprise_user_credit_usage(self, async_client: AsyncGitpod) -> None:
        response = await async_client.billing.with_raw_response.list_enterprise_user_credit_usage(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        billing = await response.parse()
        assert_matches_type(AsyncUserUsagePage[UserCreditBudgetUsage], billing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_enterprise_user_credit_usage(self, async_client: AsyncGitpod) -> None:
        async with async_client.billing.with_streaming_response.list_enterprise_user_credit_usage(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            billing = await response.parse()
            assert_matches_type(AsyncUserUsagePage[UserCreditBudgetUsage], billing, path=["response"])

        assert cast(Any, response.is_closed) is True
