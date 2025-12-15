# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

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
from ...pagination import SyncAssignmentsPage, AsyncAssignmentsPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.groups import (
    ResourceRole,
    role_assignment_list_params,
    role_assignment_create_params,
    role_assignment_delete_params,
)
from ...types.groups.resource_role import ResourceRole
from ...types.shared.resource_type import ResourceType
from ...types.groups.role_assignment import RoleAssignment
from ...types.groups.role_assignment_create_response import RoleAssignmentCreateResponse

__all__ = ["RoleAssignmentsResource", "AsyncRoleAssignmentsResource"]


class RoleAssignmentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RoleAssignmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return RoleAssignmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RoleAssignmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return RoleAssignmentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        group_id: str | Omit = omit,
        resource_id: str | Omit = omit,
        resource_role: ResourceRole | Omit = omit,
        resource_type: ResourceType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoleAssignmentCreateResponse:
        """
        Creates a role assignment for a group on a resource.

        Use this method to:

        - Assign specific roles to groups on runners, projects, or environments
        - Grant group-based access to resources

        ### Examples

        - Assign admin role on a runner:

          Grants the group admin access to a runner.

          ```yaml
          groupId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          resourceType: RESOURCE_TYPE_RUNNER
          resourceId: "f53d2330-3795-4c5d-a1f3-453121af9c60"
          resourceRole: RESOURCE_ROLE_RUNNER_ADMIN
          ```

        - Assign user role on a project:

          Grants the group user access to a project.

          ```yaml
          groupId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          resourceType: RESOURCE_TYPE_PROJECT
          resourceId: "a1b2c3d4-5678-90ab-cdef-1234567890ab"
          resourceRole: RESOURCE_ROLE_PROJECT_USER
          ```

        ### Authorization

        Requires admin role on the specific resource.

        Args:
          resource_role: ResourceRole represents roles that can be assigned to groups on resources These
              map directly to the roles defined in backend/db/rule/rbac/role/role.go

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.GroupService/CreateRoleAssignment",
            body=maybe_transform(
                {
                    "group_id": group_id,
                    "resource_id": resource_id,
                    "resource_role": resource_role,
                    "resource_type": resource_type,
                },
                role_assignment_create_params.RoleAssignmentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoleAssignmentCreateResponse,
        )

    def list(
        self,
        *,
        token: str | Omit = omit,
        page_size: int | Omit = omit,
        filter: role_assignment_list_params.Filter | Omit = omit,
        pagination: role_assignment_list_params.Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncAssignmentsPage[RoleAssignment]:
        """
        Lists role assignments for a group or resource.

        Use this method to:

        - View all role assignments for a group
        - Audit resource access
        - Check which groups have access to resources

        ### Examples

        - List role assignments for a group:

          Shows all role assignments for a specific group.

          ```yaml
          filter:
            groupId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          pagination:
            pageSize: 20
          ```

        - List role assignments by resource type:

          Shows all role assignments for runners.

          ```yaml
          filter:
            resourceTypes:
              - RESOURCE_TYPE_RUNNER
          pagination:
            pageSize: 20
          ```

        ### Authorization

        All organization members can view role assignments (transparency model).

        Args:
          filter: Filter parameters

          pagination: Pagination parameters

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.GroupService/ListRoleAssignments",
            page=SyncAssignmentsPage[RoleAssignment],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                role_assignment_list_params.RoleAssignmentListParams,
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
                    role_assignment_list_params.RoleAssignmentListParams,
                ),
            ),
            model=RoleAssignment,
            method="post",
        )

    def delete(
        self,
        *,
        assignment_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Deletes a role assignment.

        Use this method to:

        - Remove group access to resources
        - Revoke role-based permissions

        ### Examples

        - Delete a role assignment:

          Removes a role assignment by its ID.

          ```yaml
          assignmentId: "a1b2c3d4-5678-90ab-cdef-1234567890ab"
          ```

        ### Authorization

        Requires admin role on the specific resource.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.GroupService/DeleteRoleAssignment",
            body=maybe_transform(
                {"assignment_id": assignment_id}, role_assignment_delete_params.RoleAssignmentDeleteParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncRoleAssignmentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRoleAssignmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRoleAssignmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRoleAssignmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return AsyncRoleAssignmentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        group_id: str | Omit = omit,
        resource_id: str | Omit = omit,
        resource_role: ResourceRole | Omit = omit,
        resource_type: ResourceType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RoleAssignmentCreateResponse:
        """
        Creates a role assignment for a group on a resource.

        Use this method to:

        - Assign specific roles to groups on runners, projects, or environments
        - Grant group-based access to resources

        ### Examples

        - Assign admin role on a runner:

          Grants the group admin access to a runner.

          ```yaml
          groupId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          resourceType: RESOURCE_TYPE_RUNNER
          resourceId: "f53d2330-3795-4c5d-a1f3-453121af9c60"
          resourceRole: RESOURCE_ROLE_RUNNER_ADMIN
          ```

        - Assign user role on a project:

          Grants the group user access to a project.

          ```yaml
          groupId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          resourceType: RESOURCE_TYPE_PROJECT
          resourceId: "a1b2c3d4-5678-90ab-cdef-1234567890ab"
          resourceRole: RESOURCE_ROLE_PROJECT_USER
          ```

        ### Authorization

        Requires admin role on the specific resource.

        Args:
          resource_role: ResourceRole represents roles that can be assigned to groups on resources These
              map directly to the roles defined in backend/db/rule/rbac/role/role.go

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.GroupService/CreateRoleAssignment",
            body=await async_maybe_transform(
                {
                    "group_id": group_id,
                    "resource_id": resource_id,
                    "resource_role": resource_role,
                    "resource_type": resource_type,
                },
                role_assignment_create_params.RoleAssignmentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoleAssignmentCreateResponse,
        )

    def list(
        self,
        *,
        token: str | Omit = omit,
        page_size: int | Omit = omit,
        filter: role_assignment_list_params.Filter | Omit = omit,
        pagination: role_assignment_list_params.Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[RoleAssignment, AsyncAssignmentsPage[RoleAssignment]]:
        """
        Lists role assignments for a group or resource.

        Use this method to:

        - View all role assignments for a group
        - Audit resource access
        - Check which groups have access to resources

        ### Examples

        - List role assignments for a group:

          Shows all role assignments for a specific group.

          ```yaml
          filter:
            groupId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          pagination:
            pageSize: 20
          ```

        - List role assignments by resource type:

          Shows all role assignments for runners.

          ```yaml
          filter:
            resourceTypes:
              - RESOURCE_TYPE_RUNNER
          pagination:
            pageSize: 20
          ```

        ### Authorization

        All organization members can view role assignments (transparency model).

        Args:
          filter: Filter parameters

          pagination: Pagination parameters

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.GroupService/ListRoleAssignments",
            page=AsyncAssignmentsPage[RoleAssignment],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                role_assignment_list_params.RoleAssignmentListParams,
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
                    role_assignment_list_params.RoleAssignmentListParams,
                ),
            ),
            model=RoleAssignment,
            method="post",
        )

    async def delete(
        self,
        *,
        assignment_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Deletes a role assignment.

        Use this method to:

        - Remove group access to resources
        - Revoke role-based permissions

        ### Examples

        - Delete a role assignment:

          Removes a role assignment by its ID.

          ```yaml
          assignmentId: "a1b2c3d4-5678-90ab-cdef-1234567890ab"
          ```

        ### Authorization

        Requires admin role on the specific resource.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.GroupService/DeleteRoleAssignment",
            body=await async_maybe_transform(
                {"assignment_id": assignment_id}, role_assignment_delete_params.RoleAssignmentDeleteParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class RoleAssignmentsResourceWithRawResponse:
    def __init__(self, role_assignments: RoleAssignmentsResource) -> None:
        self._role_assignments = role_assignments

        self.create = to_raw_response_wrapper(
            role_assignments.create,
        )
        self.list = to_raw_response_wrapper(
            role_assignments.list,
        )
        self.delete = to_raw_response_wrapper(
            role_assignments.delete,
        )


class AsyncRoleAssignmentsResourceWithRawResponse:
    def __init__(self, role_assignments: AsyncRoleAssignmentsResource) -> None:
        self._role_assignments = role_assignments

        self.create = async_to_raw_response_wrapper(
            role_assignments.create,
        )
        self.list = async_to_raw_response_wrapper(
            role_assignments.list,
        )
        self.delete = async_to_raw_response_wrapper(
            role_assignments.delete,
        )


class RoleAssignmentsResourceWithStreamingResponse:
    def __init__(self, role_assignments: RoleAssignmentsResource) -> None:
        self._role_assignments = role_assignments

        self.create = to_streamed_response_wrapper(
            role_assignments.create,
        )
        self.list = to_streamed_response_wrapper(
            role_assignments.list,
        )
        self.delete = to_streamed_response_wrapper(
            role_assignments.delete,
        )


class AsyncRoleAssignmentsResourceWithStreamingResponse:
    def __init__(self, role_assignments: AsyncRoleAssignmentsResource) -> None:
        self._role_assignments = role_assignments

        self.create = async_to_streamed_response_wrapper(
            role_assignments.create,
        )
        self.list = async_to_streamed_response_wrapper(
            role_assignments.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            role_assignments.delete,
        )
