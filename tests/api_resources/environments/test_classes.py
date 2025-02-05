# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.pagination import SyncEnvironmentClassesPage, AsyncEnvironmentClassesPage
from gitpod.types.environments import ClassListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClasses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Gitpod) -> None:
        class_ = client.environments.classes.list()
        assert_matches_type(SyncEnvironmentClassesPage[ClassListResponse], class_, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gitpod) -> None:
        class_ = client.environments.classes.list(
            token="token",
            page_size=0,
            filter={"enabled": True},
            pagination={
                "token": "token",
                "page_size": 100,
            },
        )
        assert_matches_type(SyncEnvironmentClassesPage[ClassListResponse], class_, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gitpod) -> None:
        response = client.environments.classes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        class_ = response.parse()
        assert_matches_type(SyncEnvironmentClassesPage[ClassListResponse], class_, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gitpod) -> None:
        with client.environments.classes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            class_ = response.parse()
            assert_matches_type(SyncEnvironmentClassesPage[ClassListResponse], class_, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncClasses:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncGitpod) -> None:
        class_ = await async_client.environments.classes.list()
        assert_matches_type(AsyncEnvironmentClassesPage[ClassListResponse], class_, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGitpod) -> None:
        class_ = await async_client.environments.classes.list(
            token="token",
            page_size=0,
            filter={"enabled": True},
            pagination={
                "token": "token",
                "page_size": 100,
            },
        )
        assert_matches_type(AsyncEnvironmentClassesPage[ClassListResponse], class_, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.classes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        class_ = await response.parse()
        assert_matches_type(AsyncEnvironmentClassesPage[ClassListResponse], class_, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.classes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            class_ = await response.parse()
            assert_matches_type(AsyncEnvironmentClassesPage[ClassListResponse], class_, path=["response"])

        assert cast(Any, response.is_closed) is True
