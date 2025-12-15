# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.types import (
    Prebuild,
    PrebuildCancelResponse,
    PrebuildCreateResponse,
    PrebuildRetrieveResponse,
    PrebuildCreateLogsTokenResponse,
)
from gitpod.pagination import SyncPrebuildsPage, AsyncPrebuildsPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPrebuilds:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Gitpod) -> None:
        prebuild = client.prebuilds.create(
            project_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            spec={},
        )
        assert_matches_type(PrebuildCreateResponse, prebuild, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Gitpod) -> None:
        prebuild = client.prebuilds.create(
            project_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            spec={
                "desired_phase": "PREBUILD_PHASE_UNSPECIFIED",
                "spec_version": "specVersion",
                "timeout": "3600s",
            },
            environment_class_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PrebuildCreateResponse, prebuild, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Gitpod) -> None:
        response = client.prebuilds.with_raw_response.create(
            project_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            spec={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prebuild = response.parse()
        assert_matches_type(PrebuildCreateResponse, prebuild, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Gitpod) -> None:
        with client.prebuilds.with_streaming_response.create(
            project_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            spec={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prebuild = response.parse()
            assert_matches_type(PrebuildCreateResponse, prebuild, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Gitpod) -> None:
        prebuild = client.prebuilds.retrieve(
            prebuild_id="07e03a28-65a5-4d98-b532-8ea67b188048",
        )
        assert_matches_type(PrebuildRetrieveResponse, prebuild, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Gitpod) -> None:
        response = client.prebuilds.with_raw_response.retrieve(
            prebuild_id="07e03a28-65a5-4d98-b532-8ea67b188048",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prebuild = response.parse()
        assert_matches_type(PrebuildRetrieveResponse, prebuild, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Gitpod) -> None:
        with client.prebuilds.with_streaming_response.retrieve(
            prebuild_id="07e03a28-65a5-4d98-b532-8ea67b188048",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prebuild = response.parse()
            assert_matches_type(PrebuildRetrieveResponse, prebuild, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Gitpod) -> None:
        prebuild = client.prebuilds.list()
        assert_matches_type(SyncPrebuildsPage[Prebuild], prebuild, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Gitpod) -> None:
        prebuild = client.prebuilds.list(
            token="token",
            page_size=0,
            filter={
                "phases": ["PREBUILD_PHASE_UNSPECIFIED"],
                "project_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            },
            pagination={
                "token": "token",
                "page_size": 100,
            },
        )
        assert_matches_type(SyncPrebuildsPage[Prebuild], prebuild, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Gitpod) -> None:
        response = client.prebuilds.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prebuild = response.parse()
        assert_matches_type(SyncPrebuildsPage[Prebuild], prebuild, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Gitpod) -> None:
        with client.prebuilds.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prebuild = response.parse()
            assert_matches_type(SyncPrebuildsPage[Prebuild], prebuild, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Gitpod) -> None:
        prebuild = client.prebuilds.delete(
            prebuild_id="07e03a28-65a5-4d98-b532-8ea67b188048",
        )
        assert_matches_type(object, prebuild, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Gitpod) -> None:
        response = client.prebuilds.with_raw_response.delete(
            prebuild_id="07e03a28-65a5-4d98-b532-8ea67b188048",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prebuild = response.parse()
        assert_matches_type(object, prebuild, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Gitpod) -> None:
        with client.prebuilds.with_streaming_response.delete(
            prebuild_id="07e03a28-65a5-4d98-b532-8ea67b188048",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prebuild = response.parse()
            assert_matches_type(object, prebuild, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_cancel(self, client: Gitpod) -> None:
        prebuild = client.prebuilds.cancel(
            prebuild_id="07e03a28-65a5-4d98-b532-8ea67b188048",
        )
        assert_matches_type(PrebuildCancelResponse, prebuild, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_cancel(self, client: Gitpod) -> None:
        response = client.prebuilds.with_raw_response.cancel(
            prebuild_id="07e03a28-65a5-4d98-b532-8ea67b188048",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prebuild = response.parse()
        assert_matches_type(PrebuildCancelResponse, prebuild, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_cancel(self, client: Gitpod) -> None:
        with client.prebuilds.with_streaming_response.cancel(
            prebuild_id="07e03a28-65a5-4d98-b532-8ea67b188048",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prebuild = response.parse()
            assert_matches_type(PrebuildCancelResponse, prebuild, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_logs_token(self, client: Gitpod) -> None:
        prebuild = client.prebuilds.create_logs_token(
            prebuild_id="07e03a28-65a5-4d98-b532-8ea67b188048",
        )
        assert_matches_type(PrebuildCreateLogsTokenResponse, prebuild, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_logs_token(self, client: Gitpod) -> None:
        response = client.prebuilds.with_raw_response.create_logs_token(
            prebuild_id="07e03a28-65a5-4d98-b532-8ea67b188048",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prebuild = response.parse()
        assert_matches_type(PrebuildCreateLogsTokenResponse, prebuild, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_logs_token(self, client: Gitpod) -> None:
        with client.prebuilds.with_streaming_response.create_logs_token(
            prebuild_id="07e03a28-65a5-4d98-b532-8ea67b188048",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prebuild = response.parse()
            assert_matches_type(PrebuildCreateLogsTokenResponse, prebuild, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPrebuilds:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncGitpod) -> None:
        prebuild = await async_client.prebuilds.create(
            project_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            spec={},
        )
        assert_matches_type(PrebuildCreateResponse, prebuild, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGitpod) -> None:
        prebuild = await async_client.prebuilds.create(
            project_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            spec={
                "desired_phase": "PREBUILD_PHASE_UNSPECIFIED",
                "spec_version": "specVersion",
                "timeout": "3600s",
            },
            environment_class_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PrebuildCreateResponse, prebuild, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGitpod) -> None:
        response = await async_client.prebuilds.with_raw_response.create(
            project_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            spec={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prebuild = await response.parse()
        assert_matches_type(PrebuildCreateResponse, prebuild, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGitpod) -> None:
        async with async_client.prebuilds.with_streaming_response.create(
            project_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            spec={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prebuild = await response.parse()
            assert_matches_type(PrebuildCreateResponse, prebuild, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGitpod) -> None:
        prebuild = await async_client.prebuilds.retrieve(
            prebuild_id="07e03a28-65a5-4d98-b532-8ea67b188048",
        )
        assert_matches_type(PrebuildRetrieveResponse, prebuild, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGitpod) -> None:
        response = await async_client.prebuilds.with_raw_response.retrieve(
            prebuild_id="07e03a28-65a5-4d98-b532-8ea67b188048",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prebuild = await response.parse()
        assert_matches_type(PrebuildRetrieveResponse, prebuild, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGitpod) -> None:
        async with async_client.prebuilds.with_streaming_response.retrieve(
            prebuild_id="07e03a28-65a5-4d98-b532-8ea67b188048",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prebuild = await response.parse()
            assert_matches_type(PrebuildRetrieveResponse, prebuild, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncGitpod) -> None:
        prebuild = await async_client.prebuilds.list()
        assert_matches_type(AsyncPrebuildsPage[Prebuild], prebuild, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGitpod) -> None:
        prebuild = await async_client.prebuilds.list(
            token="token",
            page_size=0,
            filter={
                "phases": ["PREBUILD_PHASE_UNSPECIFIED"],
                "project_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            },
            pagination={
                "token": "token",
                "page_size": 100,
            },
        )
        assert_matches_type(AsyncPrebuildsPage[Prebuild], prebuild, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGitpod) -> None:
        response = await async_client.prebuilds.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prebuild = await response.parse()
        assert_matches_type(AsyncPrebuildsPage[Prebuild], prebuild, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGitpod) -> None:
        async with async_client.prebuilds.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prebuild = await response.parse()
            assert_matches_type(AsyncPrebuildsPage[Prebuild], prebuild, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncGitpod) -> None:
        prebuild = await async_client.prebuilds.delete(
            prebuild_id="07e03a28-65a5-4d98-b532-8ea67b188048",
        )
        assert_matches_type(object, prebuild, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGitpod) -> None:
        response = await async_client.prebuilds.with_raw_response.delete(
            prebuild_id="07e03a28-65a5-4d98-b532-8ea67b188048",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prebuild = await response.parse()
        assert_matches_type(object, prebuild, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGitpod) -> None:
        async with async_client.prebuilds.with_streaming_response.delete(
            prebuild_id="07e03a28-65a5-4d98-b532-8ea67b188048",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prebuild = await response.parse()
            assert_matches_type(object, prebuild, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncGitpod) -> None:
        prebuild = await async_client.prebuilds.cancel(
            prebuild_id="07e03a28-65a5-4d98-b532-8ea67b188048",
        )
        assert_matches_type(PrebuildCancelResponse, prebuild, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncGitpod) -> None:
        response = await async_client.prebuilds.with_raw_response.cancel(
            prebuild_id="07e03a28-65a5-4d98-b532-8ea67b188048",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prebuild = await response.parse()
        assert_matches_type(PrebuildCancelResponse, prebuild, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncGitpod) -> None:
        async with async_client.prebuilds.with_streaming_response.cancel(
            prebuild_id="07e03a28-65a5-4d98-b532-8ea67b188048",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prebuild = await response.parse()
            assert_matches_type(PrebuildCancelResponse, prebuild, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_logs_token(self, async_client: AsyncGitpod) -> None:
        prebuild = await async_client.prebuilds.create_logs_token(
            prebuild_id="07e03a28-65a5-4d98-b532-8ea67b188048",
        )
        assert_matches_type(PrebuildCreateLogsTokenResponse, prebuild, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_logs_token(self, async_client: AsyncGitpod) -> None:
        response = await async_client.prebuilds.with_raw_response.create_logs_token(
            prebuild_id="07e03a28-65a5-4d98-b532-8ea67b188048",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prebuild = await response.parse()
        assert_matches_type(PrebuildCreateLogsTokenResponse, prebuild, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_logs_token(self, async_client: AsyncGitpod) -> None:
        async with async_client.prebuilds.with_streaming_response.create_logs_token(
            prebuild_id="07e03a28-65a5-4d98-b532-8ea67b188048",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prebuild = await response.parse()
            assert_matches_type(PrebuildCreateLogsTokenResponse, prebuild, path=["response"])

        assert cast(Any, response.is_closed) is True
