# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.types import (
    AccountRetrieveResponse,
    AccountGetSSOLoginURLResponse,
    AccountListLoginProvidersResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Gitpod) -> None:
        account = client.accounts.retrieve(
            encoding="proto",
            connect_protocol_version=1,
        )
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Gitpod) -> None:
        account = client.accounts.retrieve(
            encoding="proto",
            connect_protocol_version=1,
            base64=True,
            compression="identity",
            connect="v1",
            message="message",
            connect_timeout_ms=0,
        )
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Gitpod) -> None:
        response = client.accounts.with_raw_response.retrieve(
            encoding="proto",
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Gitpod) -> None:
        with client.accounts.with_streaming_response.retrieve(
            encoding="proto",
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountRetrieveResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gitpod) -> None:
        account = client.accounts.delete(
            connect_protocol_version=1,
        )
        assert_matches_type(object, account, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Gitpod) -> None:
        account = client.accounts.delete(
            connect_protocol_version=1,
            account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(object, account, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gitpod) -> None:
        response = client.accounts.with_raw_response.delete(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(object, account, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gitpod) -> None:
        with client.accounts.with_streaming_response.delete(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(object, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_sso_login_url(self, client: Gitpod) -> None:
        account = client.accounts.get_sso_login_url(
            encoding="proto",
            connect_protocol_version=1,
        )
        assert_matches_type(AccountGetSSOLoginURLResponse, account, path=["response"])

    @parametrize
    def test_method_get_sso_login_url_with_all_params(self, client: Gitpod) -> None:
        account = client.accounts.get_sso_login_url(
            encoding="proto",
            connect_protocol_version=1,
            base64=True,
            compression="identity",
            connect="v1",
            message="message",
            connect_timeout_ms=0,
        )
        assert_matches_type(AccountGetSSOLoginURLResponse, account, path=["response"])

    @parametrize
    def test_raw_response_get_sso_login_url(self, client: Gitpod) -> None:
        response = client.accounts.with_raw_response.get_sso_login_url(
            encoding="proto",
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountGetSSOLoginURLResponse, account, path=["response"])

    @parametrize
    def test_streaming_response_get_sso_login_url(self, client: Gitpod) -> None:
        with client.accounts.with_streaming_response.get_sso_login_url(
            encoding="proto",
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountGetSSOLoginURLResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_login_providers(self, client: Gitpod) -> None:
        account = client.accounts.list_login_providers(
            encoding="proto",
            connect_protocol_version=1,
        )
        assert_matches_type(AccountListLoginProvidersResponse, account, path=["response"])

    @parametrize
    def test_method_list_login_providers_with_all_params(self, client: Gitpod) -> None:
        account = client.accounts.list_login_providers(
            encoding="proto",
            connect_protocol_version=1,
            base64=True,
            compression="identity",
            connect="v1",
            message="message",
            connect_timeout_ms=0,
        )
        assert_matches_type(AccountListLoginProvidersResponse, account, path=["response"])

    @parametrize
    def test_raw_response_list_login_providers(self, client: Gitpod) -> None:
        response = client.accounts.with_raw_response.list_login_providers(
            encoding="proto",
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountListLoginProvidersResponse, account, path=["response"])

    @parametrize
    def test_streaming_response_list_login_providers(self, client: Gitpod) -> None:
        with client.accounts.with_streaming_response.list_login_providers(
            encoding="proto",
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountListLoginProvidersResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAccounts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGitpod) -> None:
        account = await async_client.accounts.retrieve(
            encoding="proto",
            connect_protocol_version=1,
        )
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncGitpod) -> None:
        account = await async_client.accounts.retrieve(
            encoding="proto",
            connect_protocol_version=1,
            base64=True,
            compression="identity",
            connect="v1",
            message="message",
            connect_timeout_ms=0,
        )
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGitpod) -> None:
        response = await async_client.accounts.with_raw_response.retrieve(
            encoding="proto",
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGitpod) -> None:
        async with async_client.accounts.with_streaming_response.retrieve(
            encoding="proto",
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountRetrieveResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGitpod) -> None:
        account = await async_client.accounts.delete(
            connect_protocol_version=1,
        )
        assert_matches_type(object, account, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncGitpod) -> None:
        account = await async_client.accounts.delete(
            connect_protocol_version=1,
            account_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(object, account, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGitpod) -> None:
        response = await async_client.accounts.with_raw_response.delete(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(object, account, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGitpod) -> None:
        async with async_client.accounts.with_streaming_response.delete(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(object, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_sso_login_url(self, async_client: AsyncGitpod) -> None:
        account = await async_client.accounts.get_sso_login_url(
            encoding="proto",
            connect_protocol_version=1,
        )
        assert_matches_type(AccountGetSSOLoginURLResponse, account, path=["response"])

    @parametrize
    async def test_method_get_sso_login_url_with_all_params(self, async_client: AsyncGitpod) -> None:
        account = await async_client.accounts.get_sso_login_url(
            encoding="proto",
            connect_protocol_version=1,
            base64=True,
            compression="identity",
            connect="v1",
            message="message",
            connect_timeout_ms=0,
        )
        assert_matches_type(AccountGetSSOLoginURLResponse, account, path=["response"])

    @parametrize
    async def test_raw_response_get_sso_login_url(self, async_client: AsyncGitpod) -> None:
        response = await async_client.accounts.with_raw_response.get_sso_login_url(
            encoding="proto",
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountGetSSOLoginURLResponse, account, path=["response"])

    @parametrize
    async def test_streaming_response_get_sso_login_url(self, async_client: AsyncGitpod) -> None:
        async with async_client.accounts.with_streaming_response.get_sso_login_url(
            encoding="proto",
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountGetSSOLoginURLResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_login_providers(self, async_client: AsyncGitpod) -> None:
        account = await async_client.accounts.list_login_providers(
            encoding="proto",
            connect_protocol_version=1,
        )
        assert_matches_type(AccountListLoginProvidersResponse, account, path=["response"])

    @parametrize
    async def test_method_list_login_providers_with_all_params(self, async_client: AsyncGitpod) -> None:
        account = await async_client.accounts.list_login_providers(
            encoding="proto",
            connect_protocol_version=1,
            base64=True,
            compression="identity",
            connect="v1",
            message="message",
            connect_timeout_ms=0,
        )
        assert_matches_type(AccountListLoginProvidersResponse, account, path=["response"])

    @parametrize
    async def test_raw_response_list_login_providers(self, async_client: AsyncGitpod) -> None:
        response = await async_client.accounts.with_raw_response.list_login_providers(
            encoding="proto",
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountListLoginProvidersResponse, account, path=["response"])

    @parametrize
    async def test_streaming_response_list_login_providers(self, async_client: AsyncGitpod) -> None:
        async with async_client.accounts.with_streaming_response.list_login_providers(
            encoding="proto",
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountListLoginProvidersResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True
