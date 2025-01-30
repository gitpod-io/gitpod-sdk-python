# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.types import (
    IdentityGetIDTokenResponse,
    IdentityExchangeTokenResponse,
    IdentityGetAuthenticatedIdentityResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIdentity:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_exchange_token(self, client: Gitpod) -> None:
        identity = client.identity.exchange_token(
            connect_protocol_version=1,
        )
        assert_matches_type(IdentityExchangeTokenResponse, identity, path=["response"])

    @parametrize
    def test_method_exchange_token_with_all_params(self, client: Gitpod) -> None:
        identity = client.identity.exchange_token(
            connect_protocol_version=1,
            exchange_token="exchangeToken",
            connect_timeout_ms=0,
        )
        assert_matches_type(IdentityExchangeTokenResponse, identity, path=["response"])

    @parametrize
    def test_raw_response_exchange_token(self, client: Gitpod) -> None:
        response = client.identity.with_raw_response.exchange_token(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity = response.parse()
        assert_matches_type(IdentityExchangeTokenResponse, identity, path=["response"])

    @parametrize
    def test_streaming_response_exchange_token(self, client: Gitpod) -> None:
        with client.identity.with_streaming_response.exchange_token(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity = response.parse()
            assert_matches_type(IdentityExchangeTokenResponse, identity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_authenticated_identity(self, client: Gitpod) -> None:
        identity = client.identity.get_authenticated_identity(
            encoding="proto",
            connect_protocol_version=1,
        )
        assert_matches_type(IdentityGetAuthenticatedIdentityResponse, identity, path=["response"])

    @parametrize
    def test_method_get_authenticated_identity_with_all_params(self, client: Gitpod) -> None:
        identity = client.identity.get_authenticated_identity(
            encoding="proto",
            connect_protocol_version=1,
            base64=True,
            compression="identity",
            connect="v1",
            message="message",
            connect_timeout_ms=0,
        )
        assert_matches_type(IdentityGetAuthenticatedIdentityResponse, identity, path=["response"])

    @parametrize
    def test_raw_response_get_authenticated_identity(self, client: Gitpod) -> None:
        response = client.identity.with_raw_response.get_authenticated_identity(
            encoding="proto",
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity = response.parse()
        assert_matches_type(IdentityGetAuthenticatedIdentityResponse, identity, path=["response"])

    @parametrize
    def test_streaming_response_get_authenticated_identity(self, client: Gitpod) -> None:
        with client.identity.with_streaming_response.get_authenticated_identity(
            encoding="proto",
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity = response.parse()
            assert_matches_type(IdentityGetAuthenticatedIdentityResponse, identity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_id_token(self, client: Gitpod) -> None:
        identity = client.identity.get_id_token(
            connect_protocol_version=1,
        )
        assert_matches_type(IdentityGetIDTokenResponse, identity, path=["response"])

    @parametrize
    def test_method_get_id_token_with_all_params(self, client: Gitpod) -> None:
        identity = client.identity.get_id_token(
            connect_protocol_version=1,
            audience=["string"],
            connect_timeout_ms=0,
        )
        assert_matches_type(IdentityGetIDTokenResponse, identity, path=["response"])

    @parametrize
    def test_raw_response_get_id_token(self, client: Gitpod) -> None:
        response = client.identity.with_raw_response.get_id_token(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity = response.parse()
        assert_matches_type(IdentityGetIDTokenResponse, identity, path=["response"])

    @parametrize
    def test_streaming_response_get_id_token(self, client: Gitpod) -> None:
        with client.identity.with_streaming_response.get_id_token(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity = response.parse()
            assert_matches_type(IdentityGetIDTokenResponse, identity, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncIdentity:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_exchange_token(self, async_client: AsyncGitpod) -> None:
        identity = await async_client.identity.exchange_token(
            connect_protocol_version=1,
        )
        assert_matches_type(IdentityExchangeTokenResponse, identity, path=["response"])

    @parametrize
    async def test_method_exchange_token_with_all_params(self, async_client: AsyncGitpod) -> None:
        identity = await async_client.identity.exchange_token(
            connect_protocol_version=1,
            exchange_token="exchangeToken",
            connect_timeout_ms=0,
        )
        assert_matches_type(IdentityExchangeTokenResponse, identity, path=["response"])

    @parametrize
    async def test_raw_response_exchange_token(self, async_client: AsyncGitpod) -> None:
        response = await async_client.identity.with_raw_response.exchange_token(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity = await response.parse()
        assert_matches_type(IdentityExchangeTokenResponse, identity, path=["response"])

    @parametrize
    async def test_streaming_response_exchange_token(self, async_client: AsyncGitpod) -> None:
        async with async_client.identity.with_streaming_response.exchange_token(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity = await response.parse()
            assert_matches_type(IdentityExchangeTokenResponse, identity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_authenticated_identity(self, async_client: AsyncGitpod) -> None:
        identity = await async_client.identity.get_authenticated_identity(
            encoding="proto",
            connect_protocol_version=1,
        )
        assert_matches_type(IdentityGetAuthenticatedIdentityResponse, identity, path=["response"])

    @parametrize
    async def test_method_get_authenticated_identity_with_all_params(self, async_client: AsyncGitpod) -> None:
        identity = await async_client.identity.get_authenticated_identity(
            encoding="proto",
            connect_protocol_version=1,
            base64=True,
            compression="identity",
            connect="v1",
            message="message",
            connect_timeout_ms=0,
        )
        assert_matches_type(IdentityGetAuthenticatedIdentityResponse, identity, path=["response"])

    @parametrize
    async def test_raw_response_get_authenticated_identity(self, async_client: AsyncGitpod) -> None:
        response = await async_client.identity.with_raw_response.get_authenticated_identity(
            encoding="proto",
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity = await response.parse()
        assert_matches_type(IdentityGetAuthenticatedIdentityResponse, identity, path=["response"])

    @parametrize
    async def test_streaming_response_get_authenticated_identity(self, async_client: AsyncGitpod) -> None:
        async with async_client.identity.with_streaming_response.get_authenticated_identity(
            encoding="proto",
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity = await response.parse()
            assert_matches_type(IdentityGetAuthenticatedIdentityResponse, identity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_id_token(self, async_client: AsyncGitpod) -> None:
        identity = await async_client.identity.get_id_token(
            connect_protocol_version=1,
        )
        assert_matches_type(IdentityGetIDTokenResponse, identity, path=["response"])

    @parametrize
    async def test_method_get_id_token_with_all_params(self, async_client: AsyncGitpod) -> None:
        identity = await async_client.identity.get_id_token(
            connect_protocol_version=1,
            audience=["string"],
            connect_timeout_ms=0,
        )
        assert_matches_type(IdentityGetIDTokenResponse, identity, path=["response"])

    @parametrize
    async def test_raw_response_get_id_token(self, async_client: AsyncGitpod) -> None:
        response = await async_client.identity.with_raw_response.get_id_token(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        identity = await response.parse()
        assert_matches_type(IdentityGetIDTokenResponse, identity, path=["response"])

    @parametrize
    async def test_streaming_response_get_id_token(self, async_client: AsyncGitpod) -> None:
        async with async_client.identity.with_streaming_response.get_id_token(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            identity = await response.parse()
            assert_matches_type(IdentityGetIDTokenResponse, identity, path=["response"])

        assert cast(Any, response.is_closed) is True
