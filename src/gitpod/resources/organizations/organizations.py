# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, overload

import httpx

from ...types import (
    organization_join_params,
    organization_list_params,
    organization_leave_params,
    organization_create_params,
    organization_delete_params,
    organization_update_params,
    organization_retrieve_params,
    organization_set_role_params,
    organization_list_members_params,
)
from .invites import (
    InvitesResource,
    AsyncInvitesResource,
    InvitesResourceWithRawResponse,
    AsyncInvitesResourceWithRawResponse,
    InvitesResourceWithStreamingResponse,
    AsyncInvitesResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    required_args,
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncMembersPage, AsyncMembersPage, SyncOrganizationsPage, AsyncOrganizationsPage
from ..._base_client import AsyncPaginator, make_request_options
from .sso_configurations import (
    SSOConfigurationsResource,
    AsyncSSOConfigurationsResource,
    SSOConfigurationsResourceWithRawResponse,
    AsyncSSOConfigurationsResourceWithRawResponse,
    SSOConfigurationsResourceWithStreamingResponse,
    AsyncSSOConfigurationsResourceWithStreamingResponse,
)
from ...types.organization_join_response import OrganizationJoinResponse
from ...types.organization_list_response import OrganizationListResponse
from ...types.organization_create_response import OrganizationCreateResponse
from ...types.organization_update_response import OrganizationUpdateResponse
from ...types.organization_retrieve_response import OrganizationRetrieveResponse
from ...types.organization_list_members_response import OrganizationListMembersResponse

__all__ = ["OrganizationsResource", "AsyncOrganizationsResource"]


class OrganizationsResource(SyncAPIResource):
    @cached_property
    def invites(self) -> InvitesResource:
        return InvitesResource(self._client)

    @cached_property
    def sso_configurations(self) -> SSOConfigurationsResource:
        return SSOConfigurationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> OrganizationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return OrganizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrganizationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return OrganizationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        invite_accounts_with_matching_domain: bool | NotGiven = NOT_GIVEN,
        join_organization: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationCreateResponse:
        """
        CreateOrganization creates a new Organization.

        Args:
          invite_accounts_with_matching_domain: Should other Accounts with the same domain be automatically invited to the
              organization?

          join_organization: join_organization decides whether the Identity issuing this request joins the
              org on creation

          name: name is the organization name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.OrganizationService/CreateOrganization",
            body=maybe_transform(
                {
                    "invite_accounts_with_matching_domain": invite_accounts_with_matching_domain,
                    "join_organization": join_organization,
                    "name": name,
                },
                organization_create_params.OrganizationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationCreateResponse,
        )

    def retrieve(
        self,
        *,
        organization_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationRetrieveResponse:
        """
        GetOrganization retrieves a single Organization.

        Args:
          organization_id: organization_id is the unique identifier of the Organization to retreive.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.OrganizationService/GetOrganization",
            body=maybe_transform(
                {"organization_id": organization_id}, organization_retrieve_params.OrganizationRetrieveParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationRetrieveResponse,
        )

    @overload
    def update(
        self,
        *,
        invite_domains: organization_update_params.InviteDomainsIsTheDomainAllowlistOfTheOrganizationInviteDomains,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationUpdateResponse:
        """
        UpdateOrganization updates the properties of an Organization.

        Args:
          invite_domains: invite_domains is the domain allowlist of the organization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationUpdateResponse:
        """
        UpdateOrganization updates the properties of an Organization.

        Args:
          name: name is the new name of the organization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["invite_domains"], ["name"])
    def update(
        self,
        *,
        invite_domains: organization_update_params.InviteDomainsIsTheDomainAllowlistOfTheOrganizationInviteDomains
        | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationUpdateResponse:
        return self._post(
            "/gitpod.v1.OrganizationService/UpdateOrganization",
            body=maybe_transform(
                {
                    "invite_domains": invite_domains,
                    "name": name,
                },
                organization_update_params.OrganizationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationUpdateResponse,
        )

    def list(
        self,
        *,
        token: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        pagination: organization_list_params.Pagination | NotGiven = NOT_GIVEN,
        scope: Literal["SCOPE_UNSPECIFIED", "SCOPE_MEMBER", "SCOPE_ALL"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOrganizationsPage[OrganizationListResponse]:
        """
        ListOrganizations lists all organization the caller has access to.

        Args:
          pagination: pagination contains the pagination options for listing organizations

          scope: scope is the scope of the organizations to list

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.OrganizationService/ListOrganizations",
            page=SyncOrganizationsPage[OrganizationListResponse],
            body=maybe_transform(
                {
                    "pagination": pagination,
                    "scope": scope,
                },
                organization_list_params.OrganizationListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "token": token,
                        "page_size": page_size,
                    },
                    organization_list_params.OrganizationListParams,
                ),
            ),
            model=OrganizationListResponse,
            method="post",
        )

    def delete(
        self,
        *,
        organization_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        DeleteOrganization deletes the specified organization.

        Args:
          organization_id: organization_id is the ID of the organization to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.OrganizationService/DeleteOrganization",
            body=maybe_transform(
                {"organization_id": organization_id}, organization_delete_params.OrganizationDeleteParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    @overload
    def join(
        self,
        *,
        invite_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationJoinResponse:
        """
        JoinOrganization lets accounts join an Organization.

        Args:
          invite_id: invite_id is the unique identifier of the invite to join the organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def join(
        self,
        *,
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationJoinResponse:
        """
        JoinOrganization lets accounts join an Organization.

        Args:
          organization_id: organization_id is the unique identifier of the Organization to join.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["invite_id"], ["organization_id"])
    def join(
        self,
        *,
        invite_id: str | NotGiven = NOT_GIVEN,
        organization_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationJoinResponse:
        return self._post(
            "/gitpod.v1.OrganizationService/JoinOrganization",
            body=maybe_transform(
                {
                    "invite_id": invite_id,
                    "organization_id": organization_id,
                },
                organization_join_params.OrganizationJoinParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationJoinResponse,
        )

    def leave(
        self,
        *,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        LeaveOrganization lets the passed user leave an Organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.OrganizationService/LeaveOrganization",
            body=maybe_transform({"user_id": user_id}, organization_leave_params.OrganizationLeaveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def list_members(
        self,
        *,
        token: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        organization_id: str | NotGiven = NOT_GIVEN,
        pagination: organization_list_members_params.Pagination | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncMembersPage[OrganizationListMembersResponse]:
        """
        ListMembers lists all members of the specified organization.

        Args:
          organization_id: organization_id is the ID of the organization to list members for

          pagination: pagination contains the pagination options for listing members

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.OrganizationService/ListMembers",
            page=SyncMembersPage[OrganizationListMembersResponse],
            body=maybe_transform(
                {
                    "organization_id": organization_id,
                    "pagination": pagination,
                },
                organization_list_members_params.OrganizationListMembersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "token": token,
                        "page_size": page_size,
                    },
                    organization_list_members_params.OrganizationListMembersParams,
                ),
            ),
            model=OrganizationListMembersResponse,
            method="post",
        )

    def set_role(
        self,
        *,
        organization_id: str | NotGiven = NOT_GIVEN,
        role: Literal["ORGANIZATION_ROLE_UNSPECIFIED", "ORGANIZATION_ROLE_ADMIN", "ORGANIZATION_ROLE_MEMBER"]
        | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        SetRole

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.OrganizationService/SetRole",
            body=maybe_transform(
                {
                    "organization_id": organization_id,
                    "role": role,
                    "user_id": user_id,
                },
                organization_set_role_params.OrganizationSetRoleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncOrganizationsResource(AsyncAPIResource):
    @cached_property
    def invites(self) -> AsyncInvitesResource:
        return AsyncInvitesResource(self._client)

    @cached_property
    def sso_configurations(self) -> AsyncSSOConfigurationsResource:
        return AsyncSSOConfigurationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOrganizationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOrganizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrganizationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return AsyncOrganizationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        invite_accounts_with_matching_domain: bool | NotGiven = NOT_GIVEN,
        join_organization: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationCreateResponse:
        """
        CreateOrganization creates a new Organization.

        Args:
          invite_accounts_with_matching_domain: Should other Accounts with the same domain be automatically invited to the
              organization?

          join_organization: join_organization decides whether the Identity issuing this request joins the
              org on creation

          name: name is the organization name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.OrganizationService/CreateOrganization",
            body=await async_maybe_transform(
                {
                    "invite_accounts_with_matching_domain": invite_accounts_with_matching_domain,
                    "join_organization": join_organization,
                    "name": name,
                },
                organization_create_params.OrganizationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationCreateResponse,
        )

    async def retrieve(
        self,
        *,
        organization_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationRetrieveResponse:
        """
        GetOrganization retrieves a single Organization.

        Args:
          organization_id: organization_id is the unique identifier of the Organization to retreive.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.OrganizationService/GetOrganization",
            body=await async_maybe_transform(
                {"organization_id": organization_id}, organization_retrieve_params.OrganizationRetrieveParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationRetrieveResponse,
        )

    @overload
    async def update(
        self,
        *,
        invite_domains: organization_update_params.InviteDomainsIsTheDomainAllowlistOfTheOrganizationInviteDomains,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationUpdateResponse:
        """
        UpdateOrganization updates the properties of an Organization.

        Args:
          invite_domains: invite_domains is the domain allowlist of the organization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationUpdateResponse:
        """
        UpdateOrganization updates the properties of an Organization.

        Args:
          name: name is the new name of the organization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["invite_domains"], ["name"])
    async def update(
        self,
        *,
        invite_domains: organization_update_params.InviteDomainsIsTheDomainAllowlistOfTheOrganizationInviteDomains
        | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationUpdateResponse:
        return await self._post(
            "/gitpod.v1.OrganizationService/UpdateOrganization",
            body=await async_maybe_transform(
                {
                    "invite_domains": invite_domains,
                    "name": name,
                },
                organization_update_params.OrganizationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationUpdateResponse,
        )

    def list(
        self,
        *,
        token: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        pagination: organization_list_params.Pagination | NotGiven = NOT_GIVEN,
        scope: Literal["SCOPE_UNSPECIFIED", "SCOPE_MEMBER", "SCOPE_ALL"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[OrganizationListResponse, AsyncOrganizationsPage[OrganizationListResponse]]:
        """
        ListOrganizations lists all organization the caller has access to.

        Args:
          pagination: pagination contains the pagination options for listing organizations

          scope: scope is the scope of the organizations to list

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.OrganizationService/ListOrganizations",
            page=AsyncOrganizationsPage[OrganizationListResponse],
            body=maybe_transform(
                {
                    "pagination": pagination,
                    "scope": scope,
                },
                organization_list_params.OrganizationListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "token": token,
                        "page_size": page_size,
                    },
                    organization_list_params.OrganizationListParams,
                ),
            ),
            model=OrganizationListResponse,
            method="post",
        )

    async def delete(
        self,
        *,
        organization_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        DeleteOrganization deletes the specified organization.

        Args:
          organization_id: organization_id is the ID of the organization to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.OrganizationService/DeleteOrganization",
            body=await async_maybe_transform(
                {"organization_id": organization_id}, organization_delete_params.OrganizationDeleteParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    @overload
    async def join(
        self,
        *,
        invite_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationJoinResponse:
        """
        JoinOrganization lets accounts join an Organization.

        Args:
          invite_id: invite_id is the unique identifier of the invite to join the organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def join(
        self,
        *,
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationJoinResponse:
        """
        JoinOrganization lets accounts join an Organization.

        Args:
          organization_id: organization_id is the unique identifier of the Organization to join.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["invite_id"], ["organization_id"])
    async def join(
        self,
        *,
        invite_id: str | NotGiven = NOT_GIVEN,
        organization_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationJoinResponse:
        return await self._post(
            "/gitpod.v1.OrganizationService/JoinOrganization",
            body=await async_maybe_transform(
                {
                    "invite_id": invite_id,
                    "organization_id": organization_id,
                },
                organization_join_params.OrganizationJoinParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganizationJoinResponse,
        )

    async def leave(
        self,
        *,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        LeaveOrganization lets the passed user leave an Organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.OrganizationService/LeaveOrganization",
            body=await async_maybe_transform({"user_id": user_id}, organization_leave_params.OrganizationLeaveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def list_members(
        self,
        *,
        token: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        organization_id: str | NotGiven = NOT_GIVEN,
        pagination: organization_list_members_params.Pagination | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[OrganizationListMembersResponse, AsyncMembersPage[OrganizationListMembersResponse]]:
        """
        ListMembers lists all members of the specified organization.

        Args:
          organization_id: organization_id is the ID of the organization to list members for

          pagination: pagination contains the pagination options for listing members

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.OrganizationService/ListMembers",
            page=AsyncMembersPage[OrganizationListMembersResponse],
            body=maybe_transform(
                {
                    "organization_id": organization_id,
                    "pagination": pagination,
                },
                organization_list_members_params.OrganizationListMembersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "token": token,
                        "page_size": page_size,
                    },
                    organization_list_members_params.OrganizationListMembersParams,
                ),
            ),
            model=OrganizationListMembersResponse,
            method="post",
        )

    async def set_role(
        self,
        *,
        organization_id: str | NotGiven = NOT_GIVEN,
        role: Literal["ORGANIZATION_ROLE_UNSPECIFIED", "ORGANIZATION_ROLE_ADMIN", "ORGANIZATION_ROLE_MEMBER"]
        | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        SetRole

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.OrganizationService/SetRole",
            body=await async_maybe_transform(
                {
                    "organization_id": organization_id,
                    "role": role,
                    "user_id": user_id,
                },
                organization_set_role_params.OrganizationSetRoleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class OrganizationsResourceWithRawResponse:
    def __init__(self, organizations: OrganizationsResource) -> None:
        self._organizations = organizations

        self.create = to_raw_response_wrapper(
            organizations.create,
        )
        self.retrieve = to_raw_response_wrapper(
            organizations.retrieve,
        )
        self.update = to_raw_response_wrapper(
            organizations.update,
        )
        self.list = to_raw_response_wrapper(
            organizations.list,
        )
        self.delete = to_raw_response_wrapper(
            organizations.delete,
        )
        self.join = to_raw_response_wrapper(
            organizations.join,
        )
        self.leave = to_raw_response_wrapper(
            organizations.leave,
        )
        self.list_members = to_raw_response_wrapper(
            organizations.list_members,
        )
        self.set_role = to_raw_response_wrapper(
            organizations.set_role,
        )

    @cached_property
    def invites(self) -> InvitesResourceWithRawResponse:
        return InvitesResourceWithRawResponse(self._organizations.invites)

    @cached_property
    def sso_configurations(self) -> SSOConfigurationsResourceWithRawResponse:
        return SSOConfigurationsResourceWithRawResponse(self._organizations.sso_configurations)


class AsyncOrganizationsResourceWithRawResponse:
    def __init__(self, organizations: AsyncOrganizationsResource) -> None:
        self._organizations = organizations

        self.create = async_to_raw_response_wrapper(
            organizations.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            organizations.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            organizations.update,
        )
        self.list = async_to_raw_response_wrapper(
            organizations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            organizations.delete,
        )
        self.join = async_to_raw_response_wrapper(
            organizations.join,
        )
        self.leave = async_to_raw_response_wrapper(
            organizations.leave,
        )
        self.list_members = async_to_raw_response_wrapper(
            organizations.list_members,
        )
        self.set_role = async_to_raw_response_wrapper(
            organizations.set_role,
        )

    @cached_property
    def invites(self) -> AsyncInvitesResourceWithRawResponse:
        return AsyncInvitesResourceWithRawResponse(self._organizations.invites)

    @cached_property
    def sso_configurations(self) -> AsyncSSOConfigurationsResourceWithRawResponse:
        return AsyncSSOConfigurationsResourceWithRawResponse(self._organizations.sso_configurations)


class OrganizationsResourceWithStreamingResponse:
    def __init__(self, organizations: OrganizationsResource) -> None:
        self._organizations = organizations

        self.create = to_streamed_response_wrapper(
            organizations.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            organizations.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            organizations.update,
        )
        self.list = to_streamed_response_wrapper(
            organizations.list,
        )
        self.delete = to_streamed_response_wrapper(
            organizations.delete,
        )
        self.join = to_streamed_response_wrapper(
            organizations.join,
        )
        self.leave = to_streamed_response_wrapper(
            organizations.leave,
        )
        self.list_members = to_streamed_response_wrapper(
            organizations.list_members,
        )
        self.set_role = to_streamed_response_wrapper(
            organizations.set_role,
        )

    @cached_property
    def invites(self) -> InvitesResourceWithStreamingResponse:
        return InvitesResourceWithStreamingResponse(self._organizations.invites)

    @cached_property
    def sso_configurations(self) -> SSOConfigurationsResourceWithStreamingResponse:
        return SSOConfigurationsResourceWithStreamingResponse(self._organizations.sso_configurations)


class AsyncOrganizationsResourceWithStreamingResponse:
    def __init__(self, organizations: AsyncOrganizationsResource) -> None:
        self._organizations = organizations

        self.create = async_to_streamed_response_wrapper(
            organizations.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            organizations.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            organizations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            organizations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            organizations.delete,
        )
        self.join = async_to_streamed_response_wrapper(
            organizations.join,
        )
        self.leave = async_to_streamed_response_wrapper(
            organizations.leave,
        )
        self.list_members = async_to_streamed_response_wrapper(
            organizations.list_members,
        )
        self.set_role = async_to_streamed_response_wrapper(
            organizations.set_role,
        )

    @cached_property
    def invites(self) -> AsyncInvitesResourceWithStreamingResponse:
        return AsyncInvitesResourceWithStreamingResponse(self._organizations.invites)

    @cached_property
    def sso_configurations(self) -> AsyncSSOConfigurationsResourceWithStreamingResponse:
        return AsyncSSOConfigurationsResourceWithStreamingResponse(self._organizations.sso_configurations)
