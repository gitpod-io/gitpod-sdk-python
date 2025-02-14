# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.pagination import SyncDomainVerificationsPage, AsyncDomainVerificationsPage
from gitpod.types.organizations import (
    DomainVerification,
    DomainVerificationCreateResponse,
    DomainVerificationVerifyResponse,
    DomainVerificationRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDomainVerifications:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Gitpod) -> None:
        domain_verification = client.organizations.domain_verifications.create(
            domain="acme-corp.com",
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(DomainVerificationCreateResponse, domain_verification, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Gitpod) -> None:
        response = client.organizations.domain_verifications.with_raw_response.create(
            domain="acme-corp.com",
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain_verification = response.parse()
        assert_matches_type(DomainVerificationCreateResponse, domain_verification, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Gitpod) -> None:
        with client.organizations.domain_verifications.with_streaming_response.create(
            domain="acme-corp.com",
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain_verification = response.parse()
            assert_matches_type(DomainVerificationCreateResponse, domain_verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Gitpod) -> None:
        domain_verification = client.organizations.domain_verifications.retrieve(
            domain_verification_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(DomainVerificationRetrieveResponse, domain_verification, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Gitpod) -> None:
        response = client.organizations.domain_verifications.with_raw_response.retrieve(
            domain_verification_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain_verification = response.parse()
        assert_matches_type(DomainVerificationRetrieveResponse, domain_verification, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Gitpod) -> None:
        with client.organizations.domain_verifications.with_streaming_response.retrieve(
            domain_verification_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain_verification = response.parse()
            assert_matches_type(DomainVerificationRetrieveResponse, domain_verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Gitpod) -> None:
        domain_verification = client.organizations.domain_verifications.list(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(SyncDomainVerificationsPage[DomainVerification], domain_verification, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Gitpod) -> None:
        domain_verification = client.organizations.domain_verifications.list(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            token="token",
            page_size=0,
            pagination={
                "token": "token",
                "page_size": 20,
            },
        )
        assert_matches_type(SyncDomainVerificationsPage[DomainVerification], domain_verification, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Gitpod) -> None:
        response = client.organizations.domain_verifications.with_raw_response.list(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain_verification = response.parse()
        assert_matches_type(SyncDomainVerificationsPage[DomainVerification], domain_verification, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Gitpod) -> None:
        with client.organizations.domain_verifications.with_streaming_response.list(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain_verification = response.parse()
            assert_matches_type(SyncDomainVerificationsPage[DomainVerification], domain_verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Gitpod) -> None:
        domain_verification = client.organizations.domain_verifications.delete(
            domain_verification_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(object, domain_verification, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Gitpod) -> None:
        response = client.organizations.domain_verifications.with_raw_response.delete(
            domain_verification_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain_verification = response.parse()
        assert_matches_type(object, domain_verification, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Gitpod) -> None:
        with client.organizations.domain_verifications.with_streaming_response.delete(
            domain_verification_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain_verification = response.parse()
            assert_matches_type(object, domain_verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_verify(self, client: Gitpod) -> None:
        domain_verification = client.organizations.domain_verifications.verify(
            domain_verification_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(DomainVerificationVerifyResponse, domain_verification, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_verify(self, client: Gitpod) -> None:
        response = client.organizations.domain_verifications.with_raw_response.verify(
            domain_verification_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain_verification = response.parse()
        assert_matches_type(DomainVerificationVerifyResponse, domain_verification, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_verify(self, client: Gitpod) -> None:
        with client.organizations.domain_verifications.with_streaming_response.verify(
            domain_verification_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain_verification = response.parse()
            assert_matches_type(DomainVerificationVerifyResponse, domain_verification, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDomainVerifications:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncGitpod) -> None:
        domain_verification = await async_client.organizations.domain_verifications.create(
            domain="acme-corp.com",
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(DomainVerificationCreateResponse, domain_verification, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.domain_verifications.with_raw_response.create(
            domain="acme-corp.com",
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain_verification = await response.parse()
        assert_matches_type(DomainVerificationCreateResponse, domain_verification, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.domain_verifications.with_streaming_response.create(
            domain="acme-corp.com",
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain_verification = await response.parse()
            assert_matches_type(DomainVerificationCreateResponse, domain_verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGitpod) -> None:
        domain_verification = await async_client.organizations.domain_verifications.retrieve(
            domain_verification_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(DomainVerificationRetrieveResponse, domain_verification, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.domain_verifications.with_raw_response.retrieve(
            domain_verification_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain_verification = await response.parse()
        assert_matches_type(DomainVerificationRetrieveResponse, domain_verification, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.domain_verifications.with_streaming_response.retrieve(
            domain_verification_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain_verification = await response.parse()
            assert_matches_type(DomainVerificationRetrieveResponse, domain_verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncGitpod) -> None:
        domain_verification = await async_client.organizations.domain_verifications.list(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(AsyncDomainVerificationsPage[DomainVerification], domain_verification, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGitpod) -> None:
        domain_verification = await async_client.organizations.domain_verifications.list(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            token="token",
            page_size=0,
            pagination={
                "token": "token",
                "page_size": 20,
            },
        )
        assert_matches_type(AsyncDomainVerificationsPage[DomainVerification], domain_verification, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.domain_verifications.with_raw_response.list(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain_verification = await response.parse()
        assert_matches_type(AsyncDomainVerificationsPage[DomainVerification], domain_verification, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.domain_verifications.with_streaming_response.list(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain_verification = await response.parse()
            assert_matches_type(
                AsyncDomainVerificationsPage[DomainVerification], domain_verification, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncGitpod) -> None:
        domain_verification = await async_client.organizations.domain_verifications.delete(
            domain_verification_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(object, domain_verification, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.domain_verifications.with_raw_response.delete(
            domain_verification_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain_verification = await response.parse()
        assert_matches_type(object, domain_verification, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.domain_verifications.with_streaming_response.delete(
            domain_verification_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain_verification = await response.parse()
            assert_matches_type(object, domain_verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_verify(self, async_client: AsyncGitpod) -> None:
        domain_verification = await async_client.organizations.domain_verifications.verify(
            domain_verification_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(DomainVerificationVerifyResponse, domain_verification, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_verify(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.domain_verifications.with_raw_response.verify(
            domain_verification_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain_verification = await response.parse()
        assert_matches_type(DomainVerificationVerifyResponse, domain_verification, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_verify(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.domain_verifications.with_streaming_response.verify(
            domain_verification_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain_verification = await response.parse()
            assert_matches_type(DomainVerificationVerifyResponse, domain_verification, path=["response"])

        assert cast(Any, response.is_closed) is True
