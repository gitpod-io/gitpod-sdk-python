# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.types import (
    OrganizationListMembersResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrganizations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_leave(self, client: Gitpod) -> None:
        organization = client.organizations.leave(
            connect_protocol_version=1,
        )
        assert_matches_type(object, organization, path=["response"])

    @parametrize
    def test_method_leave_with_all_params(self, client: Gitpod) -> None:
        organization = client.organizations.leave(
            connect_protocol_version=1,
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(object, organization, path=["response"])

    @parametrize
    def test_raw_response_leave(self, client: Gitpod) -> None:
        response = client.organizations.with_raw_response.leave(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(object, organization, path=["response"])

    @parametrize
    def test_streaming_response_leave(self, client: Gitpod) -> None:
        with client.organizations.with_streaming_response.leave(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(object, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_members(self, client: Gitpod) -> None:
        organization = client.organizations.list_members(
            connect_protocol_version=1,
        )
        assert_matches_type(OrganizationListMembersResponse, organization, path=["response"])

    @parametrize
    def test_method_list_members_with_all_params(self, client: Gitpod) -> None:
        organization = client.organizations.list_members(
            connect_protocol_version=1,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            pagination={
                "token": "token",
                "page_size": 100,
            },
            connect_timeout_ms=0,
        )
        assert_matches_type(OrganizationListMembersResponse, organization, path=["response"])

    @parametrize
    def test_raw_response_list_members(self, client: Gitpod) -> None:
        response = client.organizations.with_raw_response.list_members(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(OrganizationListMembersResponse, organization, path=["response"])

    @parametrize
    def test_streaming_response_list_members(self, client: Gitpod) -> None:
        with client.organizations.with_streaming_response.list_members(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(OrganizationListMembersResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_set_role(self, client: Gitpod) -> None:
        organization = client.organizations.set_role(
            connect_protocol_version=1,
        )
        assert_matches_type(object, organization, path=["response"])

    @parametrize
    def test_method_set_role_with_all_params(self, client: Gitpod) -> None:
        organization = client.organizations.set_role(
            connect_protocol_version=1,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            role="ORGANIZATION_ROLE_UNSPECIFIED",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(object, organization, path=["response"])

    @parametrize
    def test_raw_response_set_role(self, client: Gitpod) -> None:
        response = client.organizations.with_raw_response.set_role(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(object, organization, path=["response"])

    @parametrize
    def test_streaming_response_set_role(self, client: Gitpod) -> None:
        with client.organizations.with_streaming_response.set_role(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(object, organization, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOrganizations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_leave(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.leave(
            connect_protocol_version=1,
        )
        assert_matches_type(object, organization, path=["response"])

    @parametrize
    async def test_method_leave_with_all_params(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.leave(
            connect_protocol_version=1,
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(object, organization, path=["response"])

    @parametrize
    async def test_raw_response_leave(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.with_raw_response.leave(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(object, organization, path=["response"])

    @parametrize
    async def test_streaming_response_leave(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.with_streaming_response.leave(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(object, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_members(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.list_members(
            connect_protocol_version=1,
        )
        assert_matches_type(OrganizationListMembersResponse, organization, path=["response"])

    @parametrize
    async def test_method_list_members_with_all_params(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.list_members(
            connect_protocol_version=1,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            pagination={
                "token": "token",
                "page_size": 100,
            },
            connect_timeout_ms=0,
        )
        assert_matches_type(OrganizationListMembersResponse, organization, path=["response"])

    @parametrize
    async def test_raw_response_list_members(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.with_raw_response.list_members(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(OrganizationListMembersResponse, organization, path=["response"])

    @parametrize
    async def test_streaming_response_list_members(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.with_streaming_response.list_members(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(OrganizationListMembersResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_set_role(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.set_role(
            connect_protocol_version=1,
        )
        assert_matches_type(object, organization, path=["response"])

    @parametrize
    async def test_method_set_role_with_all_params(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.set_role(
            connect_protocol_version=1,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            role="ORGANIZATION_ROLE_UNSPECIFIED",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(object, organization, path=["response"])

    @parametrize
    async def test_raw_response_set_role(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.with_raw_response.set_role(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(object, organization, path=["response"])

    @parametrize
    async def test_streaming_response_set_role(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.with_streaming_response.set_role(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(object, organization, path=["response"])

        assert cast(Any, response.is_closed) is True
