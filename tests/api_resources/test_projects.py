# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.types import (
    ProjectCreateResponse,
    ProjectRetrieveResponse,
    ProjectCreateFromEnvironmentResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProjects:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gitpod) -> None:
        project = client.projects.create(
            environment_class={},
            initializer={},
            connect_protocol_version=1,
        )
        assert_matches_type(ProjectCreateResponse, project, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gitpod) -> None:
        project = client.projects.create(
            environment_class={},
            initializer={"specs": [{}, {}, {}]},
            connect_protocol_version=1,
            automations_file_path="automationsFilePath",
            devcontainer_file_path="devcontainerFilePath",
            name="x",
            connect_timeout_ms=0,
        )
        assert_matches_type(ProjectCreateResponse, project, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gitpod) -> None:
        response = client.projects.with_raw_response.create(
            environment_class={},
            initializer={},
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectCreateResponse, project, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gitpod) -> None:
        with client.projects.with_streaming_response.create(
            environment_class={},
            initializer={},
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectCreateResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Gitpod) -> None:
        project = client.projects.retrieve(
            connect_protocol_version=1,
        )
        assert_matches_type(ProjectRetrieveResponse, project, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Gitpod) -> None:
        project = client.projects.retrieve(
            connect_protocol_version=1,
            base64="base64",
            compression="compression",
            connect="connect",
            encoding="encoding",
            message="message",
            connect_timeout_ms=0,
        )
        assert_matches_type(ProjectRetrieveResponse, project, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Gitpod) -> None:
        response = client.projects.with_raw_response.retrieve(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectRetrieveResponse, project, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Gitpod) -> None:
        with client.projects.with_streaming_response.retrieve(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectRetrieveResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_from_environment(self, client: Gitpod) -> None:
        project = client.projects.create_from_environment(
            connect_protocol_version=1,
        )
        assert_matches_type(ProjectCreateFromEnvironmentResponse, project, path=["response"])

    @parametrize
    def test_method_create_from_environment_with_all_params(self, client: Gitpod) -> None:
        project = client.projects.create_from_environment(
            connect_protocol_version=1,
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
            connect_timeout_ms=0,
        )
        assert_matches_type(ProjectCreateFromEnvironmentResponse, project, path=["response"])

    @parametrize
    def test_raw_response_create_from_environment(self, client: Gitpod) -> None:
        response = client.projects.with_raw_response.create_from_environment(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectCreateFromEnvironmentResponse, project, path=["response"])

    @parametrize
    def test_streaming_response_create_from_environment(self, client: Gitpod) -> None:
        with client.projects.with_streaming_response.create_from_environment(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectCreateFromEnvironmentResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncProjects:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncGitpod) -> None:
        project = await async_client.projects.create(
            environment_class={},
            initializer={},
            connect_protocol_version=1,
        )
        assert_matches_type(ProjectCreateResponse, project, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGitpod) -> None:
        project = await async_client.projects.create(
            environment_class={},
            initializer={"specs": [{}, {}, {}]},
            connect_protocol_version=1,
            automations_file_path="automationsFilePath",
            devcontainer_file_path="devcontainerFilePath",
            name="x",
            connect_timeout_ms=0,
        )
        assert_matches_type(ProjectCreateResponse, project, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGitpod) -> None:
        response = await async_client.projects.with_raw_response.create(
            environment_class={},
            initializer={},
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectCreateResponse, project, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGitpod) -> None:
        async with async_client.projects.with_streaming_response.create(
            environment_class={},
            initializer={},
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectCreateResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGitpod) -> None:
        project = await async_client.projects.retrieve(
            connect_protocol_version=1,
        )
        assert_matches_type(ProjectRetrieveResponse, project, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncGitpod) -> None:
        project = await async_client.projects.retrieve(
            connect_protocol_version=1,
            base64="base64",
            compression="compression",
            connect="connect",
            encoding="encoding",
            message="message",
            connect_timeout_ms=0,
        )
        assert_matches_type(ProjectRetrieveResponse, project, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGitpod) -> None:
        response = await async_client.projects.with_raw_response.retrieve(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectRetrieveResponse, project, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGitpod) -> None:
        async with async_client.projects.with_streaming_response.retrieve(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectRetrieveResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_from_environment(self, async_client: AsyncGitpod) -> None:
        project = await async_client.projects.create_from_environment(
            connect_protocol_version=1,
        )
        assert_matches_type(ProjectCreateFromEnvironmentResponse, project, path=["response"])

    @parametrize
    async def test_method_create_from_environment_with_all_params(self, async_client: AsyncGitpod) -> None:
        project = await async_client.projects.create_from_environment(
            connect_protocol_version=1,
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
            connect_timeout_ms=0,
        )
        assert_matches_type(ProjectCreateFromEnvironmentResponse, project, path=["response"])

    @parametrize
    async def test_raw_response_create_from_environment(self, async_client: AsyncGitpod) -> None:
        response = await async_client.projects.with_raw_response.create_from_environment(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectCreateFromEnvironmentResponse, project, path=["response"])

    @parametrize
    async def test_streaming_response_create_from_environment(self, async_client: AsyncGitpod) -> None:
        async with async_client.projects.with_streaming_response.create_from_environment(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectCreateFromEnvironmentResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True
