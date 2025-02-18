# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.types import (
    Environment,
    EnvironmentCreateResponse,
    EnvironmentRetrieveResponse,
    EnvironmentCreateLogsTokenResponse,
    EnvironmentCreateFromProjectResponse,
)
from gitpod._utils import parse_datetime
from gitpod.pagination import SyncEnvironmentsPage, AsyncEnvironmentsPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEnvironments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Gitpod) -> None:
        environment = client.environments.create()
        assert_matches_type(EnvironmentCreateResponse, environment, path=["response"])

    @pytest.mark.skip()
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
                    "initializer": {
                        "specs": [
                            {
                                "context_url": {"url": "https://github.com/gitpod-io/gitpod"},
                                "git": {
                                    "checkout_location": "checkoutLocation",
                                    "clone_target": "cloneTarget",
                                    "remote_uri": "remoteUri",
                                    "target_mode": "CLONE_TARGET_MODE_UNSPECIFIED",
                                    "upstream_remote_uri": "upstreamRemoteUri",
                                },
                            }
                        ]
                    },
                    "session": "session",
                },
                "desired_phase": "ENVIRONMENT_PHASE_UNSPECIFIED",
                "devcontainer": {
                    "devcontainer_file_path": "devcontainerFilePath",
                    "dotfiles": {
                        "repository": "https://example.com",
                        "install_command": "installCommand",
                        "target_path": "targetPath",
                    },
                    "session": "session",
                },
                "machine": {
                    "class": "d2c94c27-3b76-4a42-b88c-95a85e392c68",
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
                        "container_registry_basic_auth_host": "containerRegistryBasicAuthHost",
                        "environment_variable": "environmentVariable",
                        "file_path": "filePath",
                        "git_credential_host": "gitCredentialHost",
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

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Gitpod) -> None:
        response = client.environments.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(EnvironmentCreateResponse, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Gitpod) -> None:
        with client.environments.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(EnvironmentCreateResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Gitpod) -> None:
        environment = client.environments.retrieve(
            environment_id="07e03a28-65a5-4d98-b532-8ea67b188048",
        )
        assert_matches_type(EnvironmentRetrieveResponse, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Gitpod) -> None:
        response = client.environments.with_raw_response.retrieve(
            environment_id="07e03a28-65a5-4d98-b532-8ea67b188048",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(EnvironmentRetrieveResponse, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Gitpod) -> None:
        with client.environments.with_streaming_response.retrieve(
            environment_id="07e03a28-65a5-4d98-b532-8ea67b188048",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(EnvironmentRetrieveResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Gitpod) -> None:
        environment = client.environments.update()
        assert_matches_type(object, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Gitpod) -> None:
        environment = client.environments.update(
            environment_id="07e03a28-65a5-4d98-b532-8ea67b188048",
            metadata={},
            spec={
                "automations_file": {
                    "automations_file_path": "automationsFilePath",
                    "session": "session",
                },
                "content": {
                    "git_email": "gitEmail",
                    "git_username": "gitUsername",
                    "initializer": {
                        "specs": [
                            {
                                "context_url": {"url": "https://example.com"},
                                "git": {
                                    "checkout_location": "checkoutLocation",
                                    "clone_target": "cloneTarget",
                                    "remote_uri": "remoteUri",
                                    "target_mode": "CLONE_TARGET_MODE_UNSPECIFIED",
                                    "upstream_remote_uri": "upstreamRemoteUri",
                                },
                            }
                        ]
                    },
                    "session": "session",
                },
                "devcontainer": {
                    "devcontainer_file_path": "devcontainerFilePath",
                    "session": "session",
                },
                "ports": [
                    {
                        "admission": "ADMISSION_LEVEL_UNSPECIFIED",
                        "name": "x",
                        "port": 1,
                    }
                ],
                "ssh_public_keys": [
                    {
                        "id": "0194b7c1-c954-718d-91a4-9a742aa5fc11",
                        "value": "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAI...",
                    }
                ],
                "timeout": {"disconnected": "+9125115.360s"},
            },
        )
        assert_matches_type(object, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Gitpod) -> None:
        response = client.environments.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(object, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Gitpod) -> None:
        with client.environments.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(object, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Gitpod) -> None:
        environment = client.environments.list()
        assert_matches_type(SyncEnvironmentsPage[Environment], environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Gitpod) -> None:
        environment = client.environments.list(
            token="token",
            page_size=0,
            filter={
                "creator_ids": ["f53d2330-3795-4c5d-a1f3-453121af9c60"],
                "project_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "runner_ids": ["e6aa9c54-89d3-42c1-ac31-bd8d8f1concentrate"],
                "runner_kinds": ["RUNNER_KIND_UNSPECIFIED"],
                "status_phases": ["ENVIRONMENT_PHASE_UNSPECIFIED"],
            },
            pagination={
                "token": "token",
                "page_size": 100,
            },
        )
        assert_matches_type(SyncEnvironmentsPage[Environment], environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Gitpod) -> None:
        response = client.environments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(SyncEnvironmentsPage[Environment], environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Gitpod) -> None:
        with client.environments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(SyncEnvironmentsPage[Environment], environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Gitpod) -> None:
        environment = client.environments.delete()
        assert_matches_type(object, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_with_all_params(self, client: Gitpod) -> None:
        environment = client.environments.delete(
            environment_id="07e03a28-65a5-4d98-b532-8ea67b188048",
            force=False,
        )
        assert_matches_type(object, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Gitpod) -> None:
        response = client.environments.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(object, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Gitpod) -> None:
        with client.environments.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(object, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_create_from_project(self, client: Gitpod) -> None:
        environment = client.environments.create_from_project()
        assert_matches_type(EnvironmentCreateFromProjectResponse, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_from_project_with_all_params(self, client: Gitpod) -> None:
        environment = client.environments.create_from_project(
            project_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            spec={
                "admission": "ADMISSION_LEVEL_UNSPECIFIED",
                "automations_file": {
                    "automations_file_path": "automationsFilePath",
                    "session": "session",
                },
                "content": {
                    "git_email": "gitEmail",
                    "git_username": "gitUsername",
                    "initializer": {
                        "specs": [
                            {
                                "context_url": {"url": "https://example.com"},
                                "git": {
                                    "checkout_location": "checkoutLocation",
                                    "clone_target": "cloneTarget",
                                    "remote_uri": "remoteUri",
                                    "target_mode": "CLONE_TARGET_MODE_UNSPECIFIED",
                                    "upstream_remote_uri": "upstreamRemoteUri",
                                },
                            }
                        ]
                    },
                    "session": "session",
                },
                "desired_phase": "ENVIRONMENT_PHASE_UNSPECIFIED",
                "devcontainer": {
                    "devcontainer_file_path": "devcontainerFilePath",
                    "dotfiles": {
                        "repository": "https://example.com",
                        "install_command": "installCommand",
                        "target_path": "targetPath",
                    },
                    "session": "session",
                },
                "machine": {
                    "class": "d2c94c27-3b76-4a42-b88c-95a85e392c68",
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
                        "container_registry_basic_auth_host": "containerRegistryBasicAuthHost",
                        "environment_variable": "environmentVariable",
                        "file_path": "filePath",
                        "git_credential_host": "gitCredentialHost",
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
                "timeout": {"disconnected": "14400s"},
            },
        )
        assert_matches_type(EnvironmentCreateFromProjectResponse, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_from_project(self, client: Gitpod) -> None:
        response = client.environments.with_raw_response.create_from_project()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(EnvironmentCreateFromProjectResponse, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_from_project(self, client: Gitpod) -> None:
        with client.environments.with_streaming_response.create_from_project() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(EnvironmentCreateFromProjectResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_create_logs_token(self, client: Gitpod) -> None:
        environment = client.environments.create_logs_token()
        assert_matches_type(EnvironmentCreateLogsTokenResponse, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_logs_token_with_all_params(self, client: Gitpod) -> None:
        environment = client.environments.create_logs_token(
            environment_id="07e03a28-65a5-4d98-b532-8ea67b188048",
        )
        assert_matches_type(EnvironmentCreateLogsTokenResponse, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_logs_token(self, client: Gitpod) -> None:
        response = client.environments.with_raw_response.create_logs_token()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(EnvironmentCreateLogsTokenResponse, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_logs_token(self, client: Gitpod) -> None:
        with client.environments.with_streaming_response.create_logs_token() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(EnvironmentCreateLogsTokenResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_mark_active(self, client: Gitpod) -> None:
        environment = client.environments.mark_active()
        assert_matches_type(object, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_mark_active_with_all_params(self, client: Gitpod) -> None:
        environment = client.environments.mark_active(
            activity_signal={
                "source": "VS Code",
                "timestamp": parse_datetime("2025-02-12T14:30:00Z"),
            },
            environment_id="07e03a28-65a5-4d98-b532-8ea67b188048",
        )
        assert_matches_type(object, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_mark_active(self, client: Gitpod) -> None:
        response = client.environments.with_raw_response.mark_active()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(object, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_mark_active(self, client: Gitpod) -> None:
        with client.environments.with_streaming_response.mark_active() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(object, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_start(self, client: Gitpod) -> None:
        environment = client.environments.start()
        assert_matches_type(object, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_start_with_all_params(self, client: Gitpod) -> None:
        environment = client.environments.start(
            environment_id="07e03a28-65a5-4d98-b532-8ea67b188048",
        )
        assert_matches_type(object, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_start(self, client: Gitpod) -> None:
        response = client.environments.with_raw_response.start()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(object, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_start(self, client: Gitpod) -> None:
        with client.environments.with_streaming_response.start() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(object, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_stop(self, client: Gitpod) -> None:
        environment = client.environments.stop()
        assert_matches_type(object, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_stop_with_all_params(self, client: Gitpod) -> None:
        environment = client.environments.stop(
            environment_id="07e03a28-65a5-4d98-b532-8ea67b188048",
        )
        assert_matches_type(object, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_stop(self, client: Gitpod) -> None:
        response = client.environments.with_raw_response.stop()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(object, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_stop(self, client: Gitpod) -> None:
        with client.environments.with_streaming_response.stop() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(object, environment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEnvironments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.create()
        assert_matches_type(EnvironmentCreateResponse, environment, path=["response"])

    @pytest.mark.skip()
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
                    "initializer": {
                        "specs": [
                            {
                                "context_url": {"url": "https://github.com/gitpod-io/gitpod"},
                                "git": {
                                    "checkout_location": "checkoutLocation",
                                    "clone_target": "cloneTarget",
                                    "remote_uri": "remoteUri",
                                    "target_mode": "CLONE_TARGET_MODE_UNSPECIFIED",
                                    "upstream_remote_uri": "upstreamRemoteUri",
                                },
                            }
                        ]
                    },
                    "session": "session",
                },
                "desired_phase": "ENVIRONMENT_PHASE_UNSPECIFIED",
                "devcontainer": {
                    "devcontainer_file_path": "devcontainerFilePath",
                    "dotfiles": {
                        "repository": "https://example.com",
                        "install_command": "installCommand",
                        "target_path": "targetPath",
                    },
                    "session": "session",
                },
                "machine": {
                    "class": "d2c94c27-3b76-4a42-b88c-95a85e392c68",
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
                        "container_registry_basic_auth_host": "containerRegistryBasicAuthHost",
                        "environment_variable": "environmentVariable",
                        "file_path": "filePath",
                        "git_credential_host": "gitCredentialHost",
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

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(EnvironmentCreateResponse, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(EnvironmentCreateResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.retrieve(
            environment_id="07e03a28-65a5-4d98-b532-8ea67b188048",
        )
        assert_matches_type(EnvironmentRetrieveResponse, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.with_raw_response.retrieve(
            environment_id="07e03a28-65a5-4d98-b532-8ea67b188048",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(EnvironmentRetrieveResponse, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.with_streaming_response.retrieve(
            environment_id="07e03a28-65a5-4d98-b532-8ea67b188048",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(EnvironmentRetrieveResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.update()
        assert_matches_type(object, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.update(
            environment_id="07e03a28-65a5-4d98-b532-8ea67b188048",
            metadata={},
            spec={
                "automations_file": {
                    "automations_file_path": "automationsFilePath",
                    "session": "session",
                },
                "content": {
                    "git_email": "gitEmail",
                    "git_username": "gitUsername",
                    "initializer": {
                        "specs": [
                            {
                                "context_url": {"url": "https://example.com"},
                                "git": {
                                    "checkout_location": "checkoutLocation",
                                    "clone_target": "cloneTarget",
                                    "remote_uri": "remoteUri",
                                    "target_mode": "CLONE_TARGET_MODE_UNSPECIFIED",
                                    "upstream_remote_uri": "upstreamRemoteUri",
                                },
                            }
                        ]
                    },
                    "session": "session",
                },
                "devcontainer": {
                    "devcontainer_file_path": "devcontainerFilePath",
                    "session": "session",
                },
                "ports": [
                    {
                        "admission": "ADMISSION_LEVEL_UNSPECIFIED",
                        "name": "x",
                        "port": 1,
                    }
                ],
                "ssh_public_keys": [
                    {
                        "id": "0194b7c1-c954-718d-91a4-9a742aa5fc11",
                        "value": "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAI...",
                    }
                ],
                "timeout": {"disconnected": "+9125115.360s"},
            },
        )
        assert_matches_type(object, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(object, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(object, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.list()
        assert_matches_type(AsyncEnvironmentsPage[Environment], environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.list(
            token="token",
            page_size=0,
            filter={
                "creator_ids": ["f53d2330-3795-4c5d-a1f3-453121af9c60"],
                "project_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "runner_ids": ["e6aa9c54-89d3-42c1-ac31-bd8d8f1concentrate"],
                "runner_kinds": ["RUNNER_KIND_UNSPECIFIED"],
                "status_phases": ["ENVIRONMENT_PHASE_UNSPECIFIED"],
            },
            pagination={
                "token": "token",
                "page_size": 100,
            },
        )
        assert_matches_type(AsyncEnvironmentsPage[Environment], environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(AsyncEnvironmentsPage[Environment], environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(AsyncEnvironmentsPage[Environment], environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.delete()
        assert_matches_type(object, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.delete(
            environment_id="07e03a28-65a5-4d98-b532-8ea67b188048",
            force=False,
        )
        assert_matches_type(object, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(object, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(object, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_from_project(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.create_from_project()
        assert_matches_type(EnvironmentCreateFromProjectResponse, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_from_project_with_all_params(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.create_from_project(
            project_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            spec={
                "admission": "ADMISSION_LEVEL_UNSPECIFIED",
                "automations_file": {
                    "automations_file_path": "automationsFilePath",
                    "session": "session",
                },
                "content": {
                    "git_email": "gitEmail",
                    "git_username": "gitUsername",
                    "initializer": {
                        "specs": [
                            {
                                "context_url": {"url": "https://example.com"},
                                "git": {
                                    "checkout_location": "checkoutLocation",
                                    "clone_target": "cloneTarget",
                                    "remote_uri": "remoteUri",
                                    "target_mode": "CLONE_TARGET_MODE_UNSPECIFIED",
                                    "upstream_remote_uri": "upstreamRemoteUri",
                                },
                            }
                        ]
                    },
                    "session": "session",
                },
                "desired_phase": "ENVIRONMENT_PHASE_UNSPECIFIED",
                "devcontainer": {
                    "devcontainer_file_path": "devcontainerFilePath",
                    "dotfiles": {
                        "repository": "https://example.com",
                        "install_command": "installCommand",
                        "target_path": "targetPath",
                    },
                    "session": "session",
                },
                "machine": {
                    "class": "d2c94c27-3b76-4a42-b88c-95a85e392c68",
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
                        "container_registry_basic_auth_host": "containerRegistryBasicAuthHost",
                        "environment_variable": "environmentVariable",
                        "file_path": "filePath",
                        "git_credential_host": "gitCredentialHost",
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
                "timeout": {"disconnected": "14400s"},
            },
        )
        assert_matches_type(EnvironmentCreateFromProjectResponse, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_from_project(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.with_raw_response.create_from_project()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(EnvironmentCreateFromProjectResponse, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_from_project(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.with_streaming_response.create_from_project() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(EnvironmentCreateFromProjectResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_logs_token(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.create_logs_token()
        assert_matches_type(EnvironmentCreateLogsTokenResponse, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_logs_token_with_all_params(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.create_logs_token(
            environment_id="07e03a28-65a5-4d98-b532-8ea67b188048",
        )
        assert_matches_type(EnvironmentCreateLogsTokenResponse, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_logs_token(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.with_raw_response.create_logs_token()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(EnvironmentCreateLogsTokenResponse, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_logs_token(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.with_streaming_response.create_logs_token() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(EnvironmentCreateLogsTokenResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_mark_active(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.mark_active()
        assert_matches_type(object, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_mark_active_with_all_params(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.mark_active(
            activity_signal={
                "source": "VS Code",
                "timestamp": parse_datetime("2025-02-12T14:30:00Z"),
            },
            environment_id="07e03a28-65a5-4d98-b532-8ea67b188048",
        )
        assert_matches_type(object, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_mark_active(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.with_raw_response.mark_active()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(object, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_mark_active(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.with_streaming_response.mark_active() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(object, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_start(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.start()
        assert_matches_type(object, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_start_with_all_params(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.start(
            environment_id="07e03a28-65a5-4d98-b532-8ea67b188048",
        )
        assert_matches_type(object, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_start(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.with_raw_response.start()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(object, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_start(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.with_streaming_response.start() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(object, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_stop(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.stop()
        assert_matches_type(object, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_stop_with_all_params(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.stop(
            environment_id="07e03a28-65a5-4d98-b532-8ea67b188048",
        )
        assert_matches_type(object, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_stop(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.with_raw_response.stop()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(object, environment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_stop(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.with_streaming_response.stop() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(object, environment, path=["response"])

        assert cast(Any, response.is_closed) is True
