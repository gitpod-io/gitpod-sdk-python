# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.pagination import SyncProjectEnvironmentClassesPage, AsyncProjectEnvironmentClassesPage
from gitpod.types.shared import ProjectEnvironmentClass

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEnvironmentClases:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Gitpod) -> None:
        environment_clase = client.projects.environment_clases.update()
        assert_matches_type(object, environment_clase, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Gitpod) -> None:
        environment_clase = client.projects.environment_clases.update(
            project_environment_classes=[
                {
                    "environment_class_id": "b0e12f6c-4c67-429d-a4a6-d9838b5da041",
                    "local_runner": True,
                    "order": 0,
                },
                {
                    "environment_class_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "local_runner": True,
                    "order": 1,
                },
            ],
            project_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(object, environment_clase, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Gitpod) -> None:
        response = client.projects.environment_clases.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment_clase = response.parse()
        assert_matches_type(object, environment_clase, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Gitpod) -> None:
        with client.projects.environment_clases.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment_clase = response.parse()
            assert_matches_type(object, environment_clase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Gitpod) -> None:
        environment_clase = client.projects.environment_clases.list()
        assert_matches_type(
            SyncProjectEnvironmentClassesPage[ProjectEnvironmentClass], environment_clase, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Gitpod) -> None:
        environment_clase = client.projects.environment_clases.list(
            token="token",
            page_size=0,
            pagination={
                "token": "token",
                "page_size": 20,
            },
            project_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(
            SyncProjectEnvironmentClassesPage[ProjectEnvironmentClass], environment_clase, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Gitpod) -> None:
        response = client.projects.environment_clases.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment_clase = response.parse()
        assert_matches_type(
            SyncProjectEnvironmentClassesPage[ProjectEnvironmentClass], environment_clase, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Gitpod) -> None:
        with client.projects.environment_clases.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment_clase = response.parse()
            assert_matches_type(
                SyncProjectEnvironmentClassesPage[ProjectEnvironmentClass], environment_clase, path=["response"]
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncEnvironmentClases:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncGitpod) -> None:
        environment_clase = await async_client.projects.environment_clases.update()
        assert_matches_type(object, environment_clase, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGitpod) -> None:
        environment_clase = await async_client.projects.environment_clases.update(
            project_environment_classes=[
                {
                    "environment_class_id": "b0e12f6c-4c67-429d-a4a6-d9838b5da041",
                    "local_runner": True,
                    "order": 0,
                },
                {
                    "environment_class_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "local_runner": True,
                    "order": 1,
                },
            ],
            project_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(object, environment_clase, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGitpod) -> None:
        response = await async_client.projects.environment_clases.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment_clase = await response.parse()
        assert_matches_type(object, environment_clase, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGitpod) -> None:
        async with async_client.projects.environment_clases.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment_clase = await response.parse()
            assert_matches_type(object, environment_clase, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncGitpod) -> None:
        environment_clase = await async_client.projects.environment_clases.list()
        assert_matches_type(
            AsyncProjectEnvironmentClassesPage[ProjectEnvironmentClass], environment_clase, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGitpod) -> None:
        environment_clase = await async_client.projects.environment_clases.list(
            token="token",
            page_size=0,
            pagination={
                "token": "token",
                "page_size": 20,
            },
            project_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(
            AsyncProjectEnvironmentClassesPage[ProjectEnvironmentClass], environment_clase, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGitpod) -> None:
        response = await async_client.projects.environment_clases.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment_clase = await response.parse()
        assert_matches_type(
            AsyncProjectEnvironmentClassesPage[ProjectEnvironmentClass], environment_clase, path=["response"]
        )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGitpod) -> None:
        async with async_client.projects.environment_clases.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment_clase = await response.parse()
            assert_matches_type(
                AsyncProjectEnvironmentClassesPage[ProjectEnvironmentClass], environment_clase, path=["response"]
            )

        assert cast(Any, response.is_closed) is True
