# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.types import EnvironmentClassListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEnvironmentClasses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Gitpod) -> None:
        environment_class = client.environment_classes.list(
            connect_protocol_version=1,
        )
        assert_matches_type(EnvironmentClassListResponse, environment_class, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gitpod) -> None:
        environment_class = client.environment_classes.list(
            connect_protocol_version=1,
            filter={},
            pagination={
                "token": "token",
                "page_size": 100,
            },
            connect_timeout_ms=0,
        )
        assert_matches_type(EnvironmentClassListResponse, environment_class, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gitpod) -> None:
        response = client.environment_classes.with_raw_response.list(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment_class = response.parse()
        assert_matches_type(EnvironmentClassListResponse, environment_class, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gitpod) -> None:
        with client.environment_classes.with_streaming_response.list(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment_class = response.parse()
            assert_matches_type(EnvironmentClassListResponse, environment_class, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEnvironmentClasses:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncGitpod) -> None:
        environment_class = await async_client.environment_classes.list(
            connect_protocol_version=1,
        )
        assert_matches_type(EnvironmentClassListResponse, environment_class, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGitpod) -> None:
        environment_class = await async_client.environment_classes.list(
            connect_protocol_version=1,
            filter={},
            pagination={
                "token": "token",
                "page_size": 100,
            },
            connect_timeout_ms=0,
        )
        assert_matches_type(EnvironmentClassListResponse, environment_class, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environment_classes.with_raw_response.list(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment_class = await response.parse()
        assert_matches_type(EnvironmentClassListResponse, environment_class, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGitpod) -> None:
        async with async_client.environment_classes.with_streaming_response.list(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment_class = await response.parse()
            assert_matches_type(EnvironmentClassListResponse, environment_class, path=["response"])

        assert cast(Any, response.is_closed) is True
