# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...types import organization_leave_params, organization_set_role_params
from .members import (
    MembersResource,
    AsyncMembersResource,
    MembersResourceWithRawResponse,
    AsyncMembersResourceWithRawResponse,
    MembersResourceWithStreamingResponse,
    AsyncMembersResourceWithStreamingResponse,
)
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
from .invite.invite import (
    InviteResource,
    AsyncInviteResource,
    InviteResourceWithRawResponse,
    AsyncInviteResourceWithRawResponse,
    InviteResourceWithStreamingResponse,
    AsyncInviteResourceWithStreamingResponse,
)
from ..._base_client import make_request_options

__all__ = ["OrganizationsResource", "AsyncOrganizationsResource"]


class OrganizationsResource(SyncAPIResource):
    @cached_property
    def members(self) -> MembersResource:
        return MembersResource(self._client)

    @cached_property
    def invite(self) -> InviteResource:
        return InviteResource(self._client)

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

    def leave(
        self,
        *,
        connect_protocol_version: Literal[1],
        user_id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
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
            "/gitpod.v1.OrganizationService/LeaveOrganization",
            body=maybe_transform({"user_id": user_id}, organization_leave_params.OrganizationLeaveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def set_role(
        self,
        *,
        connect_protocol_version: Literal[1],
        organization_id: str | NotGiven = NOT_GIVEN,
        role: Literal["ORGANIZATION_ROLE_UNSPECIFIED", "ORGANIZATION_ROLE_ADMIN", "ORGANIZATION_ROLE_MEMBER"]
        | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
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
    def members(self) -> AsyncMembersResource:
        return AsyncMembersResource(self._client)

    @cached_property
    def invite(self) -> AsyncInviteResource:
        return AsyncInviteResource(self._client)

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

    async def leave(
        self,
        *,
        connect_protocol_version: Literal[1],
        user_id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
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
            "/gitpod.v1.OrganizationService/LeaveOrganization",
            body=await async_maybe_transform({"user_id": user_id}, organization_leave_params.OrganizationLeaveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def set_role(
        self,
        *,
        connect_protocol_version: Literal[1],
        organization_id: str | NotGiven = NOT_GIVEN,
        role: Literal["ORGANIZATION_ROLE_UNSPECIFIED", "ORGANIZATION_ROLE_ADMIN", "ORGANIZATION_ROLE_MEMBER"]
        | NotGiven = NOT_GIVEN,
        user_id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
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

        self.leave = to_raw_response_wrapper(
            organizations.leave,
        )
        self.set_role = to_raw_response_wrapper(
            organizations.set_role,
        )

    @cached_property
    def members(self) -> MembersResourceWithRawResponse:
        return MembersResourceWithRawResponse(self._organizations.members)

    @cached_property
    def invite(self) -> InviteResourceWithRawResponse:
        return InviteResourceWithRawResponse(self._organizations.invite)


class AsyncOrganizationsResourceWithRawResponse:
    def __init__(self, organizations: AsyncOrganizationsResource) -> None:
        self._organizations = organizations

        self.leave = async_to_raw_response_wrapper(
            organizations.leave,
        )
        self.set_role = async_to_raw_response_wrapper(
            organizations.set_role,
        )

    @cached_property
    def members(self) -> AsyncMembersResourceWithRawResponse:
        return AsyncMembersResourceWithRawResponse(self._organizations.members)

    @cached_property
    def invite(self) -> AsyncInviteResourceWithRawResponse:
        return AsyncInviteResourceWithRawResponse(self._organizations.invite)


class OrganizationsResourceWithStreamingResponse:
    def __init__(self, organizations: OrganizationsResource) -> None:
        self._organizations = organizations

        self.leave = to_streamed_response_wrapper(
            organizations.leave,
        )
        self.set_role = to_streamed_response_wrapper(
            organizations.set_role,
        )

    @cached_property
    def members(self) -> MembersResourceWithStreamingResponse:
        return MembersResourceWithStreamingResponse(self._organizations.members)

    @cached_property
    def invite(self) -> InviteResourceWithStreamingResponse:
        return InviteResourceWithStreamingResponse(self._organizations.invite)


class AsyncOrganizationsResourceWithStreamingResponse:
    def __init__(self, organizations: AsyncOrganizationsResource) -> None:
        self._organizations = organizations

        self.leave = async_to_streamed_response_wrapper(
            organizations.leave,
        )
        self.set_role = async_to_streamed_response_wrapper(
            organizations.set_role,
        )

    @cached_property
    def members(self) -> AsyncMembersResourceWithStreamingResponse:
        return AsyncMembersResourceWithStreamingResponse(self._organizations.members)

    @cached_property
    def invite(self) -> AsyncInviteResourceWithStreamingResponse:
        return AsyncInviteResourceWithStreamingResponse(self._organizations.invite)
