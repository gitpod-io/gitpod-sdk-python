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
        sso_configuration = client.organizations.sso_configurations.create(
            client_id="012345678-abcdefghijklmnopqrstuvwxyz.apps.googleusercontent.com",
            client_secret="GOCSPX-abcdefghijklmnopqrstuvwxyz123456",
            email_domain="acme-corp.com",
            issuer_url="https://accounts.google.com",
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(SSOConfigurationCreateResponse, sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Gitpod) -> None:
        response = client.organizations.sso_configurations.with_raw_response.create(
            client_id="012345678-abcdefghijklmnopqrstuvwxyz.apps.googleusercontent.com",
            client_secret="GOCSPX-abcdefghijklmnopqrstuvwxyz123456",
            email_domain="acme-corp.com",
            issuer_url="https://accounts.google.com",
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sso_configuration = response.parse()
        assert_matches_type(SSOConfigurationCreateResponse, sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Gitpod) -> None:
        with client.organizations.sso_configurations.with_streaming_response.create(
            client_id="012345678-abcdefghijklmnopqrstuvwxyz.apps.googleusercontent.com",
            client_secret="GOCSPX-abcdefghijklmnopqrstuvwxyz123456",
            email_domain="acme-corp.com",
            issuer_url="https://accounts.google.com",
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sso_configuration = response.parse()
            assert_matches_type(SSOConfigurationCreateResponse, sso_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Gitpod) -> None:
        sso_configuration = client.organizations.sso_configurations.retrieve(
            sso_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(SSOConfigurationRetrieveResponse, sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Gitpod) -> None:
        response = client.organizations.sso_configurations.with_raw_response.retrieve(
            sso_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sso_configuration = response.parse()
        assert_matches_type(SSOConfigurationRetrieveResponse, sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Gitpod) -> None:
        with client.organizations.sso_configurations.with_streaming_response.retrieve(
            sso_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sso_configuration = response.parse()
            assert_matches_type(SSOConfigurationRetrieveResponse, sso_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Gitpod) -> None:
        sso_configuration = client.organizations.sso_configurations.update(
            sso_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(object, sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Gitpod) -> None:
        sso_configuration = client.organizations.sso_configurations.update(
            sso_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
            claims={"foo": "string"},
            client_id="new-client-id",
            client_secret="new-client-secret",
            email_domain="xxxx",
            issuer_url="https://example.com",
            state="SSO_CONFIGURATION_STATE_UNSPECIFIED",
        )
        assert_matches_type(object, sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Gitpod) -> None:
        response = client.organizations.sso_configurations.with_raw_response.update(
            sso_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sso_configuration = response.parse()
        assert_matches_type(object, sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Gitpod) -> None:
        with client.organizations.sso_configurations.with_streaming_response.update(
            sso_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sso_configuration = response.parse()
            assert_matches_type(object, sso_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Gitpod) -> None:
        sso_configuration = client.organizations.sso_configurations.list(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(SyncSSOConfigurationsPage[SSOConfiguration], sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Gitpod) -> None:
        sso_configuration = client.organizations.sso_configurations.list(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            token="token",
            page_size=0,
            pagination={
                "token": "token",
                "page_size": 20,
            },
        )
        assert_matches_type(SyncSSOConfigurationsPage[SSOConfiguration], sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Gitpod) -> None:
        response = client.organizations.sso_configurations.with_raw_response.list(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sso_configuration = response.parse()
        assert_matches_type(SyncSSOConfigurationsPage[SSOConfiguration], sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Gitpod) -> None:
        with client.organizations.sso_configurations.with_streaming_response.list(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sso_configuration = response.parse()
            assert_matches_type(SyncSSOConfigurationsPage[SSOConfiguration], sso_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Gitpod) -> None:
        sso_configuration = client.organizations.sso_configurations.delete(
            sso_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(object, sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Gitpod) -> None:
        response = client.organizations.sso_configurations.with_raw_response.delete(
            sso_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sso_configuration = response.parse()
        assert_matches_type(object, sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Gitpod) -> None:
        with client.organizations.sso_configurations.with_streaming_response.delete(
            sso_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        ) as response:
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
        sso_configuration = await async_client.organizations.sso_configurations.create(
            client_id="012345678-abcdefghijklmnopqrstuvwxyz.apps.googleusercontent.com",
            client_secret="GOCSPX-abcdefghijklmnopqrstuvwxyz123456",
            email_domain="acme-corp.com",
            issuer_url="https://accounts.google.com",
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(SSOConfigurationCreateResponse, sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.sso_configurations.with_raw_response.create(
            client_id="012345678-abcdefghijklmnopqrstuvwxyz.apps.googleusercontent.com",
            client_secret="GOCSPX-abcdefghijklmnopqrstuvwxyz123456",
            email_domain="acme-corp.com",
            issuer_url="https://accounts.google.com",
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sso_configuration = await response.parse()
        assert_matches_type(SSOConfigurationCreateResponse, sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.sso_configurations.with_streaming_response.create(
            client_id="012345678-abcdefghijklmnopqrstuvwxyz.apps.googleusercontent.com",
            client_secret="GOCSPX-abcdefghijklmnopqrstuvwxyz123456",
            email_domain="acme-corp.com",
            issuer_url="https://accounts.google.com",
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sso_configuration = await response.parse()
            assert_matches_type(SSOConfigurationCreateResponse, sso_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGitpod) -> None:
        sso_configuration = await async_client.organizations.sso_configurations.retrieve(
            sso_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(SSOConfigurationRetrieveResponse, sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.sso_configurations.with_raw_response.retrieve(
            sso_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sso_configuration = await response.parse()
        assert_matches_type(SSOConfigurationRetrieveResponse, sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.sso_configurations.with_streaming_response.retrieve(
            sso_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sso_configuration = await response.parse()
            assert_matches_type(SSOConfigurationRetrieveResponse, sso_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncGitpod) -> None:
        sso_configuration = await async_client.organizations.sso_configurations.update(
            sso_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(object, sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGitpod) -> None:
        sso_configuration = await async_client.organizations.sso_configurations.update(
            sso_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
            claims={"foo": "string"},
            client_id="new-client-id",
            client_secret="new-client-secret",
            email_domain="xxxx",
            issuer_url="https://example.com",
            state="SSO_CONFIGURATION_STATE_UNSPECIFIED",
        )
        assert_matches_type(object, sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.sso_configurations.with_raw_response.update(
            sso_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sso_configuration = await response.parse()
        assert_matches_type(object, sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.sso_configurations.with_streaming_response.update(
            sso_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sso_configuration = await response.parse()
            assert_matches_type(object, sso_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncGitpod) -> None:
        sso_configuration = await async_client.organizations.sso_configurations.list(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(AsyncSSOConfigurationsPage[SSOConfiguration], sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGitpod) -> None:
        sso_configuration = await async_client.organizations.sso_configurations.list(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            token="token",
            page_size=0,
            pagination={
                "token": "token",
                "page_size": 20,
            },
        )
        assert_matches_type(AsyncSSOConfigurationsPage[SSOConfiguration], sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.sso_configurations.with_raw_response.list(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sso_configuration = await response.parse()
        assert_matches_type(AsyncSSOConfigurationsPage[SSOConfiguration], sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.sso_configurations.with_streaming_response.list(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sso_configuration = await response.parse()
            assert_matches_type(AsyncSSOConfigurationsPage[SSOConfiguration], sso_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncGitpod) -> None:
        sso_configuration = await async_client.organizations.sso_configurations.delete(
            sso_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(object, sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.sso_configurations.with_raw_response.delete(
            sso_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sso_configuration = await response.parse()
        assert_matches_type(object, sso_configuration, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.sso_configurations.with_streaming_response.delete(
            sso_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sso_configuration = await response.parse()
            assert_matches_type(object, sso_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True
