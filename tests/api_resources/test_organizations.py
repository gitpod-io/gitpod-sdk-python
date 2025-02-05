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
from gitpod.pagination import SyncPersonalAccessTokensPage, AsyncPersonalAccessTokensPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrganizations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Gitpod) -> None:
        organization = client.organizations.create()
        assert_matches_type(OrganizationCreateResponse, organization, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Gitpod) -> None:
        organization = client.organizations.create(
            invite_accounts_with_matching_domain=True,
            join_organization=True,
            name="xxx",
        )
        assert_matches_type(OrganizationCreateResponse, organization, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Gitpod) -> None:
        response = client.organizations.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(OrganizationCreateResponse, organization, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Gitpod) -> None:
        with client.organizations.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(OrganizationCreateResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Gitpod) -> None:
        organization = client.organizations.retrieve()
        assert_matches_type(OrganizationRetrieveResponse, organization, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Gitpod) -> None:
        organization = client.organizations.retrieve(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(OrganizationRetrieveResponse, organization, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Gitpod) -> None:
        response = client.organizations.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(OrganizationRetrieveResponse, organization, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Gitpod) -> None:
        with client.organizations.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(OrganizationRetrieveResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_overload_1(self, client: Gitpod) -> None:
        organization = client.organizations.update(
            invite_domains={},
        )
        assert_matches_type(OrganizationUpdateResponse, organization, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_1(self, client: Gitpod) -> None:
        organization = client.organizations.update(
            invite_domains={"domains": ["sfN2.l.iJR-BU.u9JV9.a.m.o2D-4b-Jd.0Z-kX.L.n.S.f.UKbxB"]},
        )
        assert_matches_type(OrganizationUpdateResponse, organization, path=["response"])

    @parametrize
    def test_raw_response_update_overload_1(self, client: Gitpod) -> None:
        response = client.organizations.with_raw_response.update(
            invite_domains={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(OrganizationUpdateResponse, organization, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_1(self, client: Gitpod) -> None:
        with client.organizations.with_streaming_response.update(
            invite_domains={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(OrganizationUpdateResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_overload_2(self, client: Gitpod) -> None:
        organization = client.organizations.update(
            name="name",
        )
        assert_matches_type(OrganizationUpdateResponse, organization, path=["response"])

    @parametrize
    def test_raw_response_update_overload_2(self, client: Gitpod) -> None:
        response = client.organizations.with_raw_response.update(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(OrganizationUpdateResponse, organization, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_2(self, client: Gitpod) -> None:
        with client.organizations.with_streaming_response.update(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(OrganizationUpdateResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Gitpod) -> None:
        organization = client.organizations.list()
        assert_matches_type(SyncPersonalAccessTokensPage[OrganizationListResponse], organization, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Gitpod) -> None:
        organization = client.organizations.list(
            token="token",
            page_size=0,
            pagination={
                "token": "token",
                "page_size": 100,
            },
            scope="SCOPE_UNSPECIFIED",
        )
        assert_matches_type(SyncPersonalAccessTokensPage[OrganizationListResponse], organization, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Gitpod) -> None:
        response = client.organizations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(SyncPersonalAccessTokensPage[OrganizationListResponse], organization, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Gitpod) -> None:
        with client.organizations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(SyncPersonalAccessTokensPage[OrganizationListResponse], organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Gitpod) -> None:
        organization = client.organizations.delete()
        assert_matches_type(object, organization, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Gitpod) -> None:
        organization = client.organizations.delete(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, organization, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Gitpod) -> None:
        response = client.organizations.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(object, organization, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Gitpod) -> None:
        with client.organizations.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(object, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_join_overload_1(self, client: Gitpod) -> None:
        organization = client.organizations.join(
            invite_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(OrganizationJoinResponse, organization, path=["response"])

    @parametrize
    def test_raw_response_join_overload_1(self, client: Gitpod) -> None:
        response = client.organizations.with_raw_response.join(
            invite_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(OrganizationJoinResponse, organization, path=["response"])

    @parametrize
    def test_streaming_response_join_overload_1(self, client: Gitpod) -> None:
        with client.organizations.with_streaming_response.join(
            invite_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
        )
        assert_matches_type(OrganizationJoinResponse, organization, path=["response"])

    @parametrize
    def test_raw_response_join_overload_2(self, client: Gitpod) -> None:
        response = client.organizations.with_raw_response.join(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(OrganizationJoinResponse, organization, path=["response"])

    @parametrize
    def test_streaming_response_join_overload_2(self, client: Gitpod) -> None:
        with client.organizations.with_streaming_response.join(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(OrganizationJoinResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_leave(self, client: Gitpod) -> None:
        organization = client.organizations.leave()
        assert_matches_type(object, organization, path=["response"])

    @parametrize
    def test_method_leave_with_all_params(self, client: Gitpod) -> None:
        organization = client.organizations.leave(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, organization, path=["response"])

    @parametrize
    def test_raw_response_leave(self, client: Gitpod) -> None:
        response = client.organizations.with_raw_response.leave()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(object, organization, path=["response"])

    @parametrize
    def test_streaming_response_leave(self, client: Gitpod) -> None:
        with client.organizations.with_streaming_response.leave() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(object, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_members(self, client: Gitpod) -> None:
        organization = client.organizations.list_members()
        assert_matches_type(
            SyncPersonalAccessTokensPage[OrganizationListMembersResponse], organization, path=["response"]
        )

    @parametrize
    def test_method_list_members_with_all_params(self, client: Gitpod) -> None:
        organization = client.organizations.list_members(
            token="token",
            page_size=0,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            pagination={
                "token": "token",
                "page_size": 100,
            },
        )
        assert_matches_type(
            SyncPersonalAccessTokensPage[OrganizationListMembersResponse], organization, path=["response"]
        )

    @parametrize
    def test_raw_response_list_members(self, client: Gitpod) -> None:
        response = client.organizations.with_raw_response.list_members()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(
            SyncPersonalAccessTokensPage[OrganizationListMembersResponse], organization, path=["response"]
        )

    @parametrize
    def test_streaming_response_list_members(self, client: Gitpod) -> None:
        with client.organizations.with_streaming_response.list_members() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(
                SyncPersonalAccessTokensPage[OrganizationListMembersResponse], organization, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_set_role(self, client: Gitpod) -> None:
        organization = client.organizations.set_role()
        assert_matches_type(object, organization, path=["response"])

    @parametrize
    def test_method_set_role_with_all_params(self, client: Gitpod) -> None:
        organization = client.organizations.set_role(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            role="ORGANIZATION_ROLE_UNSPECIFIED",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, organization, path=["response"])

    @parametrize
    def test_raw_response_set_role(self, client: Gitpod) -> None:
        response = client.organizations.with_raw_response.set_role()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = response.parse()
        assert_matches_type(object, organization, path=["response"])

    @parametrize
    def test_streaming_response_set_role(self, client: Gitpod) -> None:
        with client.organizations.with_streaming_response.set_role() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = response.parse()
            assert_matches_type(object, organization, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOrganizations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.create()
        assert_matches_type(OrganizationCreateResponse, organization, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.create(
            invite_accounts_with_matching_domain=True,
            join_organization=True,
            name="xxx",
        )
        assert_matches_type(OrganizationCreateResponse, organization, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(OrganizationCreateResponse, organization, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(OrganizationCreateResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.retrieve()
        assert_matches_type(OrganizationRetrieveResponse, organization, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.retrieve(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(OrganizationRetrieveResponse, organization, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(OrganizationRetrieveResponse, organization, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(OrganizationRetrieveResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.update(
            invite_domains={},
        )
        assert_matches_type(OrganizationUpdateResponse, organization, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_1(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.update(
            invite_domains={"domains": ["sfN2.l.iJR-BU.u9JV9.a.m.o2D-4b-Jd.0Z-kX.L.n.S.f.UKbxB"]},
        )
        assert_matches_type(OrganizationUpdateResponse, organization, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.with_raw_response.update(
            invite_domains={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(OrganizationUpdateResponse, organization, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.with_streaming_response.update(
            invite_domains={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(OrganizationUpdateResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.update(
            name="name",
        )
        assert_matches_type(OrganizationUpdateResponse, organization, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.with_raw_response.update(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(OrganizationUpdateResponse, organization, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.with_streaming_response.update(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(OrganizationUpdateResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.list()
        assert_matches_type(AsyncPersonalAccessTokensPage[OrganizationListResponse], organization, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.list(
            token="token",
            page_size=0,
            pagination={
                "token": "token",
                "page_size": 100,
            },
            scope="SCOPE_UNSPECIFIED",
        )
        assert_matches_type(AsyncPersonalAccessTokensPage[OrganizationListResponse], organization, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(AsyncPersonalAccessTokensPage[OrganizationListResponse], organization, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(
                AsyncPersonalAccessTokensPage[OrganizationListResponse], organization, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.delete()
        assert_matches_type(object, organization, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.delete(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, organization, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(object, organization, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(object, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_join_overload_1(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.join(
            invite_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(OrganizationJoinResponse, organization, path=["response"])

    @parametrize
    async def test_raw_response_join_overload_1(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.with_raw_response.join(
            invite_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(OrganizationJoinResponse, organization, path=["response"])

    @parametrize
    async def test_streaming_response_join_overload_1(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.with_streaming_response.join(
            invite_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
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
        )
        assert_matches_type(OrganizationJoinResponse, organization, path=["response"])

    @parametrize
    async def test_raw_response_join_overload_2(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.with_raw_response.join(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(OrganizationJoinResponse, organization, path=["response"])

    @parametrize
    async def test_streaming_response_join_overload_2(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.with_streaming_response.join(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(OrganizationJoinResponse, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_leave(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.leave()
        assert_matches_type(object, organization, path=["response"])

    @parametrize
    async def test_method_leave_with_all_params(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.leave(
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, organization, path=["response"])

    @parametrize
    async def test_raw_response_leave(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.with_raw_response.leave()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(object, organization, path=["response"])

    @parametrize
    async def test_streaming_response_leave(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.with_streaming_response.leave() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(object, organization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_members(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.list_members()
        assert_matches_type(
            AsyncPersonalAccessTokensPage[OrganizationListMembersResponse], organization, path=["response"]
        )

    @parametrize
    async def test_method_list_members_with_all_params(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.list_members(
            token="token",
            page_size=0,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            pagination={
                "token": "token",
                "page_size": 100,
            },
        )
        assert_matches_type(
            AsyncPersonalAccessTokensPage[OrganizationListMembersResponse], organization, path=["response"]
        )

    @parametrize
    async def test_raw_response_list_members(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.with_raw_response.list_members()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(
            AsyncPersonalAccessTokensPage[OrganizationListMembersResponse], organization, path=["response"]
        )

    @parametrize
    async def test_streaming_response_list_members(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.with_streaming_response.list_members() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(
                AsyncPersonalAccessTokensPage[OrganizationListMembersResponse], organization, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_set_role(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.set_role()
        assert_matches_type(object, organization, path=["response"])

    @parametrize
    async def test_method_set_role_with_all_params(self, async_client: AsyncGitpod) -> None:
        organization = await async_client.organizations.set_role(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            role="ORGANIZATION_ROLE_UNSPECIFIED",
            user_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, organization, path=["response"])

    @parametrize
    async def test_raw_response_set_role(self, async_client: AsyncGitpod) -> None:
        response = await async_client.organizations.with_raw_response.set_role()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organization = await response.parse()
        assert_matches_type(object, organization, path=["response"])

    @parametrize
    async def test_streaming_response_set_role(self, async_client: AsyncGitpod) -> None:
        async with async_client.organizations.with_streaming_response.set_role() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organization = await response.parse()
            assert_matches_type(object, organization, path=["response"])

        assert cast(Any, response.is_closed) is True
