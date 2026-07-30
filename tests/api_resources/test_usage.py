# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.types import (
    EnvironmentUsageRecord,
    UsageGetPrSummaryResponse,
    UsageGetPrTimeSeriesResponse,
    UsageGetCoAuthorSummaryResponse,
    UsageGetAgentTraceSummaryResponse,
    UsageGetCoAuthorTimeSeriesResponse,
    UsageGetAdoptionUsageSummaryResponse,
    UsageGetAgentTraceTimeSeriesResponse,
)
from gitpod._utils import parse_datetime
from gitpod.pagination import SyncRecordsPage, AsyncRecordsPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_adoption_usage_summary(self, client: Gitpod) -> None:
        usage = client.usage.get_adoption_usage_summary(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
        )
        assert_matches_type(UsageGetAdoptionUsageSummaryResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_adoption_usage_summary_with_all_params(self, client: Gitpod) -> None:
        usage = client.usage.get_adoption_usage_summary(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            project_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
            team_id="teamId",
            user_id="userId",
        )
        assert_matches_type(UsageGetAdoptionUsageSummaryResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_adoption_usage_summary(self, client: Gitpod) -> None:
        response = client.usage.with_raw_response.get_adoption_usage_summary(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageGetAdoptionUsageSummaryResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_adoption_usage_summary(self, client: Gitpod) -> None:
        with client.usage.with_streaming_response.get_adoption_usage_summary(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageGetAdoptionUsageSummaryResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_agent_trace_summary(self, client: Gitpod) -> None:
        usage = client.usage.get_agent_trace_summary(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
        )
        assert_matches_type(UsageGetAgentTraceSummaryResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_agent_trace_summary_with_all_params(self, client: Gitpod) -> None:
        usage = client.usage.get_agent_trace_summary(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            project_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
            team_id="teamId",
            user_id="userId",
        )
        assert_matches_type(UsageGetAgentTraceSummaryResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_agent_trace_summary(self, client: Gitpod) -> None:
        response = client.usage.with_raw_response.get_agent_trace_summary(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageGetAgentTraceSummaryResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_agent_trace_summary(self, client: Gitpod) -> None:
        with client.usage.with_streaming_response.get_agent_trace_summary(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageGetAgentTraceSummaryResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_agent_trace_time_series(self, client: Gitpod) -> None:
        usage = client.usage.get_agent_trace_time_series(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
        )
        assert_matches_type(UsageGetAgentTraceTimeSeriesResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_agent_trace_time_series_with_all_params(self, client: Gitpod) -> None:
        usage = client.usage.get_agent_trace_time_series(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            project_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
            resolution="RESOLUTION_WEEKLY",
            team_id="teamId",
            user_id="userId",
        )
        assert_matches_type(UsageGetAgentTraceTimeSeriesResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_agent_trace_time_series(self, client: Gitpod) -> None:
        response = client.usage.with_raw_response.get_agent_trace_time_series(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageGetAgentTraceTimeSeriesResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_agent_trace_time_series(self, client: Gitpod) -> None:
        with client.usage.with_streaming_response.get_agent_trace_time_series(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageGetAgentTraceTimeSeriesResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_co_author_summary(self, client: Gitpod) -> None:
        usage = client.usage.get_co_author_summary(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
        )
        assert_matches_type(UsageGetCoAuthorSummaryResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_co_author_summary_with_all_params(self, client: Gitpod) -> None:
        usage = client.usage.get_co_author_summary(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            project_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
            team_id="teamId",
            user_id="userId",
        )
        assert_matches_type(UsageGetCoAuthorSummaryResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_co_author_summary(self, client: Gitpod) -> None:
        response = client.usage.with_raw_response.get_co_author_summary(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageGetCoAuthorSummaryResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_co_author_summary(self, client: Gitpod) -> None:
        with client.usage.with_streaming_response.get_co_author_summary(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageGetCoAuthorSummaryResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_co_author_time_series(self, client: Gitpod) -> None:
        usage = client.usage.get_co_author_time_series(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
        )
        assert_matches_type(UsageGetCoAuthorTimeSeriesResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_co_author_time_series_with_all_params(self, client: Gitpod) -> None:
        usage = client.usage.get_co_author_time_series(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            project_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
            resolution="RESOLUTION_WEEKLY",
            team_id="teamId",
            user_id="userId",
        )
        assert_matches_type(UsageGetCoAuthorTimeSeriesResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_co_author_time_series(self, client: Gitpod) -> None:
        response = client.usage.with_raw_response.get_co_author_time_series(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageGetCoAuthorTimeSeriesResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_co_author_time_series(self, client: Gitpod) -> None:
        with client.usage.with_streaming_response.get_co_author_time_series(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageGetCoAuthorTimeSeriesResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_pr_summary(self, client: Gitpod) -> None:
        usage = client.usage.get_pr_summary(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
        )
        assert_matches_type(UsageGetPrSummaryResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_pr_summary_with_all_params(self, client: Gitpod) -> None:
        usage = client.usage.get_pr_summary(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            project_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
            team_id="teamId",
            user_id="userId",
        )
        assert_matches_type(UsageGetPrSummaryResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_pr_summary(self, client: Gitpod) -> None:
        response = client.usage.with_raw_response.get_pr_summary(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageGetPrSummaryResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_pr_summary(self, client: Gitpod) -> None:
        with client.usage.with_streaming_response.get_pr_summary(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageGetPrSummaryResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_pr_time_series(self, client: Gitpod) -> None:
        usage = client.usage.get_pr_time_series(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
        )
        assert_matches_type(UsageGetPrTimeSeriesResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_pr_time_series_with_all_params(self, client: Gitpod) -> None:
        usage = client.usage.get_pr_time_series(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            project_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
            resolution="RESOLUTION_WEEKLY",
            team_id="teamId",
            user_id="userId",
        )
        assert_matches_type(UsageGetPrTimeSeriesResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_pr_time_series(self, client: Gitpod) -> None:
        response = client.usage.with_raw_response.get_pr_time_series(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageGetPrTimeSeriesResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_pr_time_series(self, client: Gitpod) -> None:
        with client.usage.with_streaming_response.get_pr_time_series(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageGetPrTimeSeriesResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_environment_runtime_records(self, client: Gitpod) -> None:
        usage = client.usage.list_environment_runtime_records()
        assert_matches_type(SyncRecordsPage[EnvironmentUsageRecord], usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_environment_runtime_records_with_all_params(self, client: Gitpod) -> None:
        usage = client.usage.list_environment_runtime_records(
            token="token",
            page_size=0,
            filter={
                "date_range": {
                    "end_time": parse_datetime("2024-01-02T00:00:00Z"),
                    "start_time": parse_datetime("2024-01-01T00:00:00Z"),
                },
                "project_id": "d2c94c27-3b76-4a42-b88c-95a85e392c68",
            },
            pagination={
                "token": "token",
                "page_size": 100,
            },
        )
        assert_matches_type(SyncRecordsPage[EnvironmentUsageRecord], usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_environment_runtime_records(self, client: Gitpod) -> None:
        response = client.usage.with_raw_response.list_environment_runtime_records()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(SyncRecordsPage[EnvironmentUsageRecord], usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_environment_runtime_records(self, client: Gitpod) -> None:
        with client.usage.with_streaming_response.list_environment_runtime_records() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(SyncRecordsPage[EnvironmentUsageRecord], usage, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUsage:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_adoption_usage_summary(self, async_client: AsyncGitpod) -> None:
        usage = await async_client.usage.get_adoption_usage_summary(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
        )
        assert_matches_type(UsageGetAdoptionUsageSummaryResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_adoption_usage_summary_with_all_params(self, async_client: AsyncGitpod) -> None:
        usage = await async_client.usage.get_adoption_usage_summary(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            project_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
            team_id="teamId",
            user_id="userId",
        )
        assert_matches_type(UsageGetAdoptionUsageSummaryResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_adoption_usage_summary(self, async_client: AsyncGitpod) -> None:
        response = await async_client.usage.with_raw_response.get_adoption_usage_summary(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(UsageGetAdoptionUsageSummaryResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_adoption_usage_summary(self, async_client: AsyncGitpod) -> None:
        async with async_client.usage.with_streaming_response.get_adoption_usage_summary(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageGetAdoptionUsageSummaryResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_agent_trace_summary(self, async_client: AsyncGitpod) -> None:
        usage = await async_client.usage.get_agent_trace_summary(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
        )
        assert_matches_type(UsageGetAgentTraceSummaryResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_agent_trace_summary_with_all_params(self, async_client: AsyncGitpod) -> None:
        usage = await async_client.usage.get_agent_trace_summary(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            project_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
            team_id="teamId",
            user_id="userId",
        )
        assert_matches_type(UsageGetAgentTraceSummaryResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_agent_trace_summary(self, async_client: AsyncGitpod) -> None:
        response = await async_client.usage.with_raw_response.get_agent_trace_summary(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(UsageGetAgentTraceSummaryResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_agent_trace_summary(self, async_client: AsyncGitpod) -> None:
        async with async_client.usage.with_streaming_response.get_agent_trace_summary(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageGetAgentTraceSummaryResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_agent_trace_time_series(self, async_client: AsyncGitpod) -> None:
        usage = await async_client.usage.get_agent_trace_time_series(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
        )
        assert_matches_type(UsageGetAgentTraceTimeSeriesResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_agent_trace_time_series_with_all_params(self, async_client: AsyncGitpod) -> None:
        usage = await async_client.usage.get_agent_trace_time_series(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            project_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
            resolution="RESOLUTION_WEEKLY",
            team_id="teamId",
            user_id="userId",
        )
        assert_matches_type(UsageGetAgentTraceTimeSeriesResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_agent_trace_time_series(self, async_client: AsyncGitpod) -> None:
        response = await async_client.usage.with_raw_response.get_agent_trace_time_series(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(UsageGetAgentTraceTimeSeriesResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_agent_trace_time_series(self, async_client: AsyncGitpod) -> None:
        async with async_client.usage.with_streaming_response.get_agent_trace_time_series(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageGetAgentTraceTimeSeriesResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_co_author_summary(self, async_client: AsyncGitpod) -> None:
        usage = await async_client.usage.get_co_author_summary(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
        )
        assert_matches_type(UsageGetCoAuthorSummaryResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_co_author_summary_with_all_params(self, async_client: AsyncGitpod) -> None:
        usage = await async_client.usage.get_co_author_summary(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            project_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
            team_id="teamId",
            user_id="userId",
        )
        assert_matches_type(UsageGetCoAuthorSummaryResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_co_author_summary(self, async_client: AsyncGitpod) -> None:
        response = await async_client.usage.with_raw_response.get_co_author_summary(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(UsageGetCoAuthorSummaryResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_co_author_summary(self, async_client: AsyncGitpod) -> None:
        async with async_client.usage.with_streaming_response.get_co_author_summary(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageGetCoAuthorSummaryResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_co_author_time_series(self, async_client: AsyncGitpod) -> None:
        usage = await async_client.usage.get_co_author_time_series(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
        )
        assert_matches_type(UsageGetCoAuthorTimeSeriesResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_co_author_time_series_with_all_params(self, async_client: AsyncGitpod) -> None:
        usage = await async_client.usage.get_co_author_time_series(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            project_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
            resolution="RESOLUTION_WEEKLY",
            team_id="teamId",
            user_id="userId",
        )
        assert_matches_type(UsageGetCoAuthorTimeSeriesResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_co_author_time_series(self, async_client: AsyncGitpod) -> None:
        response = await async_client.usage.with_raw_response.get_co_author_time_series(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(UsageGetCoAuthorTimeSeriesResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_co_author_time_series(self, async_client: AsyncGitpod) -> None:
        async with async_client.usage.with_streaming_response.get_co_author_time_series(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageGetCoAuthorTimeSeriesResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_pr_summary(self, async_client: AsyncGitpod) -> None:
        usage = await async_client.usage.get_pr_summary(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
        )
        assert_matches_type(UsageGetPrSummaryResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_pr_summary_with_all_params(self, async_client: AsyncGitpod) -> None:
        usage = await async_client.usage.get_pr_summary(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            project_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
            team_id="teamId",
            user_id="userId",
        )
        assert_matches_type(UsageGetPrSummaryResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_pr_summary(self, async_client: AsyncGitpod) -> None:
        response = await async_client.usage.with_raw_response.get_pr_summary(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(UsageGetPrSummaryResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_pr_summary(self, async_client: AsyncGitpod) -> None:
        async with async_client.usage.with_streaming_response.get_pr_summary(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageGetPrSummaryResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_pr_time_series(self, async_client: AsyncGitpod) -> None:
        usage = await async_client.usage.get_pr_time_series(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
        )
        assert_matches_type(UsageGetPrTimeSeriesResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_pr_time_series_with_all_params(self, async_client: AsyncGitpod) -> None:
        usage = await async_client.usage.get_pr_time_series(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
            project_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
            resolution="RESOLUTION_WEEKLY",
            team_id="teamId",
            user_id="userId",
        )
        assert_matches_type(UsageGetPrTimeSeriesResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_pr_time_series(self, async_client: AsyncGitpod) -> None:
        response = await async_client.usage.with_raw_response.get_pr_time_series(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(UsageGetPrTimeSeriesResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_pr_time_series(self, async_client: AsyncGitpod) -> None:
        async with async_client.usage.with_streaming_response.get_pr_time_series(
            date_range={
                "end_time": parse_datetime("2024-02-01T00:00:00Z"),
                "start_time": parse_datetime("2024-01-01T00:00:00Z"),
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageGetPrTimeSeriesResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_environment_runtime_records(self, async_client: AsyncGitpod) -> None:
        usage = await async_client.usage.list_environment_runtime_records()
        assert_matches_type(AsyncRecordsPage[EnvironmentUsageRecord], usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_environment_runtime_records_with_all_params(self, async_client: AsyncGitpod) -> None:
        usage = await async_client.usage.list_environment_runtime_records(
            token="token",
            page_size=0,
            filter={
                "date_range": {
                    "end_time": parse_datetime("2024-01-02T00:00:00Z"),
                    "start_time": parse_datetime("2024-01-01T00:00:00Z"),
                },
                "project_id": "d2c94c27-3b76-4a42-b88c-95a85e392c68",
            },
            pagination={
                "token": "token",
                "page_size": 100,
            },
        )
        assert_matches_type(AsyncRecordsPage[EnvironmentUsageRecord], usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_environment_runtime_records(self, async_client: AsyncGitpod) -> None:
        response = await async_client.usage.with_raw_response.list_environment_runtime_records()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(AsyncRecordsPage[EnvironmentUsageRecord], usage, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_environment_runtime_records(self, async_client: AsyncGitpod) -> None:
        async with async_client.usage.with_streaming_response.list_environment_runtime_records() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(AsyncRecordsPage[EnvironmentUsageRecord], usage, path=["response"])

        assert cast(Any, response.is_closed) is True
