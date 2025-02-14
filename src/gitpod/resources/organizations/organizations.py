# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...types import (
    Scope,
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
from ...types.scope import Scope
from ..._base_client import AsyncPaginator, make_request_options
from .sso_configurations import (
    SSOConfigurationsResource,
    AsyncSSOConfigurationsResource,
    SSOConfigurationsResourceWithRawResponse,
    AsyncSSOConfigurationsResourceWithRawResponse,
    SSOConfigurationsResourceWithStreamingResponse,
    AsyncSSOConfigurationsResourceWithStreamingResponse,
)
from ...types.organization import Organization
from .domain_verifications import (
    DomainVerificationsResource,
    AsyncDomainVerificationsResource,
    DomainVerificationsResourceWithRawResponse,
    AsyncDomainVerificationsResourceWithRawResponse,
    DomainVerificationsResourceWithStreamingResponse,
    AsyncDomainVerificationsResourceWithStreamingResponse,
)
from ...types.organization_member import OrganizationMember
from ...types.invite_domains_param import InviteDomainsParam
from ...types.shared.organization_role import OrganizationRole
from ...types.organization_join_response import OrganizationJoinResponse
from ...types.organization_create_response import OrganizationCreateResponse
from ...types.organization_update_response import OrganizationUpdateResponse
from ...types.organization_retrieve_response import OrganizationRetrieveResponse

__all__ = ["OrganizationsResource", "AsyncOrganizationsResource"]


