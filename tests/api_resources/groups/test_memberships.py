# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.pagination import SyncMembersPage, AsyncMembersPage
from gitpod.types.groups import (
    GroupMembership,
    MembershipCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMemberships:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Gitpod) -> None:
        membership = client.groups.memberships.create()
        assert_matches_type(MembershipCreateResponse, membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Gitpod) -> None:
        membership = client.groups.memberships.create(
            group_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
            subject={
                "id": "f53d2330-3795-4c5d-a1f3-453121af9c60",
                "principal": "PRINCIPAL_USER",
            },
        )
        assert_matches_type(MembershipCreateResponse, membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Gitpod) -> None:
        response = client.groups.memberships.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = response.parse()
        assert_matches_type(MembershipCreateResponse, membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Gitpod) -> None:
        with client.groups.memberships.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = response.parse()
            assert_matches_type(MembershipCreateResponse, membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Gitpod) -> None:
        membership = client.groups.memberships.list()
        assert_matches_type(SyncMembersPage[GroupMembership], membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Gitpod) -> None:
        membership = client.groups.memberships.list(
            token="token",
            page_size=0,
            group_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
            pagination={
                "token": "token",
                "page_size": 20,
            },
        )
        assert_matches_type(SyncMembersPage[GroupMembership], membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Gitpod) -> None:
        response = client.groups.memberships.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = response.parse()
        assert_matches_type(SyncMembersPage[GroupMembership], membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Gitpod) -> None:
        with client.groups.memberships.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = response.parse()
            assert_matches_type(SyncMembersPage[GroupMembership], membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Gitpod) -> None:
        membership = client.groups.memberships.delete()
        assert_matches_type(object, membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Gitpod) -> None:
        membership = client.groups.memberships.delete(
            membership_id="a1b2c3d4-5678-90ab-cdef-1234567890ab",
        )
        assert_matches_type(object, membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Gitpod) -> None:
        response = client.groups.memberships.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = response.parse()
        assert_matches_type(object, membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Gitpod) -> None:
        with client.groups.memberships.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = response.parse()
            assert_matches_type(object, membership, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMemberships:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncGitpod) -> None:
        membership = await async_client.groups.memberships.create()
        assert_matches_type(MembershipCreateResponse, membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGitpod) -> None:
        membership = await async_client.groups.memberships.create(
            group_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
            subject={
                "id": "f53d2330-3795-4c5d-a1f3-453121af9c60",
                "principal": "PRINCIPAL_USER",
            },
        )
        assert_matches_type(MembershipCreateResponse, membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGitpod) -> None:
        response = await async_client.groups.memberships.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = await response.parse()
        assert_matches_type(MembershipCreateResponse, membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGitpod) -> None:
        async with async_client.groups.memberships.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = await response.parse()
            assert_matches_type(MembershipCreateResponse, membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncGitpod) -> None:
        membership = await async_client.groups.memberships.list()
        assert_matches_type(AsyncMembersPage[GroupMembership], membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGitpod) -> None:
        membership = await async_client.groups.memberships.list(
            token="token",
            page_size=0,
            group_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
            pagination={
                "token": "token",
                "page_size": 20,
            },
        )
        assert_matches_type(AsyncMembersPage[GroupMembership], membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGitpod) -> None:
        response = await async_client.groups.memberships.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = await response.parse()
        assert_matches_type(AsyncMembersPage[GroupMembership], membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGitpod) -> None:
        async with async_client.groups.memberships.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = await response.parse()
            assert_matches_type(AsyncMembersPage[GroupMembership], membership, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncGitpod) -> None:
        membership = await async_client.groups.memberships.delete()
        assert_matches_type(object, membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncGitpod) -> None:
        membership = await async_client.groups.memberships.delete(
            membership_id="a1b2c3d4-5678-90ab-cdef-1234567890ab",
        )
        assert_matches_type(object, membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGitpod) -> None:
        response = await async_client.groups.memberships.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        membership = await response.parse()
        assert_matches_type(object, membership, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGitpod) -> None:
        async with async_client.groups.memberships.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            membership = await response.parse()
            assert_matches_type(object, membership, path=["response"])

        assert cast(Any, response.is_closed) is True
