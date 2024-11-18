# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.types import (
    ServiceListResponse,
    ServiceListCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestServices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Gitpod) -> None:
        service = client.services.update(
            connect_protocol_version=1,
        )
        assert_matches_type(object, service, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gitpod) -> None:
        service = client.services.update(
            connect_protocol_version=1,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata={},
            spec={},
            status={},
            connect_timeout_ms=0,
        )
        assert_matches_type(object, service, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gitpod) -> None:
        response = client.services.with_raw_response.update(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = response.parse()
        assert_matches_type(object, service, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gitpod) -> None:
        with client.services.with_streaming_response.update(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = response.parse()
            assert_matches_type(object, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gitpod) -> None:
        service = client.services.list(
            connect_protocol_version=1,
        )
        assert_matches_type(ServiceListResponse, service, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gitpod) -> None:
        service = client.services.list(
            connect_protocol_version=1,
            base64="base64",
            compression="compression",
            connect="connect",
            encoding="encoding",
            message="message",
            connect_timeout_ms=0,
        )
        assert_matches_type(ServiceListResponse, service, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gitpod) -> None:
        response = client.services.with_raw_response.list(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = response.parse()
        assert_matches_type(ServiceListResponse, service, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gitpod) -> None:
        with client.services.with_streaming_response.list(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = response.parse()
            assert_matches_type(ServiceListResponse, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gitpod) -> None:
        service = client.services.delete(
            connect_protocol_version=1,
        )
        assert_matches_type(object, service, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Gitpod) -> None:
        service = client.services.delete(
            connect_protocol_version=1,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            force=True,
            connect_timeout_ms=0,
        )
        assert_matches_type(object, service, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gitpod) -> None:
        response = client.services.with_raw_response.delete(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = response.parse()
        assert_matches_type(object, service, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gitpod) -> None:
        with client.services.with_streaming_response.delete(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = response.parse()
            assert_matches_type(object, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_create(self, client: Gitpod) -> None:
        service = client.services.list_create(
            connect_protocol_version=1,
        )
        assert_matches_type(ServiceListCreateResponse, service, path=["response"])

    @parametrize
    def test_method_list_create_with_all_params(self, client: Gitpod) -> None:
        service = client.services.list_create(
            connect_protocol_version=1,
            filter={
                "environment_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "references": ["x"],
                "service_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            },
            pagination={
                "token": "token",
                "page_size": 0,
            },
            connect_timeout_ms=0,
        )
        assert_matches_type(ServiceListCreateResponse, service, path=["response"])

    @parametrize
    def test_raw_response_list_create(self, client: Gitpod) -> None:
        response = client.services.with_raw_response.list_create(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = response.parse()
        assert_matches_type(ServiceListCreateResponse, service, path=["response"])

    @parametrize
    def test_streaming_response_list_create(self, client: Gitpod) -> None:
        with client.services.with_streaming_response.list_create(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = response.parse()
            assert_matches_type(ServiceListCreateResponse, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_start(self, client: Gitpod) -> None:
        service = client.services.start(
            connect_protocol_version=1,
        )
        assert_matches_type(object, service, path=["response"])

    @parametrize
    def test_method_start_with_all_params(self, client: Gitpod) -> None:
        service = client.services.start(
            connect_protocol_version=1,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(object, service, path=["response"])

    @parametrize
    def test_raw_response_start(self, client: Gitpod) -> None:
        response = client.services.with_raw_response.start(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = response.parse()
        assert_matches_type(object, service, path=["response"])

    @parametrize
    def test_streaming_response_start(self, client: Gitpod) -> None:
        with client.services.with_streaming_response.start(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = response.parse()
            assert_matches_type(object, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_stop(self, client: Gitpod) -> None:
        service = client.services.stop(
            connect_protocol_version=1,
        )
        assert_matches_type(object, service, path=["response"])

    @parametrize
    def test_method_stop_with_all_params(self, client: Gitpod) -> None:
        service = client.services.stop(
            connect_protocol_version=1,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(object, service, path=["response"])

    @parametrize
    def test_raw_response_stop(self, client: Gitpod) -> None:
        response = client.services.with_raw_response.stop(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = response.parse()
        assert_matches_type(object, service, path=["response"])

    @parametrize
    def test_streaming_response_stop(self, client: Gitpod) -> None:
        with client.services.with_streaming_response.stop(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = response.parse()
            assert_matches_type(object, service, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncServices:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncGitpod) -> None:
        service = await async_client.services.update(
            connect_protocol_version=1,
        )
        assert_matches_type(object, service, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGitpod) -> None:
        service = await async_client.services.update(
            connect_protocol_version=1,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata={},
            spec={},
            status={},
            connect_timeout_ms=0,
        )
        assert_matches_type(object, service, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGitpod) -> None:
        response = await async_client.services.with_raw_response.update(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = await response.parse()
        assert_matches_type(object, service, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGitpod) -> None:
        async with async_client.services.with_streaming_response.update(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = await response.parse()
            assert_matches_type(object, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGitpod) -> None:
        service = await async_client.services.list(
            connect_protocol_version=1,
        )
        assert_matches_type(ServiceListResponse, service, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGitpod) -> None:
        service = await async_client.services.list(
            connect_protocol_version=1,
            base64="base64",
            compression="compression",
            connect="connect",
            encoding="encoding",
            message="message",
            connect_timeout_ms=0,
        )
        assert_matches_type(ServiceListResponse, service, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGitpod) -> None:
        response = await async_client.services.with_raw_response.list(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = await response.parse()
        assert_matches_type(ServiceListResponse, service, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGitpod) -> None:
        async with async_client.services.with_streaming_response.list(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = await response.parse()
            assert_matches_type(ServiceListResponse, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGitpod) -> None:
        service = await async_client.services.delete(
            connect_protocol_version=1,
        )
        assert_matches_type(object, service, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncGitpod) -> None:
        service = await async_client.services.delete(
            connect_protocol_version=1,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            force=True,
            connect_timeout_ms=0,
        )
        assert_matches_type(object, service, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGitpod) -> None:
        response = await async_client.services.with_raw_response.delete(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = await response.parse()
        assert_matches_type(object, service, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGitpod) -> None:
        async with async_client.services.with_streaming_response.delete(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = await response.parse()
            assert_matches_type(object, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_create(self, async_client: AsyncGitpod) -> None:
        service = await async_client.services.list_create(
            connect_protocol_version=1,
        )
        assert_matches_type(ServiceListCreateResponse, service, path=["response"])

    @parametrize
    async def test_method_list_create_with_all_params(self, async_client: AsyncGitpod) -> None:
        service = await async_client.services.list_create(
            connect_protocol_version=1,
            filter={
                "environment_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "references": ["x"],
                "service_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            },
            pagination={
                "token": "token",
                "page_size": 0,
            },
            connect_timeout_ms=0,
        )
        assert_matches_type(ServiceListCreateResponse, service, path=["response"])

    @parametrize
    async def test_raw_response_list_create(self, async_client: AsyncGitpod) -> None:
        response = await async_client.services.with_raw_response.list_create(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = await response.parse()
        assert_matches_type(ServiceListCreateResponse, service, path=["response"])

    @parametrize
    async def test_streaming_response_list_create(self, async_client: AsyncGitpod) -> None:
        async with async_client.services.with_streaming_response.list_create(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = await response.parse()
            assert_matches_type(ServiceListCreateResponse, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_start(self, async_client: AsyncGitpod) -> None:
        service = await async_client.services.start(
            connect_protocol_version=1,
        )
        assert_matches_type(object, service, path=["response"])

    @parametrize
    async def test_method_start_with_all_params(self, async_client: AsyncGitpod) -> None:
        service = await async_client.services.start(
            connect_protocol_version=1,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(object, service, path=["response"])

    @parametrize
    async def test_raw_response_start(self, async_client: AsyncGitpod) -> None:
        response = await async_client.services.with_raw_response.start(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = await response.parse()
        assert_matches_type(object, service, path=["response"])

    @parametrize
    async def test_streaming_response_start(self, async_client: AsyncGitpod) -> None:
        async with async_client.services.with_streaming_response.start(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = await response.parse()
            assert_matches_type(object, service, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_stop(self, async_client: AsyncGitpod) -> None:
        service = await async_client.services.stop(
            connect_protocol_version=1,
        )
        assert_matches_type(object, service, path=["response"])

    @parametrize
    async def test_method_stop_with_all_params(self, async_client: AsyncGitpod) -> None:
        service = await async_client.services.stop(
            connect_protocol_version=1,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(object, service, path=["response"])

    @parametrize
    async def test_raw_response_stop(self, async_client: AsyncGitpod) -> None:
        response = await async_client.services.with_raw_response.stop(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        service = await response.parse()
        assert_matches_type(object, service, path=["response"])

    @parametrize
    async def test_streaming_response_stop(self, async_client: AsyncGitpod) -> None:
        async with async_client.services.with_streaming_response.stop(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            service = await response.parse()
            assert_matches_type(object, service, path=["response"])

        assert cast(Any, response.is_closed) is True
