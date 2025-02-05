# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.types import (
    ProjectListResponse,
    ProjectCreateResponse,
    ProjectUpdateResponse,
    ProjectRetrieveResponse,
    ProjectCreateFromEnvironmentResponse,
)
from gitpod.pagination import SyncPersonalAccessTokensPage, AsyncPersonalAccessTokensPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProjects:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gitpod) -> None:
        project = client.projects.create(
            environment_class={"environment_class_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            initializer={},
        )
        assert_matches_type(ProjectCreateResponse, project, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gitpod) -> None:
        project = client.projects.create(
            environment_class={"environment_class_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            initializer={"specs": [{"context_url": {"url": "https://example.com"}}]},
            automations_file_path="automationsFilePath",
            devcontainer_file_path="devcontainerFilePath",
            name="x",
        )
        assert_matches_type(ProjectCreateResponse, project, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gitpod) -> None:
        response = client.projects.with_raw_response.create(
            environment_class={"environment_class_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            initializer={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectCreateResponse, project, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gitpod) -> None:
        with client.projects.with_streaming_response.create(
            environment_class={"environment_class_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            initializer={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectCreateResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Gitpod) -> None:
        project = client.projects.retrieve()
        assert_matches_type(ProjectRetrieveResponse, project, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Gitpod) -> None:
        project = client.projects.retrieve(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProjectRetrieveResponse, project, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Gitpod) -> None:
        response = client.projects.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectRetrieveResponse, project, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Gitpod) -> None:
        with client.projects.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectRetrieveResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_overload_1(self, client: Gitpod) -> None:
        project = client.projects.update(
            automations_file_path="automationsFilePath",
        )
        assert_matches_type(ProjectUpdateResponse, project, path=["response"])

    @parametrize
    def test_raw_response_update_overload_1(self, client: Gitpod) -> None:
        response = client.projects.with_raw_response.update(
            automations_file_path="automationsFilePath",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectUpdateResponse, project, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_1(self, client: Gitpod) -> None:
        with client.projects.with_streaming_response.update(
            automations_file_path="automationsFilePath",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectUpdateResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_overload_2(self, client: Gitpod) -> None:
        project = client.projects.update(
            devcontainer_file_path="devcontainerFilePath",
        )
        assert_matches_type(ProjectUpdateResponse, project, path=["response"])

    @parametrize
    def test_raw_response_update_overload_2(self, client: Gitpod) -> None:
        response = client.projects.with_raw_response.update(
            devcontainer_file_path="devcontainerFilePath",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectUpdateResponse, project, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_2(self, client: Gitpod) -> None:
        with client.projects.with_streaming_response.update(
            devcontainer_file_path="devcontainerFilePath",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectUpdateResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_overload_3(self, client: Gitpod) -> None:
        project = client.projects.update(
            environment_class={"environment_class_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
        )
        assert_matches_type(ProjectUpdateResponse, project, path=["response"])

    @parametrize
    def test_raw_response_update_overload_3(self, client: Gitpod) -> None:
        response = client.projects.with_raw_response.update(
            environment_class={"environment_class_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectUpdateResponse, project, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_3(self, client: Gitpod) -> None:
        with client.projects.with_streaming_response.update(
            environment_class={"environment_class_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectUpdateResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_overload_4(self, client: Gitpod) -> None:
        project = client.projects.update(
            initializer={},
        )
        assert_matches_type(ProjectUpdateResponse, project, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_4(self, client: Gitpod) -> None:
        project = client.projects.update(
            initializer={"specs": [{"context_url": {"url": "https://example.com"}}]},
        )
        assert_matches_type(ProjectUpdateResponse, project, path=["response"])

    @parametrize
    def test_raw_response_update_overload_4(self, client: Gitpod) -> None:
        response = client.projects.with_raw_response.update(
            initializer={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectUpdateResponse, project, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_4(self, client: Gitpod) -> None:
        with client.projects.with_streaming_response.update(
            initializer={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectUpdateResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_overload_5(self, client: Gitpod) -> None:
        project = client.projects.update(
            name="x",
        )
        assert_matches_type(ProjectUpdateResponse, project, path=["response"])

    @parametrize
    def test_raw_response_update_overload_5(self, client: Gitpod) -> None:
        response = client.projects.with_raw_response.update(
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectUpdateResponse, project, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_5(self, client: Gitpod) -> None:
        with client.projects.with_streaming_response.update(
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(ProjectUpdateResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gitpod) -> None:
        project = client.projects.list()
        assert_matches_type(SyncPersonalAccessTokensPage[ProjectListResponse], project, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gitpod) -> None:
        project = client.projects.list(
            token="token",
            page_size=0,
            pagination={
                "token": "token",
                "page_size": 100,
            },
        )
        assert_matches_type(SyncPersonalAccessTokensPage[ProjectListResponse], project, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gitpod) -> None:
        response = client.projects.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(SyncPersonalAccessTokensPage[ProjectListResponse], project, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gitpod) -> None:
        with client.projects.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(SyncPersonalAccessTokensPage[ProjectListResponse], project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gitpod) -> None:
        project = client.projects.delete()
        assert_matches_type(object, project, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Gitpod) -> None:
        project = client.projects.delete(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, project, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gitpod) -> None:
        response = client.projects.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(object, project, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gitpod) -> None:
        with client.projects.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = response.parse()
            assert_matches_type(object, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_from_environment(self, client: Gitpod) -> None:
        project = client.projects.create_from_environment()
        assert_matches_type(ProjectCreateFromEnvironmentResponse, project, path=["response"])

    @parametrize
    def test_method_create_from_environment_with_all_params(self, client: Gitpod) -> None:
        project = client.projects.create_from_environment(
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
        )
        assert_matches_type(ProjectCreateFromEnvironmentResponse, project, path=["response"])

    @parametrize
    def test_raw_response_create_from_environment(self, client: Gitpod) -> None:
        response = client.projects.with_raw_response.create_from_environment()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = response.parse()
        assert_matches_type(ProjectCreateFromEnvironmentResponse, project, path=["response"])

    @parametrize
    def test_streaming_response_create_from_environment(self, client: Gitpod) -> None:
        with client.projects.with_streaming_response.create_from_environment() as response:
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
            environment_class={"environment_class_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            initializer={},
        )
        assert_matches_type(ProjectCreateResponse, project, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGitpod) -> None:
        project = await async_client.projects.create(
            environment_class={"environment_class_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            initializer={"specs": [{"context_url": {"url": "https://example.com"}}]},
            automations_file_path="automationsFilePath",
            devcontainer_file_path="devcontainerFilePath",
            name="x",
        )
        assert_matches_type(ProjectCreateResponse, project, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGitpod) -> None:
        response = await async_client.projects.with_raw_response.create(
            environment_class={"environment_class_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            initializer={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectCreateResponse, project, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGitpod) -> None:
        async with async_client.projects.with_streaming_response.create(
            environment_class={"environment_class_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            initializer={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectCreateResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGitpod) -> None:
        project = await async_client.projects.retrieve()
        assert_matches_type(ProjectRetrieveResponse, project, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncGitpod) -> None:
        project = await async_client.projects.retrieve(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ProjectRetrieveResponse, project, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGitpod) -> None:
        response = await async_client.projects.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectRetrieveResponse, project, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGitpod) -> None:
        async with async_client.projects.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectRetrieveResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncGitpod) -> None:
        project = await async_client.projects.update(
            automations_file_path="automationsFilePath",
        )
        assert_matches_type(ProjectUpdateResponse, project, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncGitpod) -> None:
        response = await async_client.projects.with_raw_response.update(
            automations_file_path="automationsFilePath",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectUpdateResponse, project, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncGitpod) -> None:
        async with async_client.projects.with_streaming_response.update(
            automations_file_path="automationsFilePath",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectUpdateResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncGitpod) -> None:
        project = await async_client.projects.update(
            devcontainer_file_path="devcontainerFilePath",
        )
        assert_matches_type(ProjectUpdateResponse, project, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncGitpod) -> None:
        response = await async_client.projects.with_raw_response.update(
            devcontainer_file_path="devcontainerFilePath",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectUpdateResponse, project, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncGitpod) -> None:
        async with async_client.projects.with_streaming_response.update(
            devcontainer_file_path="devcontainerFilePath",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectUpdateResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_overload_3(self, async_client: AsyncGitpod) -> None:
        project = await async_client.projects.update(
            environment_class={"environment_class_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
        )
        assert_matches_type(ProjectUpdateResponse, project, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_3(self, async_client: AsyncGitpod) -> None:
        response = await async_client.projects.with_raw_response.update(
            environment_class={"environment_class_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectUpdateResponse, project, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_3(self, async_client: AsyncGitpod) -> None:
        async with async_client.projects.with_streaming_response.update(
            environment_class={"environment_class_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectUpdateResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_overload_4(self, async_client: AsyncGitpod) -> None:
        project = await async_client.projects.update(
            initializer={},
        )
        assert_matches_type(ProjectUpdateResponse, project, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_4(self, async_client: AsyncGitpod) -> None:
        project = await async_client.projects.update(
            initializer={"specs": [{"context_url": {"url": "https://example.com"}}]},
        )
        assert_matches_type(ProjectUpdateResponse, project, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_4(self, async_client: AsyncGitpod) -> None:
        response = await async_client.projects.with_raw_response.update(
            initializer={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectUpdateResponse, project, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_4(self, async_client: AsyncGitpod) -> None:
        async with async_client.projects.with_streaming_response.update(
            initializer={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectUpdateResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_overload_5(self, async_client: AsyncGitpod) -> None:
        project = await async_client.projects.update(
            name="x",
        )
        assert_matches_type(ProjectUpdateResponse, project, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_5(self, async_client: AsyncGitpod) -> None:
        response = await async_client.projects.with_raw_response.update(
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectUpdateResponse, project, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_5(self, async_client: AsyncGitpod) -> None:
        async with async_client.projects.with_streaming_response.update(
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectUpdateResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGitpod) -> None:
        project = await async_client.projects.list()
        assert_matches_type(AsyncPersonalAccessTokensPage[ProjectListResponse], project, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGitpod) -> None:
        project = await async_client.projects.list(
            token="token",
            page_size=0,
            pagination={
                "token": "token",
                "page_size": 100,
            },
        )
        assert_matches_type(AsyncPersonalAccessTokensPage[ProjectListResponse], project, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGitpod) -> None:
        response = await async_client.projects.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(AsyncPersonalAccessTokensPage[ProjectListResponse], project, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGitpod) -> None:
        async with async_client.projects.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(AsyncPersonalAccessTokensPage[ProjectListResponse], project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGitpod) -> None:
        project = await async_client.projects.delete()
        assert_matches_type(object, project, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncGitpod) -> None:
        project = await async_client.projects.delete(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, project, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGitpod) -> None:
        response = await async_client.projects.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(object, project, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGitpod) -> None:
        async with async_client.projects.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(object, project, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_from_environment(self, async_client: AsyncGitpod) -> None:
        project = await async_client.projects.create_from_environment()
        assert_matches_type(ProjectCreateFromEnvironmentResponse, project, path=["response"])

    @parametrize
    async def test_method_create_from_environment_with_all_params(self, async_client: AsyncGitpod) -> None:
        project = await async_client.projects.create_from_environment(
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
        )
        assert_matches_type(ProjectCreateFromEnvironmentResponse, project, path=["response"])

    @parametrize
    async def test_raw_response_create_from_environment(self, async_client: AsyncGitpod) -> None:
        response = await async_client.projects.with_raw_response.create_from_environment()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        project = await response.parse()
        assert_matches_type(ProjectCreateFromEnvironmentResponse, project, path=["response"])

    @parametrize
    async def test_streaming_response_create_from_environment(self, async_client: AsyncGitpod) -> None:
        async with async_client.projects.with_streaming_response.create_from_environment() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            project = await response.parse()
            assert_matches_type(ProjectCreateFromEnvironmentResponse, project, path=["response"])

        assert cast(Any, response.is_closed) is True
