# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.types import (
    RunnerInteractionGetLatestVersionResponse,
    RunnerInteractionListRunnerScmIntegrationsResponse,
    RunnerInteractionListRunnerEnvironmentClassesResponse,
    RunnerInteractionGetHostAuthenticationTokenValueResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRunnerInteraction:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_host_authentication_token_value(self, client: Gitpod) -> None:
        runner_interaction = client.runner_interaction.get_host_authentication_token_value(
            connect_protocol_version=1,
        )
        assert_matches_type(
            RunnerInteractionGetHostAuthenticationTokenValueResponse, runner_interaction, path=["response"]
        )

    @parametrize
    def test_method_get_host_authentication_token_value_with_all_params(self, client: Gitpod) -> None:
        runner_interaction = client.runner_interaction.get_host_authentication_token_value(
            connect_protocol_version=1,
            host="host",
            principal_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(
            RunnerInteractionGetHostAuthenticationTokenValueResponse, runner_interaction, path=["response"]
        )

    @parametrize
    def test_raw_response_get_host_authentication_token_value(self, client: Gitpod) -> None:
        response = client.runner_interaction.with_raw_response.get_host_authentication_token_value(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner_interaction = response.parse()
        assert_matches_type(
            RunnerInteractionGetHostAuthenticationTokenValueResponse, runner_interaction, path=["response"]
        )

    @parametrize
    def test_streaming_response_get_host_authentication_token_value(self, client: Gitpod) -> None:
        with client.runner_interaction.with_streaming_response.get_host_authentication_token_value(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner_interaction = response.parse()
            assert_matches_type(
                RunnerInteractionGetHostAuthenticationTokenValueResponse, runner_interaction, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_latest_version(self, client: Gitpod) -> None:
        runner_interaction = client.runner_interaction.get_latest_version(
            connect_protocol_version=1,
        )
        assert_matches_type(RunnerInteractionGetLatestVersionResponse, runner_interaction, path=["response"])

    @parametrize
    def test_method_get_latest_version_with_all_params(self, client: Gitpod) -> None:
        runner_interaction = client.runner_interaction.get_latest_version(
            connect_protocol_version=1,
            current_version="currentVersion",
            infrastructure_version="infrastructureVersion",
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(RunnerInteractionGetLatestVersionResponse, runner_interaction, path=["response"])

    @parametrize
    def test_raw_response_get_latest_version(self, client: Gitpod) -> None:
        response = client.runner_interaction.with_raw_response.get_latest_version(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner_interaction = response.parse()
        assert_matches_type(RunnerInteractionGetLatestVersionResponse, runner_interaction, path=["response"])

    @parametrize
    def test_streaming_response_get_latest_version(self, client: Gitpod) -> None:
        with client.runner_interaction.with_streaming_response.get_latest_version(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner_interaction = response.parse()
            assert_matches_type(RunnerInteractionGetLatestVersionResponse, runner_interaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_runner_environment_classes(self, client: Gitpod) -> None:
        runner_interaction = client.runner_interaction.list_runner_environment_classes(
            connect_protocol_version=1,
        )
        assert_matches_type(
            RunnerInteractionListRunnerEnvironmentClassesResponse, runner_interaction, path=["response"]
        )

    @parametrize
    def test_method_list_runner_environment_classes_with_all_params(self, client: Gitpod) -> None:
        runner_interaction = client.runner_interaction.list_runner_environment_classes(
            connect_protocol_version=1,
            filter={
                "environment_class_ids": [
                    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                ]
            },
            pagination={
                "token": "token",
                "page_size": 0,
            },
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(
            RunnerInteractionListRunnerEnvironmentClassesResponse, runner_interaction, path=["response"]
        )

    @parametrize
    def test_raw_response_list_runner_environment_classes(self, client: Gitpod) -> None:
        response = client.runner_interaction.with_raw_response.list_runner_environment_classes(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner_interaction = response.parse()
        assert_matches_type(
            RunnerInteractionListRunnerEnvironmentClassesResponse, runner_interaction, path=["response"]
        )

    @parametrize
    def test_streaming_response_list_runner_environment_classes(self, client: Gitpod) -> None:
        with client.runner_interaction.with_streaming_response.list_runner_environment_classes(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner_interaction = response.parse()
            assert_matches_type(
                RunnerInteractionListRunnerEnvironmentClassesResponse, runner_interaction, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_runner_scm_integrations(self, client: Gitpod) -> None:
        runner_interaction = client.runner_interaction.list_runner_scm_integrations(
            connect_protocol_version=1,
        )
        assert_matches_type(RunnerInteractionListRunnerScmIntegrationsResponse, runner_interaction, path=["response"])

    @parametrize
    def test_method_list_runner_scm_integrations_with_all_params(self, client: Gitpod) -> None:
        runner_interaction = client.runner_interaction.list_runner_scm_integrations(
            connect_protocol_version=1,
            filter={
                "scm_integration_ids": [
                    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                ]
            },
            pagination={
                "token": "token",
                "page_size": 0,
            },
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(RunnerInteractionListRunnerScmIntegrationsResponse, runner_interaction, path=["response"])

    @parametrize
    def test_raw_response_list_runner_scm_integrations(self, client: Gitpod) -> None:
        response = client.runner_interaction.with_raw_response.list_runner_scm_integrations(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner_interaction = response.parse()
        assert_matches_type(RunnerInteractionListRunnerScmIntegrationsResponse, runner_interaction, path=["response"])

    @parametrize
    def test_streaming_response_list_runner_scm_integrations(self, client: Gitpod) -> None:
        with client.runner_interaction.with_streaming_response.list_runner_scm_integrations(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner_interaction = response.parse()
            assert_matches_type(
                RunnerInteractionListRunnerScmIntegrationsResponse, runner_interaction, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_send_response_overload_1(self, client: Gitpod) -> None:
        runner_interaction = client.runner_interaction.send_response(
            body={},
            connect_protocol_version=1,
        )
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    def test_method_send_response_with_all_params_overload_1(self, client: Gitpod) -> None:
        runner_interaction = client.runner_interaction.send_response(
            body={},
            connect_protocol_version=1,
            connect_timeout_ms=0,
        )
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    def test_raw_response_send_response_overload_1(self, client: Gitpod) -> None:
        response = client.runner_interaction.with_raw_response.send_response(
            body={},
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner_interaction = response.parse()
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    def test_streaming_response_send_response_overload_1(self, client: Gitpod) -> None:
        with client.runner_interaction.with_streaming_response.send_response(
            body={},
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner_interaction = response.parse()
            assert_matches_type(object, runner_interaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_send_response_overload_2(self, client: Gitpod) -> None:
        runner_interaction = client.runner_interaction.send_response(
            body={},
            connect_protocol_version=1,
        )
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    def test_method_send_response_with_all_params_overload_2(self, client: Gitpod) -> None:
        runner_interaction = client.runner_interaction.send_response(
            body={},
            connect_protocol_version=1,
            connect_timeout_ms=0,
        )
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    def test_raw_response_send_response_overload_2(self, client: Gitpod) -> None:
        response = client.runner_interaction.with_raw_response.send_response(
            body={},
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner_interaction = response.parse()
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    def test_streaming_response_send_response_overload_2(self, client: Gitpod) -> None:
        with client.runner_interaction.with_streaming_response.send_response(
            body={},
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner_interaction = response.parse()
            assert_matches_type(object, runner_interaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_send_response_overload_3(self, client: Gitpod) -> None:
        runner_interaction = client.runner_interaction.send_response(
            body={},
            connect_protocol_version=1,
        )
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    def test_method_send_response_with_all_params_overload_3(self, client: Gitpod) -> None:
        runner_interaction = client.runner_interaction.send_response(
            body={},
            connect_protocol_version=1,
            connect_timeout_ms=0,
        )
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    def test_raw_response_send_response_overload_3(self, client: Gitpod) -> None:
        response = client.runner_interaction.with_raw_response.send_response(
            body={},
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner_interaction = response.parse()
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    def test_streaming_response_send_response_overload_3(self, client: Gitpod) -> None:
        with client.runner_interaction.with_streaming_response.send_response(
            body={},
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner_interaction = response.parse()
            assert_matches_type(object, runner_interaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_send_response_overload_4(self, client: Gitpod) -> None:
        runner_interaction = client.runner_interaction.send_response(
            body={},
            connect_protocol_version=1,
        )
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    def test_method_send_response_with_all_params_overload_4(self, client: Gitpod) -> None:
        runner_interaction = client.runner_interaction.send_response(
            body={},
            connect_protocol_version=1,
            connect_timeout_ms=0,
        )
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    def test_raw_response_send_response_overload_4(self, client: Gitpod) -> None:
        response = client.runner_interaction.with_raw_response.send_response(
            body={},
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner_interaction = response.parse()
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    def test_streaming_response_send_response_overload_4(self, client: Gitpod) -> None:
        with client.runner_interaction.with_streaming_response.send_response(
            body={},
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner_interaction = response.parse()
            assert_matches_type(object, runner_interaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_send_response_overload_5(self, client: Gitpod) -> None:
        runner_interaction = client.runner_interaction.send_response(
            body={},
            connect_protocol_version=1,
        )
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    def test_method_send_response_with_all_params_overload_5(self, client: Gitpod) -> None:
        runner_interaction = client.runner_interaction.send_response(
            body={},
            connect_protocol_version=1,
            connect_timeout_ms=0,
        )
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    def test_raw_response_send_response_overload_5(self, client: Gitpod) -> None:
        response = client.runner_interaction.with_raw_response.send_response(
            body={},
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner_interaction = response.parse()
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    def test_streaming_response_send_response_overload_5(self, client: Gitpod) -> None:
        with client.runner_interaction.with_streaming_response.send_response(
            body={},
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner_interaction = response.parse()
            assert_matches_type(object, runner_interaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_send_response_overload_6(self, client: Gitpod) -> None:
        runner_interaction = client.runner_interaction.send_response(
            body={},
            connect_protocol_version=1,
        )
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    def test_method_send_response_with_all_params_overload_6(self, client: Gitpod) -> None:
        runner_interaction = client.runner_interaction.send_response(
            body={},
            connect_protocol_version=1,
            connect_timeout_ms=0,
        )
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    def test_raw_response_send_response_overload_6(self, client: Gitpod) -> None:
        response = client.runner_interaction.with_raw_response.send_response(
            body={},
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner_interaction = response.parse()
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    def test_streaming_response_send_response_overload_6(self, client: Gitpod) -> None:
        with client.runner_interaction.with_streaming_response.send_response(
            body={},
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner_interaction = response.parse()
            assert_matches_type(object, runner_interaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_runner_configuration_schema(self, client: Gitpod) -> None:
        runner_interaction = client.runner_interaction.update_runner_configuration_schema(
            connect_protocol_version=1,
        )
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    def test_method_update_runner_configuration_schema_with_all_params(self, client: Gitpod) -> None:
        runner_interaction = client.runner_interaction.update_runner_configuration_schema(
            connect_protocol_version=1,
            config_schema={
                "environment_classes": [{}, {}, {}],
                "runner_config": [{}, {}, {}],
                "scm": [
                    {
                        "default_hosts": ["string", "string", "string"],
                        "name": "name",
                        "oauth": {"callback_url": "callbackUrl"},
                        "pat": {
                            "description": "description",
                            "docs_link": "docsLink",
                        },
                        "scm_id": "scmId",
                    },
                    {
                        "default_hosts": ["string", "string", "string"],
                        "name": "name",
                        "oauth": {"callback_url": "callbackUrl"},
                        "pat": {
                            "description": "description",
                            "docs_link": "docsLink",
                        },
                        "scm_id": "scmId",
                    },
                    {
                        "default_hosts": ["string", "string", "string"],
                        "name": "name",
                        "oauth": {"callback_url": "callbackUrl"},
                        "pat": {
                            "description": "description",
                            "docs_link": "docsLink",
                        },
                        "scm_id": "scmId",
                    },
                ],
                "version": "version",
            },
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    def test_raw_response_update_runner_configuration_schema(self, client: Gitpod) -> None:
        response = client.runner_interaction.with_raw_response.update_runner_configuration_schema(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner_interaction = response.parse()
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    def test_streaming_response_update_runner_configuration_schema(self, client: Gitpod) -> None:
        with client.runner_interaction.with_streaming_response.update_runner_configuration_schema(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner_interaction = response.parse()
            assert_matches_type(object, runner_interaction, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRunnerInteraction:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get_host_authentication_token_value(self, async_client: AsyncGitpod) -> None:
        runner_interaction = await async_client.runner_interaction.get_host_authentication_token_value(
            connect_protocol_version=1,
        )
        assert_matches_type(
            RunnerInteractionGetHostAuthenticationTokenValueResponse, runner_interaction, path=["response"]
        )

    @parametrize
    async def test_method_get_host_authentication_token_value_with_all_params(self, async_client: AsyncGitpod) -> None:
        runner_interaction = await async_client.runner_interaction.get_host_authentication_token_value(
            connect_protocol_version=1,
            host="host",
            principal_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(
            RunnerInteractionGetHostAuthenticationTokenValueResponse, runner_interaction, path=["response"]
        )

    @parametrize
    async def test_raw_response_get_host_authentication_token_value(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runner_interaction.with_raw_response.get_host_authentication_token_value(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner_interaction = await response.parse()
        assert_matches_type(
            RunnerInteractionGetHostAuthenticationTokenValueResponse, runner_interaction, path=["response"]
        )

    @parametrize
    async def test_streaming_response_get_host_authentication_token_value(self, async_client: AsyncGitpod) -> None:
        async with async_client.runner_interaction.with_streaming_response.get_host_authentication_token_value(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner_interaction = await response.parse()
            assert_matches_type(
                RunnerInteractionGetHostAuthenticationTokenValueResponse, runner_interaction, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_latest_version(self, async_client: AsyncGitpod) -> None:
        runner_interaction = await async_client.runner_interaction.get_latest_version(
            connect_protocol_version=1,
        )
        assert_matches_type(RunnerInteractionGetLatestVersionResponse, runner_interaction, path=["response"])

    @parametrize
    async def test_method_get_latest_version_with_all_params(self, async_client: AsyncGitpod) -> None:
        runner_interaction = await async_client.runner_interaction.get_latest_version(
            connect_protocol_version=1,
            current_version="currentVersion",
            infrastructure_version="infrastructureVersion",
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(RunnerInteractionGetLatestVersionResponse, runner_interaction, path=["response"])

    @parametrize
    async def test_raw_response_get_latest_version(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runner_interaction.with_raw_response.get_latest_version(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner_interaction = await response.parse()
        assert_matches_type(RunnerInteractionGetLatestVersionResponse, runner_interaction, path=["response"])

    @parametrize
    async def test_streaming_response_get_latest_version(self, async_client: AsyncGitpod) -> None:
        async with async_client.runner_interaction.with_streaming_response.get_latest_version(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner_interaction = await response.parse()
            assert_matches_type(RunnerInteractionGetLatestVersionResponse, runner_interaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_runner_environment_classes(self, async_client: AsyncGitpod) -> None:
        runner_interaction = await async_client.runner_interaction.list_runner_environment_classes(
            connect_protocol_version=1,
        )
        assert_matches_type(
            RunnerInteractionListRunnerEnvironmentClassesResponse, runner_interaction, path=["response"]
        )

    @parametrize
    async def test_method_list_runner_environment_classes_with_all_params(self, async_client: AsyncGitpod) -> None:
        runner_interaction = await async_client.runner_interaction.list_runner_environment_classes(
            connect_protocol_version=1,
            filter={
                "environment_class_ids": [
                    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                ]
            },
            pagination={
                "token": "token",
                "page_size": 0,
            },
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(
            RunnerInteractionListRunnerEnvironmentClassesResponse, runner_interaction, path=["response"]
        )

    @parametrize
    async def test_raw_response_list_runner_environment_classes(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runner_interaction.with_raw_response.list_runner_environment_classes(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner_interaction = await response.parse()
        assert_matches_type(
            RunnerInteractionListRunnerEnvironmentClassesResponse, runner_interaction, path=["response"]
        )

    @parametrize
    async def test_streaming_response_list_runner_environment_classes(self, async_client: AsyncGitpod) -> None:
        async with async_client.runner_interaction.with_streaming_response.list_runner_environment_classes(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner_interaction = await response.parse()
            assert_matches_type(
                RunnerInteractionListRunnerEnvironmentClassesResponse, runner_interaction, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_runner_scm_integrations(self, async_client: AsyncGitpod) -> None:
        runner_interaction = await async_client.runner_interaction.list_runner_scm_integrations(
            connect_protocol_version=1,
        )
        assert_matches_type(RunnerInteractionListRunnerScmIntegrationsResponse, runner_interaction, path=["response"])

    @parametrize
    async def test_method_list_runner_scm_integrations_with_all_params(self, async_client: AsyncGitpod) -> None:
        runner_interaction = await async_client.runner_interaction.list_runner_scm_integrations(
            connect_protocol_version=1,
            filter={
                "scm_integration_ids": [
                    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                ]
            },
            pagination={
                "token": "token",
                "page_size": 0,
            },
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(RunnerInteractionListRunnerScmIntegrationsResponse, runner_interaction, path=["response"])

    @parametrize
    async def test_raw_response_list_runner_scm_integrations(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runner_interaction.with_raw_response.list_runner_scm_integrations(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner_interaction = await response.parse()
        assert_matches_type(RunnerInteractionListRunnerScmIntegrationsResponse, runner_interaction, path=["response"])

    @parametrize
    async def test_streaming_response_list_runner_scm_integrations(self, async_client: AsyncGitpod) -> None:
        async with async_client.runner_interaction.with_streaming_response.list_runner_scm_integrations(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner_interaction = await response.parse()
            assert_matches_type(
                RunnerInteractionListRunnerScmIntegrationsResponse, runner_interaction, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_send_response_overload_1(self, async_client: AsyncGitpod) -> None:
        runner_interaction = await async_client.runner_interaction.send_response(
            body={},
            connect_protocol_version=1,
        )
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    async def test_method_send_response_with_all_params_overload_1(self, async_client: AsyncGitpod) -> None:
        runner_interaction = await async_client.runner_interaction.send_response(
            body={},
            connect_protocol_version=1,
            connect_timeout_ms=0,
        )
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    async def test_raw_response_send_response_overload_1(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runner_interaction.with_raw_response.send_response(
            body={},
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner_interaction = await response.parse()
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    async def test_streaming_response_send_response_overload_1(self, async_client: AsyncGitpod) -> None:
        async with async_client.runner_interaction.with_streaming_response.send_response(
            body={},
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner_interaction = await response.parse()
            assert_matches_type(object, runner_interaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_send_response_overload_2(self, async_client: AsyncGitpod) -> None:
        runner_interaction = await async_client.runner_interaction.send_response(
            body={},
            connect_protocol_version=1,
        )
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    async def test_method_send_response_with_all_params_overload_2(self, async_client: AsyncGitpod) -> None:
        runner_interaction = await async_client.runner_interaction.send_response(
            body={},
            connect_protocol_version=1,
            connect_timeout_ms=0,
        )
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    async def test_raw_response_send_response_overload_2(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runner_interaction.with_raw_response.send_response(
            body={},
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner_interaction = await response.parse()
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    async def test_streaming_response_send_response_overload_2(self, async_client: AsyncGitpod) -> None:
        async with async_client.runner_interaction.with_streaming_response.send_response(
            body={},
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner_interaction = await response.parse()
            assert_matches_type(object, runner_interaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_send_response_overload_3(self, async_client: AsyncGitpod) -> None:
        runner_interaction = await async_client.runner_interaction.send_response(
            body={},
            connect_protocol_version=1,
        )
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    async def test_method_send_response_with_all_params_overload_3(self, async_client: AsyncGitpod) -> None:
        runner_interaction = await async_client.runner_interaction.send_response(
            body={},
            connect_protocol_version=1,
            connect_timeout_ms=0,
        )
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    async def test_raw_response_send_response_overload_3(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runner_interaction.with_raw_response.send_response(
            body={},
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner_interaction = await response.parse()
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    async def test_streaming_response_send_response_overload_3(self, async_client: AsyncGitpod) -> None:
        async with async_client.runner_interaction.with_streaming_response.send_response(
            body={},
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner_interaction = await response.parse()
            assert_matches_type(object, runner_interaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_send_response_overload_4(self, async_client: AsyncGitpod) -> None:
        runner_interaction = await async_client.runner_interaction.send_response(
            body={},
            connect_protocol_version=1,
        )
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    async def test_method_send_response_with_all_params_overload_4(self, async_client: AsyncGitpod) -> None:
        runner_interaction = await async_client.runner_interaction.send_response(
            body={},
            connect_protocol_version=1,
            connect_timeout_ms=0,
        )
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    async def test_raw_response_send_response_overload_4(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runner_interaction.with_raw_response.send_response(
            body={},
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner_interaction = await response.parse()
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    async def test_streaming_response_send_response_overload_4(self, async_client: AsyncGitpod) -> None:
        async with async_client.runner_interaction.with_streaming_response.send_response(
            body={},
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner_interaction = await response.parse()
            assert_matches_type(object, runner_interaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_send_response_overload_5(self, async_client: AsyncGitpod) -> None:
        runner_interaction = await async_client.runner_interaction.send_response(
            body={},
            connect_protocol_version=1,
        )
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    async def test_method_send_response_with_all_params_overload_5(self, async_client: AsyncGitpod) -> None:
        runner_interaction = await async_client.runner_interaction.send_response(
            body={},
            connect_protocol_version=1,
            connect_timeout_ms=0,
        )
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    async def test_raw_response_send_response_overload_5(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runner_interaction.with_raw_response.send_response(
            body={},
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner_interaction = await response.parse()
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    async def test_streaming_response_send_response_overload_5(self, async_client: AsyncGitpod) -> None:
        async with async_client.runner_interaction.with_streaming_response.send_response(
            body={},
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner_interaction = await response.parse()
            assert_matches_type(object, runner_interaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_send_response_overload_6(self, async_client: AsyncGitpod) -> None:
        runner_interaction = await async_client.runner_interaction.send_response(
            body={},
            connect_protocol_version=1,
        )
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    async def test_method_send_response_with_all_params_overload_6(self, async_client: AsyncGitpod) -> None:
        runner_interaction = await async_client.runner_interaction.send_response(
            body={},
            connect_protocol_version=1,
            connect_timeout_ms=0,
        )
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    async def test_raw_response_send_response_overload_6(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runner_interaction.with_raw_response.send_response(
            body={},
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner_interaction = await response.parse()
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    async def test_streaming_response_send_response_overload_6(self, async_client: AsyncGitpod) -> None:
        async with async_client.runner_interaction.with_streaming_response.send_response(
            body={},
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner_interaction = await response.parse()
            assert_matches_type(object, runner_interaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_runner_configuration_schema(self, async_client: AsyncGitpod) -> None:
        runner_interaction = await async_client.runner_interaction.update_runner_configuration_schema(
            connect_protocol_version=1,
        )
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    async def test_method_update_runner_configuration_schema_with_all_params(self, async_client: AsyncGitpod) -> None:
        runner_interaction = await async_client.runner_interaction.update_runner_configuration_schema(
            connect_protocol_version=1,
            config_schema={
                "environment_classes": [{}, {}, {}],
                "runner_config": [{}, {}, {}],
                "scm": [
                    {
                        "default_hosts": ["string", "string", "string"],
                        "name": "name",
                        "oauth": {"callback_url": "callbackUrl"},
                        "pat": {
                            "description": "description",
                            "docs_link": "docsLink",
                        },
                        "scm_id": "scmId",
                    },
                    {
                        "default_hosts": ["string", "string", "string"],
                        "name": "name",
                        "oauth": {"callback_url": "callbackUrl"},
                        "pat": {
                            "description": "description",
                            "docs_link": "docsLink",
                        },
                        "scm_id": "scmId",
                    },
                    {
                        "default_hosts": ["string", "string", "string"],
                        "name": "name",
                        "oauth": {"callback_url": "callbackUrl"},
                        "pat": {
                            "description": "description",
                            "docs_link": "docsLink",
                        },
                        "scm_id": "scmId",
                    },
                ],
                "version": "version",
            },
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    async def test_raw_response_update_runner_configuration_schema(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runner_interaction.with_raw_response.update_runner_configuration_schema(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        runner_interaction = await response.parse()
        assert_matches_type(object, runner_interaction, path=["response"])

    @parametrize
    async def test_streaming_response_update_runner_configuration_schema(self, async_client: AsyncGitpod) -> None:
        async with async_client.runner_interaction.with_streaming_response.update_runner_configuration_schema(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            runner_interaction = await response.parse()
            assert_matches_type(object, runner_interaction, path=["response"])

        assert cast(Any, response.is_closed) is True
