# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.types import (
    Organization,
    OrganizationMember,
    OrganizationJoinResponse,
    OrganizationCreateResponse,
    OrganizationUpdateResponse,
    OrganizationRetrieveResponse,
)
from gitpod.pagination import SyncMembersPage, AsyncMembersPage, SyncOrganizationsPage, AsyncOrganizationsPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrganizations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Gitpod) -> None:
        organization = client.organizations.create(
            name="Acme Corp Engineering",
        )
        assert_matches_type(OrganizationCreateResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Gitpod) -> None:
        organization = client.organizations.create(
            name="Acme Corp Engineering",
            invite_accounts_with_matching_domain=True,
            join_organization=True,
        )
        assert_matches_type(OrganizationCreateResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Gitpod) -> None:
        response = client.organizations.with_raw_response.create(
            name="Acme Corp Engineering",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(OrganizationCreateResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Gitpod) -> None:
        with client.organizations.with_streaming_response.create(
            name="Acme Corp Engineering",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(OrganizationCreateResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Gitpod) -> None:
        organization = client.organizations.retrieve(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(OrganizationRetrieveResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Gitpod) -> None:
        response = client.organizations.with_raw_response.retrieve(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(OrganizationRetrieveResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Gitpod) -> None:
        with client.organizations.with_streaming_response.retrieve(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(OrganizationRetrieveResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Gitpod) -> None:
        organization = client.organizations.update(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(OrganizationUpdateResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Gitpod) -> None:
        organization = client.organizations.update(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            invite_domains={"domains": ["sfN2.l.iJR-BU.u9JV9.a.m.o2D-4b-Jd.0Z-kX.L.n.S.f.UKbxB"]},
            name="name",
        )
        assert_matches_type(OrganizationUpdateResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Gitpod) -> None:
        response = client.organizations.with_raw_response.update(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(OrganizationUpdateResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Gitpod) -> None:
        with client.organizations.with_streaming_response.update(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(OrganizationUpdateResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Gitpod) -> None:
        organization = client.organizations.list()
        assert_matches_type(SyncOrganizationsPage[Organization], organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Gitpod) -> None:
        organization = client.organizations.list(
            token="token",
            page_size=0,
            pagination={
                "token": "token",
                "page_size": 50,
            },
            scope="SCOPE_UNSPECIFIED",
        )
        assert_matches_type(SyncOrganizationsPage[Organization], organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Gitpod) -> None:
        response = client.organizations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(SyncOrganizationsPage[Organization], organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Gitpod) -> None:
        with client.organizations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(SyncOrganizationsPage[Organization], organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Gitpod) -> None:
        organization = client.organizations.delete(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(object, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Gitpod) -> None:
        response = client.organizations.with_raw_response.delete(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(object, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Gitpod) -> None:
        with client.organizations.with_streaming_response.delete(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(object, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_join(self, client: Gitpod) -> None:
        organization = client.organizations.join()
        assert_matches_type(OrganizationJoinResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_join_with_all_params(self, client: Gitpod) -> None:
        organization = client.organizations.join(
            invite_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(OrganizationJoinResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_join(self, client: Gitpod) -> None:
        response = client.organizations.with_raw_response.join()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(OrganizationJoinResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_join(self, client: Gitpod) -> None:
        with client.organizations.with_streaming_response.join() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(OrganizationJoinResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_leave(self, client: Gitpod) -> None:
        organization = client.organizations.leave(
            user_id="f53d2330-3795-4c5d-a1f3-453121af9c60",
        )
        assert_matches_type(object, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_leave(self, client: Gitpod) -> None:
        response = client.organizations.with_raw_response.leave(
            user_id="f53d2330-3795-4c5d-a1f3-453121af9c60",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(object, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_leave(self, client: Gitpod) -> None:
        with client.organizations.with_streaming_response.leave(
            user_id="f53d2330-3795-4c5d-a1f3-453121af9c60",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(object, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_members(self, client: Gitpod) -> None:
        organization = client.organizations.list_members(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(SyncMembersPage[OrganizationMember], organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_members_with_all_params(self, client: Gitpod) -> None:
        organization = client.organizations.list_members(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            token="token",
            page_size=0,
            pagination={
                "token": "token",
                "page_size": 20,
            },
        )
        assert_matches_type(SyncMembersPage[OrganizationMember], organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_members(self, client: Gitpod) -> None:
        response = client.organizations.with_raw_response.list_members(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(SyncMembersPage[OrganizationMember], organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_members(self, client: Gitpod) -> None:
        with client.organizations.with_streaming_response.list_members(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(SyncMembersPage[OrganizationMember], organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_set_role(self, client: Gitpod) -> None:
        organization = client.organizations.set_role(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            user_id="f53d2330-3795-4c5d-a1f3-453121af9c60",
        )
        assert_matches_type(object, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_set_role_with_all_params(self, client: Gitpod) -> None:
        organization = client.organizations.set_role(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            user_id="f53d2330-3795-4c5d-a1f3-453121af9c60",
            role="ORGANIZATION_ROLE_UNSPECIFIED",
        )
        assert_matches_type(object, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_set_role(self, client: Gitpod) -> None:
        response = client.organizations.with_raw_response.set_role(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            user_id="f53d2330-3795-4c5d-a1f3-453121af9c60",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(object, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_set_role(self, client: Gitpod) -> None:
        with client.organizations.with_streaming_response.set_role(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            user_id="f53d2330-3795-4c5d-a1f3-453121af9c60",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(object, organization, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOrganizations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.create(
            name="Acme Corp Engineering",
        )
        assert_matches_type(OrganizationCreateResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.create(
            name="Acme Corp Engineering",
            invite_accounts_with_matching_domain=True,
            join_organization=True,
        )
        assert_matches_type(OrganizationCreateResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.with_raw_response.create(
            name="Acme Corp Engineering",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(OrganizationCreateResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.with_streaming_response.create(
            name="Acme Corp Engineering",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(OrganizationCreateResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.retrieve(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(OrganizationRetrieveResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.with_raw_response.retrieve(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(OrganizationRetrieveResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.with_streaming_response.retrieve(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(OrganizationRetrieveResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.update(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(OrganizationUpdateResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.update(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            invite_domains={"domains": ["sfN2.l.iJR-BU.u9JV9.a.m.o2D-4b-Jd.0Z-kX.L.n.S.f.UKbxB"]},
            name="name",
        )
        assert_matches_type(OrganizationUpdateResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.with_raw_response.update(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(OrganizationUpdateResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.with_streaming_response.update(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(OrganizationUpdateResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.list()
        assert_matches_type(AsyncOrganizationsPage[Organization], organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.list(
            token="token",
            page_size=0,
            pagination={
                "token": "token",
                "page_size": 50,
            },
            scope="SCOPE_UNSPECIFIED",
        )
        assert_matches_type(AsyncOrganizationsPage[Organization], organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(AsyncOrganizationsPage[Organization], organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(AsyncOrganizationsPage[Organization], organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.delete(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(object, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.with_raw_response.delete(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(object, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.with_streaming_response.delete(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(object, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_join(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.join()
        assert_matches_type(OrganizationJoinResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_join_with_all_params(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.join(
            invite_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(OrganizationJoinResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_join(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.with_raw_response.join()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(OrganizationJoinResponse, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_join(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.with_streaming_response.join() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(OrganizationJoinResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_leave(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.leave(
            user_id="f53d2330-3795-4c5d-a1f3-453121af9c60",
        )
        assert_matches_type(object, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_leave(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.with_raw_response.leave(
            user_id="f53d2330-3795-4c5d-a1f3-453121af9c60",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(object, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_leave(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.with_streaming_response.leave(
            user_id="f53d2330-3795-4c5d-a1f3-453121af9c60",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(object, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_members(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.list_members(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(AsyncMembersPage[OrganizationMember], organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_members_with_all_params(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.list_members(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            token="token",
            page_size=0,
            pagination={
                "token": "token",
                "page_size": 20,
            },
        )
        assert_matches_type(AsyncMembersPage[OrganizationMember], organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_members(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.with_raw_response.list_members(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(AsyncMembersPage[OrganizationMember], organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_members(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.with_streaming_response.list_members(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(AsyncMembersPage[OrganizationMember], organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_set_role(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.set_role(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            user_id="f53d2330-3795-4c5d-a1f3-453121af9c60",
        )
        assert_matches_type(object, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_set_role_with_all_params(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.set_role(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            user_id="f53d2330-3795-4c5d-a1f3-453121af9c60",
            role="ORGANIZATION_ROLE_UNSPECIFIED",
        )
        assert_matches_type(object, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_set_role(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.with_raw_response.set_role(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            user_id="f53d2330-3795-4c5d-a1f3-453121af9c60",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(object, organization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_set_role(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.with_streaming_response.set_role(
            organization_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
            user_id="f53d2330-3795-4c5d-a1f3-453121af9c60",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(object, organization, path=["response"])

        assert cast(Any, response.is_closed) is True
