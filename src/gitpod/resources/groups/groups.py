# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import (
    group_list_params,
    group_create_params,
    group_delete_params,
    group_update_params,
    group_retrieve_params,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .memberships import (
    MembershipsResource,
    AsyncMembershipsResource,
    MembershipsResourceWithRawResponse,
    AsyncMembershipsResourceWithRawResponse,
    MembershipsResourceWithStreamingResponse,
    AsyncMembershipsResourceWithStreamingResponse,
)
from ...pagination import SyncGroupsPage, AsyncGroupsPage
from ...types.group import Group
from ..._base_client import AsyncPaginator, make_request_options
from .role_assignments import (
    RoleAssignmentsResource,
    AsyncRoleAssignmentsResource,
    RoleAssignmentsResourceWithRawResponse,
    AsyncRoleAssignmentsResourceWithRawResponse,
    RoleAssignmentsResourceWithStreamingResponse,
    AsyncRoleAssignmentsResourceWithStreamingResponse,
)
from ...types.group_create_response import GroupCreateResponse
from ...types.group_update_response import GroupUpdateResponse
from ...types.group_retrieve_response import GroupRetrieveResponse

__all__ = ["GroupsResource", "AsyncGroupsResource"]


class GroupsResource(SyncAPIResource):
    @cached_property
    def memberships(self) -> MembershipsResource:
        return MembershipsResource(self._client)

    @cached_property
    def role_assignments(self) -> RoleAssignmentsResource:
        return RoleAssignmentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> GroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return GroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return GroupsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        description: str | Omit = omit,
        name: str | Omit = omit,
        organization_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GroupCreateResponse:
        """
        Creates a new group within an organization.

        Use this method to:

        - Create teams for access control
        - Organize users by department or function
        - Set up role-based access groups

        ### Examples

        - Create a basic group:

          Creates a group with name and description.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          name: "Backend Team"
          description: "Backend engineering team"
          ```

        ### Authorization

        Requires `org:admin` role on the organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.GroupService/CreateGroup",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "organization_id": organization_id,
                },
                group_create_params.GroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupCreateResponse,
        )

    def retrieve(
        self,
        *,
        group_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GroupRetrieveResponse:
        """
        Gets information about a specific group.

        Use this method to:

        - Retrieve group details and metadata
        - Check group configuration
        - View member count

        ### Examples

        - Get group details:

          Retrieves information about a specific group.

          ```yaml
          groupId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        ### Authorization

        All organization members can view group information (transparency model).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.GroupService/GetGroup",
            body=maybe_transform({"group_id": group_id}, group_retrieve_params.GroupRetrieveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupRetrieveResponse,
        )

    def update(
        self,
        *,
        description: str | Omit = omit,
        group_id: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GroupUpdateResponse:
        """
        Updates group information.

        Use this method to:

        - Rename a group
        - Update group description

        ### Examples

        - Update group name:

          Changes the name of an existing group.

          ```yaml
          groupId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          name: "Platform Team"
          description: "Platform engineering team"
          ```

        ### Authorization

        Requires `org:admin` permission on the organization or `group:admin` permission
        on the specific group.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.GroupService/UpdateGroup",
            body=maybe_transform(
                {
                    "description": description,
                    "group_id": group_id,
                    "name": name,
                },
                group_update_params.GroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupUpdateResponse,
        )

    def list(
        self,
        *,
        token: str | Omit = omit,
        page_size: int | Omit = omit,
        pagination: group_list_params.Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncGroupsPage[Group]:
        """
        Lists groups with optional pagination.

        Use this method to:

        - View all groups in an organization
        - Check group memberships
        - Monitor group configurations
        - Audit group access

        ### Examples

        - List all groups:

          Shows all groups with pagination.

          ```yaml
          pagination:
            pageSize: 20
          ```

        - List with custom page size:

          Shows groups with specified page size.

          ```yaml
          pagination:
            pageSize: 50
            token: "next-page-token-from-previous-response"
          ```

        ### Authorization

        All organization members can list groups (transparency model).

        Args:
          pagination: pagination contains the pagination options for listing groups

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.GroupService/ListGroups",
            page=SyncGroupsPage[Group],
            body=maybe_transform({"pagination": pagination}, group_list_params.GroupListParams),
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
                    group_list_params.GroupListParams,
                ),
            ),
            model=Group,
            method="post",
        )

    def delete(
        self,
        *,
        group_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Deletes a group and removes all its resource assignments.

        When a group is deleted, all resource assignments revert to org-level scope.

        Use this method to:

        - Remove unused groups
        - Clean up after team reorganization

        ### Examples

        - Delete a group:

          Permanently removes a group.

          ```yaml
          groupId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        ### Authorization

        Requires `org:admin` role on the organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.GroupService/DeleteGroup",
            body=maybe_transform({"group_id": group_id}, group_delete_params.GroupDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncGroupsResource(AsyncAPIResource):
    @cached_property
    def memberships(self) -> AsyncMembershipsResource:
        return AsyncMembershipsResource(self._client)

    @cached_property
    def role_assignments(self) -> AsyncRoleAssignmentsResource:
        return AsyncRoleAssignmentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return AsyncGroupsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        description: str | Omit = omit,
        name: str | Omit = omit,
        organization_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GroupCreateResponse:
        """
        Creates a new group within an organization.

        Use this method to:

        - Create teams for access control
        - Organize users by department or function
        - Set up role-based access groups

        ### Examples

        - Create a basic group:

          Creates a group with name and description.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          name: "Backend Team"
          description: "Backend engineering team"
          ```

        ### Authorization

        Requires `org:admin` role on the organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.GroupService/CreateGroup",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "organization_id": organization_id,
                },
                group_create_params.GroupCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupCreateResponse,
        )

    async def retrieve(
        self,
        *,
        group_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GroupRetrieveResponse:
        """
        Gets information about a specific group.

        Use this method to:

        - Retrieve group details and metadata
        - Check group configuration
        - View member count

        ### Examples

        - Get group details:

          Retrieves information about a specific group.

          ```yaml
          groupId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        ### Authorization

        All organization members can view group information (transparency model).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.GroupService/GetGroup",
            body=await async_maybe_transform({"group_id": group_id}, group_retrieve_params.GroupRetrieveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupRetrieveResponse,
        )

    async def update(
        self,
        *,
        description: str | Omit = omit,
        group_id: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GroupUpdateResponse:
        """
        Updates group information.

        Use this method to:

        - Rename a group
        - Update group description

        ### Examples

        - Update group name:

          Changes the name of an existing group.

          ```yaml
          groupId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          name: "Platform Team"
          description: "Platform engineering team"
          ```

        ### Authorization

        Requires `org:admin` permission on the organization or `group:admin` permission
        on the specific group.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.GroupService/UpdateGroup",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "group_id": group_id,
                    "name": name,
                },
                group_update_params.GroupUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GroupUpdateResponse,
        )

    def list(
        self,
        *,
        token: str | Omit = omit,
        page_size: int | Omit = omit,
        pagination: group_list_params.Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Group, AsyncGroupsPage[Group]]:
        """
        Lists groups with optional pagination.

        Use this method to:

        - View all groups in an organization
        - Check group memberships
        - Monitor group configurations
        - Audit group access

        ### Examples

        - List all groups:

          Shows all groups with pagination.

          ```yaml
          pagination:
            pageSize: 20
          ```

        - List with custom page size:

          Shows groups with specified page size.

          ```yaml
          pagination:
            pageSize: 50
            token: "next-page-token-from-previous-response"
          ```

        ### Authorization

        All organization members can list groups (transparency model).

        Args:
          pagination: pagination contains the pagination options for listing groups

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.GroupService/ListGroups",
            page=AsyncGroupsPage[Group],
            body=maybe_transform({"pagination": pagination}, group_list_params.GroupListParams),
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
                    group_list_params.GroupListParams,
                ),
            ),
            model=Group,
            method="post",
        )

    async def delete(
        self,
        *,
        group_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Deletes a group and removes all its resource assignments.

        When a group is deleted, all resource assignments revert to org-level scope.

        Use this method to:

        - Remove unused groups
        - Clean up after team reorganization

        ### Examples

        - Delete a group:

          Permanently removes a group.

          ```yaml
          groupId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        ### Authorization

        Requires `org:admin` role on the organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.GroupService/DeleteGroup",
            body=await async_maybe_transform({"group_id": group_id}, group_delete_params.GroupDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class GroupsResourceWithRawResponse:
    def __init__(self, groups: GroupsResource) -> None:
        self._groups = groups

        self.create = to_raw_response_wrapper(
            groups.create,
        )
        self.retrieve = to_raw_response_wrapper(
            groups.retrieve,
        )
        self.update = to_raw_response_wrapper(
            groups.update,
        )
        self.list = to_raw_response_wrapper(
            groups.list,
        )
        self.delete = to_raw_response_wrapper(
            groups.delete,
        )

    @cached_property
    def memberships(self) -> MembershipsResourceWithRawResponse:
        return MembershipsResourceWithRawResponse(self._groups.memberships)

    @cached_property
    def role_assignments(self) -> RoleAssignmentsResourceWithRawResponse:
        return RoleAssignmentsResourceWithRawResponse(self._groups.role_assignments)


class AsyncGroupsResourceWithRawResponse:
    def __init__(self, groups: AsyncGroupsResource) -> None:
        self._groups = groups

        self.create = async_to_raw_response_wrapper(
            groups.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            groups.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            groups.update,
        )
        self.list = async_to_raw_response_wrapper(
            groups.list,
        )
        self.delete = async_to_raw_response_wrapper(
            groups.delete,
        )

    @cached_property
    def memberships(self) -> AsyncMembershipsResourceWithRawResponse:
        return AsyncMembershipsResourceWithRawResponse(self._groups.memberships)

    @cached_property
    def role_assignments(self) -> AsyncRoleAssignmentsResourceWithRawResponse:
        return AsyncRoleAssignmentsResourceWithRawResponse(self._groups.role_assignments)


class GroupsResourceWithStreamingResponse:
    def __init__(self, groups: GroupsResource) -> None:
        self._groups = groups

        self.create = to_streamed_response_wrapper(
            groups.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            groups.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            groups.update,
        )
        self.list = to_streamed_response_wrapper(
            groups.list,
        )
        self.delete = to_streamed_response_wrapper(
            groups.delete,
        )

    @cached_property
    def memberships(self) -> MembershipsResourceWithStreamingResponse:
        return MembershipsResourceWithStreamingResponse(self._groups.memberships)

    @cached_property
    def role_assignments(self) -> RoleAssignmentsResourceWithStreamingResponse:
        return RoleAssignmentsResourceWithStreamingResponse(self._groups.role_assignments)


class AsyncGroupsResourceWithStreamingResponse:
    def __init__(self, groups: AsyncGroupsResource) -> None:
        self._groups = groups

        self.create = async_to_streamed_response_wrapper(
            groups.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            groups.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            groups.update,
        )
        self.list = async_to_streamed_response_wrapper(
            groups.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            groups.delete,
        )

    @cached_property
    def memberships(self) -> AsyncMembershipsResourceWithStreamingResponse:
        return AsyncMembershipsResourceWithStreamingResponse(self._groups.memberships)

    @cached_property
    def role_assignments(self) -> AsyncRoleAssignmentsResourceWithStreamingResponse:
        return AsyncRoleAssignmentsResourceWithStreamingResponse(self._groups.role_assignments)
