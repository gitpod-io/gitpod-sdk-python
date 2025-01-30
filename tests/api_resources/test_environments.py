# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.types import (
    EnvironmentListResponse,
    EnvironmentCreateResponse,
    EnvironmentRetrieveResponse,
    EnvironmentCreateFromProjectResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEnvironments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gitpod) -> None:
        environment = client.environments.create()
        assert_matches_type(EnvironmentCreateResponse, environment, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gitpod) -> None:
        environment = client.environments.create(
            spec={
                "admission": "ADMISSION_LEVEL_UNSPECIFIED",
                "automations_file": {
                    "automations_file_path": "automationsFilePath",
                    "session": "session",
                },
                "content": {
                    "git_email": "gitEmail",
                    "git_username": "gitUsername",
                    "initializer": {"specs": [{"context_url": {"url": "https://example.com"}}]},
                    "session": "session",
                },
                "desired_phase": "ENVIRONMENT_PHASE_UNSPECIFIED",
                "devcontainer": {
                    "devcontainer_file_path": "devcontainerFilePath",
                    "session": "session",
                },
                "machine": {
                    "class": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "session": "session",
                },
                "ports": [
                    {
                        "admission": "ADMISSION_LEVEL_UNSPECIFIED",
                        "name": "x",
                        "port": 1,
                    }
                ],
                "secrets": [
                    {
                        "environment_variable": "environmentVariable",
                        "name": "name",
                        "session": "session",
                        "source": "source",
                        "source_ref": "sourceRef",
                    }
                ],
                "spec_version": "specVersion",
                "ssh_public_keys": [
                    {
                        "id": "id",
                        "value": "value",
                    }
                ],
                "timeout": {"disconnected": "+9125115.360s"},
            },
        )
        assert_matches_type(EnvironmentCreateResponse, environment, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gitpod) -> None:
        response = client.environments.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(EnvironmentCreateResponse, environment, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gitpod) -> None:
        with client.environments.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(EnvironmentCreateResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Gitpod) -> None:
        environment = client.environments.retrieve()
        assert_matches_type(EnvironmentRetrieveResponse, environment, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Gitpod) -> None:
        environment = client.environments.retrieve(
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EnvironmentRetrieveResponse, environment, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Gitpod) -> None:
        response = client.environments.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(EnvironmentRetrieveResponse, environment, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Gitpod) -> None:
        with client.environments.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(EnvironmentRetrieveResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gitpod) -> None:
        environment = client.environments.list()
        assert_matches_type(EnvironmentListResponse, environment, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gitpod) -> None:
        environment = client.environments.list(
            filter={
                "creator_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "project_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "runner_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "runner_kinds": ["RUNNER_KIND_UNSPECIFIED"],
                "status_phases": ["ENVIRONMENT_PHASE_UNSPECIFIED"],
            },
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            pagination={
                "token": "token",
                "page_size": 100,
            },
        )
        assert_matches_type(EnvironmentListResponse, environment, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gitpod) -> None:
        response = client.environments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(EnvironmentListResponse, environment, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gitpod) -> None:
        with client.environments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(EnvironmentListResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_from_project(self, client: Gitpod) -> None:
        environment = client.environments.create_from_project()
        assert_matches_type(EnvironmentCreateFromProjectResponse, environment, path=["response"])

    @parametrize
    def test_method_create_from_project_with_all_params(self, client: Gitpod) -> None:
        environment = client.environments.create_from_project(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            spec={
                "admission": "ADMISSION_LEVEL_UNSPECIFIED",
                "automations_file": {
                    "automations_file_path": "automationsFilePath",
                    "session": "session",
                },
                "content": {
                    "git_email": "gitEmail",
                    "git_username": "gitUsername",
                    "initializer": {"specs": [{"context_url": {"url": "https://example.com"}}]},
                    "session": "session",
                },
                "desired_phase": "ENVIRONMENT_PHASE_UNSPECIFIED",
                "devcontainer": {
                    "devcontainer_file_path": "devcontainerFilePath",
                    "session": "session",
                },
                "machine": {
                    "class": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "session": "session",
                },
                "ports": [
                    {
                        "admission": "ADMISSION_LEVEL_UNSPECIFIED",
                        "name": "x",
                        "port": 1,
                    }
                ],
                "secrets": [
                    {
                        "environment_variable": "environmentVariable",
                        "name": "name",
                        "session": "session",
                        "source": "source",
                        "source_ref": "sourceRef",
                    }
                ],
                "spec_version": "specVersion",
                "ssh_public_keys": [
                    {
                        "id": "id",
                        "value": "value",
                    }
                ],
                "timeout": {"disconnected": "+9125115.360s"},
            },
        )
        assert_matches_type(EnvironmentCreateFromProjectResponse, environment, path=["response"])

    @parametrize
    def test_raw_response_create_from_project(self, client: Gitpod) -> None:
        response = client.environments.with_raw_response.create_from_project()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(EnvironmentCreateFromProjectResponse, environment, path=["response"])

    @parametrize
    def test_streaming_response_create_from_project(self, client: Gitpod) -> None:
        with client.environments.with_streaming_response.create_from_project() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(EnvironmentCreateFromProjectResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_start(self, client: Gitpod) -> None:
        environment = client.environments.start()
        assert_matches_type(object, environment, path=["response"])

    @parametrize
    def test_method_start_with_all_params(self, client: Gitpod) -> None:
        environment = client.environments.start(
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, environment, path=["response"])

    @parametrize
    def test_raw_response_start(self, client: Gitpod) -> None:
        response = client.environments.with_raw_response.start()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(object, environment, path=["response"])

    @parametrize
    def test_streaming_response_start(self, client: Gitpod) -> None:
        with client.environments.with_streaming_response.start() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(object, environment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEnvironments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.create()
        assert_matches_type(EnvironmentCreateResponse, environment, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.create(
            spec={
                "admission": "ADMISSION_LEVEL_UNSPECIFIED",
                "automations_file": {
                    "automations_file_path": "automationsFilePath",
                    "session": "session",
                },
                "content": {
                    "git_email": "gitEmail",
                    "git_username": "gitUsername",
                    "initializer": {"specs": [{"context_url": {"url": "https://example.com"}}]},
                    "session": "session",
                },
                "desired_phase": "ENVIRONMENT_PHASE_UNSPECIFIED",
                "devcontainer": {
                    "devcontainer_file_path": "devcontainerFilePath",
                    "session": "session",
                },
                "machine": {
                    "class": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "session": "session",
                },
                "ports": [
                    {
                        "admission": "ADMISSION_LEVEL_UNSPECIFIED",
                        "name": "x",
                        "port": 1,
                    }
                ],
                "secrets": [
                    {
                        "environment_variable": "environmentVariable",
                        "name": "name",
                        "session": "session",
                        "source": "source",
                        "source_ref": "sourceRef",
                    }
                ],
                "spec_version": "specVersion",
                "ssh_public_keys": [
                    {
                        "id": "id",
                        "value": "value",
                    }
                ],
                "timeout": {"disconnected": "+9125115.360s"},
            },
        )
        assert_matches_type(EnvironmentCreateResponse, environment, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(EnvironmentCreateResponse, environment, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(EnvironmentCreateResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.retrieve()
        assert_matches_type(EnvironmentRetrieveResponse, environment, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.retrieve(
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EnvironmentRetrieveResponse, environment, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(EnvironmentRetrieveResponse, environment, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(EnvironmentRetrieveResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.list()
        assert_matches_type(EnvironmentListResponse, environment, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.list(
            filter={
                "creator_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "project_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "runner_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "runner_kinds": ["RUNNER_KIND_UNSPECIFIED"],
                "status_phases": ["ENVIRONMENT_PHASE_UNSPECIFIED"],
            },
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            pagination={
                "token": "token",
                "page_size": 100,
            },
        )
        assert_matches_type(EnvironmentListResponse, environment, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(EnvironmentListResponse, environment, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(EnvironmentListResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_from_project(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.create_from_project()
        assert_matches_type(EnvironmentCreateFromProjectResponse, environment, path=["response"])

    @parametrize
    async def test_method_create_from_project_with_all_params(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.create_from_project(
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            spec={
                "admission": "ADMISSION_LEVEL_UNSPECIFIED",
                "automations_file": {
                    "automations_file_path": "automationsFilePath",
                    "session": "session",
                },
                "content": {
                    "git_email": "gitEmail",
                    "git_username": "gitUsername",
                    "initializer": {"specs": [{"context_url": {"url": "https://example.com"}}]},
                    "session": "session",
                },
                "desired_phase": "ENVIRONMENT_PHASE_UNSPECIFIED",
                "devcontainer": {
                    "devcontainer_file_path": "devcontainerFilePath",
                    "session": "session",
                },
                "machine": {
                    "class": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "session": "session",
                },
                "ports": [
                    {
                        "admission": "ADMISSION_LEVEL_UNSPECIFIED",
                        "name": "x",
                        "port": 1,
                    }
                ],
                "secrets": [
                    {
                        "environment_variable": "environmentVariable",
                        "name": "name",
                        "session": "session",
                        "source": "source",
                        "source_ref": "sourceRef",
                    }
                ],
                "spec_version": "specVersion",
                "ssh_public_keys": [
                    {
                        "id": "id",
                        "value": "value",
                    }
                ],
                "timeout": {"disconnected": "+9125115.360s"},
            },
        )
        assert_matches_type(EnvironmentCreateFromProjectResponse, environment, path=["response"])

    @parametrize
    async def test_raw_response_create_from_project(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.with_raw_response.create_from_project()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(EnvironmentCreateFromProjectResponse, environment, path=["response"])

    @parametrize
    async def test_streaming_response_create_from_project(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.with_streaming_response.create_from_project() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(EnvironmentCreateFromProjectResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_start(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.start()
        assert_matches_type(object, environment, path=["response"])

    @parametrize
    async def test_method_start_with_all_params(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.start(
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, environment, path=["response"])

    @parametrize
    async def test_raw_response_start(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.with_raw_response.start()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(object, environment, path=["response"])

    @parametrize
    async def test_streaming_response_start(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.with_streaming_response.start() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(object, environment, path=["response"])

        assert cast(Any, response.is_closed) is True
