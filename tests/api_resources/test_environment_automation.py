# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEnvironmentAutomation:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update_task_execution_status(self, client: Gitpod) -> None:
        environment_automation = client.environment_automation.update_task_execution_status(
            body={},
            connect_protocol_version=1,
        )
        assert_matches_type(object, environment_automation, path=["response"])

    @parametrize
    def test_method_update_task_execution_status_with_all_params(self, client: Gitpod) -> None:
        environment_automation = client.environment_automation.update_task_execution_status(
            body={
                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "failureMessage": "failureMessage",
                "logUrl": "logUrl",
                "steps": [
                    {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "failure_message": "failureMessage",
                        "phase": "TASK_EXECUTION_PHASE_UNSPECIFIED",
                    },
                    {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "failure_message": "failureMessage",
                        "phase": "TASK_EXECUTION_PHASE_UNSPECIFIED",
                    },
                    {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "failure_message": "failureMessage",
                        "phase": "TASK_EXECUTION_PHASE_UNSPECIFIED",
                    },
                ],
            },
            connect_protocol_version=1,
            connect_timeout_ms=0,
        )
        assert_matches_type(object, environment_automation, path=["response"])

    @parametrize
    def test_raw_response_update_task_execution_status(self, client: Gitpod) -> None:
        response = client.environment_automation.with_raw_response.update_task_execution_status(
            body={},
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment_automation = response.parse()
        assert_matches_type(object, environment_automation, path=["response"])

    @parametrize
    def test_streaming_response_update_task_execution_status(self, client: Gitpod) -> None:
        with client.environment_automation.with_streaming_response.update_task_execution_status(
            body={},
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment_automation = response.parse()
            assert_matches_type(object, environment_automation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEnvironmentAutomation:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update_task_execution_status(self, async_client: AsyncGitpod) -> None:
        environment_automation = await async_client.environment_automation.update_task_execution_status(
            body={},
            connect_protocol_version=1,
        )
        assert_matches_type(object, environment_automation, path=["response"])

    @parametrize
    async def test_method_update_task_execution_status_with_all_params(self, async_client: AsyncGitpod) -> None:
        environment_automation = await async_client.environment_automation.update_task_execution_status(
            body={
                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "failureMessage": "failureMessage",
                "logUrl": "logUrl",
                "steps": [
                    {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "failure_message": "failureMessage",
                        "phase": "TASK_EXECUTION_PHASE_UNSPECIFIED",
                    },
                    {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "failure_message": "failureMessage",
                        "phase": "TASK_EXECUTION_PHASE_UNSPECIFIED",
                    },
                    {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "failure_message": "failureMessage",
                        "phase": "TASK_EXECUTION_PHASE_UNSPECIFIED",
                    },
                ],
            },
            connect_protocol_version=1,
            connect_timeout_ms=0,
        )
        assert_matches_type(object, environment_automation, path=["response"])

    @parametrize
    async def test_raw_response_update_task_execution_status(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environment_automation.with_raw_response.update_task_execution_status(
            body={},
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        environment_automation = await response.parse()
        assert_matches_type(object, environment_automation, path=["response"])

    @parametrize
    async def test_streaming_response_update_task_execution_status(self, async_client: AsyncGitpod) -> None:
        async with async_client.environment_automation.with_streaming_response.update_task_execution_status(
            body={},
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            environment_automation = await response.parse()
            assert_matches_type(object, environment_automation, path=["response"])

        assert cast(Any, response.is_closed) is True
