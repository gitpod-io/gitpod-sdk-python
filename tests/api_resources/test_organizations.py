# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.types import (
    OrganizationJoinResponse,
    OrganizationListResponse,
    OrganizationCreateResponse,
    OrganizationUpdateResponse,
    OrganizationRetrieveResponse,
    OrganizationListMembersResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrganizations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gitpod) -> None:
        organization = client.organizations.create(
            connect_protocol_version=1,
        )
        assert_matches_type(OrganizationCreateResponse, organization, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gitpod) -> None:
        organization = client.organizations.create(
            connect_protocol_version=1,
            invite_accounts_with_matching_domain=True,
            join_organization=True,
            name="xxx",
            connect_timeout_ms=0,
        )
        assert_matches_type(OrganizationCreateResponse, organization, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gitpod) -> None:
        response = client.organizations.with_raw_response.create(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(OrganizationCreateResponse, organization, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gitpod) -> None:
        with client.organizations.with_streaming_response.create(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(OrganizationCreateResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Gitpod) -> None:
        organization = client.organizations.retrieve(
            encoding="proto",
            connect_protocol_version=1,
        )
        assert_matches_type(OrganizationRetrieveResponse, organization, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Gitpod) -> None:
        organization = client.organizations.retrieve(
            encoding="proto",
            connect_protocol_version=1,
            base64=True,
            compression="identity",
            connect="v1",
            message="message",
            connect_timeout_ms=0,
        )
        assert_matches_type(OrganizationRetrieveResponse, organization, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Gitpod) -> None:
        response = client.organizations.with_raw_response.retrieve(
            encoding="proto",
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(OrganizationRetrieveResponse, organization, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Gitpod) -> None:
        with client.organizations.with_streaming_response.retrieve(
            encoding="proto",
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(OrganizationRetrieveResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Gitpod) -> None:
        organization = client.organizations.update(
            body={},
            connect_protocol_version=1,
        )
        assert_matches_type(OrganizationUpdateResponse, organization, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Gitpod) -> None:
        organization = client.organizations.update(
            body={
                "inviteDomains": {"domains": ["sfN2.l.iJR-BU.u9JV9.a.m.o2D-4b-Jd.0Z-kX.L.n.S.f.UKbxB"]},
                "name": "name",
                "organizationId": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            connect_protocol_version=1,
            connect_timeout_ms=0,
        )
        assert_matches_type(OrganizationUpdateResponse, organization, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Gitpod) -> None:
        response = client.organizations.with_raw_response.update(
            body={},
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(OrganizationUpdateResponse, organization, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Gitpod) -> None:
        with client.organizations.with_streaming_response.update(
            body={},
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(OrganizationUpdateResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gitpod) -> None:
        organization = client.organizations.list(
            encoding="proto",
            connect_protocol_version=1,
        )
        assert_matches_type(OrganizationListResponse, organization, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gitpod) -> None:
        organization = client.organizations.list(
            encoding="proto",
            connect_protocol_version=1,
            base64=True,
            compression="identity",
            connect="v1",
            message="message",
            connect_timeout_ms=0,
        )
        assert_matches_type(OrganizationListResponse, organization, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gitpod) -> None:
        response = client.organizations.with_raw_response.list(
            encoding="proto",
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(OrganizationListResponse, organization, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gitpod) -> None:
        with client.organizations.with_streaming_response.list(
            encoding="proto",
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(OrganizationListResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gitpod) -> None:
        organization = client.organizations.delete(
            connect_protocol_version=1,
        )
        assert_matches_type(object, organization, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Gitpod) -> None:
        organization = client.organizations.delete(
            connect_protocol_version=1,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(object, organization, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gitpod) -> None:
        response = client.organizations.with_raw_response.delete(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(object, organization, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gitpod) -> None:
        with client.organizations.with_streaming_response.delete(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(object, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_join_overload_1(self, client: Gitpod) -> None:
        organization = client.organizations.join(
            invite_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_protocol_version=1,
        )
        assert_matches_type(OrganizationJoinResponse, organization, path=["response"])

    @parametrize
    def test_method_join_with_all_params_overload_1(self, client: Gitpod) -> None:
        organization = client.organizations.join(
            invite_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_protocol_version=1,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(OrganizationJoinResponse, organization, path=["response"])

    @parametrize
    def test_raw_response_join_overload_1(self, client: Gitpod) -> None:
        response = client.organizations.with_raw_response.join(
            invite_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(OrganizationJoinResponse, organization, path=["response"])

    @parametrize
    def test_streaming_response_join_overload_1(self, client: Gitpod) -> None:
        with client.organizations.with_streaming_response.join(
            invite_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(OrganizationJoinResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_join_overload_2(self, client: Gitpod) -> None:
        organization = client.organizations.join(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_protocol_version=1,
        )
        assert_matches_type(OrganizationJoinResponse, organization, path=["response"])

    @parametrize
    def test_method_join_with_all_params_overload_2(self, client: Gitpod) -> None:
        organization = client.organizations.join(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_protocol_version=1,
            invite_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(OrganizationJoinResponse, organization, path=["response"])

    @parametrize
    def test_raw_response_join_overload_2(self, client: Gitpod) -> None:
        response = client.organizations.with_raw_response.join(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(OrganizationJoinResponse, organization, path=["response"])

    @parametrize
    def test_streaming_response_join_overload_2(self, client: Gitpod) -> None:
        with client.organizations.with_streaming_response.join(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(OrganizationJoinResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_join_overload_3(self, client: Gitpod) -> None:
        organization = client.organizations.join(
            connect_protocol_version=1,
        )
        assert_matches_type(OrganizationJoinResponse, organization, path=["response"])

    @parametrize
    def test_method_join_with_all_params_overload_3(self, client: Gitpod) -> None:
        organization = client.organizations.join(
            connect_protocol_version=1,
            invite_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(OrganizationJoinResponse, organization, path=["response"])

    @parametrize
    def test_raw_response_join_overload_3(self, client: Gitpod) -> None:
        response = client.organizations.with_raw_response.join(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(OrganizationJoinResponse, organization, path=["response"])

    @parametrize
    def test_streaming_response_join_overload_3(self, client: Gitpod) -> None:
        with client.organizations.with_streaming_response.join(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(OrganizationJoinResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

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
            encoding="proto",
            connect_protocol_version=1,
        )
        assert_matches_type(OrganizationListMembersResponse, organization, path=["response"])

    @parametrize
    def test_method_list_members_with_all_params(self, client: Gitpod) -> None:
        organization = client.organizations.list_members(
            encoding="proto",
            connect_protocol_version=1,
            base64=True,
            compression="identity",
            connect="v1",
            message="message",
            connect_timeout_ms=0,
        )
        assert_matches_type(OrganizationListMembersResponse, organization, path=["response"])

    @parametrize
    def test_raw_response_list_members(self, client: Gitpod) -> None:
        response = client.organizations.with_raw_response.list_members(
            encoding="proto",
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(OrganizationListMembersResponse, organization, path=["response"])

    @parametrize
    def test_streaming_response_list_members(self, client: Gitpod) -> None:
        with client.organizations.with_streaming_response.list_members(
            encoding="proto",
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
    async def test_method_create(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.create(
            connect_protocol_version=1,
        )
        assert_matches_type(OrganizationCreateResponse, organization, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.create(
            connect_protocol_version=1,
            invite_accounts_with_matching_domain=True,
            join_organization=True,
            name="xxx",
            connect_timeout_ms=0,
        )
        assert_matches_type(OrganizationCreateResponse, organization, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.with_raw_response.create(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(OrganizationCreateResponse, organization, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.with_streaming_response.create(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(OrganizationCreateResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.retrieve(
            encoding="proto",
            connect_protocol_version=1,
        )
        assert_matches_type(OrganizationRetrieveResponse, organization, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.retrieve(
            encoding="proto",
            connect_protocol_version=1,
            base64=True,
            compression="identity",
            connect="v1",
            message="message",
            connect_timeout_ms=0,
        )
        assert_matches_type(OrganizationRetrieveResponse, organization, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.with_raw_response.retrieve(
            encoding="proto",
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(OrganizationRetrieveResponse, organization, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.with_streaming_response.retrieve(
            encoding="proto",
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(OrganizationRetrieveResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.update(
            body={},
            connect_protocol_version=1,
        )
        assert_matches_type(OrganizationUpdateResponse, organization, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.update(
            body={
                "inviteDomains": {"domains": ["sfN2.l.iJR-BU.u9JV9.a.m.o2D-4b-Jd.0Z-kX.L.n.S.f.UKbxB"]},
                "name": "name",
                "organizationId": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            connect_protocol_version=1,
            connect_timeout_ms=0,
        )
        assert_matches_type(OrganizationUpdateResponse, organization, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.with_raw_response.update(
            body={},
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(OrganizationUpdateResponse, organization, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.with_streaming_response.update(
            body={},
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(OrganizationUpdateResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.list(
            encoding="proto",
            connect_protocol_version=1,
        )
        assert_matches_type(OrganizationListResponse, organization, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.list(
            encoding="proto",
            connect_protocol_version=1,
            base64=True,
            compression="identity",
            connect="v1",
            message="message",
            connect_timeout_ms=0,
        )
        assert_matches_type(OrganizationListResponse, organization, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.with_raw_response.list(
            encoding="proto",
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(OrganizationListResponse, organization, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.with_streaming_response.list(
            encoding="proto",
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(OrganizationListResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.delete(
            connect_protocol_version=1,
        )
        assert_matches_type(object, organization, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.delete(
            connect_protocol_version=1,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(object, organization, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.with_raw_response.delete(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(object, organization, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.with_streaming_response.delete(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(object, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_join_overload_1(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.join(
            invite_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_protocol_version=1,
        )
        assert_matches_type(OrganizationJoinResponse, organization, path=["response"])

    @parametrize
    async def test_method_join_with_all_params_overload_1(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.join(
            invite_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_protocol_version=1,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(OrganizationJoinResponse, organization, path=["response"])

    @parametrize
    async def test_raw_response_join_overload_1(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.with_raw_response.join(
            invite_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(OrganizationJoinResponse, organization, path=["response"])

    @parametrize
    async def test_streaming_response_join_overload_1(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.with_streaming_response.join(
            invite_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(OrganizationJoinResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_join_overload_2(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.join(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_protocol_version=1,
        )
        assert_matches_type(OrganizationJoinResponse, organization, path=["response"])

    @parametrize
    async def test_method_join_with_all_params_overload_2(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.join(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_protocol_version=1,
            invite_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(OrganizationJoinResponse, organization, path=["response"])

    @parametrize
    async def test_raw_response_join_overload_2(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.with_raw_response.join(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(OrganizationJoinResponse, organization, path=["response"])

    @parametrize
    async def test_streaming_response_join_overload_2(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.with_streaming_response.join(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(OrganizationJoinResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_join_overload_3(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.join(
            connect_protocol_version=1,
        )
        assert_matches_type(OrganizationJoinResponse, organization, path=["response"])

    @parametrize
    async def test_method_join_with_all_params_overload_3(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.join(
            connect_protocol_version=1,
            invite_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            connect_timeout_ms=0,
        )
        assert_matches_type(OrganizationJoinResponse, organization, path=["response"])

    @parametrize
    async def test_raw_response_join_overload_3(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.with_raw_response.join(
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(OrganizationJoinResponse, organization, path=["response"])

    @parametrize
    async def test_streaming_response_join_overload_3(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.with_streaming_response.join(
            connect_protocol_version=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(OrganizationJoinResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

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
            encoding="proto",
            connect_protocol_version=1,
        )
        assert_matches_type(OrganizationListMembersResponse, organization, path=["response"])

    @parametrize
    async def test_method_list_members_with_all_params(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.list_members(
            encoding="proto",
            connect_protocol_version=1,
            base64=True,
            compression="identity",
            connect="v1",
            message="message",
            connect_timeout_ms=0,
        )
        assert_matches_type(OrganizationListMembersResponse, organization, path=["response"])

    @parametrize
    async def test_raw_response_list_members(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.with_raw_response.list_members(
            encoding="proto",
            connect_protocol_version=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(OrganizationListMembersResponse, organization, path=["response"])

    @parametrize
    async def test_streaming_response_list_members(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.with_streaming_response.list_members(
            encoding="proto",
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
