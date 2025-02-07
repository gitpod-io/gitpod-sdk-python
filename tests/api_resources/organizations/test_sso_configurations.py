# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.pagination import SyncSSOConfigurationsPage, AsyncSSOConfigurationsPage
from gitpod.types.organizations import (
    SSOConfiguration,
    SSOConfigurationCreateResponse,
    SSOConfigurationRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSSOConfigurations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Gitpod) -> None:
        sso_configuration = client.organizations.sso_configurations.create()
        assert_matches_type(SSOConfigurationCreateResponse, sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Gitpod) -> None:
        sso_configuration = client.organizations.sso_configurations.create(
            client_id="x",
            client_secret="x",
            email_domain="xxxx",
            issuer_url="https://example.com",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SSOConfigurationCreateResponse, sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Gitpod) -> None:
        response = client.organizations.sso_configurations.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sso_configuration = response.parse()
        assert_matches_type(SSOConfigurationCreateResponse, sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Gitpod) -> None:
        with client.organizations.sso_configurations.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sso_configuration = response.parse()
            assert_matches_type(SSOConfigurationCreateResponse, sso_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Gitpod) -> None:
        sso_configuration = client.organizations.sso_configurations.retrieve()
        assert_matches_type(SSOConfigurationRetrieveResponse, sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Gitpod) -> None:
        sso_configuration = client.organizations.sso_configurations.retrieve(
            sso_configuration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SSOConfigurationRetrieveResponse, sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Gitpod) -> None:
        response = client.organizations.sso_configurations.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sso_configuration = response.parse()
        assert_matches_type(SSOConfigurationRetrieveResponse, sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Gitpod) -> None:
        with client.organizations.sso_configurations.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sso_configuration = response.parse()
            assert_matches_type(SSOConfigurationRetrieveResponse, sso_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Gitpod) -> None:
        sso_configuration = client.organizations.sso_configurations.update()
        assert_matches_type(object, sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Gitpod) -> None:
        sso_configuration = client.organizations.sso_configurations.update(
            claims={"foo": "string"},
            client_id="x",
            client_secret="x",
            email_domain="xxxx",
            issuer_url="https://example.com",
            sso_configuration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            state="SSO_CONFIGURATION_STATE_UNSPECIFIED",
        )
        assert_matches_type(object, sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Gitpod) -> None:
        response = client.organizations.sso_configurations.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sso_configuration = response.parse()
        assert_matches_type(object, sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Gitpod) -> None:
        with client.organizations.sso_configurations.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sso_configuration = response.parse()
            assert_matches_type(object, sso_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Gitpod) -> None:
        sso_configuration = client.organizations.sso_configurations.list()
        assert_matches_type(SyncSSOConfigurationsPage[SSOConfiguration], sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Gitpod) -> None:
        sso_configuration = client.organizations.sso_configurations.list(
            token="token",
            page_size=0,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            pagination={
                "token": "token",
                "page_size": 100,
            },
        )
        assert_matches_type(SyncSSOConfigurationsPage[SSOConfiguration], sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Gitpod) -> None:
        response = client.organizations.sso_configurations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sso_configuration = response.parse()
        assert_matches_type(SyncSSOConfigurationsPage[SSOConfiguration], sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Gitpod) -> None:
        with client.organizations.sso_configurations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sso_configuration = response.parse()
            assert_matches_type(SyncSSOConfigurationsPage[SSOConfiguration], sso_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Gitpod) -> None:
        sso_configuration = client.organizations.sso_configurations.delete()
        assert_matches_type(object, sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete_with_all_params(self, client: Gitpod) -> None:
        sso_configuration = client.organizations.sso_configurations.delete(
            sso_configuration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Gitpod) -> None:
        response = client.organizations.sso_configurations.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sso_configuration = response.parse()
        assert_matches_type(object, sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Gitpod) -> None:
        with client.organizations.sso_configurations.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sso_configuration = response.parse()
            assert_matches_type(object, sso_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSSOConfigurations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncGitpod) -> None:
        sso_configuration = await async_client.organizations.sso_configurations.create()
        assert_matches_type(SSOConfigurationCreateResponse, sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGitpod) -> None:
        sso_configuration = await async_client.organizations.sso_configurations.create(
            client_id="x",
            client_secret="x",
            email_domain="xxxx",
            issuer_url="https://example.com",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SSOConfigurationCreateResponse, sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.sso_configurations.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sso_configuration = await response.parse()
        assert_matches_type(SSOConfigurationCreateResponse, sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.sso_configurations.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sso_configuration = await response.parse()
            assert_matches_type(SSOConfigurationCreateResponse, sso_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGitpod) -> None:
        sso_configuration = await async_client.organizations.sso_configurations.retrieve()
        assert_matches_type(SSOConfigurationRetrieveResponse, sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncGitpod) -> None:
        sso_configuration = await async_client.organizations.sso_configurations.retrieve(
            sso_configuration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SSOConfigurationRetrieveResponse, sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.sso_configurations.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sso_configuration = await response.parse()
        assert_matches_type(SSOConfigurationRetrieveResponse, sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.sso_configurations.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sso_configuration = await response.parse()
            assert_matches_type(SSOConfigurationRetrieveResponse, sso_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncGitpod) -> None:
        sso_configuration = await async_client.organizations.sso_configurations.update()
        assert_matches_type(object, sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGitpod) -> None:
        sso_configuration = await async_client.organizations.sso_configurations.update(
            claims={"foo": "string"},
            client_id="x",
            client_secret="x",
            email_domain="xxxx",
            issuer_url="https://example.com",
            sso_configuration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            state="SSO_CONFIGURATION_STATE_UNSPECIFIED",
        )
        assert_matches_type(object, sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.sso_configurations.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sso_configuration = await response.parse()
        assert_matches_type(object, sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.sso_configurations.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sso_configuration = await response.parse()
            assert_matches_type(object, sso_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncGitpod) -> None:
        sso_configuration = await async_client.organizations.sso_configurations.list()
        assert_matches_type(AsyncSSOConfigurationsPage[SSOConfiguration], sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGitpod) -> None:
        sso_configuration = await async_client.organizations.sso_configurations.list(
            token="token",
            page_size=0,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            pagination={
                "token": "token",
                "page_size": 100,
            },
        )
        assert_matches_type(AsyncSSOConfigurationsPage[SSOConfiguration], sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.sso_configurations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sso_configuration = await response.parse()
        assert_matches_type(AsyncSSOConfigurationsPage[SSOConfiguration], sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.sso_configurations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sso_configuration = await response.parse()
            assert_matches_type(AsyncSSOConfigurationsPage[SSOConfiguration], sso_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncGitpod) -> None:
        sso_configuration = await async_client.organizations.sso_configurations.delete()
        assert_matches_type(object, sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncGitpod) -> None:
        sso_configuration = await async_client.organizations.sso_configurations.delete(
            sso_configuration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.sso_configurations.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sso_configuration = await response.parse()
        assert_matches_type(object, sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.sso_configurations.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sso_configuration = await response.parse()
            assert_matches_type(object, sso_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True
