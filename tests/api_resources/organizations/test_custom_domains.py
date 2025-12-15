# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.types.organizations import (
    CustomDomainCreateResponse,
    CustomDomainUpdateResponse,
    CustomDomainRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomDomains:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Gitpod) -> None:
        custom_domain = client.organizations.custom_domains.create(
            domain_name="workspaces.acme-corp.com",
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(CustomDomainCreateResponse, custom_domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Gitpod) -> None:
        custom_domain = client.organizations.custom_domains.create(
            domain_name="workspaces.acme-corp.com",
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            aws_account_id="123456789012",
            cloud_account_id="cloudAccountId",
            provider="CUSTOM_DOMAIN_PROVIDER_AWS",
        )
        assert_matches_type(CustomDomainCreateResponse, custom_domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Gitpod) -> None:
        response = client.organizations.custom_domains.with_raw_response.create(
            domain_name="workspaces.acme-corp.com",
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_domain = response.parse()
        assert_matches_type(CustomDomainCreateResponse, custom_domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Gitpod) -> None:
        with client.organizations.custom_domains.with_streaming_response.create(
            domain_name="workspaces.acme-corp.com",
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_domain = response.parse()
            assert_matches_type(CustomDomainCreateResponse, custom_domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Gitpod) -> None:
        custom_domain = client.organizations.custom_domains.retrieve(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(CustomDomainRetrieveResponse, custom_domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Gitpod) -> None:
        response = client.organizations.custom_domains.with_raw_response.retrieve(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_domain = response.parse()
        assert_matches_type(CustomDomainRetrieveResponse, custom_domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Gitpod) -> None:
        with client.organizations.custom_domains.with_streaming_response.retrieve(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_domain = response.parse()
            assert_matches_type(CustomDomainRetrieveResponse, custom_domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Gitpod) -> None:
        custom_domain = client.organizations.custom_domains.update(
            domain_name="workspaces.acme-corp.com",
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(CustomDomainUpdateResponse, custom_domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Gitpod) -> None:
        custom_domain = client.organizations.custom_domains.update(
            domain_name="workspaces.acme-corp.com",
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            aws_account_id="987654321098",
            cloud_account_id="cloudAccountId",
            provider="CUSTOM_DOMAIN_PROVIDER_UNSPECIFIED",
        )
        assert_matches_type(CustomDomainUpdateResponse, custom_domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Gitpod) -> None:
        response = client.organizations.custom_domains.with_raw_response.update(
            domain_name="workspaces.acme-corp.com",
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_domain = response.parse()
        assert_matches_type(CustomDomainUpdateResponse, custom_domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Gitpod) -> None:
        with client.organizations.custom_domains.with_streaming_response.update(
            domain_name="workspaces.acme-corp.com",
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_domain = response.parse()
            assert_matches_type(CustomDomainUpdateResponse, custom_domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Gitpod) -> None:
        custom_domain = client.organizations.custom_domains.delete(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(object, custom_domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Gitpod) -> None:
        response = client.organizations.custom_domains.with_raw_response.delete(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_domain = response.parse()
        assert_matches_type(object, custom_domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Gitpod) -> None:
        with client.organizations.custom_domains.with_streaming_response.delete(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_domain = response.parse()
            assert_matches_type(object, custom_domain, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCustomDomains:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncGitpod) -> None:
        custom_domain = await async_client.organizations.custom_domains.create(
            domain_name="workspaces.acme-corp.com",
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(CustomDomainCreateResponse, custom_domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGitpod) -> None:
        custom_domain = await async_client.organizations.custom_domains.create(
            domain_name="workspaces.acme-corp.com",
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            aws_account_id="123456789012",
            cloud_account_id="cloudAccountId",
            provider="CUSTOM_DOMAIN_PROVIDER_AWS",
        )
        assert_matches_type(CustomDomainCreateResponse, custom_domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.custom_domains.with_raw_response.create(
            domain_name="workspaces.acme-corp.com",
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_domain = await response.parse()
        assert_matches_type(CustomDomainCreateResponse, custom_domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.custom_domains.with_streaming_response.create(
            domain_name="workspaces.acme-corp.com",
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_domain = await response.parse()
            assert_matches_type(CustomDomainCreateResponse, custom_domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGitpod) -> None:
        custom_domain = await async_client.organizations.custom_domains.retrieve(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(CustomDomainRetrieveResponse, custom_domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.custom_domains.with_raw_response.retrieve(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_domain = await response.parse()
        assert_matches_type(CustomDomainRetrieveResponse, custom_domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.custom_domains.with_streaming_response.retrieve(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_domain = await response.parse()
            assert_matches_type(CustomDomainRetrieveResponse, custom_domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncGitpod) -> None:
        custom_domain = await async_client.organizations.custom_domains.update(
            domain_name="workspaces.acme-corp.com",
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(CustomDomainUpdateResponse, custom_domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGitpod) -> None:
        custom_domain = await async_client.organizations.custom_domains.update(
            domain_name="workspaces.acme-corp.com",
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            aws_account_id="987654321098",
            cloud_account_id="cloudAccountId",
            provider="CUSTOM_DOMAIN_PROVIDER_UNSPECIFIED",
        )
        assert_matches_type(CustomDomainUpdateResponse, custom_domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.custom_domains.with_raw_response.update(
            domain_name="workspaces.acme-corp.com",
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_domain = await response.parse()
        assert_matches_type(CustomDomainUpdateResponse, custom_domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.custom_domains.with_streaming_response.update(
            domain_name="workspaces.acme-corp.com",
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_domain = await response.parse()
            assert_matches_type(CustomDomainUpdateResponse, custom_domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncGitpod) -> None:
        custom_domain = await async_client.organizations.custom_domains.delete(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(object, custom_domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.custom_domains.with_raw_response.delete(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_domain = await response.parse()
        assert_matches_type(object, custom_domain, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.custom_domains.with_streaming_response.delete(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_domain = await response.parse()
            assert_matches_type(object, custom_domain, path=["response"])

        assert cast(Any, response.is_closed) is True
