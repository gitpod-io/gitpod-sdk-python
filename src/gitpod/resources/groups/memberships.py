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
from ...pagination import SyncMembersPage, AsyncMembersPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.groups import membership_list_params, membership_create_params, membership_delete_params
from ...types.shared_params.subject import Subject
from ...types.groups.group_membership import GroupMembership
from ...types.groups.membership_create_response import MembershipCreateResponse

__all__ = ["MembershipsResource", "AsyncMembershipsResource"]


class MembershipsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MembershipsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return MembershipsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MembershipsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return MembershipsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        group_id: str | Omit = omit,
        subject: Subject | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MembershipCreateResponse:
        """
        Creates a membership for a user in a group.

        Use this method to:

        - Add users to groups
        - Grant group-based permissions to users

        ### Examples

        - Add a user to a group:

          Creates a membership for a user in a group.

          ```yaml
          groupId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          subject:
            id: "f53d2330-3795-4c5d-a1f3-453121af9c60"
            principal: PRINCIPAL_USER
          ```

        ### Authorization

        Requires `org:admin` permission on the organization or `group:admin` permission
        on the specific group.

        Args:
          subject: Subject to add to the group

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.GroupService/CreateMembership",
            body=maybe_transform(
                {
                    "group_id": group_id,
                    "subject": subject,
                },
                membership_create_params.MembershipCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MembershipCreateResponse,
        )

    def list(
        self,
        *,
        token: str | Omit = omit,
        page_size: int | Omit = omit,
        group_id: str | Omit = omit,
        pagination: membership_list_params.Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncMembersPage[GroupMembership]:
        """
        Lists all memberships of a group.

        Use this method to:

        - View all members of a group
        - Audit group membership

        ### Examples

        - List group members:

          Shows all members of a specific group.

          ```yaml
          groupId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          pagination:
            pageSize: 20
          ```

        ### Authorization

        All organization members can view group membership (transparency model).

        Args:
          pagination: pagination contains the pagination options for listing memberships

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.GroupService/ListMemberships",
            page=SyncMembersPage[GroupMembership],
            body=maybe_transform(
                {
                    "group_id": group_id,
                    "pagination": pagination,
                },
                membership_list_params.MembershipListParams,
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
                    membership_list_params.MembershipListParams,
                ),
            ),
            model=GroupMembership,
            method="post",
        )

    def delete(
        self,
        *,
        membership_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Deletes a membership for a user in a group.

        Use this method to:

        - Remove users from groups
        - Revoke group-based permissions

        ### Examples

        - Remove a user from a group:

          Deletes a membership by its ID.

          ```yaml
          membershipId: "a1b2c3d4-5678-90ab-cdef-1234567890ab"
          ```

        ### Authorization

        Requires `org:admin` permission on the organization or `group:admin` permission
        on the specific group.

        Args:
          membership_id: The membership to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.GroupService/DeleteMembership",
            body=maybe_transform({"membership_id": membership_id}, membership_delete_params.MembershipDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncMembershipsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMembershipsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMembershipsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMembershipsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return AsyncMembershipsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        group_id: str | Omit = omit,
        subject: Subject | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MembershipCreateResponse:
        """
        Creates a membership for a user in a group.

        Use this method to:

        - Add users to groups
        - Grant group-based permissions to users

        ### Examples

        - Add a user to a group:

          Creates a membership for a user in a group.

          ```yaml
          groupId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          subject:
            id: "f53d2330-3795-4c5d-a1f3-453121af9c60"
            principal: PRINCIPAL_USER
          ```

        ### Authorization

        Requires `org:admin` permission on the organization or `group:admin` permission
        on the specific group.

        Args:
          subject: Subject to add to the group

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.GroupService/CreateMembership",
            body=await async_maybe_transform(
                {
                    "group_id": group_id,
                    "subject": subject,
                },
                membership_create_params.MembershipCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MembershipCreateResponse,
        )

    def list(
        self,
        *,
        token: str | Omit = omit,
        page_size: int | Omit = omit,
        group_id: str | Omit = omit,
        pagination: membership_list_params.Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[GroupMembership, AsyncMembersPage[GroupMembership]]:
        """
        Lists all memberships of a group.

        Use this method to:

        - View all members of a group
        - Audit group membership

        ### Examples

        - List group members:

          Shows all members of a specific group.

          ```yaml
          groupId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          pagination:
            pageSize: 20
          ```

        ### Authorization

        All organization members can view group membership (transparency model).

        Args:
          pagination: pagination contains the pagination options for listing memberships

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.GroupService/ListMemberships",
            page=AsyncMembersPage[GroupMembership],
            body=maybe_transform(
                {
                    "group_id": group_id,
                    "pagination": pagination,
                },
                membership_list_params.MembershipListParams,
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
                    membership_list_params.MembershipListParams,
                ),
            ),
            model=GroupMembership,
            method="post",
        )

    async def delete(
        self,
        *,
        membership_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Deletes a membership for a user in a group.

        Use this method to:

        - Remove users from groups
        - Revoke group-based permissions

        ### Examples

        - Remove a user from a group:

          Deletes a membership by its ID.

          ```yaml
          membershipId: "a1b2c3d4-5678-90ab-cdef-1234567890ab"
          ```

        ### Authorization

        Requires `org:admin` permission on the organization or `group:admin` permission
        on the specific group.

        Args:
          membership_id: The membership to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.GroupService/DeleteMembership",
            body=await async_maybe_transform(
                {"membership_id": membership_id}, membership_delete_params.MembershipDeleteParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class MembershipsResourceWithRawResponse:
    def __init__(self, memberships: MembershipsResource) -> None:
        self._memberships = memberships

        self.create = to_raw_response_wrapper(
            memberships.create,
        )
        self.list = to_raw_response_wrapper(
            memberships.list,
        )
        self.delete = to_raw_response_wrapper(
            memberships.delete,
        )


class AsyncMembershipsResourceWithRawResponse:
    def __init__(self, memberships: AsyncMembershipsResource) -> None:
        self._memberships = memberships

        self.create = async_to_raw_response_wrapper(
            memberships.create,
        )
        self.list = async_to_raw_response_wrapper(
            memberships.list,
        )
        self.delete = async_to_raw_response_wrapper(
            memberships.delete,
        )


class MembershipsResourceWithStreamingResponse:
    def __init__(self, memberships: MembershipsResource) -> None:
        self._memberships = memberships

        self.create = to_streamed_response_wrapper(
            memberships.create,
        )
        self.list = to_streamed_response_wrapper(
            memberships.list,
        )
        self.delete = to_streamed_response_wrapper(
            memberships.delete,
        )


class AsyncMembershipsResourceWithStreamingResponse:
    def __init__(self, memberships: AsyncMembershipsResource) -> None:
        self._memberships = memberships

        self.create = async_to_streamed_response_wrapper(
            memberships.create,
        )
        self.list = async_to_streamed_response_wrapper(
            memberships.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            memberships.delete,
        )
