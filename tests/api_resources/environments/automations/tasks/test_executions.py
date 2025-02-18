# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.pagination import SyncTaskExecutionsPage, AsyncTaskExecutionsPage
from gitpod.types.shared import TaskExecution
from gitpod.types.environments.automations.tasks import (
    ExecutionRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExecutions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Gitpod) -> None:
        execution = client.environments.automations.tasks.executions.retrieve()
        assert_matches_type(ExecutionRetrieveResponse, execution, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Gitpod) -> None:
        execution = client.environments.automations.tasks.executions.retrieve(
            id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(ExecutionRetrieveResponse, execution, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Gitpod) -> None:
        response = client.environments.automations.tasks.executions.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = response.parse()
        assert_matches_type(ExecutionRetrieveResponse, execution, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Gitpod) -> None:
        with client.environments.automations.tasks.executions.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = response.parse()
            assert_matches_type(ExecutionRetrieveResponse, execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Gitpod) -> None:
        execution = client.environments.automations.tasks.executions.list()
        assert_matches_type(SyncTaskExecutionsPage[TaskExecution], execution, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Gitpod) -> None:
        execution = client.environments.automations.tasks.executions.list(
            token="token",
            page_size=0,
            filter={
                "environment_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "phases": ["TASK_EXECUTION_PHASE_UNSPECIFIED", "TASK_EXECUTION_PHASE_PENDING"],
                "task_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "task_references": ["string"],
            },
            pagination={
                "token": "token",
                "page_size": 20,
            },
        )
        assert_matches_type(SyncTaskExecutionsPage[TaskExecution], execution, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Gitpod) -> None:
        response = client.environments.automations.tasks.executions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = response.parse()
        assert_matches_type(SyncTaskExecutionsPage[TaskExecution], execution, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Gitpod) -> None:
        with client.environments.automations.tasks.executions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = response.parse()
            assert_matches_type(SyncTaskExecutionsPage[TaskExecution], execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_stop(self, client: Gitpod) -> None:
        execution = client.environments.automations.tasks.executions.stop()
        assert_matches_type(object, execution, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_stop_with_all_params(self, client: Gitpod) -> None:
        execution = client.environments.automations.tasks.executions.stop(
            id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(object, execution, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_stop(self, client: Gitpod) -> None:
        response = client.environments.automations.tasks.executions.with_raw_response.stop()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = response.parse()
        assert_matches_type(object, execution, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_stop(self, client: Gitpod) -> None:
        with client.environments.automations.tasks.executions.with_streaming_response.stop() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = response.parse()
            assert_matches_type(object, execution, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExecutions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGitpod) -> None:
        execution = await async_client.environments.automations.tasks.executions.retrieve()
        assert_matches_type(ExecutionRetrieveResponse, execution, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncGitpod) -> None:
        execution = await async_client.environments.automations.tasks.executions.retrieve(
            id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(ExecutionRetrieveResponse, execution, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.automations.tasks.executions.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = await response.parse()
        assert_matches_type(ExecutionRetrieveResponse, execution, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGitpod) -> None:
        async with (
            async_client.environments.automations.tasks.executions.with_streaming_response.retrieve()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = await response.parse()
            assert_matches_type(ExecutionRetrieveResponse, execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncGitpod) -> None:
        execution = await async_client.environments.automations.tasks.executions.list()
        assert_matches_type(AsyncTaskExecutionsPage[TaskExecution], execution, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGitpod) -> None:
        execution = await async_client.environments.automations.tasks.executions.list(
            token="token",
            page_size=0,
            filter={
                "environment_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "phases": ["TASK_EXECUTION_PHASE_UNSPECIFIED", "TASK_EXECUTION_PHASE_PENDING"],
                "task_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "task_references": ["string"],
            },
            pagination={
                "token": "token",
                "page_size": 20,
            },
        )
        assert_matches_type(AsyncTaskExecutionsPage[TaskExecution], execution, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.automations.tasks.executions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = await response.parse()
        assert_matches_type(AsyncTaskExecutionsPage[TaskExecution], execution, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.automations.tasks.executions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = await response.parse()
            assert_matches_type(AsyncTaskExecutionsPage[TaskExecution], execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_stop(self, async_client: AsyncGitpod) -> None:
        execution = await async_client.environments.automations.tasks.executions.stop()
        assert_matches_type(object, execution, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_stop_with_all_params(self, async_client: AsyncGitpod) -> None:
        execution = await async_client.environments.automations.tasks.executions.stop(
            id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(object, execution, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_stop(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.automations.tasks.executions.with_raw_response.stop()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = await response.parse()
        assert_matches_type(object, execution, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_stop(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.automations.tasks.executions.with_streaming_response.stop() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = await response.parse()
            assert_matches_type(object, execution, path=["response"])

        assert cast(Any, response.is_closed) is True
