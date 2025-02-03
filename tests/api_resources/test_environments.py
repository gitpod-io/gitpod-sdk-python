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
    EnvironmentCreateLogsTokenResponse,
    EnvironmentCreateFromProjectResponse,
)
from gitpod._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEnvironments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gitpod) -> None:
        environment = client.environments.create(
            connect_protocol_version=1,
        )
        assert_matches_type(EnvironmentCreateResponse, environment, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gitpod) -> None:
        environment = client.environments.create(
            connect_protocol_version=1,
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
            connect_timeout_ms=0,
        )
        assert_matches_type(EnvironmentCreateResponse, environment, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gitpod) -> None:
        response = client.environments.with_raw_response.create(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(EnvironmentCreateResponse, environment, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gitpod) -> None:
        with client.environments.with_streaming_response.create(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(EnvironmentCreateResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Gitpod) -> None:
        environment = client.environments.retrieve(
            encoding="proto",
            connect_protocol_version=1,
        )
        assert_matches_type(EnvironmentRetrieveResponse, environment, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Gitpod) -> None:
        environment = client.environments.retrieve(
            encoding="proto",
            connect_protocol_version=1,
            base64=True,
            compression="identity",
            connect="v1",
            message="message",
            connect_timeout_ms=0,
        )
        assert_matches_type(EnvironmentRetrieveResponse, environment, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Gitpod) -> None:
        response = client.environments.with_raw_response.retrieve(
            encoding="proto",
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(EnvironmentRetrieveResponse, environment, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Gitpod) -> None:
        with client.environments.with_streaming_response.retrieve(
            encoding="proto",
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(EnvironmentRetrieveResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gitpod) -> None:
        environment = client.environments.update(
            body={},
            connect_protocol_version=1,
        )
        assert_matches_type(object, environment, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gitpod) -> None:
        environment = client.environments.update(
            body={
                "environmentId": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "metadata": {},
                "spec": {},
            },
            connect_protocol_version=1,
            connect_timeout_ms=0,
        )
        assert_matches_type(object, environment, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gitpod) -> None:
        response = client.environments.with_raw_response.update(
            body={},
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(object, environment, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gitpod) -> None:
        with client.environments.with_streaming_response.update(
            body={},
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(object, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gitpod) -> None:
        environment = client.environments.list(
            encoding="proto",
            connect_protocol_version=1,
        )
        assert_matches_type(EnvironmentListResponse, environment, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gitpod) -> None:
        environment = client.environments.list(
            encoding="proto",
            connect_protocol_version=1,
            base64=True,
            compression="identity",
            connect="v1",
            message="message",
            connect_timeout_ms=0,
        )
        assert_matches_type(EnvironmentListResponse, environment, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gitpod) -> None:
        response = client.environments.with_raw_response.list(
            encoding="proto",
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(EnvironmentListResponse, environment, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gitpod) -> None:
        with client.environments.with_streaming_response.list(
            encoding="proto",
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(EnvironmentListResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gitpod) -> None:
        environment = client.environments.delete(
            connect_protocol_version=1,
        )
        assert_matches_type(object, environment, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Gitpod) -> None:
        environment = client.environments.delete(
            connect_protocol_version=1,
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            force=True,
            connect_timeout_ms=0,
        )
        assert_matches_type(object, environment, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gitpod) -> None:
        response = client.environments.with_raw_response.delete(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(object, environment, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gitpod) -> None:
        with client.environments.with_streaming_response.delete(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(object, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_from_project(self, client: Gitpod) -> None:
        environment = client.environments.create_from_project(
            connect_protocol_version=1,
        )
        assert_matches_type(EnvironmentCreateFromProjectResponse, environment, path=["response"])

    @parametrize
    def test_method_create_from_project_with_all_params(self, client: Gitpod) -> None:
        environment = client.environments.create_from_project(
            connect_protocol_version=1,
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
            connect_timeout_ms=0,
        )
        assert_matches_type(EnvironmentCreateFromProjectResponse, environment, path=["response"])

    @parametrize
    def test_raw_response_create_from_project(self, client: Gitpod) -> None:
        response = client.environments.with_raw_response.create_from_project(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(EnvironmentCreateFromProjectResponse, environment, path=["response"])

    @parametrize
    def test_streaming_response_create_from_project(self, client: Gitpod) -> None:
        with client.environments.with_streaming_response.create_from_project(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(EnvironmentCreateFromProjectResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_logs_token(self, client: Gitpod) -> None:
        environment = client.environments.create_logs_token(
            connect_protocol_version=1,
        )
        assert_matches_type(EnvironmentCreateLogsTokenResponse, environment, path=["response"])

    @parametrize
    def test_method_create_logs_token_with_all_params(self, client: Gitpod) -> None:
        environment = client.environments.create_logs_token(
            connect_protocol_version=1,
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(EnvironmentCreateLogsTokenResponse, environment, path=["response"])

    @parametrize
    def test_raw_response_create_logs_token(self, client: Gitpod) -> None:
        response = client.environments.with_raw_response.create_logs_token(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(EnvironmentCreateLogsTokenResponse, environment, path=["response"])

    @parametrize
    def test_streaming_response_create_logs_token(self, client: Gitpod) -> None:
        with client.environments.with_streaming_response.create_logs_token(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(EnvironmentCreateLogsTokenResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_mark_active(self, client: Gitpod) -> None:
        environment = client.environments.mark_active(
            connect_protocol_version=1,
        )
        assert_matches_type(object, environment, path=["response"])

    @parametrize
    def test_method_mark_active_with_all_params(self, client: Gitpod) -> None:
        environment = client.environments.mark_active(
            connect_protocol_version=1,
            activity_signal={
                "source": "xxx",
                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(object, environment, path=["response"])

    @parametrize
    def test_raw_response_mark_active(self, client: Gitpod) -> None:
        response = client.environments.with_raw_response.mark_active(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(object, environment, path=["response"])

    @parametrize
    def test_streaming_response_mark_active(self, client: Gitpod) -> None:
        with client.environments.with_streaming_response.mark_active(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(object, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_start(self, client: Gitpod) -> None:
        environment = client.environments.start(
            connect_protocol_version=1,
        )
        assert_matches_type(object, environment, path=["response"])

    @parametrize
    def test_method_start_with_all_params(self, client: Gitpod) -> None:
        environment = client.environments.start(
            connect_protocol_version=1,
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(object, environment, path=["response"])

    @parametrize
    def test_raw_response_start(self, client: Gitpod) -> None:
        response = client.environments.with_raw_response.start(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(object, environment, path=["response"])

    @parametrize
    def test_streaming_response_start(self, client: Gitpod) -> None:
        with client.environments.with_streaming_response.start(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(object, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_stop(self, client: Gitpod) -> None:
        environment = client.environments.stop(
            connect_protocol_version=1,
        )
        assert_matches_type(object, environment, path=["response"])

    @parametrize
    def test_method_stop_with_all_params(self, client: Gitpod) -> None:
        environment = client.environments.stop(
            connect_protocol_version=1,
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(object, environment, path=["response"])

    @parametrize
    def test_raw_response_stop(self, client: Gitpod) -> None:
        response = client.environments.with_raw_response.stop(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(object, environment, path=["response"])

    @parametrize
    def test_streaming_response_stop(self, client: Gitpod) -> None:
        with client.environments.with_streaming_response.stop(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(object, environment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEnvironments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.create(
            connect_protocol_version=1,
        )
        assert_matches_type(EnvironmentCreateResponse, environment, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.create(
            connect_protocol_version=1,
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
            connect_timeout_ms=0,
        )
        assert_matches_type(EnvironmentCreateResponse, environment, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.with_raw_response.create(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(EnvironmentCreateResponse, environment, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.with_streaming_response.create(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(EnvironmentCreateResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.retrieve(
            encoding="proto",
            connect_protocol_version=1,
        )
        assert_matches_type(EnvironmentRetrieveResponse, environment, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.retrieve(
            encoding="proto",
            connect_protocol_version=1,
            base64=True,
            compression="identity",
            connect="v1",
            message="message",
            connect_timeout_ms=0,
        )
        assert_matches_type(EnvironmentRetrieveResponse, environment, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.with_raw_response.retrieve(
            encoding="proto",
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(EnvironmentRetrieveResponse, environment, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.with_streaming_response.retrieve(
            encoding="proto",
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(EnvironmentRetrieveResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.update(
            body={},
            connect_protocol_version=1,
        )
        assert_matches_type(object, environment, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.update(
            body={
                "environmentId": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "metadata": {},
                "spec": {},
            },
            connect_protocol_version=1,
            connect_timeout_ms=0,
        )
        assert_matches_type(object, environment, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.with_raw_response.update(
            body={},
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(object, environment, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.with_streaming_response.update(
            body={},
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(object, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.list(
            encoding="proto",
            connect_protocol_version=1,
        )
        assert_matches_type(EnvironmentListResponse, environment, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.list(
            encoding="proto",
            connect_protocol_version=1,
            base64=True,
            compression="identity",
            connect="v1",
            message="message",
            connect_timeout_ms=0,
        )
        assert_matches_type(EnvironmentListResponse, environment, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.with_raw_response.list(
            encoding="proto",
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(EnvironmentListResponse, environment, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.with_streaming_response.list(
            encoding="proto",
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(EnvironmentListResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.delete(
            connect_protocol_version=1,
        )
        assert_matches_type(object, environment, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.delete(
            connect_protocol_version=1,
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            force=True,
            connect_timeout_ms=0,
        )
        assert_matches_type(object, environment, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.with_raw_response.delete(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(object, environment, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.with_streaming_response.delete(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(object, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_from_project(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.create_from_project(
            connect_protocol_version=1,
        )
        assert_matches_type(EnvironmentCreateFromProjectResponse, environment, path=["response"])

    @parametrize
    async def test_method_create_from_project_with_all_params(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.create_from_project(
            connect_protocol_version=1,
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
            connect_timeout_ms=0,
        )
        assert_matches_type(EnvironmentCreateFromProjectResponse, environment, path=["response"])

    @parametrize
    async def test_raw_response_create_from_project(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.with_raw_response.create_from_project(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(EnvironmentCreateFromProjectResponse, environment, path=["response"])

    @parametrize
    async def test_streaming_response_create_from_project(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.with_streaming_response.create_from_project(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(EnvironmentCreateFromProjectResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_logs_token(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.create_logs_token(
            connect_protocol_version=1,
        )
        assert_matches_type(EnvironmentCreateLogsTokenResponse, environment, path=["response"])

    @parametrize
    async def test_method_create_logs_token_with_all_params(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.create_logs_token(
            connect_protocol_version=1,
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(EnvironmentCreateLogsTokenResponse, environment, path=["response"])

    @parametrize
    async def test_raw_response_create_logs_token(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.with_raw_response.create_logs_token(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(EnvironmentCreateLogsTokenResponse, environment, path=["response"])

    @parametrize
    async def test_streaming_response_create_logs_token(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.with_streaming_response.create_logs_token(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(EnvironmentCreateLogsTokenResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_mark_active(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.mark_active(
            connect_protocol_version=1,
        )
        assert_matches_type(object, environment, path=["response"])

    @parametrize
    async def test_method_mark_active_with_all_params(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.mark_active(
            connect_protocol_version=1,
            activity_signal={
                "source": "xxx",
                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(object, environment, path=["response"])

    @parametrize
    async def test_raw_response_mark_active(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.with_raw_response.mark_active(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(object, environment, path=["response"])

    @parametrize
    async def test_streaming_response_mark_active(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.with_streaming_response.mark_active(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(object, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_start(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.start(
            connect_protocol_version=1,
        )
        assert_matches_type(object, environment, path=["response"])

    @parametrize
    async def test_method_start_with_all_params(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.start(
            connect_protocol_version=1,
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(object, environment, path=["response"])

    @parametrize
    async def test_raw_response_start(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.with_raw_response.start(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(object, environment, path=["response"])

    @parametrize
    async def test_streaming_response_start(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.with_streaming_response.start(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(object, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_stop(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.stop(
            connect_protocol_version=1,
        )
        assert_matches_type(object, environment, path=["response"])

    @parametrize
    async def test_method_stop_with_all_params(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.environments.stop(
            connect_protocol_version=1,
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(object, environment, path=["response"])

    @parametrize
    async def test_raw_response_stop(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.with_raw_response.stop(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(object, environment, path=["response"])

    @parametrize
    async def test_streaming_response_stop(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.with_streaming_response.stop(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(object, environment, path=["response"])

        assert cast(Any, response.is_closed) is True
