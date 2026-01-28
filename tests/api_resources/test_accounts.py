# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.types import (
    LoginProvider,
    JoinableOrganization,
    AccountRetrieveResponse,
    AccountListSSOLoginsResponse,
    AccountGetSSOLoginURLResponse,
)
from gitpod.pagination import (
    SyncLoginsPage,
    AsyncLoginsPage,
    SyncLoginProvidersPage,
    AsyncLoginProvidersPage,
    SyncJoinableOrganizationsPage,
    AsyncJoinableOrganizationsPage,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Gitpod) -> None:
        account = client.accounts.retrieve()
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Gitpod) -> None:
        account = client.accounts.retrieve(
            empty=True,
        )
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Gitpod) -> None:
        response = client.accounts.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Gitpod) -> None:
        with client.accounts.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountRetrieveResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Gitpod) -> None:
        account = client.accounts.delete(
            account_id="f53d2330-3795-4c5d-a1f3-453121af9c60",
        )
        assert_matches_type(object, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Gitpod) -> None:
        account = client.accounts.delete(
            account_id="f53d2330-3795-4c5d-a1f3-453121af9c60",
            reason="reason",
        )
        assert_matches_type(object, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Gitpod) -> None:
        response = client.accounts.with_raw_response.delete(
            account_id="f53d2330-3795-4c5d-a1f3-453121af9c60",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(object, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Gitpod) -> None:
        with client.accounts.with_streaming_response.delete(
            account_id="f53d2330-3795-4c5d-a1f3-453121af9c60",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(object, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_sso_login_url(self, client: Gitpod) -> None:
        account = client.accounts.get_sso_login_url(
            email="user@company.com",
        )
        assert_matches_type(AccountGetSSOLoginURLResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_sso_login_url_with_all_params(self, client: Gitpod) -> None:
        account = client.accounts.get_sso_login_url(
            email="user@company.com",
            return_to="https://example.com",
        )
        assert_matches_type(AccountGetSSOLoginURLResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_sso_login_url(self, client: Gitpod) -> None:
        response = client.accounts.with_raw_response.get_sso_login_url(
            email="user@company.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountGetSSOLoginURLResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_sso_login_url(self, client: Gitpod) -> None:
        with client.accounts.with_streaming_response.get_sso_login_url(
            email="user@company.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountGetSSOLoginURLResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_joinable_organizations(self, client: Gitpod) -> None:
        account = client.accounts.list_joinable_organizations()
        assert_matches_type(SyncJoinableOrganizationsPage[JoinableOrganization], account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_joinable_organizations_with_all_params(self, client: Gitpod) -> None:
        account = client.accounts.list_joinable_organizations(
            token="token",
            page_size=0,
            pagination={
                "token": "token",
                "page_size": 100,
            },
        )
        assert_matches_type(SyncJoinableOrganizationsPage[JoinableOrganization], account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_joinable_organizations(self, client: Gitpod) -> None:
        response = client.accounts.with_raw_response.list_joinable_organizations()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(SyncJoinableOrganizationsPage[JoinableOrganization], account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_joinable_organizations(self, client: Gitpod) -> None:
        with client.accounts.with_streaming_response.list_joinable_organizations() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(SyncJoinableOrganizationsPage[JoinableOrganization], account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_login_providers(self, client: Gitpod) -> None:
        account = client.accounts.list_login_providers()
        assert_matches_type(SyncLoginProvidersPage[LoginProvider], account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_login_providers_with_all_params(self, client: Gitpod) -> None:
        account = client.accounts.list_login_providers(
            token="token",
            page_size=0,
            filter={
                "email": "email",
                "invite_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            pagination={
                "token": "token",
                "page_size": 20,
            },
        )
        assert_matches_type(SyncLoginProvidersPage[LoginProvider], account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_login_providers(self, client: Gitpod) -> None:
        response = client.accounts.with_raw_response.list_login_providers()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(SyncLoginProvidersPage[LoginProvider], account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_login_providers(self, client: Gitpod) -> None:
        with client.accounts.with_streaming_response.list_login_providers() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(SyncLoginProvidersPage[LoginProvider], account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_sso_logins(self, client: Gitpod) -> None:
        account = client.accounts.list_sso_logins(
            email="dev@stainless.com",
        )
        assert_matches_type(SyncLoginsPage[AccountListSSOLoginsResponse], account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_sso_logins_with_all_params(self, client: Gitpod) -> None:
        account = client.accounts.list_sso_logins(
            email="dev@stainless.com",
            token="token",
            page_size=0,
            pagination={
                "token": "token",
                "page_size": 100,
            },
            return_to="https://example.com",
        )
        assert_matches_type(SyncLoginsPage[AccountListSSOLoginsResponse], account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_sso_logins(self, client: Gitpod) -> None:
        response = client.accounts.with_raw_response.list_sso_logins(
            email="dev@stainless.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(SyncLoginsPage[AccountListSSOLoginsResponse], account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_sso_logins(self, client: Gitpod) -> None:
        with client.accounts.with_streaming_response.list_sso_logins(
            email="dev@stainless.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(SyncLoginsPage[AccountListSSOLoginsResponse], account, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAccounts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGitpod) -> None:
        account = await async_client.accounts.retrieve()
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncGitpod) -> None:
        account = await async_client.accounts.retrieve(
            empty=True,
        )
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGitpod) -> None:
        response = await async_client.accounts.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGitpod) -> None:
        async with async_client.accounts.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountRetrieveResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncGitpod) -> None:
        account = await async_client.accounts.delete(
            account_id="f53d2330-3795-4c5d-a1f3-453121af9c60",
        )
        assert_matches_type(object, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncGitpod) -> None:
        account = await async_client.accounts.delete(
            account_id="f53d2330-3795-4c5d-a1f3-453121af9c60",
            reason="reason",
        )
        assert_matches_type(object, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGitpod) -> None:
        response = await async_client.accounts.with_raw_response.delete(
            account_id="f53d2330-3795-4c5d-a1f3-453121af9c60",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(object, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGitpod) -> None:
        async with async_client.accounts.with_streaming_response.delete(
            account_id="f53d2330-3795-4c5d-a1f3-453121af9c60",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(object, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_sso_login_url(self, async_client: AsyncGitpod) -> None:
        account = await async_client.accounts.get_sso_login_url(
            email="user@company.com",
        )
        assert_matches_type(AccountGetSSOLoginURLResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_sso_login_url_with_all_params(self, async_client: AsyncGitpod) -> None:
        account = await async_client.accounts.get_sso_login_url(
            email="user@company.com",
            return_to="https://example.com",
        )
        assert_matches_type(AccountGetSSOLoginURLResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_sso_login_url(self, async_client: AsyncGitpod) -> None:
        response = await async_client.accounts.with_raw_response.get_sso_login_url(
            email="user@company.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountGetSSOLoginURLResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_sso_login_url(self, async_client: AsyncGitpod) -> None:
        async with async_client.accounts.with_streaming_response.get_sso_login_url(
            email="user@company.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountGetSSOLoginURLResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_joinable_organizations(self, async_client: AsyncGitpod) -> None:
        account = await async_client.accounts.list_joinable_organizations()
        assert_matches_type(AsyncJoinableOrganizationsPage[JoinableOrganization], account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_joinable_organizations_with_all_params(self, async_client: AsyncGitpod) -> None:
        account = await async_client.accounts.list_joinable_organizations(
            token="token",
            page_size=0,
            pagination={
                "token": "token",
                "page_size": 100,
            },
        )
        assert_matches_type(AsyncJoinableOrganizationsPage[JoinableOrganization], account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_joinable_organizations(self, async_client: AsyncGitpod) -> None:
        response = await async_client.accounts.with_raw_response.list_joinable_organizations()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AsyncJoinableOrganizationsPage[JoinableOrganization], account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_joinable_organizations(self, async_client: AsyncGitpod) -> None:
        async with async_client.accounts.with_streaming_response.list_joinable_organizations() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AsyncJoinableOrganizationsPage[JoinableOrganization], account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_login_providers(self, async_client: AsyncGitpod) -> None:
        account = await async_client.accounts.list_login_providers()
        assert_matches_type(AsyncLoginProvidersPage[LoginProvider], account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_login_providers_with_all_params(self, async_client: AsyncGitpod) -> None:
        account = await async_client.accounts.list_login_providers(
            token="token",
            page_size=0,
            filter={
                "email": "email",
                "invite_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            pagination={
                "token": "token",
                "page_size": 20,
            },
        )
        assert_matches_type(AsyncLoginProvidersPage[LoginProvider], account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_login_providers(self, async_client: AsyncGitpod) -> None:
        response = await async_client.accounts.with_raw_response.list_login_providers()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AsyncLoginProvidersPage[LoginProvider], account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_login_providers(self, async_client: AsyncGitpod) -> None:
        async with async_client.accounts.with_streaming_response.list_login_providers() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AsyncLoginProvidersPage[LoginProvider], account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_sso_logins(self, async_client: AsyncGitpod) -> None:
        account = await async_client.accounts.list_sso_logins(
            email="dev@stainless.com",
        )
        assert_matches_type(AsyncLoginsPage[AccountListSSOLoginsResponse], account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_sso_logins_with_all_params(self, async_client: AsyncGitpod) -> None:
        account = await async_client.accounts.list_sso_logins(
            email="dev@stainless.com",
            token="token",
            page_size=0,
            pagination={
                "token": "token",
                "page_size": 100,
            },
            return_to="https://example.com",
        )
        assert_matches_type(AsyncLoginsPage[AccountListSSOLoginsResponse], account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_sso_logins(self, async_client: AsyncGitpod) -> None:
        response = await async_client.accounts.with_raw_response.list_sso_logins(
            email="dev@stainless.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AsyncLoginsPage[AccountListSSOLoginsResponse], account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_sso_logins(self, async_client: AsyncGitpod) -> None:
        async with async_client.accounts.with_streaming_response.list_sso_logins(
            email="dev@stainless.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AsyncLoginsPage[AccountListSSOLoginsResponse], account, path=["response"])

        assert cast(Any, response.is_closed) is True
