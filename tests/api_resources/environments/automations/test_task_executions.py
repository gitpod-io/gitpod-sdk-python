# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.types.environments.automations import (
    TaskExecutionListResponse,
    TaskExecutionRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTaskExecutions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Gitpod) -> None:
        task_execution = client.environments.automations.task_executions.retrieve()
        assert_matches_type(TaskExecutionRetrieveResponse, task_execution, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Gitpod) -> None:
        task_execution = client.environments.automations.task_executions.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TaskExecutionRetrieveResponse, task_execution, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Gitpod) -> None:
        response = client.environments.automations.task_executions.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_execution = response.parse()
        assert_matches_type(TaskExecutionRetrieveResponse, task_execution, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Gitpod) -> None:
        with client.environments.automations.task_executions.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task_execution = response.parse()
            assert_matches_type(TaskExecutionRetrieveResponse, task_execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gitpod) -> None:
        task_execution = client.environments.automations.task_executions.list()
        assert_matches_type(TaskExecutionListResponse, task_execution, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gitpod) -> None:
        task_execution = client.environments.automations.task_executions.list(
            filter={
                "environment_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "phases": ["TASK_EXECUTION_PHASE_UNSPECIFIED"],
                "task_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "task_references": ["string"],
            },
            pagination={
                "token": "token",
                "page_size": 100,
            },
        )
        assert_matches_type(TaskExecutionListResponse, task_execution, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gitpod) -> None:
        response = client.environments.automations.task_executions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_execution = response.parse()
        assert_matches_type(TaskExecutionListResponse, task_execution, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gitpod) -> None:
        with client.environments.automations.task_executions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task_execution = response.parse()
            assert_matches_type(TaskExecutionListResponse, task_execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_stop(self, client: Gitpod) -> None:
        task_execution = client.environments.automations.task_executions.stop()
        assert_matches_type(object, task_execution, path=["response"])

    @parametrize
    def test_method_stop_with_all_params(self, client: Gitpod) -> None:
        task_execution = client.environments.automations.task_executions.stop(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, task_execution, path=["response"])

    @parametrize
    def test_raw_response_stop(self, client: Gitpod) -> None:
        response = client.environments.automations.task_executions.with_raw_response.stop()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_execution = response.parse()
        assert_matches_type(object, task_execution, path=["response"])

    @parametrize
    def test_streaming_response_stop(self, client: Gitpod) -> None:
        with client.environments.automations.task_executions.with_streaming_response.stop() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task_execution = response.parse()
            assert_matches_type(object, task_execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_task_execution_status_overload_1(self, client: Gitpod) -> None:
        task_execution = client.environments.automations.task_executions.update_task_execution_status(
            failure_message="failureMessage",
        )
        assert_matches_type(object, task_execution, path=["response"])

    @parametrize
    def test_raw_response_update_task_execution_status_overload_1(self, client: Gitpod) -> None:
        response = client.environments.automations.task_executions.with_raw_response.update_task_execution_status(
            failure_message="failureMessage",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_execution = response.parse()
        assert_matches_type(object, task_execution, path=["response"])

    @parametrize
    def test_streaming_response_update_task_execution_status_overload_1(self, client: Gitpod) -> None:
        with client.environments.automations.task_executions.with_streaming_response.update_task_execution_status(
            failure_message="failureMessage",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task_execution = response.parse()
            assert_matches_type(object, task_execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_task_execution_status_overload_2(self, client: Gitpod) -> None:
        task_execution = client.environments.automations.task_executions.update_task_execution_status(
            log_url="logUrl",
        )
        assert_matches_type(object, task_execution, path=["response"])

    @parametrize
    def test_raw_response_update_task_execution_status_overload_2(self, client: Gitpod) -> None:
        response = client.environments.automations.task_executions.with_raw_response.update_task_execution_status(
            log_url="logUrl",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_execution = response.parse()
        assert_matches_type(object, task_execution, path=["response"])

    @parametrize
    def test_streaming_response_update_task_execution_status_overload_2(self, client: Gitpod) -> None:
        with client.environments.automations.task_executions.with_streaming_response.update_task_execution_status(
            log_url="logUrl",
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
        task_execution = await async_client.environments.automations.task_executions.retrieve()
        assert_matches_type(TaskExecutionRetrieveResponse, task_execution, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncGitpod) -> None:
        task_execution = await async_client.environments.automations.task_executions.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TaskExecutionRetrieveResponse, task_execution, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.automations.task_executions.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_execution = await response.parse()
        assert_matches_type(TaskExecutionRetrieveResponse, task_execution, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.automations.task_executions.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task_execution = await response.parse()
            assert_matches_type(TaskExecutionRetrieveResponse, task_execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGitpod) -> None:
        task_execution = await async_client.environments.automations.task_executions.list()
        assert_matches_type(TaskExecutionListResponse, task_execution, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGitpod) -> None:
        task_execution = await async_client.environments.automations.task_executions.list(
            filter={
                "environment_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "phases": ["TASK_EXECUTION_PHASE_UNSPECIFIED"],
                "task_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "task_references": ["string"],
            },
            pagination={
                "token": "token",
                "page_size": 100,
            },
        )
        assert_matches_type(TaskExecutionListResponse, task_execution, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.automations.task_executions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_execution = await response.parse()
        assert_matches_type(TaskExecutionListResponse, task_execution, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.automations.task_executions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task_execution = await response.parse()
            assert_matches_type(TaskExecutionListResponse, task_execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_stop(self, async_client: AsyncGitpod) -> None:
        task_execution = await async_client.environments.automations.task_executions.stop()
        assert_matches_type(object, task_execution, path=["response"])

    @parametrize
    async def test_method_stop_with_all_params(self, async_client: AsyncGitpod) -> None:
        task_execution = await async_client.environments.automations.task_executions.stop(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, task_execution, path=["response"])

    @parametrize
    async def test_raw_response_stop(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.automations.task_executions.with_raw_response.stop()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_execution = await response.parse()
        assert_matches_type(object, task_execution, path=["response"])

    @parametrize
    async def test_streaming_response_stop(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.automations.task_executions.with_streaming_response.stop() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task_execution = await response.parse()
            assert_matches_type(object, task_execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_task_execution_status_overload_1(self, async_client: AsyncGitpod) -> None:
        task_execution = await async_client.environments.automations.task_executions.update_task_execution_status(
            failure_message="failureMessage",
        )
        assert_matches_type(object, task_execution, path=["response"])

    @parametrize
    async def test_raw_response_update_task_execution_status_overload_1(self, async_client: AsyncGitpod) -> None:
        response = (
            await async_client.environments.automations.task_executions.with_raw_response.update_task_execution_status(
                failure_message="failureMessage",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_execution = await response.parse()
        assert_matches_type(object, task_execution, path=["response"])

    @parametrize
    async def test_streaming_response_update_task_execution_status_overload_1(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.automations.task_executions.with_streaming_response.update_task_execution_status(
            failure_message="failureMessage",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task_execution = await response.parse()
            assert_matches_type(object, task_execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_task_execution_status_overload_2(self, async_client: AsyncGitpod) -> None:
        task_execution = await async_client.environments.automations.task_executions.update_task_execution_status(
            log_url="logUrl",
        )
        assert_matches_type(object, task_execution, path=["response"])

    @parametrize
    async def test_raw_response_update_task_execution_status_overload_2(self, async_client: AsyncGitpod) -> None:
        response = (
            await async_client.environments.automations.task_executions.with_raw_response.update_task_execution_status(
                log_url="logUrl",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task_execution = await response.parse()
        assert_matches_type(object, task_execution, path=["response"])

    @parametrize
    async def test_streaming_response_update_task_execution_status_overload_2(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.automations.task_executions.with_streaming_response.update_task_execution_status(
            log_url="logUrl",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task_execution = await response.parse()
            assert_matches_type(object, task_execution, path=["response"])

        assert cast(Any, response.is_closed) is True
