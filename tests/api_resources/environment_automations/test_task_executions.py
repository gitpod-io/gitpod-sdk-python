# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.types.environment_automations import (
    TaskExecutionListResponse,
    TaskExecutionRetrieveResponse,
    TaskExecutionCreateListResponse,
    TaskExecutionCreateRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTaskExecutions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Gitpod) -> None:
        task_execution = client.environment_automations.task_executions.retrieve(
            connect_protocol_version=1,
        )
        assert_matches_type(TaskExecutionRetrieveResponse, task_execution, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Gitpod) -> None:
        task_execution = client.environment_automations.task_executions.retrieve(
            connect_protocol_version=1,
            base64="base64",
            compression="compression",
            connect="connect",
            encoding="encoding",
            message="message",
            connect_timeout_ms=0,
        )
        assert_matches_type(TaskExecutionRetrieveResponse, task_execution, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Gitpod) -> None:
        response = client.environment_automations.task_executions.with_raw_response.retrieve(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_execution = response.parse()
        assert_matches_type(TaskExecutionRetrieveResponse, task_execution, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Gitpod) -> None:
        with client.environment_automations.task_executions.with_streaming_response.retrieve(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task_execution = response.parse()
            assert_matches_type(TaskExecutionRetrieveResponse, task_execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gitpod) -> None:
        task_execution = client.environment_automations.task_executions.list(
            connect_protocol_version=1,
        )
        assert_matches_type(TaskExecutionListResponse, task_execution, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gitpod) -> None:
        task_execution = client.environment_automations.task_executions.list(
            connect_protocol_version=1,
            base64="base64",
            compression="compression",
            connect="connect",
            encoding="encoding",
            message="message",
            connect_timeout_ms=0,
        )
        assert_matches_type(TaskExecutionListResponse, task_execution, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gitpod) -> None:
        response = client.environment_automations.task_executions.with_raw_response.list(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_execution = response.parse()
        assert_matches_type(TaskExecutionListResponse, task_execution, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gitpod) -> None:
        with client.environment_automations.task_executions.with_streaming_response.list(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task_execution = response.parse()
            assert_matches_type(TaskExecutionListResponse, task_execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_list(self, client: Gitpod) -> None:
        task_execution = client.environment_automations.task_executions.create_list(
            connect_protocol_version=1,
        )
        assert_matches_type(TaskExecutionCreateListResponse, task_execution, path=["response"])

    @parametrize
    def test_method_create_list_with_all_params(self, client: Gitpod) -> None:
        task_execution = client.environment_automations.task_executions.create_list(
            connect_protocol_version=1,
            filter={
                "environment_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "phases": ["TASK_EXECUTION_PHASE_UNSPECIFIED"],
                "task_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "task_references": ["string"],
            },
            pagination={
                "token": "token",
                "page_size": 0,
            },
            connect_timeout_ms=0,
        )
        assert_matches_type(TaskExecutionCreateListResponse, task_execution, path=["response"])

    @parametrize
    def test_raw_response_create_list(self, client: Gitpod) -> None:
        response = client.environment_automations.task_executions.with_raw_response.create_list(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_execution = response.parse()
        assert_matches_type(TaskExecutionCreateListResponse, task_execution, path=["response"])

    @parametrize
    def test_streaming_response_create_list(self, client: Gitpod) -> None:
        with client.environment_automations.task_executions.with_streaming_response.create_list(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task_execution = response.parse()
            assert_matches_type(TaskExecutionCreateListResponse, task_execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_retrieve(self, client: Gitpod) -> None:
        task_execution = client.environment_automations.task_executions.create_retrieve(
            connect_protocol_version=1,
        )
        assert_matches_type(TaskExecutionCreateRetrieveResponse, task_execution, path=["response"])

    @parametrize
    def test_method_create_retrieve_with_all_params(self, client: Gitpod) -> None:
        task_execution = client.environment_automations.task_executions.create_retrieve(
            connect_protocol_version=1,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(TaskExecutionCreateRetrieveResponse, task_execution, path=["response"])

    @parametrize
    def test_raw_response_create_retrieve(self, client: Gitpod) -> None:
        response = client.environment_automations.task_executions.with_raw_response.create_retrieve(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_execution = response.parse()
        assert_matches_type(TaskExecutionCreateRetrieveResponse, task_execution, path=["response"])

    @parametrize
    def test_streaming_response_create_retrieve(self, client: Gitpod) -> None:
        with client.environment_automations.task_executions.with_streaming_response.create_retrieve(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task_execution = response.parse()
            assert_matches_type(TaskExecutionCreateRetrieveResponse, task_execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_stop(self, client: Gitpod) -> None:
        task_execution = client.environment_automations.task_executions.stop(
            connect_protocol_version=1,
        )
        assert_matches_type(object, task_execution, path=["response"])

    @parametrize
    def test_method_stop_with_all_params(self, client: Gitpod) -> None:
        task_execution = client.environment_automations.task_executions.stop(
            connect_protocol_version=1,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(object, task_execution, path=["response"])

    @parametrize
    def test_raw_response_stop(self, client: Gitpod) -> None:
        response = client.environment_automations.task_executions.with_raw_response.stop(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_execution = response.parse()
        assert_matches_type(object, task_execution, path=["response"])

    @parametrize
    def test_streaming_response_stop(self, client: Gitpod) -> None:
        with client.environment_automations.task_executions.with_streaming_response.stop(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task_execution = response.parse()
            assert_matches_type(object, task_execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_task_execution_status(self, client: Gitpod) -> None:
        task_execution = client.environment_automations.task_executions.update_task_execution_status(
            body={},
            connect_protocol_version=1,
        )
        assert_matches_type(object, task_execution, path=["response"])

    @parametrize
    def test_method_update_task_execution_status_with_all_params(self, client: Gitpod) -> None:
        task_execution = client.environment_automations.task_executions.update_task_execution_status(
            body={
                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "failureMessage": "failureMessage",
                "logUrl": "logUrl",
                "steps": [
                    {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "failure_message": "failureMessage",
                        "phase": "TASK_EXECUTION_PHASE_UNSPECIFIED",
                    }
                ],
            },
            connect_protocol_version=1,
            connect_timeout_ms=0,
        )
        assert_matches_type(object, task_execution, path=["response"])

    @parametrize
    def test_raw_response_update_task_execution_status(self, client: Gitpod) -> None:
        response = client.environment_automations.task_executions.with_raw_response.update_task_execution_status(
            body={},
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_execution = response.parse()
        assert_matches_type(object, task_execution, path=["response"])

    @parametrize
    def test_streaming_response_update_task_execution_status(self, client: Gitpod) -> None:
        with client.environment_automations.task_executions.with_streaming_response.update_task_execution_status(
            body={},
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task_execution = response.parse()
            assert_matches_type(object, task_execution, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTaskExecutions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGitpod) -> None:
        task_execution = await async_client.environment_automations.task_executions.retrieve(
            connect_protocol_version=1,
        )
        assert_matches_type(TaskExecutionRetrieveResponse, task_execution, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncGitpod) -> None:
        task_execution = await async_client.environment_automations.task_executions.retrieve(
            connect_protocol_version=1,
            base64="base64",
            compression="compression",
            connect="connect",
            encoding="encoding",
            message="message",
            connect_timeout_ms=0,
        )
        assert_matches_type(TaskExecutionRetrieveResponse, task_execution, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environment_automations.task_executions.with_raw_response.retrieve(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_execution = await response.parse()
        assert_matches_type(TaskExecutionRetrieveResponse, task_execution, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGitpod) -> None:
        async with async_client.environment_automations.task_executions.with_streaming_response.retrieve(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task_execution = await response.parse()
            assert_matches_type(TaskExecutionRetrieveResponse, task_execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGitpod) -> None:
        task_execution = await async_client.environment_automations.task_executions.list(
            connect_protocol_version=1,
        )
        assert_matches_type(TaskExecutionListResponse, task_execution, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGitpod) -> None:
        task_execution = await async_client.environment_automations.task_executions.list(
            connect_protocol_version=1,
            base64="base64",
            compression="compression",
            connect="connect",
            encoding="encoding",
            message="message",
            connect_timeout_ms=0,
        )
        assert_matches_type(TaskExecutionListResponse, task_execution, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environment_automations.task_executions.with_raw_response.list(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_execution = await response.parse()
        assert_matches_type(TaskExecutionListResponse, task_execution, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGitpod) -> None:
        async with async_client.environment_automations.task_executions.with_streaming_response.list(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task_execution = await response.parse()
            assert_matches_type(TaskExecutionListResponse, task_execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_list(self, async_client: AsyncGitpod) -> None:
        task_execution = await async_client.environment_automations.task_executions.create_list(
            connect_protocol_version=1,
        )
        assert_matches_type(TaskExecutionCreateListResponse, task_execution, path=["response"])

    @parametrize
    async def test_method_create_list_with_all_params(self, async_client: AsyncGitpod) -> None:
        task_execution = await async_client.environment_automations.task_executions.create_list(
            connect_protocol_version=1,
            filter={
                "environment_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "phases": ["TASK_EXECUTION_PHASE_UNSPECIFIED"],
                "task_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "task_references": ["string"],
            },
            pagination={
                "token": "token",
                "page_size": 0,
            },
            connect_timeout_ms=0,
        )
        assert_matches_type(TaskExecutionCreateListResponse, task_execution, path=["response"])

    @parametrize
    async def test_raw_response_create_list(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environment_automations.task_executions.with_raw_response.create_list(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_execution = await response.parse()
        assert_matches_type(TaskExecutionCreateListResponse, task_execution, path=["response"])

    @parametrize
    async def test_streaming_response_create_list(self, async_client: AsyncGitpod) -> None:
        async with async_client.environment_automations.task_executions.with_streaming_response.create_list(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task_execution = await response.parse()
            assert_matches_type(TaskExecutionCreateListResponse, task_execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_retrieve(self, async_client: AsyncGitpod) -> None:
        task_execution = await async_client.environment_automations.task_executions.create_retrieve(
            connect_protocol_version=1,
        )
        assert_matches_type(TaskExecutionCreateRetrieveResponse, task_execution, path=["response"])

    @parametrize
    async def test_method_create_retrieve_with_all_params(self, async_client: AsyncGitpod) -> None:
        task_execution = await async_client.environment_automations.task_executions.create_retrieve(
            connect_protocol_version=1,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(TaskExecutionCreateRetrieveResponse, task_execution, path=["response"])

    @parametrize
    async def test_raw_response_create_retrieve(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environment_automations.task_executions.with_raw_response.create_retrieve(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_execution = await response.parse()
        assert_matches_type(TaskExecutionCreateRetrieveResponse, task_execution, path=["response"])

    @parametrize
    async def test_streaming_response_create_retrieve(self, async_client: AsyncGitpod) -> None:
        async with async_client.environment_automations.task_executions.with_streaming_response.create_retrieve(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task_execution = await response.parse()
            assert_matches_type(TaskExecutionCreateRetrieveResponse, task_execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_stop(self, async_client: AsyncGitpod) -> None:
        task_execution = await async_client.environment_automations.task_executions.stop(
            connect_protocol_version=1,
        )
        assert_matches_type(object, task_execution, path=["response"])

    @parametrize
    async def test_method_stop_with_all_params(self, async_client: AsyncGitpod) -> None:
        task_execution = await async_client.environment_automations.task_executions.stop(
            connect_protocol_version=1,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(object, task_execution, path=["response"])

    @parametrize
    async def test_raw_response_stop(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environment_automations.task_executions.with_raw_response.stop(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_execution = await response.parse()
        assert_matches_type(object, task_execution, path=["response"])

    @parametrize
    async def test_streaming_response_stop(self, async_client: AsyncGitpod) -> None:
        async with async_client.environment_automations.task_executions.with_streaming_response.stop(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task_execution = await response.parse()
            assert_matches_type(object, task_execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_task_execution_status(self, async_client: AsyncGitpod) -> None:
        task_execution = await async_client.environment_automations.task_executions.update_task_execution_status(
            body={},
            connect_protocol_version=1,
        )
        assert_matches_type(object, task_execution, path=["response"])

    @parametrize
    async def test_method_update_task_execution_status_with_all_params(self, async_client: AsyncGitpod) -> None:
        task_execution = await async_client.environment_automations.task_executions.update_task_execution_status(
            body={
                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "failureMessage": "failureMessage",
                "logUrl": "logUrl",
                "steps": [
                    {
                        "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "failure_message": "failureMessage",
                        "phase": "TASK_EXECUTION_PHASE_UNSPECIFIED",
                    }
                ],
            },
            connect_protocol_version=1,
            connect_timeout_ms=0,
        )
        assert_matches_type(object, task_execution, path=["response"])

    @parametrize
    async def test_raw_response_update_task_execution_status(self, async_client: AsyncGitpod) -> None:
        response = (
            await async_client.environment_automations.task_executions.with_raw_response.update_task_execution_status(
                body={},
                connect_protocol_version=1,
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_execution = await response.parse()
        assert_matches_type(object, task_execution, path=["response"])

    @parametrize
    async def test_streaming_response_update_task_execution_status(self, async_client: AsyncGitpod) -> None:
        async with async_client.environment_automations.task_executions.with_streaming_response.update_task_execution_status(
            body={},
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task_execution = await response.parse()
            assert_matches_type(object, task_execution, path=["response"])

        assert cast(Any, response.is_closed) is True
