# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.pagination import SyncEnvironmentClassesPage, AsyncEnvironmentClassesPage
from gitpod.types.shared import EnvironmentClass
from gitpod.types.runners.configurations import (
    EnvironmentClassCreateResponse,
    EnvironmentClassRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEnvironmentClasses:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Gitpod) -> None:
        environment_class = client.runners.configurations.environment_classes.create()
        assert_matches_type(EnvironmentClassCreateResponse, environment_class, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Gitpod) -> None:
        environment_class = client.runners.configurations.environment_classes.create(
            configuration=[
                {
                    "key": "key",
                    "value": "value",
                }
            ],
            description="xxx",
            display_name="xxx",
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EnvironmentClassCreateResponse, environment_class, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Gitpod) -> None:
        response = client.runners.configurations.environment_classes.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment_class = response.parse()
        assert_matches_type(EnvironmentClassCreateResponse, environment_class, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Gitpod) -> None:
        with client.runners.configurations.environment_classes.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment_class = response.parse()
            assert_matches_type(EnvironmentClassCreateResponse, environment_class, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Gitpod) -> None:
        environment_class = client.runners.configurations.environment_classes.retrieve()
        assert_matches_type(EnvironmentClassRetrieveResponse, environment_class, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Gitpod) -> None:
        environment_class = client.runners.configurations.environment_classes.retrieve(
            environment_class_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EnvironmentClassRetrieveResponse, environment_class, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Gitpod) -> None:
        response = client.runners.configurations.environment_classes.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment_class = response.parse()
        assert_matches_type(EnvironmentClassRetrieveResponse, environment_class, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Gitpod) -> None:
        with client.runners.configurations.environment_classes.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment_class = response.parse()
            assert_matches_type(EnvironmentClassRetrieveResponse, environment_class, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Gitpod) -> None:
        environment_class = client.runners.configurations.environment_classes.update()
        assert_matches_type(object, environment_class, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Gitpod) -> None:
        environment_class = client.runners.configurations.environment_classes.update(
            description="xxx",
            display_name="xxx",
            enabled=True,
            environment_class_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, environment_class, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Gitpod) -> None:
        response = client.runners.configurations.environment_classes.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment_class = response.parse()
        assert_matches_type(object, environment_class, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Gitpod) -> None:
        with client.runners.configurations.environment_classes.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment_class = response.parse()
            assert_matches_type(object, environment_class, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Gitpod) -> None:
        environment_class = client.runners.configurations.environment_classes.list()
        assert_matches_type(SyncEnvironmentClassesPage[EnvironmentClass], environment_class, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Gitpod) -> None:
        environment_class = client.runners.configurations.environment_classes.list(
            token="token",
            page_size=0,
            filter={
                "can_create_environments": True,
                "enabled": True,
                "runner_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "runner_kinds": ["RUNNER_KIND_UNSPECIFIED"],
                "runner_providers": ["RUNNER_PROVIDER_UNSPECIFIED"],
            },
            pagination={
                "token": "token",
                "page_size": 100,
            },
        )
        assert_matches_type(SyncEnvironmentClassesPage[EnvironmentClass], environment_class, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Gitpod) -> None:
        response = client.runners.configurations.environment_classes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment_class = response.parse()
        assert_matches_type(SyncEnvironmentClassesPage[EnvironmentClass], environment_class, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Gitpod) -> None:
        with client.runners.configurations.environment_classes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment_class = response.parse()
            assert_matches_type(SyncEnvironmentClassesPage[EnvironmentClass], environment_class, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEnvironmentClasses:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncGitpod) -> None:
        environment_class = await async_client.runners.configurations.environment_classes.create()
        assert_matches_type(EnvironmentClassCreateResponse, environment_class, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGitpod) -> None:
        environment_class = await async_client.runners.configurations.environment_classes.create(
            configuration=[
                {
                    "key": "key",
                    "value": "value",
                }
            ],
            description="xxx",
            display_name="xxx",
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EnvironmentClassCreateResponse, environment_class, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runners.configurations.environment_classes.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment_class = await response.parse()
        assert_matches_type(EnvironmentClassCreateResponse, environment_class, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGitpod) -> None:
        async with async_client.runners.configurations.environment_classes.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment_class = await response.parse()
            assert_matches_type(EnvironmentClassCreateResponse, environment_class, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGitpod) -> None:
        environment_class = await async_client.runners.configurations.environment_classes.retrieve()
        assert_matches_type(EnvironmentClassRetrieveResponse, environment_class, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncGitpod) -> None:
        environment_class = await async_client.runners.configurations.environment_classes.retrieve(
            environment_class_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EnvironmentClassRetrieveResponse, environment_class, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runners.configurations.environment_classes.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment_class = await response.parse()
        assert_matches_type(EnvironmentClassRetrieveResponse, environment_class, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGitpod) -> None:
        async with (
            async_client.runners.configurations.environment_classes.with_streaming_response.retrieve()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment_class = await response.parse()
            assert_matches_type(EnvironmentClassRetrieveResponse, environment_class, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncGitpod) -> None:
        environment_class = await async_client.runners.configurations.environment_classes.update()
        assert_matches_type(object, environment_class, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGitpod) -> None:
        environment_class = await async_client.runners.configurations.environment_classes.update(
            description="xxx",
            display_name="xxx",
            enabled=True,
            environment_class_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, environment_class, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runners.configurations.environment_classes.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment_class = await response.parse()
        assert_matches_type(object, environment_class, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGitpod) -> None:
        async with async_client.runners.configurations.environment_classes.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment_class = await response.parse()
            assert_matches_type(object, environment_class, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncGitpod) -> None:
        environment_class = await async_client.runners.configurations.environment_classes.list()
        assert_matches_type(AsyncEnvironmentClassesPage[EnvironmentClass], environment_class, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGitpod) -> None:
        environment_class = await async_client.runners.configurations.environment_classes.list(
            token="token",
            page_size=0,
            filter={
                "can_create_environments": True,
                "enabled": True,
                "runner_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "runner_kinds": ["RUNNER_KIND_UNSPECIFIED"],
                "runner_providers": ["RUNNER_PROVIDER_UNSPECIFIED"],
            },
            pagination={
                "token": "token",
                "page_size": 100,
            },
        )
        assert_matches_type(AsyncEnvironmentClassesPage[EnvironmentClass], environment_class, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runners.configurations.environment_classes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment_class = await response.parse()
        assert_matches_type(AsyncEnvironmentClassesPage[EnvironmentClass], environment_class, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGitpod) -> None:
        async with async_client.runners.configurations.environment_classes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment_class = await response.parse()
            assert_matches_type(AsyncEnvironmentClassesPage[EnvironmentClass], environment_class, path=["response"])

        assert cast(Any, response.is_closed) is True
