# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod._utils import parse_datetime
from gitpod.pagination import SyncTokensPage, AsyncTokensPage
from gitpod.types.runners.configurations import (
    HostAuthenticationToken,
    HostAuthenticationTokenCreateResponse,
    HostAuthenticationTokenRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHostAuthenticationTokens:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Gitpod) -> None:
        host_authentication_token = client.runners.configurations.host_authentication_tokens.create()
        assert_matches_type(HostAuthenticationTokenCreateResponse, host_authentication_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Gitpod) -> None:
        host_authentication_token = client.runners.configurations.host_authentication_tokens.create(
            token="x",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            host="x",
            refresh_token="refreshToken",
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            source="HOST_AUTHENTICATION_TOKEN_SOURCE_UNSPECIFIED",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(HostAuthenticationTokenCreateResponse, host_authentication_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Gitpod) -> None:
        response = client.runners.configurations.host_authentication_tokens.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        host_authentication_token = response.parse()
        assert_matches_type(HostAuthenticationTokenCreateResponse, host_authentication_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Gitpod) -> None:
        with client.runners.configurations.host_authentication_tokens.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            host_authentication_token = response.parse()
            assert_matches_type(HostAuthenticationTokenCreateResponse, host_authentication_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Gitpod) -> None:
        host_authentication_token = client.runners.configurations.host_authentication_tokens.retrieve()
        assert_matches_type(HostAuthenticationTokenRetrieveResponse, host_authentication_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Gitpod) -> None:
        host_authentication_token = client.runners.configurations.host_authentication_tokens.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(HostAuthenticationTokenRetrieveResponse, host_authentication_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Gitpod) -> None:
        response = client.runners.configurations.host_authentication_tokens.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        host_authentication_token = response.parse()
        assert_matches_type(HostAuthenticationTokenRetrieveResponse, host_authentication_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Gitpod) -> None:
        with client.runners.configurations.host_authentication_tokens.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            host_authentication_token = response.parse()
            assert_matches_type(HostAuthenticationTokenRetrieveResponse, host_authentication_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Gitpod) -> None:
        host_authentication_token = client.runners.configurations.host_authentication_tokens.update()
        assert_matches_type(object, host_authentication_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Gitpod) -> None:
        host_authentication_token = client.runners.configurations.host_authentication_tokens.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            token="x",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            refresh_token="refreshToken",
        )
        assert_matches_type(object, host_authentication_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Gitpod) -> None:
        response = client.runners.configurations.host_authentication_tokens.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        host_authentication_token = response.parse()
        assert_matches_type(object, host_authentication_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Gitpod) -> None:
        with client.runners.configurations.host_authentication_tokens.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            host_authentication_token = response.parse()
            assert_matches_type(object, host_authentication_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Gitpod) -> None:
        host_authentication_token = client.runners.configurations.host_authentication_tokens.list()
        assert_matches_type(SyncTokensPage[HostAuthenticationToken], host_authentication_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Gitpod) -> None:
        host_authentication_token = client.runners.configurations.host_authentication_tokens.list(
            token="token",
            page_size=0,
            filter={
                "runner_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "user_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            pagination={
                "token": "token",
                "page_size": 100,
            },
        )
        assert_matches_type(SyncTokensPage[HostAuthenticationToken], host_authentication_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Gitpod) -> None:
        response = client.runners.configurations.host_authentication_tokens.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        host_authentication_token = response.parse()
        assert_matches_type(SyncTokensPage[HostAuthenticationToken], host_authentication_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Gitpod) -> None:
        with client.runners.configurations.host_authentication_tokens.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            host_authentication_token = response.parse()
            assert_matches_type(SyncTokensPage[HostAuthenticationToken], host_authentication_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Gitpod) -> None:
        host_authentication_token = client.runners.configurations.host_authentication_tokens.delete()
        assert_matches_type(object, host_authentication_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_with_all_params(self, client: Gitpod) -> None:
        host_authentication_token = client.runners.configurations.host_authentication_tokens.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, host_authentication_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Gitpod) -> None:
        response = client.runners.configurations.host_authentication_tokens.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        host_authentication_token = response.parse()
        assert_matches_type(object, host_authentication_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Gitpod) -> None:
        with client.runners.configurations.host_authentication_tokens.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            host_authentication_token = response.parse()
            assert_matches_type(object, host_authentication_token, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncHostAuthenticationTokens:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncGitpod) -> None:
        host_authentication_token = await async_client.runners.configurations.host_authentication_tokens.create()
        assert_matches_type(HostAuthenticationTokenCreateResponse, host_authentication_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGitpod) -> None:
        host_authentication_token = await async_client.runners.configurations.host_authentication_tokens.create(
            token="x",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            host="x",
            refresh_token="refreshToken",
            runner_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            source="HOST_AUTHENTICATION_TOKEN_SOURCE_UNSPECIFIED",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(HostAuthenticationTokenCreateResponse, host_authentication_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runners.configurations.host_authentication_tokens.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        host_authentication_token = await response.parse()
        assert_matches_type(HostAuthenticationTokenCreateResponse, host_authentication_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGitpod) -> None:
        async with (
            async_client.runners.configurations.host_authentication_tokens.with_streaming_response.create()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            host_authentication_token = await response.parse()
            assert_matches_type(HostAuthenticationTokenCreateResponse, host_authentication_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGitpod) -> None:
        host_authentication_token = await async_client.runners.configurations.host_authentication_tokens.retrieve()
        assert_matches_type(HostAuthenticationTokenRetrieveResponse, host_authentication_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncGitpod) -> None:
        host_authentication_token = await async_client.runners.configurations.host_authentication_tokens.retrieve(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(HostAuthenticationTokenRetrieveResponse, host_authentication_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runners.configurations.host_authentication_tokens.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        host_authentication_token = await response.parse()
        assert_matches_type(HostAuthenticationTokenRetrieveResponse, host_authentication_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGitpod) -> None:
        async with (
            async_client.runners.configurations.host_authentication_tokens.with_streaming_response.retrieve()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            host_authentication_token = await response.parse()
            assert_matches_type(HostAuthenticationTokenRetrieveResponse, host_authentication_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncGitpod) -> None:
        host_authentication_token = await async_client.runners.configurations.host_authentication_tokens.update()
        assert_matches_type(object, host_authentication_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGitpod) -> None:
        host_authentication_token = await async_client.runners.configurations.host_authentication_tokens.update(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            token="x",
            expires_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            refresh_token="refreshToken",
        )
        assert_matches_type(object, host_authentication_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runners.configurations.host_authentication_tokens.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        host_authentication_token = await response.parse()
        assert_matches_type(object, host_authentication_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGitpod) -> None:
        async with (
            async_client.runners.configurations.host_authentication_tokens.with_streaming_response.update()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            host_authentication_token = await response.parse()
            assert_matches_type(object, host_authentication_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncGitpod) -> None:
        host_authentication_token = await async_client.runners.configurations.host_authentication_tokens.list()
        assert_matches_type(AsyncTokensPage[HostAuthenticationToken], host_authentication_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGitpod) -> None:
        host_authentication_token = await async_client.runners.configurations.host_authentication_tokens.list(
            token="token",
            page_size=0,
            filter={
                "runner_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "user_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            pagination={
                "token": "token",
                "page_size": 100,
            },
        )
        assert_matches_type(AsyncTokensPage[HostAuthenticationToken], host_authentication_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runners.configurations.host_authentication_tokens.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        host_authentication_token = await response.parse()
        assert_matches_type(AsyncTokensPage[HostAuthenticationToken], host_authentication_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGitpod) -> None:
        async with (
            async_client.runners.configurations.host_authentication_tokens.with_streaming_response.list()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            host_authentication_token = await response.parse()
            assert_matches_type(AsyncTokensPage[HostAuthenticationToken], host_authentication_token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncGitpod) -> None:
        host_authentication_token = await async_client.runners.configurations.host_authentication_tokens.delete()
        assert_matches_type(object, host_authentication_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncGitpod) -> None:
        host_authentication_token = await async_client.runners.configurations.host_authentication_tokens.delete(
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, host_authentication_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGitpod) -> None:
        response = await async_client.runners.configurations.host_authentication_tokens.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        host_authentication_token = await response.parse()
        assert_matches_type(object, host_authentication_token, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGitpod) -> None:
        async with (
            async_client.runners.configurations.host_authentication_tokens.with_streaming_response.delete()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            host_authentication_token = await response.parse()
            assert_matches_type(object, host_authentication_token, path=["response"])

        assert cast(Any, response.is_closed) is True
