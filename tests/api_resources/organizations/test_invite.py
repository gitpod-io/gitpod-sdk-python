# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.types.organizations import (
    InviteCreateResponse,
    InviteRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInvite:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gitpod) -> None:
        invite = client.organizations.invite.create()
        assert_matches_type(InviteCreateResponse, invite, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gitpod) -> None:
        invite = client.organizations.invite.create(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InviteCreateResponse, invite, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gitpod) -> None:
        response = client.organizations.invite.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invite = response.parse()
        assert_matches_type(InviteCreateResponse, invite, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gitpod) -> None:
        with client.organizations.invite.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invite = response.parse()
            assert_matches_type(InviteCreateResponse, invite, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Gitpod) -> None:
        invite = client.organizations.invite.retrieve()
        assert_matches_type(InviteRetrieveResponse, invite, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Gitpod) -> None:
        invite = client.organizations.invite.retrieve(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InviteRetrieveResponse, invite, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Gitpod) -> None:
        response = client.organizations.invite.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invite = response.parse()
        assert_matches_type(InviteRetrieveResponse, invite, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Gitpod) -> None:
        with client.organizations.invite.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invite = response.parse()
            assert_matches_type(InviteRetrieveResponse, invite, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInvite:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncGitpod) -> None:
        invite = await async_client.organizations.invite.create()
        assert_matches_type(InviteCreateResponse, invite, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGitpod) -> None:
        invite = await async_client.organizations.invite.create(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InviteCreateResponse, invite, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.invite.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invite = await response.parse()
        assert_matches_type(InviteCreateResponse, invite, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.invite.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invite = await response.parse()
            assert_matches_type(InviteCreateResponse, invite, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGitpod) -> None:
        invite = await async_client.organizations.invite.retrieve()
        assert_matches_type(InviteRetrieveResponse, invite, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncGitpod) -> None:
        invite = await async_client.organizations.invite.retrieve(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InviteRetrieveResponse, invite, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.invite.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invite = await response.parse()
        assert_matches_type(InviteRetrieveResponse, invite, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.invite.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invite = await response.parse()
            assert_matches_type(InviteRetrieveResponse, invite, path=["response"])

        assert cast(Any, response.is_closed) is True
