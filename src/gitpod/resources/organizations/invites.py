# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

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
from ..._base_client import make_request_options
from ...types.organizations import invite_create_params, invite_retrieve_params, invite_get_summary_params
from ...types.organizations.invite_create_response import InviteCreateResponse
from ...types.organizations.invite_retrieve_response import InviteRetrieveResponse
from ...types.organizations.invite_get_summary_response import InviteGetSummaryResponse

__all__ = ["InvitesResource", "AsyncInvitesResource"]


class InvitesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InvitesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return InvitesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InvitesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return InvitesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InviteCreateResponse:
        """Creates an invite link for joining an organization.

        Any existing
        OrganizationInvites are invalidated and can no longer be used.

        Use this method to:

        - Generate shareable invite links
        - Manage team growth
        - Control organization access

        ### Examples

        - Create organization invite:

          Generates a new invite link for the organization.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.OrganizationService/CreateOrganizationInvite",
            body=maybe_transform({"organization_id": organization_id}, invite_create_params.InviteCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InviteCreateResponse,
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
    ) -> InviteRetrieveResponse:
        """
        GetOrganizationInvite

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.OrganizationService/GetOrganizationInvite",
            body=maybe_transform({"organization_id": organization_id}, invite_retrieve_params.InviteRetrieveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InviteRetrieveResponse,
        )

    def get_summary(
        self,
        *,
        invite_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InviteGetSummaryResponse:
        """
        Retrieves organization details and membership info based on an invite link.

        Use this method to:

        - Preview organization details before joining
        - Validate invite link authenticity
        - Check organization size and activity
        - View team information before accepting

        ### Examples

        - Get invite summary:

          Retrieves organization information from an invite.

          ```yaml
          inviteId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.OrganizationService/GetOrganizationInviteSummary",
            body=maybe_transform({"invite_id": invite_id}, invite_get_summary_params.InviteGetSummaryParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InviteGetSummaryResponse,
        )


class AsyncInvitesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInvitesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInvitesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInvitesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return AsyncInvitesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InviteCreateResponse:
        """Creates an invite link for joining an organization.

        Any existing
        OrganizationInvites are invalidated and can no longer be used.

        Use this method to:

        - Generate shareable invite links
        - Manage team growth
        - Control organization access

        ### Examples

        - Create organization invite:

          Generates a new invite link for the organization.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.OrganizationService/CreateOrganizationInvite",
            body=await async_maybe_transform(
                {"organization_id": organization_id}, invite_create_params.InviteCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InviteCreateResponse,
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
    ) -> InviteRetrieveResponse:
        """
        GetOrganizationInvite

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.OrganizationService/GetOrganizationInvite",
            body=await async_maybe_transform(
                {"organization_id": organization_id}, invite_retrieve_params.InviteRetrieveParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InviteRetrieveResponse,
        )

    async def get_summary(
        self,
        *,
        invite_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InviteGetSummaryResponse:
        """
        Retrieves organization details and membership info based on an invite link.

        Use this method to:

        - Preview organization details before joining
        - Validate invite link authenticity
        - Check organization size and activity
        - View team information before accepting

        ### Examples

        - Get invite summary:

          Retrieves organization information from an invite.

          ```yaml
          inviteId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.OrganizationService/GetOrganizationInviteSummary",
            body=await async_maybe_transform(
                {"invite_id": invite_id}, invite_get_summary_params.InviteGetSummaryParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InviteGetSummaryResponse,
        )


class InvitesResourceWithRawResponse:
    def __init__(self, invites: InvitesResource) -> None:
        self._invites = invites

        self.create = to_raw_response_wrapper(
            invites.create,
        )
        self.retrieve = to_raw_response_wrapper(
            invites.retrieve,
        )
        self.get_summary = to_raw_response_wrapper(
            invites.get_summary,
        )


class AsyncInvitesResourceWithRawResponse:
    def __init__(self, invites: AsyncInvitesResource) -> None:
        self._invites = invites

        self.create = async_to_raw_response_wrapper(
            invites.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            invites.retrieve,
        )
        self.get_summary = async_to_raw_response_wrapper(
            invites.get_summary,
        )


class InvitesResourceWithStreamingResponse:
    def __init__(self, invites: InvitesResource) -> None:
        self._invites = invites

        self.create = to_streamed_response_wrapper(
            invites.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            invites.retrieve,
        )
        self.get_summary = to_streamed_response_wrapper(
            invites.get_summary,
        )


class AsyncInvitesResourceWithStreamingResponse:
    def __init__(self, invites: AsyncInvitesResource) -> None:
        self._invites = invites

        self.create = async_to_streamed_response_wrapper(
            invites.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            invites.retrieve,
        )
        self.get_summary = async_to_streamed_response_wrapper(
            invites.get_summary,
        )