class OrganizationsResource(SyncAPIResource):
    @cached_property
    def domain_verifications(self) -> DomainVerificationsResource:
        return DomainVerificationsResource(self._client)

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

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return OrganizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrganizationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return OrganizationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        invite_accounts_with_matching_domain: bool | NotGiven = NOT_GIVEN,
        join_organization: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationCreateResponse:
        """
        Creates a new organization with the specified name and settings.

        Use this method to:

        - Create a new organization for team collaboration
        - Set up automatic domain-based invites for team members
        - Join the organization immediately upon creation

        ### Examples

        - Create a basic organization:

          Creates an organization with just a name.

          ```yaml
          name: "Acme Corp Engineering"
          joinOrganization: true
          ```

        - Create with domain-based invites:

          Creates an organization that automatically invites users with matching email
          domains.

          ```yaml
          name: "Acme Corp"
          joinOrganization: true
          inviteAccountsWithMatchingDomain: true
          ```

        Args:
          name: name is the organization name

          invite_accounts_with_matching_domain: Should other Accounts with the same domain be automatically invited to the
              organization?

          join_organization: join_organization decides whether the Identity issuing this request joins the
              org on creation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.OrganizationService/CreateOrganization",
            body=maybe_transform(
                {
                    "name": name,
                    "invite_accounts_with_matching_domain": invite_accounts_with_matching_domain,
                    "join_organization": join_organization,
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
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationRetrieveResponse:
        """
        Gets details about a specific organization.

        Use this method to:

        - Retrieve organization settings and configuration
        - Check organization membership status
        - View domain verification settings

        ### Examples

        - Get organization details:

          Retrieves information about a specific organization.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          ```

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

    def update(
        self,
        *,
        organization_id: str,
        invite_domains: Optional[InviteDomainsParam] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationUpdateResponse:
        """
        Updates an organization's settings including name, invite domains, and member
        policies.

        Use this method to:

        - Modify organization display name
        - Configure email domain restrictions
        - Update organization-wide settings
        - Manage member access policies

        ### Examples

        - Update basic settings:

          Changes organization name and invite domains.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          name: "New Company Name"
          inviteDomains:
            domains:
              - "company.com"
              - "subsidiary.com"
          ```

        - Remove domain restrictions:

          Clears all domain-based invite restrictions.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          inviteDomains:
            domains: []
          ```

        Args:
          organization_id: organization_id is the ID of the organization to update the settings for.

          invite_domains: invite_domains is the domain allowlist of the organization

          name: name is the new name of the organization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.OrganizationService/UpdateOrganization",
            body=maybe_transform(
                {
                    "organization_id": organization_id,
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
        scope: Scope | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncOrganizationsPage[Organization]:
        """
        Lists all organizations the caller has access to with optional filtering.

        Use this method to:

        - View organizations you're a member of
        - Browse all available organizations
        - Paginate through organization results

        ### Examples

        - List member organizations:

          Shows organizations where the caller is a member.

          ```yaml
          pagination:
            pageSize: 20
          scope: SCOPE_MEMBER
          ```

        - List all organizations:

          Shows all organizations visible to the caller.

          ```yaml
          pagination:
            pageSize: 50
          scope: SCOPE_ALL
          ```

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
            page=SyncOrganizationsPage[Organization],
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
            model=Organization,
            method="post",
        )

    def delete(
        self,
        *,
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Permanently deletes an organization.

        Use this method to:

        - Remove unused organizations
        - Clean up test organizations
        - Complete organization migration

        ### Examples

        - Delete organization:

          Permanently removes an organization and all its data.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          ```

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
        """
        Allows users to join an organization through direct ID, invite link, or
        domain-based auto-join.

        Use this method to:

        - Join an organization via direct ID or invite
        - Join automatically based on email domain
        - Accept organization invitations

        ### Examples

        - Join via organization ID:

          Joins an organization directly when you have the ID.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          ```

        - Join via invite:

          Accepts an organization invitation link.

          ```yaml
          inviteId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          invite_id: invite_id is the unique identifier of the invite to join the organization.

          organization_id: organization_id is the unique identifier of the Organization to join.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Removes a user from an organization while preserving organization data.

        Use this method to:

        - Remove yourself from an organization
        - Clean up inactive memberships
        - Transfer project ownership before leaving
        - Manage team transitions

        ### Examples

        - Leave organization:

          Removes user from organization membership.

          ```yaml
          userId: "f53d2330-3795-4c5d-a1f3-453121af9c60"
          ```

        Note: Ensure all projects and resources are transferred before leaving.

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
        organization_id: str,
        token: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        pagination: organization_list_members_params.Pagination | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncMembersPage[OrganizationMember]:
        """
        Lists and filters organization members with optional pagination.

        Use this method to:

        - View all organization members
        - Monitor member activity
        - Manage team membership

        ### Examples

        - List active members:

          Retrieves active members with pagination.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          pagination:
            pageSize: 20
          ```

        - List with pagination:

          Retrieves next page of members.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          pagination:
            pageSize: 50
            token: "next-page-token-from-previous-response"
          ```

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
            page=SyncMembersPage[OrganizationMember],
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
            model=OrganizationMember,
            method="post",
        )

    def set_role(
        self,
        *,
        organization_id: str,
        user_id: str,
        role: OrganizationRole | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Manages organization membership and roles by setting a user's role within the
        organization.

        Use this method to:

        - Promote members to admin role
        - Change member permissions
        - Demote admins to regular members

        ### Examples

        - Promote to admin:

          Makes a user an organization administrator.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          userId: "f53d2330-3795-4c5d-a1f3-453121af9c60"
          role: ORGANIZATION_ROLE_ADMIN
          ```

        - Change to member:

          Changes a user's role to regular member.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          userId: "f53d2330-3795-4c5d-a1f3-453121af9c60"
          role: ORGANIZATION_ROLE_MEMBER
          ```

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
                    "user_id": user_id,
                    "role": role,
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
    def domain_verifications(self) -> AsyncDomainVerificationsResource:
        return AsyncDomainVerificationsResource(self._client)

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

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOrganizationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrganizationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return AsyncOrganizationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        invite_accounts_with_matching_domain: bool | NotGiven = NOT_GIVEN,
        join_organization: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationCreateResponse:
        """
        Creates a new organization with the specified name and settings.

        Use this method to:

        - Create a new organization for team collaboration
        - Set up automatic domain-based invites for team members
        - Join the organization immediately upon creation

        ### Examples

        - Create a basic organization:

          Creates an organization with just a name.

          ```yaml
          name: "Acme Corp Engineering"
          joinOrganization: true
          ```

        - Create with domain-based invites:

          Creates an organization that automatically invites users with matching email
          domains.

          ```yaml
          name: "Acme Corp"
          joinOrganization: true
          inviteAccountsWithMatchingDomain: true
          ```

        Args:
          name: name is the organization name

          invite_accounts_with_matching_domain: Should other Accounts with the same domain be automatically invited to the
              organization?

          join_organization: join_organization decides whether the Identity issuing this request joins the
              org on creation

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.OrganizationService/CreateOrganization",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "invite_accounts_with_matching_domain": invite_accounts_with_matching_domain,
                    "join_organization": join_organization,
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
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationRetrieveResponse:
        """
        Gets details about a specific organization.

        Use this method to:

        - Retrieve organization settings and configuration
        - Check organization membership status
        - View domain verification settings

        ### Examples

        - Get organization details:

          Retrieves information about a specific organization.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          ```

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

    async def update(
        self,
        *,
        organization_id: str,
        invite_domains: Optional[InviteDomainsParam] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationUpdateResponse:
        """
        Updates an organization's settings including name, invite domains, and member
        policies.

        Use this method to:

        - Modify organization display name
        - Configure email domain restrictions
        - Update organization-wide settings
        - Manage member access policies

        ### Examples

        - Update basic settings:

          Changes organization name and invite domains.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          name: "New Company Name"
          inviteDomains:
            domains:
              - "company.com"
              - "subsidiary.com"
          ```

        - Remove domain restrictions:

          Clears all domain-based invite restrictions.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          inviteDomains:
            domains: []
          ```

        Args:
          organization_id: organization_id is the ID of the organization to update the settings for.

          invite_domains: invite_domains is the domain allowlist of the organization

          name: name is the new name of the organization

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.OrganizationService/UpdateOrganization",
            body=await async_maybe_transform(
                {
                    "organization_id": organization_id,
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
        scope: Scope | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Organization, AsyncOrganizationsPage[Organization]]:
        """
        Lists all organizations the caller has access to with optional filtering.

        Use this method to:

        - View organizations you're a member of
        - Browse all available organizations
        - Paginate through organization results

        ### Examples

        - List member organizations:

          Shows organizations where the caller is a member.

          ```yaml
          pagination:
            pageSize: 20
          scope: SCOPE_MEMBER
          ```

        - List all organizations:

          Shows all organizations visible to the caller.

          ```yaml
          pagination:
            pageSize: 50
          scope: SCOPE_ALL
          ```

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
            page=AsyncOrganizationsPage[Organization],
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
            model=Organization,
            method="post",
        )

    async def delete(
        self,
        *,
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Permanently deletes an organization.

        Use this method to:

        - Remove unused organizations
        - Clean up test organizations
        - Complete organization migration

        ### Examples

        - Delete organization:

          Permanently removes an organization and all its data.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          ```

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
        """
        Allows users to join an organization through direct ID, invite link, or
        domain-based auto-join.

        Use this method to:

        - Join an organization via direct ID or invite
        - Join automatically based on email domain
        - Accept organization invitations

        ### Examples

        - Join via organization ID:

          Joins an organization directly when you have the ID.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          ```

        - Join via invite:

          Accepts an organization invitation link.

          ```yaml
          inviteId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          invite_id: invite_id is the unique identifier of the invite to join the organization.

          organization_id: organization_id is the unique identifier of the Organization to join.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
        user_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Removes a user from an organization while preserving organization data.

        Use this method to:

        - Remove yourself from an organization
        - Clean up inactive memberships
        - Transfer project ownership before leaving
        - Manage team transitions

        ### Examples

        - Leave organization:

          Removes user from organization membership.

          ```yaml
          userId: "f53d2330-3795-4c5d-a1f3-453121af9c60"
          ```

        Note: Ensure all projects and resources are transferred before leaving.

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
        organization_id: str,
        token: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        pagination: organization_list_members_params.Pagination | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[OrganizationMember, AsyncMembersPage[OrganizationMember]]:
        """
        Lists and filters organization members with optional pagination.

        Use this method to:

        - View all organization members
        - Monitor member activity
        - Manage team membership

        ### Examples

        - List active members:

          Retrieves active members with pagination.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          pagination:
            pageSize: 20
          ```

        - List with pagination:

          Retrieves next page of members.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          pagination:
            pageSize: 50
            token: "next-page-token-from-previous-response"
          ```

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
            page=AsyncMembersPage[OrganizationMember],
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
            model=OrganizationMember,
            method="post",
        )

    async def set_role(
        self,
        *,
        organization_id: str,
        user_id: str,
        role: OrganizationRole | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Manages organization membership and roles by setting a user's role within the
        organization.

        Use this method to:

        - Promote members to admin role
        - Change member permissions
        - Demote admins to regular members

        ### Examples

        - Promote to admin:

          Makes a user an organization administrator.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          userId: "f53d2330-3795-4c5d-a1f3-453121af9c60"
          role: ORGANIZATION_ROLE_ADMIN
          ```

        - Change to member:

          Changes a user's role to regular member.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          userId: "f53d2330-3795-4c5d-a1f3-453121af9c60"
          role: ORGANIZATION_ROLE_MEMBER
          ```

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
                    "user_id": user_id,
                    "role": role,
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
    def domain_verifications(self) -> DomainVerificationsResourceWithRawResponse:
        return DomainVerificationsResourceWithRawResponse(self._organizations.domain_verifications)

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
    def domain_verifications(self) -> AsyncDomainVerificationsResourceWithRawResponse:
        return AsyncDomainVerificationsResourceWithRawResponse(self._organizations.domain_verifications)

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
    def domain_verifications(self) -> DomainVerificationsResourceWithStreamingResponse:
        return DomainVerificationsResourceWithStreamingResponse(self._organizations.domain_verifications)

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
    def domain_verifications(self) -> AsyncDomainVerificationsResourceWithStreamingResponse:
        return AsyncDomainVerificationsResourceWithStreamingResponse(self._organizations.domain_verifications)

    @cached_property
    def invites(self) -> AsyncInvitesResourceWithStreamingResponse:
        return AsyncInvitesResourceWithStreamingResponse(self._organizations.invites)

    @cached_property
    def sso_configurations(self) -> AsyncSSOConfigurationsResourceWithStreamingResponse:
        return AsyncSSOConfigurationsResourceWithStreamingResponse(self._organizations.sso_configurations)
