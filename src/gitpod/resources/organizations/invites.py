# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    is_given,
    maybe_transform,
    strip_not_given,
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

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return InvitesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InvitesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return InvitesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        connect_protocol_version: Literal[1],
        organization_id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InviteCreateResponse:
        """CreateOrganizationInvite creates an invite for the organization.

        Any existing
        OrganizationInvites are invalidated and can no longer be used.

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          connect_timeout_ms: Define the timeout, in ms

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Connect-Protocol-Version": str(connect_protocol_version),
                    "Connect-Timeout-Ms": str(connect_timeout_ms) if is_given(connect_timeout_ms) else NOT_GIVEN,
                }
            ),
            **(extra_headers or {}),
        }
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
        connect_protocol_version: Literal[1],
        organization_id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InviteRetrieveResponse:
        """GetOrganizationInvite retrieves invite for the organization.

        If no invite
        exists, a new one is created.

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          connect_timeout_ms: Define the timeout, in ms

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Connect-Protocol-Version": str(connect_protocol_version),
                    "Connect-Timeout-Ms": str(connect_timeout_ms) if is_given(connect_timeout_ms) else NOT_GIVEN,
                }
            ),
            **(extra_headers or {}),
        }
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
        connect_protocol_version: Literal[1],
        invite_id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InviteGetSummaryResponse:
        """
        GetOrganizationInviteSummary retrieves a summary of the organization based on an
        Invite ID.

        Used to discover which organization an invite is for.

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          connect_timeout_ms: Define the timeout, in ms

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Connect-Protocol-Version": str(connect_protocol_version),
                    "Connect-Timeout-Ms": str(connect_timeout_ms) if is_given(connect_timeout_ms) else NOT_GIVEN,
                }
            ),
            **(extra_headers or {}),
        }
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

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInvitesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInvitesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return AsyncInvitesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        connect_protocol_version: Literal[1],
        organization_id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InviteCreateResponse:
        """CreateOrganizationInvite creates an invite for the organization.

        Any existing
        OrganizationInvites are invalidated and can no longer be used.

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          connect_timeout_ms: Define the timeout, in ms

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Connect-Protocol-Version": str(connect_protocol_version),
                    "Connect-Timeout-Ms": str(connect_timeout_ms) if is_given(connect_timeout_ms) else NOT_GIVEN,
                }
            ),
            **(extra_headers or {}),
        }
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
        connect_protocol_version: Literal[1],
        organization_id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InviteRetrieveResponse:
        """GetOrganizationInvite retrieves invite for the organization.

        If no invite
        exists, a new one is created.

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          connect_timeout_ms: Define the timeout, in ms

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Connect-Protocol-Version": str(connect_protocol_version),
                    "Connect-Timeout-Ms": str(connect_timeout_ms) if is_given(connect_timeout_ms) else NOT_GIVEN,
                }
            ),
            **(extra_headers or {}),
        }
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
        connect_protocol_version: Literal[1],
        invite_id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InviteGetSummaryResponse:
        """
        GetOrganizationInviteSummary retrieves a summary of the organization based on an
        Invite ID.

        Used to discover which organization an invite is for.

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          connect_timeout_ms: Define the timeout, in ms

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "Connect-Protocol-Version": str(connect_protocol_version),
                    "Connect-Timeout-Ms": str(connect_timeout_ms) if is_given(connect_timeout_ms) else NOT_GIVEN,
                }
            ),
            **(extra_headers or {}),
        }
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
