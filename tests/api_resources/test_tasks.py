# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.types import (
    TaskCreateResponse,
    TaskRetrieveResponse,
    TaskRetrieveCreateResponse,
)
from gitpod._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTasks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gitpod) -> None:
        task = client.tasks.create(
            connect_protocol_version=1,
        )
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gitpod) -> None:
        task = client.tasks.create(
            connect_protocol_version=1,
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
                "triggered_by": [
                    {
                        "manual": True,
                        "postDevcontainerStart": True,
                        "postEnvironmentStart": True,
                    }
                ],
            },
            spec={"command": "command"},
            connect_timeout_ms=0,
        )
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gitpod) -> None:
        response = client.tasks.with_raw_response.create(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gitpod) -> None:
        with client.tasks.with_streaming_response.create(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskCreateResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Gitpod) -> None:
        task = client.tasks.retrieve(
            connect_protocol_version=1,
        )
        assert_matches_type(TaskRetrieveResponse, task, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Gitpod) -> None:
        task = client.tasks.retrieve(
            connect_protocol_version=1,
            base64="base64",
            compression="compression",
            connect="connect",
            encoding="encoding",
            message="message",
            connect_timeout_ms=0,
        )
        assert_matches_type(TaskRetrieveResponse, task, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Gitpod) -> None:
        response = client.tasks.with_raw_response.retrieve(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskRetrieveResponse, task, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Gitpod) -> None:
        with client.tasks.with_streaming_response.retrieve(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskRetrieveResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_create(self, client: Gitpod) -> None:
        task = client.tasks.retrieve_create(
            connect_protocol_version=1,
        )
        assert_matches_type(TaskRetrieveCreateResponse, task, path=["response"])

    @parametrize
    def test_method_retrieve_create_with_all_params(self, client: Gitpod) -> None:
        task = client.tasks.retrieve_create(
            connect_protocol_version=1,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(TaskRetrieveCreateResponse, task, path=["response"])

    @parametrize
    def test_raw_response_retrieve_create(self, client: Gitpod) -> None:
        response = client.tasks.with_raw_response.retrieve_create(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = response.parse()
        assert_matches_type(TaskRetrieveCreateResponse, task, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_create(self, client: Gitpod) -> None:
        with client.tasks.with_streaming_response.retrieve_create(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = response.parse()
            assert_matches_type(TaskRetrieveCreateResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTasks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncGitpod) -> None:
        task = await async_client.tasks.create(
            connect_protocol_version=1,
        )
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGitpod) -> None:
        task = await async_client.tasks.create(
            connect_protocol_version=1,
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
                "triggered_by": [
                    {
                        "manual": True,
                        "postDevcontainerStart": True,
                        "postEnvironmentStart": True,
                    }
                ],
            },
            spec={"command": "command"},
            connect_timeout_ms=0,
        )
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGitpod) -> None:
        response = await async_client.tasks.with_raw_response.create(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskCreateResponse, task, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGitpod) -> None:
        async with async_client.tasks.with_streaming_response.create(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskCreateResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGitpod) -> None:
        task = await async_client.tasks.retrieve(
            connect_protocol_version=1,
        )
        assert_matches_type(TaskRetrieveResponse, task, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncGitpod) -> None:
        task = await async_client.tasks.retrieve(
            connect_protocol_version=1,
            base64="base64",
            compression="compression",
            connect="connect",
            encoding="encoding",
            message="message",
            connect_timeout_ms=0,
        )
        assert_matches_type(TaskRetrieveResponse, task, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGitpod) -> None:
        response = await async_client.tasks.with_raw_response.retrieve(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskRetrieveResponse, task, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGitpod) -> None:
        async with async_client.tasks.with_streaming_response.retrieve(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskRetrieveResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_create(self, async_client: AsyncGitpod) -> None:
        task = await async_client.tasks.retrieve_create(
            connect_protocol_version=1,
        )
        assert_matches_type(TaskRetrieveCreateResponse, task, path=["response"])

    @parametrize
    async def test_method_retrieve_create_with_all_params(self, async_client: AsyncGitpod) -> None:
        task = await async_client.tasks.retrieve_create(
            connect_protocol_version=1,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(TaskRetrieveCreateResponse, task, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_create(self, async_client: AsyncGitpod) -> None:
        response = await async_client.tasks.with_raw_response.retrieve_create(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        task = await response.parse()
        assert_matches_type(TaskRetrieveCreateResponse, task, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_create(self, async_client: AsyncGitpod) -> None:
        async with async_client.tasks.with_streaming_response.retrieve_create(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            task = await response.parse()
            assert_matches_type(TaskRetrieveCreateResponse, task, path=["response"])

        assert cast(Any, response.is_closed) is True
