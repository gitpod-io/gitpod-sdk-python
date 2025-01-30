# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.types.environments.automations.tasks import (
    ExecutionListResponse,
    ExecutionRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExecutions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Gitpod) -> None:
        execution = client.environments.automations.tasks.executions.retrieve(
            encoding="proto",
            connect_protocol_version=1,
        )
        assert_matches_type(ExecutionRetrieveResponse, execution, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Gitpod) -> None:
        execution = client.environments.automations.tasks.executions.retrieve(
            encoding="proto",
            connect_protocol_version=1,
            base64=True,
            compression="identity",
            connect="v1",
            message="message",
            connect_timeout_ms=0,
        )
        assert_matches_type(ExecutionRetrieveResponse, execution, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Gitpod) -> None:
        response = client.environments.automations.tasks.executions.with_raw_response.retrieve(
            encoding="proto",
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = response.parse()
        assert_matches_type(ExecutionRetrieveResponse, execution, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Gitpod) -> None:
        with client.environments.automations.tasks.executions.with_streaming_response.retrieve(
            encoding="proto",
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = response.parse()
            assert_matches_type(ExecutionRetrieveResponse, execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gitpod) -> None:
        execution = client.environments.automations.tasks.executions.list(
            encoding="proto",
            connect_protocol_version=1,
        )
        assert_matches_type(ExecutionListResponse, execution, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gitpod) -> None:
        execution = client.environments.automations.tasks.executions.list(
            encoding="proto",
            connect_protocol_version=1,
            base64=True,
            compression="identity",
            connect="v1",
            message="message",
            connect_timeout_ms=0,
        )
        assert_matches_type(ExecutionListResponse, execution, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gitpod) -> None:
        response = client.environments.automations.tasks.executions.with_raw_response.list(
            encoding="proto",
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = response.parse()
        assert_matches_type(ExecutionListResponse, execution, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gitpod) -> None:
        with client.environments.automations.tasks.executions.with_streaming_response.list(
            encoding="proto",
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = response.parse()
            assert_matches_type(ExecutionListResponse, execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_stop(self, client: Gitpod) -> None:
        execution = client.environments.automations.tasks.executions.stop(
            connect_protocol_version=1,
        )
        assert_matches_type(object, execution, path=["response"])

    @parametrize
    def test_method_stop_with_all_params(self, client: Gitpod) -> None:
        execution = client.environments.automations.tasks.executions.stop(
            connect_protocol_version=1,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(object, execution, path=["response"])

    @parametrize
    def test_raw_response_stop(self, client: Gitpod) -> None:
        response = client.environments.automations.tasks.executions.with_raw_response.stop(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = response.parse()
        assert_matches_type(object, execution, path=["response"])

    @parametrize
    def test_streaming_response_stop(self, client: Gitpod) -> None:
        with client.environments.automations.tasks.executions.with_streaming_response.stop(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = response.parse()
            assert_matches_type(object, execution, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExecutions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGitpod) -> None:
        execution = await async_client.environments.automations.tasks.executions.retrieve(
            encoding="proto",
            connect_protocol_version=1,
        )
        assert_matches_type(ExecutionRetrieveResponse, execution, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncGitpod) -> None:
        execution = await async_client.environments.automations.tasks.executions.retrieve(
            encoding="proto",
            connect_protocol_version=1,
            base64=True,
            compression="identity",
            connect="v1",
            message="message",
            connect_timeout_ms=0,
        )
        assert_matches_type(ExecutionRetrieveResponse, execution, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.automations.tasks.executions.with_raw_response.retrieve(
            encoding="proto",
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = await response.parse()
        assert_matches_type(ExecutionRetrieveResponse, execution, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.automations.tasks.executions.with_streaming_response.retrieve(
            encoding="proto",
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = await response.parse()
            assert_matches_type(ExecutionRetrieveResponse, execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGitpod) -> None:
        execution = await async_client.environments.automations.tasks.executions.list(
            encoding="proto",
            connect_protocol_version=1,
        )
        assert_matches_type(ExecutionListResponse, execution, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGitpod) -> None:
        execution = await async_client.environments.automations.tasks.executions.list(
            encoding="proto",
            connect_protocol_version=1,
            base64=True,
            compression="identity",
            connect="v1",
            message="message",
            connect_timeout_ms=0,
        )
        assert_matches_type(ExecutionListResponse, execution, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.automations.tasks.executions.with_raw_response.list(
            encoding="proto",
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = await response.parse()
        assert_matches_type(ExecutionListResponse, execution, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.automations.tasks.executions.with_streaming_response.list(
            encoding="proto",
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = await response.parse()
            assert_matches_type(ExecutionListResponse, execution, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_stop(self, async_client: AsyncGitpod) -> None:
        execution = await async_client.environments.automations.tasks.executions.stop(
            connect_protocol_version=1,
        )
        assert_matches_type(object, execution, path=["response"])

    @parametrize
    async def test_method_stop_with_all_params(self, async_client: AsyncGitpod) -> None:
        execution = await async_client.environments.automations.tasks.executions.stop(
            connect_protocol_version=1,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(object, execution, path=["response"])

    @parametrize
    async def test_raw_response_stop(self, async_client: AsyncGitpod) -> None:
        response = await async_client.environments.automations.tasks.executions.with_raw_response.stop(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        execution = await response.parse()
        assert_matches_type(object, execution, path=["response"])

    @parametrize
    async def test_streaming_response_stop(self, async_client: AsyncGitpod) -> None:
        async with async_client.environments.automations.tasks.executions.with_streaming_response.stop(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            execution = await response.parse()
            assert_matches_type(object, execution, path=["response"])

        assert cast(Any, response.is_closed) is True
