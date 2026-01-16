# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.pagination import SyncScimConfigurationsPage, AsyncScimConfigurationsPage
from gitpod.types.organizations import (
    ScimConfiguration,
    ScimConfigurationCreateResponse,
    ScimConfigurationUpdateResponse,
    ScimConfigurationRetrieveResponse,
    ScimConfigurationRegenerateTokenResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScimConfigurations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Gitpod) -> None:
        scim_configuration = client.organizations.scim_configurations.create(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            sso_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(ScimConfigurationCreateResponse, scim_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Gitpod) -> None:
        scim_configuration = client.organizations.scim_configurations.create(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            sso_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
            name="name",
        )
        assert_matches_type(ScimConfigurationCreateResponse, scim_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Gitpod) -> None:
        response = client.organizations.scim_configurations.with_raw_response.create(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            sso_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scim_configuration = response.parse()
        assert_matches_type(ScimConfigurationCreateResponse, scim_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Gitpod) -> None:
        with client.organizations.scim_configurations.with_streaming_response.create(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            sso_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scim_configuration = response.parse()
            assert_matches_type(ScimConfigurationCreateResponse, scim_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Gitpod) -> None:
        scim_configuration = client.organizations.scim_configurations.retrieve(
            scim_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(ScimConfigurationRetrieveResponse, scim_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Gitpod) -> None:
        response = client.organizations.scim_configurations.with_raw_response.retrieve(
            scim_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scim_configuration = response.parse()
        assert_matches_type(ScimConfigurationRetrieveResponse, scim_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Gitpod) -> None:
        with client.organizations.scim_configurations.with_streaming_response.retrieve(
            scim_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scim_configuration = response.parse()
            assert_matches_type(ScimConfigurationRetrieveResponse, scim_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Gitpod) -> None:
        scim_configuration = client.organizations.scim_configurations.update(
            scim_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(ScimConfigurationUpdateResponse, scim_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Gitpod) -> None:
        scim_configuration = client.organizations.scim_configurations.update(
            scim_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
            enabled=False,
            name="name",
            sso_configuration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ScimConfigurationUpdateResponse, scim_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Gitpod) -> None:
        response = client.organizations.scim_configurations.with_raw_response.update(
            scim_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scim_configuration = response.parse()
        assert_matches_type(ScimConfigurationUpdateResponse, scim_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Gitpod) -> None:
        with client.organizations.scim_configurations.with_streaming_response.update(
            scim_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scim_configuration = response.parse()
            assert_matches_type(ScimConfigurationUpdateResponse, scim_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Gitpod) -> None:
        scim_configuration = client.organizations.scim_configurations.list()
        assert_matches_type(SyncScimConfigurationsPage[ScimConfiguration], scim_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Gitpod) -> None:
        scim_configuration = client.organizations.scim_configurations.list(
            token="token",
            page_size=0,
            pagination={
                "token": "token",
                "page_size": 20,
            },
        )
        assert_matches_type(SyncScimConfigurationsPage[ScimConfiguration], scim_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Gitpod) -> None:
        response = client.organizations.scim_configurations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scim_configuration = response.parse()
        assert_matches_type(SyncScimConfigurationsPage[ScimConfiguration], scim_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Gitpod) -> None:
        with client.organizations.scim_configurations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scim_configuration = response.parse()
            assert_matches_type(SyncScimConfigurationsPage[ScimConfiguration], scim_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Gitpod) -> None:
        scim_configuration = client.organizations.scim_configurations.delete(
            scim_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(object, scim_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Gitpod) -> None:
        response = client.organizations.scim_configurations.with_raw_response.delete(
            scim_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scim_configuration = response.parse()
        assert_matches_type(object, scim_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Gitpod) -> None:
        with client.organizations.scim_configurations.with_streaming_response.delete(
            scim_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scim_configuration = response.parse()
            assert_matches_type(object, scim_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_regenerate_token(self, client: Gitpod) -> None:
        scim_configuration = client.organizations.scim_configurations.regenerate_token(
            scim_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(ScimConfigurationRegenerateTokenResponse, scim_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_regenerate_token(self, client: Gitpod) -> None:
        response = client.organizations.scim_configurations.with_raw_response.regenerate_token(
            scim_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scim_configuration = response.parse()
        assert_matches_type(ScimConfigurationRegenerateTokenResponse, scim_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_regenerate_token(self, client: Gitpod) -> None:
        with client.organizations.scim_configurations.with_streaming_response.regenerate_token(
            scim_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scim_configuration = response.parse()
            assert_matches_type(ScimConfigurationRegenerateTokenResponse, scim_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncScimConfigurations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncGitpod) -> None:
        scim_configuration = await async_client.organizations.scim_configurations.create(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            sso_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(ScimConfigurationCreateResponse, scim_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGitpod) -> None:
        scim_configuration = await async_client.organizations.scim_configurations.create(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            sso_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
            name="name",
        )
        assert_matches_type(ScimConfigurationCreateResponse, scim_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.scim_configurations.with_raw_response.create(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            sso_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scim_configuration = await response.parse()
        assert_matches_type(ScimConfigurationCreateResponse, scim_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.scim_configurations.with_streaming_response.create(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            sso_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scim_configuration = await response.parse()
            assert_matches_type(ScimConfigurationCreateResponse, scim_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGitpod) -> None:
        scim_configuration = await async_client.organizations.scim_configurations.retrieve(
            scim_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(ScimConfigurationRetrieveResponse, scim_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.scim_configurations.with_raw_response.retrieve(
            scim_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scim_configuration = await response.parse()
        assert_matches_type(ScimConfigurationRetrieveResponse, scim_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.scim_configurations.with_streaming_response.retrieve(
            scim_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scim_configuration = await response.parse()
            assert_matches_type(ScimConfigurationRetrieveResponse, scim_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncGitpod) -> None:
        scim_configuration = await async_client.organizations.scim_configurations.update(
            scim_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(ScimConfigurationUpdateResponse, scim_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGitpod) -> None:
        scim_configuration = await async_client.organizations.scim_configurations.update(
            scim_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
            enabled=False,
            name="name",
            sso_configuration_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ScimConfigurationUpdateResponse, scim_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.scim_configurations.with_raw_response.update(
            scim_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scim_configuration = await response.parse()
        assert_matches_type(ScimConfigurationUpdateResponse, scim_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.scim_configurations.with_streaming_response.update(
            scim_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scim_configuration = await response.parse()
            assert_matches_type(ScimConfigurationUpdateResponse, scim_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncGitpod) -> None:
        scim_configuration = await async_client.organizations.scim_configurations.list()
        assert_matches_type(AsyncScimConfigurationsPage[ScimConfiguration], scim_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGitpod) -> None:
        scim_configuration = await async_client.organizations.scim_configurations.list(
            token="token",
            page_size=0,
            pagination={
                "token": "token",
                "page_size": 20,
            },
        )
        assert_matches_type(AsyncScimConfigurationsPage[ScimConfiguration], scim_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.scim_configurations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scim_configuration = await response.parse()
        assert_matches_type(AsyncScimConfigurationsPage[ScimConfiguration], scim_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.scim_configurations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scim_configuration = await response.parse()
            assert_matches_type(AsyncScimConfigurationsPage[ScimConfiguration], scim_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncGitpod) -> None:
        scim_configuration = await async_client.organizations.scim_configurations.delete(
            scim_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(object, scim_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.scim_configurations.with_raw_response.delete(
            scim_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scim_configuration = await response.parse()
        assert_matches_type(object, scim_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.scim_configurations.with_streaming_response.delete(
            scim_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scim_configuration = await response.parse()
            assert_matches_type(object, scim_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_regenerate_token(self, async_client: AsyncGitpod) -> None:
        scim_configuration = await async_client.organizations.scim_configurations.regenerate_token(
            scim_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(ScimConfigurationRegenerateTokenResponse, scim_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_regenerate_token(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.scim_configurations.with_raw_response.regenerate_token(
            scim_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scim_configuration = await response.parse()
        assert_matches_type(ScimConfigurationRegenerateTokenResponse, scim_configuration, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_regenerate_token(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.scim_configurations.with_streaming_response.regenerate_token(
            scim_configuration_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scim_configuration = await response.parse()
            assert_matches_type(ScimConfigurationRegenerateTokenResponse, scim_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True
