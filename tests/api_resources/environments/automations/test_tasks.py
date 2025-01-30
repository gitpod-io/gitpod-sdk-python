# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod._utils import parse_datetime
from gitpod.types.environments.automations import (
    TaskListResponse,
    TaskStartResponse,
    TaskCreateResponse,
    TaskRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTasks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gitpod) -> None:
        task = client.environments.automations.tasks.create()
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gitpod) -> None:
        task = client.environments.automations.tasks.create(
            depends_on=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata={
                "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "creator": {
                    "id": "id",
                    "principal": "PRINCIPAL_UNSPECIFIED",
                },
                "description": "description",
                "name": "x",
                "reference": "reference",
                "triggered_by": [{"manual": True}],
            },
            spec={
                "command": "command",
                "runs_on": {
                    "docker": {
                        "environment": ["string"],
                        "image": "x",
                    }
                },
            },
        )
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gitpod) -> None:
        response = client.environments.automations.tasks.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gitpod) -> None:
        with client.environments.automations.tasks.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskCreateResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Gitpod) -> None:
        task = client.environments.automations.tasks.retrieve()
        assert_matches_type(TaskRetrieveResponse, task, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Gitpod) -> None:
        task = client.environments.automations.tasks.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TaskRetrieveResponse, task, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Gitpod) -> None:
        response = client.environments.automations.tasks.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskRetrieveResponse, task, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Gitpod) -> None:
        with client.environments.automations.tasks.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskRetrieveResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gitpod) -> None:
        task = client.environments.automations.tasks.update()
        assert_matches_type(object, task, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gitpod) -> None:
        task = client.environments.automations.tasks.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            depends_on=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            metadata={"description": "description"},
            spec={"command": "command"},
        )
        assert_matches_type(object, task, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gitpod) -> None:
        response = client.environments.automations.tasks.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(object, task, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gitpod) -> None:
        with client.environments.automations.tasks.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(object, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gitpod) -> None:
        task = client.environments.automations.tasks.list()
        assert_matches_type(TaskListResponse, task, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gitpod) -> None:
        task = client.environments.automations.tasks.list(
            filter={
                "environment_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "references": ["x"],
                "task_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            },
            pagination={
                "token": "token",
                "page_size": 100,
            },
        )
        assert_matches_type(TaskListResponse, task, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gitpod) -> None:
        response = client.environments.automations.tasks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskListResponse, task, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gitpod) -> None:
        with client.environments.automations.tasks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskListResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gitpod) -> None:
        task = client.environments.automations.tasks.delete()
        assert_matches_type(object, task, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Gitpod) -> None:
        task = client.environments.automations.tasks.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, task, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gitpod) -> None:
        response = client.environments.automations.tasks.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(object, task, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gitpod) -> None:
        with client.environments.automations.tasks.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(object, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_start(self, client: Gitpod) -> None:
        task = client.environments.automations.tasks.start()
        assert_matches_type(TaskStartResponse, task, path=["response"])

    @parametrize
    def test_method_start_with_all_params(self, client: Gitpod) -> None:
        task = client.environments.automations.tasks.start(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TaskStartResponse, task, path=["response"])

    @parametrize
    def test_raw_response_start(self, client: Gitpod) -> None:
        response = client.environments.automations.tasks.with_raw_response.start()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskStartResponse, task, path=["response"])

    @parametrize
    def test_streaming_response_start(self, client: Gitpod) -> None:
        with client.environments.automations.tasks.with_streaming_response.start() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskStartResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTasks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncGitpod) -> None:
        task = await async_client.environments.automations.tasks.create()
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGitpod) -> None:
        task = await async_client.environments.automations.tasks.create(
            depends_on=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            environment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata={
                "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
                "creator": {
                    "id": "id",
                    "principal": "PRINCIPAL_UNSPECIFIED",
                },
                "description": "description",
                "name": "x",
                "reference": "reference",
                "triggered_by": [{"manual": True}],
            },
            spec={
                "command": "command",
                "runs_on": {
                    "docker": {
                        "environment": ["string"],
                        "image": "x",
                    }
                },
            },
        )
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.automations.tasks.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.automations.tasks.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskCreateResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGitpod) -> None:
        task = await async_client.environments.automations.tasks.retrieve()
        assert_matches_type(TaskRetrieveResponse, task, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncGitpod) -> None:
        task = await async_client.environments.automations.tasks.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TaskRetrieveResponse, task, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.automations.tasks.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskRetrieveResponse, task, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.automations.tasks.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskRetrieveResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGitpod) -> None:
        task = await async_client.environments.automations.tasks.update()
        assert_matches_type(object, task, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGitpod) -> None:
        task = await async_client.environments.automations.tasks.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            depends_on=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            metadata={"description": "description"},
            spec={"command": "command"},
        )
        assert_matches_type(object, task, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.automations.tasks.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(object, task, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.automations.tasks.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(object, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGitpod) -> None:
        task = await async_client.environments.automations.tasks.list()
        assert_matches_type(TaskListResponse, task, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGitpod) -> None:
        task = await async_client.environments.automations.tasks.list(
            filter={
                "environment_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "references": ["x"],
                "task_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            },
            pagination={
                "token": "token",
                "page_size": 100,
            },
        )
        assert_matches_type(TaskListResponse, task, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.automations.tasks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskListResponse, task, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.automations.tasks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskListResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGitpod) -> None:
        task = await async_client.environments.automations.tasks.delete()
        assert_matches_type(object, task, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncGitpod) -> None:
        task = await async_client.environments.automations.tasks.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, task, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.automations.tasks.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(object, task, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.automations.tasks.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(object, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_start(self, async_client: AsyncGitpod) -> None:
        task = await async_client.environments.automations.tasks.start()
        assert_matches_type(TaskStartResponse, task, path=["response"])

    @parametrize
    async def test_method_start_with_all_params(self, async_client: AsyncGitpod) -> None:
        task = await async_client.environments.automations.tasks.start(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TaskStartResponse, task, path=["response"])

    @parametrize
    async def test_raw_response_start(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.automations.tasks.with_raw_response.start()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskStartResponse, task, path=["response"])

    @parametrize
    async def test_streaming_response_start(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.automations.tasks.with_streaming_response.start() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskStartResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True
