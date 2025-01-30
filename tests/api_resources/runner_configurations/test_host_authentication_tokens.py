# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod._utils import parse_datetime
from gitpod.types.runner_configurations import (
    HostAuthenticationTokenListResponse,
    HostAuthenticationTokenCreateResponse,
    HostAuthenticationTokenRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHostAuthenticationTokens:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gitpod) -> None:
        host_authentication_token = client.runner_configurations.host_authentication_tokens.create(
            connect_protocol_version=1,
        )
        assert_matches_type(HostAuthenticationTokenCreateResponse, host_authentication_token, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gitpod) -> None:
        host_authentication_token = client.runner_configurations.host_authentication_tokens.create(
            connect_protocol_version=1,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(HostAuthenticationTokenCreateResponse, host_authentication_token, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gitpod) -> None:
        response = client.runner_configurations.host_authentication_tokens.with_raw_response.create(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        host_authentication_token = response.parse()
        assert_matches_type(HostAuthenticationTokenCreateResponse, host_authentication_token, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gitpod) -> None:
        with client.runner_configurations.host_authentication_tokens.with_streaming_response.create(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            host_authentication_token = response.parse()
            assert_matches_type(HostAuthenticationTokenCreateResponse, host_authentication_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Gitpod) -> None:
        host_authentication_token = client.runner_configurations.host_authentication_tokens.retrieve(
            connect_protocol_version=1,
        )
        assert_matches_type(HostAuthenticationTokenRetrieveResponse, host_authentication_token, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Gitpod) -> None:
        host_authentication_token = client.runner_configurations.host_authentication_tokens.retrieve(
            connect_protocol_version=1,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(HostAuthenticationTokenRetrieveResponse, host_authentication_token, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Gitpod) -> None:
        response = client.runner_configurations.host_authentication_tokens.with_raw_response.retrieve(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        host_authentication_token = response.parse()
        assert_matches_type(HostAuthenticationTokenRetrieveResponse, host_authentication_token, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Gitpod) -> None:
        with client.runner_configurations.host_authentication_tokens.with_streaming_response.retrieve(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            host_authentication_token = response.parse()
            assert_matches_type(HostAuthenticationTokenRetrieveResponse, host_authentication_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_overload_1(self, client: Gitpod) -> None:
        host_authentication_token = client.runner_configurations.host_authentication_tokens.update(
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            connect_protocol_version=1,
        )
        assert_matches_type(object, host_authentication_token, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_1(self, client: Gitpod) -> None:
        host_authentication_token = client.runner_configurations.host_authentication_tokens.update(
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            connect_protocol_version=1,
            connect_timeout_ms=0,
        )
        assert_matches_type(object, host_authentication_token, path=["response"])

    @parametrize
    def test_raw_response_update_overload_1(self, client: Gitpod) -> None:
        response = client.runner_configurations.host_authentication_tokens.with_raw_response.update(
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        host_authentication_token = response.parse()
        assert_matches_type(object, host_authentication_token, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_1(self, client: Gitpod) -> None:
        with client.runner_configurations.host_authentication_tokens.with_streaming_response.update(
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            host_authentication_token = response.parse()
            assert_matches_type(object, host_authentication_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_overload_2(self, client: Gitpod) -> None:
        host_authentication_token = client.runner_configurations.host_authentication_tokens.update(
            refresh_token="refreshToken",
            connect_protocol_version=1,
        )
        assert_matches_type(object, host_authentication_token, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_2(self, client: Gitpod) -> None:
        host_authentication_token = client.runner_configurations.host_authentication_tokens.update(
            refresh_token="refreshToken",
            connect_protocol_version=1,
            connect_timeout_ms=0,
        )
        assert_matches_type(object, host_authentication_token, path=["response"])

    @parametrize
    def test_raw_response_update_overload_2(self, client: Gitpod) -> None:
        response = client.runner_configurations.host_authentication_tokens.with_raw_response.update(
            refresh_token="refreshToken",
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        host_authentication_token = response.parse()
        assert_matches_type(object, host_authentication_token, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_2(self, client: Gitpod) -> None:
        with client.runner_configurations.host_authentication_tokens.with_streaming_response.update(
            refresh_token="refreshToken",
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            host_authentication_token = response.parse()
            assert_matches_type(object, host_authentication_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_overload_3(self, client: Gitpod) -> None:
        host_authentication_token = client.runner_configurations.host_authentication_tokens.update(
            token="x",
            connect_protocol_version=1,
        )
        assert_matches_type(object, host_authentication_token, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_3(self, client: Gitpod) -> None:
        host_authentication_token = client.runner_configurations.host_authentication_tokens.update(
            token="x",
            connect_protocol_version=1,
            connect_timeout_ms=0,
        )
        assert_matches_type(object, host_authentication_token, path=["response"])

    @parametrize
    def test_raw_response_update_overload_3(self, client: Gitpod) -> None:
        response = client.runner_configurations.host_authentication_tokens.with_raw_response.update(
            token="x",
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        host_authentication_token = response.parse()
        assert_matches_type(object, host_authentication_token, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_3(self, client: Gitpod) -> None:
        with client.runner_configurations.host_authentication_tokens.with_streaming_response.update(
            token="x",
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            host_authentication_token = response.parse()
            assert_matches_type(object, host_authentication_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gitpod) -> None:
        host_authentication_token = client.runner_configurations.host_authentication_tokens.list(
            connect_protocol_version=1,
        )
        assert_matches_type(HostAuthenticationTokenListResponse, host_authentication_token, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gitpod) -> None:
        host_authentication_token = client.runner_configurations.host_authentication_tokens.list(
            connect_protocol_version=1,
            filter={"runner_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            pagination={
                "token": "token",
                "page_size": 100,
            },
            connect_timeout_ms=0,
        )
        assert_matches_type(HostAuthenticationTokenListResponse, host_authentication_token, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gitpod) -> None:
        response = client.runner_configurations.host_authentication_tokens.with_raw_response.list(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        host_authentication_token = response.parse()
        assert_matches_type(HostAuthenticationTokenListResponse, host_authentication_token, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gitpod) -> None:
        with client.runner_configurations.host_authentication_tokens.with_streaming_response.list(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            host_authentication_token = response.parse()
            assert_matches_type(HostAuthenticationTokenListResponse, host_authentication_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gitpod) -> None:
        host_authentication_token = client.runner_configurations.host_authentication_tokens.delete(
            connect_protocol_version=1,
        )
        assert_matches_type(object, host_authentication_token, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Gitpod) -> None:
        host_authentication_token = client.runner_configurations.host_authentication_tokens.delete(
            connect_protocol_version=1,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(object, host_authentication_token, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gitpod) -> None:
        response = client.runner_configurations.host_authentication_tokens.with_raw_response.delete(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        host_authentication_token = response.parse()
        assert_matches_type(object, host_authentication_token, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gitpod) -> None:
        with client.runner_configurations.host_authentication_tokens.with_streaming_response.delete(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            host_authentication_token = response.parse()
            assert_matches_type(object, host_authentication_token, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncHostAuthenticationTokens:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncGitpod) -> None:
        host_authentication_token = await async_client.runner_configurations.host_authentication_tokens.create(
            connect_protocol_version=1,
        )
        assert_matches_type(HostAuthenticationTokenCreateResponse, host_authentication_token, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGitpod) -> None:
        host_authentication_token = await async_client.runner_configurations.host_authentication_tokens.create(
            connect_protocol_version=1,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(HostAuthenticationTokenCreateResponse, host_authentication_token, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runner_configurations.host_authentication_tokens.with_raw_response.create(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        host_authentication_token = await response.parse()
        assert_matches_type(HostAuthenticationTokenCreateResponse, host_authentication_token, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGitpod) -> None:
        async with async_client.runner_configurations.host_authentication_tokens.with_streaming_response.create(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            host_authentication_token = await response.parse()
            assert_matches_type(HostAuthenticationTokenCreateResponse, host_authentication_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGitpod) -> None:
        host_authentication_token = await async_client.runner_configurations.host_authentication_tokens.retrieve(
            connect_protocol_version=1,
        )
        assert_matches_type(HostAuthenticationTokenRetrieveResponse, host_authentication_token, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncGitpod) -> None:
        host_authentication_token = await async_client.runner_configurations.host_authentication_tokens.retrieve(
            connect_protocol_version=1,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(HostAuthenticationTokenRetrieveResponse, host_authentication_token, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runner_configurations.host_authentication_tokens.with_raw_response.retrieve(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        host_authentication_token = await response.parse()
        assert_matches_type(HostAuthenticationTokenRetrieveResponse, host_authentication_token, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGitpod) -> None:
        async with async_client.runner_configurations.host_authentication_tokens.with_streaming_response.retrieve(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            host_authentication_token = await response.parse()
            assert_matches_type(HostAuthenticationTokenRetrieveResponse, host_authentication_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncGitpod) -> None:
        host_authentication_token = await async_client.runner_configurations.host_authentication_tokens.update(
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            connect_protocol_version=1,
        )
        assert_matches_type(object, host_authentication_token, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_1(self, async_client: AsyncGitpod) -> None:
        host_authentication_token = await async_client.runner_configurations.host_authentication_tokens.update(
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            connect_protocol_version=1,
            connect_timeout_ms=0,
        )
        assert_matches_type(object, host_authentication_token, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runner_configurations.host_authentication_tokens.with_raw_response.update(
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        host_authentication_token = await response.parse()
        assert_matches_type(object, host_authentication_token, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncGitpod) -> None:
        async with async_client.runner_configurations.host_authentication_tokens.with_streaming_response.update(
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            host_authentication_token = await response.parse()
            assert_matches_type(object, host_authentication_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncGitpod) -> None:
        host_authentication_token = await async_client.runner_configurations.host_authentication_tokens.update(
            refresh_token="refreshToken",
            connect_protocol_version=1,
        )
        assert_matches_type(object, host_authentication_token, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_2(self, async_client: AsyncGitpod) -> None:
        host_authentication_token = await async_client.runner_configurations.host_authentication_tokens.update(
            refresh_token="refreshToken",
            connect_protocol_version=1,
            connect_timeout_ms=0,
        )
        assert_matches_type(object, host_authentication_token, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runner_configurations.host_authentication_tokens.with_raw_response.update(
            refresh_token="refreshToken",
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        host_authentication_token = await response.parse()
        assert_matches_type(object, host_authentication_token, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncGitpod) -> None:
        async with async_client.runner_configurations.host_authentication_tokens.with_streaming_response.update(
            refresh_token="refreshToken",
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            host_authentication_token = await response.parse()
            assert_matches_type(object, host_authentication_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_overload_3(self, async_client: AsyncGitpod) -> None:
        host_authentication_token = await async_client.runner_configurations.host_authentication_tokens.update(
            token="x",
            connect_protocol_version=1,
        )
        assert_matches_type(object, host_authentication_token, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_3(self, async_client: AsyncGitpod) -> None:
        host_authentication_token = await async_client.runner_configurations.host_authentication_tokens.update(
            token="x",
            connect_protocol_version=1,
            connect_timeout_ms=0,
        )
        assert_matches_type(object, host_authentication_token, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_3(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runner_configurations.host_authentication_tokens.with_raw_response.update(
            token="x",
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        host_authentication_token = await response.parse()
        assert_matches_type(object, host_authentication_token, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_3(self, async_client: AsyncGitpod) -> None:
        async with async_client.runner_configurations.host_authentication_tokens.with_streaming_response.update(
            token="x",
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            host_authentication_token = await response.parse()
            assert_matches_type(object, host_authentication_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGitpod) -> None:
        host_authentication_token = await async_client.runner_configurations.host_authentication_tokens.list(
            connect_protocol_version=1,
        )
        assert_matches_type(HostAuthenticationTokenListResponse, host_authentication_token, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGitpod) -> None:
        host_authentication_token = await async_client.runner_configurations.host_authentication_tokens.list(
            connect_protocol_version=1,
            filter={"runner_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"},
            pagination={
                "token": "token",
                "page_size": 100,
            },
            connect_timeout_ms=0,
        )
        assert_matches_type(HostAuthenticationTokenListResponse, host_authentication_token, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runner_configurations.host_authentication_tokens.with_raw_response.list(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        host_authentication_token = await response.parse()
        assert_matches_type(HostAuthenticationTokenListResponse, host_authentication_token, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGitpod) -> None:
        async with async_client.runner_configurations.host_authentication_tokens.with_streaming_response.list(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            host_authentication_token = await response.parse()
            assert_matches_type(HostAuthenticationTokenListResponse, host_authentication_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGitpod) -> None:
        host_authentication_token = await async_client.runner_configurations.host_authentication_tokens.delete(
            connect_protocol_version=1,
        )
        assert_matches_type(object, host_authentication_token, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncGitpod) -> None:
        host_authentication_token = await async_client.runner_configurations.host_authentication_tokens.delete(
            connect_protocol_version=1,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(object, host_authentication_token, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runner_configurations.host_authentication_tokens.with_raw_response.delete(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        host_authentication_token = await response.parse()
        assert_matches_type(object, host_authentication_token, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGitpod) -> None:
        async with async_client.runner_configurations.host_authentication_tokens.with_streaming_response.delete(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            host_authentication_token = await response.parse()
            assert_matches_type(object, host_authentication_token, path=["response"])

        assert cast(Any, response.is_closed) is True
