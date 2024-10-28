# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.types.runner_interactions import (
    EnvironmentRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEnvironment:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Gitpod) -> None:
        environment = client.runner_interactions.environment.retrieve(
            connect_protocol_version=1,
        )
        assert_matches_type(EnvironmentRetrieveResponse, environment, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Gitpod) -> None:
        environment = client.runner_interactions.environment.retrieve(
            connect_protocol_version=1,
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(EnvironmentRetrieveResponse, environment, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Gitpod) -> None:
        response = client.runner_interactions.environment.with_raw_response.retrieve(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(EnvironmentRetrieveResponse, environment, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Gitpod) -> None:
        with client.runner_interactions.environment.with_streaming_response.retrieve(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(EnvironmentRetrieveResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_status(self, client: Gitpod) -> None:
        environment = client.runner_interactions.environment.update_status(
            connect_protocol_version=1,
        )
        assert_matches_type(object, environment, path=["response"])

    @parametrize
    def test_method_update_status_with_all_params(self, client: Gitpod) -> None:
        environment = client.runner_interactions.environment.update_status(
            connect_protocol_version=1,
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status={
                "automations_file": {
                    "automations_file_path": "automationsFilePath",
                    "automations_file_presence": "PRESENCE_UNSPECIFIED",
                    "failure_message": "failureMessage",
                    "phase": "CONTENT_PHASE_UNSPECIFIED",
                    "session": "session",
                },
                "content": {
                    "content_location_in_machine": "contentLocationInMachine",
                    "failure_message": "failureMessage",
                    "git": {
                        "branch": "branch",
                        "changed_files": [
                            {
                                "change_type": "CHANGE_TYPE_UNSPECIFIED",
                                "path": "path",
                            },
                            {
                                "change_type": "CHANGE_TYPE_UNSPECIFIED",
                                "path": "path",
                            },
                            {
                                "change_type": "CHANGE_TYPE_UNSPECIFIED",
                                "path": "path",
                            },
                        ],
                        "clone_url": "cloneUrl",
                        "latest_commit": "latestCommit",
                        "total_changed_files": 0,
                        "total_unpushed_commits": 0,
                        "unpushed_commits": ["string", "string", "string"],
                    },
                    "phase": "CONTENT_PHASE_UNSPECIFIED",
                    "session": "session",
                    "warning_message": "warningMessage",
                },
                "devcontainer": {
                    "container_id": "containerId",
                    "container_name": "containerName",
                    "devcontainerconfig_in_sync": True,
                    "devcontainer_file_path": "devcontainerFilePath",
                    "devcontainer_file_presence": "PRESENCE_UNSPECIFIED",
                    "failure_message": "failureMessage",
                    "phase": "PHASE_UNSPECIFIED",
                    "remote_user": "remoteUser",
                    "remote_workspace_folder": "remoteWorkspaceFolder",
                    "secrets_in_sync": True,
                    "session": "session",
                    "warning_message": "warningMessage",
                },
                "environment_urls": {
                    "logs": "logs",
                    "ports": [
                        {
                            "port": 1,
                            "url": "url",
                        },
                        {
                            "port": 1,
                            "url": "url",
                        },
                        {
                            "port": 1,
                            "url": "url",
                        },
                    ],
                    "ssh": {"url": "url"},
                },
                "failure_message": ["string", "string", "string"],
                "machine": {
                    "failure_message": "failureMessage",
                    "phase": "PHASE_UNSPECIFIED",
                    "session": "session",
                    "timeout": "timeout",
                    "versions": {
                        "supervisor_commit": "supervisorCommit",
                        "supervisor_version": "supervisorVersion",
                    },
                    "warning_message": "warningMessage",
                },
                "phase": "ENVIRONMENT_PHASE_UNSPECIFIED",
                "runner_ack": {
                    "message": "message",
                    "spec_version": "string",
                    "status_code": "STATUS_CODE_UNSPECIFIED",
                },
                "secrets": [
                    {
                        "failure_message": "failureMessage",
                        "phase": "CONTENT_PHASE_UNSPECIFIED",
                        "secret_name": "secretName",
                        "warning_message": "warningMessage",
                    },
                    {
                        "failure_message": "failureMessage",
                        "phase": "CONTENT_PHASE_UNSPECIFIED",
                        "secret_name": "secretName",
                        "warning_message": "warningMessage",
                    },
                    {
                        "failure_message": "failureMessage",
                        "phase": "CONTENT_PHASE_UNSPECIFIED",
                        "secret_name": "secretName",
                        "warning_message": "warningMessage",
                    },
                ],
                "ssh_public_keys": [
                    {
                        "id": "id",
                        "phase": "CONTENT_PHASE_UNSPECIFIED",
                    },
                    {
                        "id": "id",
                        "phase": "CONTENT_PHASE_UNSPECIFIED",
                    },
                    {
                        "id": "id",
                        "phase": "CONTENT_PHASE_UNSPECIFIED",
                    },
                ],
                "status_version": "string",
                "warning_message": ["string", "string", "string"],
            },
            connect_timeout_ms=0,
        )
        assert_matches_type(object, environment, path=["response"])

    @parametrize
    def test_raw_response_update_status(self, client: Gitpod) -> None:
        response = client.runner_interactions.environment.with_raw_response.update_status(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = response.parse()
        assert_matches_type(object, environment, path=["response"])

    @parametrize
    def test_streaming_response_update_status(self, client: Gitpod) -> None:
        with client.runner_interactions.environment.with_streaming_response.update_status(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = response.parse()
            assert_matches_type(object, environment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEnvironment:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.runner_interactions.environment.retrieve(
            connect_protocol_version=1,
        )
        assert_matches_type(EnvironmentRetrieveResponse, environment, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.runner_interactions.environment.retrieve(
            connect_protocol_version=1,
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(EnvironmentRetrieveResponse, environment, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runner_interactions.environment.with_raw_response.retrieve(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(EnvironmentRetrieveResponse, environment, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGitpod) -> None:
        async with async_client.runner_interactions.environment.with_streaming_response.retrieve(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(EnvironmentRetrieveResponse, environment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_status(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.runner_interactions.environment.update_status(
            connect_protocol_version=1,
        )
        assert_matches_type(object, environment, path=["response"])

    @parametrize
    async def test_method_update_status_with_all_params(self, async_client: AsyncGitpod) -> None:
        environment = await async_client.runner_interactions.environment.update_status(
            connect_protocol_version=1,
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status={
                "automations_file": {
                    "automations_file_path": "automationsFilePath",
                    "automations_file_presence": "PRESENCE_UNSPECIFIED",
                    "failure_message": "failureMessage",
                    "phase": "CONTENT_PHASE_UNSPECIFIED",
                    "session": "session",
                },
                "content": {
                    "content_location_in_machine": "contentLocationInMachine",
                    "failure_message": "failureMessage",
                    "git": {
                        "branch": "branch",
                        "changed_files": [
                            {
                                "change_type": "CHANGE_TYPE_UNSPECIFIED",
                                "path": "path",
                            },
                            {
                                "change_type": "CHANGE_TYPE_UNSPECIFIED",
                                "path": "path",
                            },
                            {
                                "change_type": "CHANGE_TYPE_UNSPECIFIED",
                                "path": "path",
                            },
                        ],
                        "clone_url": "cloneUrl",
                        "latest_commit": "latestCommit",
                        "total_changed_files": 0,
                        "total_unpushed_commits": 0,
                        "unpushed_commits": ["string", "string", "string"],
                    },
                    "phase": "CONTENT_PHASE_UNSPECIFIED",
                    "session": "session",
                    "warning_message": "warningMessage",
                },
                "devcontainer": {
                    "container_id": "containerId",
                    "container_name": "containerName",
                    "devcontainerconfig_in_sync": True,
                    "devcontainer_file_path": "devcontainerFilePath",
                    "devcontainer_file_presence": "PRESENCE_UNSPECIFIED",
                    "failure_message": "failureMessage",
                    "phase": "PHASE_UNSPECIFIED",
                    "remote_user": "remoteUser",
                    "remote_workspace_folder": "remoteWorkspaceFolder",
                    "secrets_in_sync": True,
                    "session": "session",
                    "warning_message": "warningMessage",
                },
                "environment_urls": {
                    "logs": "logs",
                    "ports": [
                        {
                            "port": 1,
                            "url": "url",
                        },
                        {
                            "port": 1,
                            "url": "url",
                        },
                        {
                            "port": 1,
                            "url": "url",
                        },
                    ],
                    "ssh": {"url": "url"},
                },
                "failure_message": ["string", "string", "string"],
                "machine": {
                    "failure_message": "failureMessage",
                    "phase": "PHASE_UNSPECIFIED",
                    "session": "session",
                    "timeout": "timeout",
                    "versions": {
                        "supervisor_commit": "supervisorCommit",
                        "supervisor_version": "supervisorVersion",
                    },
                    "warning_message": "warningMessage",
                },
                "phase": "ENVIRONMENT_PHASE_UNSPECIFIED",
                "runner_ack": {
                    "message": "message",
                    "spec_version": "string",
                    "status_code": "STATUS_CODE_UNSPECIFIED",
                },
                "secrets": [
                    {
                        "failure_message": "failureMessage",
                        "phase": "CONTENT_PHASE_UNSPECIFIED",
                        "secret_name": "secretName",
                        "warning_message": "warningMessage",
                    },
                    {
                        "failure_message": "failureMessage",
                        "phase": "CONTENT_PHASE_UNSPECIFIED",
                        "secret_name": "secretName",
                        "warning_message": "warningMessage",
                    },
                    {
                        "failure_message": "failureMessage",
                        "phase": "CONTENT_PHASE_UNSPECIFIED",
                        "secret_name": "secretName",
                        "warning_message": "warningMessage",
                    },
                ],
                "ssh_public_keys": [
                    {
                        "id": "id",
                        "phase": "CONTENT_PHASE_UNSPECIFIED",
                    },
                    {
                        "id": "id",
                        "phase": "CONTENT_PHASE_UNSPECIFIED",
                    },
                    {
                        "id": "id",
                        "phase": "CONTENT_PHASE_UNSPECIFIED",
                    },
                ],
                "status_version": "string",
                "warning_message": ["string", "string", "string"],
            },
            connect_timeout_ms=0,
        )
        assert_matches_type(object, environment, path=["response"])

    @parametrize
    async def test_raw_response_update_status(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runner_interactions.environment.with_raw_response.update_status(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment = await response.parse()
        assert_matches_type(object, environment, path=["response"])

    @parametrize
    async def test_streaming_response_update_status(self, async_client: AsyncGitpod) -> None:
        async with async_client.runner_interactions.environment.with_streaming_response.update_status(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment = await response.parse()
            assert_matches_type(object, environment, path=["response"])

        assert cast(Any, response.is_closed) is True
