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
from ..._base_client import make_request_options
from ...types.groups import share_create_params, share_delete_params
from ...types.shared.principal import Principal
from ...types.shared.resource_role import ResourceRole
from ...types.shared.resource_type import ResourceType

__all__ = ["SharesResource", "AsyncSharesResource"]


class SharesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SharesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SharesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SharesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return SharesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        principal: Principal | Omit = omit,
        principal_id: str | Omit = omit,
        resource_id: str | Omit = omit,
        resource_type: ResourceType | Omit = omit,
        role: ResourceRole | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Shares a resource directly with a principal (user or service account).

        Use this method to:

        - Grant a user or service account direct access to a runner, project, or other
          resource
        - Share resources without creating and managing groups manually

        ### Examples

        - Share a runner with a user:

          Grants admin access to a runner for a specific user.

          ```yaml
          resourceType: RESOURCE_TYPE_RUNNER
          resourceId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          principal: PRINCIPAL_USER
          principalId: "f53d2330-3795-4c5d-a1f3-453121af9c60"
          role: RESOURCE_ROLE_RUNNER_ADMIN
          ```

        - Share a runner with a service account:

          Grants user access to a runner for a service account.

          ```yaml
          resourceType: RESOURCE_TYPE_RUNNER
          resourceId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          principal: PRINCIPAL_SERVICE_ACCOUNT
          principalId: "a1b2c3d4-5678-90ab-cdef-1234567890ab"
          role: RESOURCE_ROLE_RUNNER_USER
          ```

        ### Authorization

        Requires admin role on the specific resource.

        Args:
          principal: Type of principal to share with (user or service account)

          principal_id: ID of the principal (user or service account) to share with

          resource_id: ID of the resource to share

          resource_type: Type of resource to share (runner, project, etc.)

          role: Role to grant the principal on the resource

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.GroupService/ShareResourceWithPrincipal",
            body=maybe_transform(
                {
                    "principal": principal,
                    "principal_id": principal_id,
                    "resource_id": resource_id,
                    "resource_type": resource_type,
                    "role": role,
                },
                share_create_params.ShareCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def delete(
        self,
        *,
        principal: Principal | Omit = omit,
        principal_id: str | Omit = omit,
        resource_id: str | Omit = omit,
        resource_type: ResourceType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Removes direct access for a principal (user or service account) from a resource.

        Use this method to:

        - Revoke a principal's direct access to a resource
        - Remove sharing without affecting group-based access

        ### Examples

        - Remove user access from a runner:

          Revokes a user's direct access to a runner.

          ```yaml
          resourceType: RESOURCE_TYPE_RUNNER
          resourceId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          principal: PRINCIPAL_USER
          principalId: "f53d2330-3795-4c5d-a1f3-453121af9c60"
          ```

        ### Authorization

        Requires admin role on the specific resource.

        Args:
          principal: Type of principal to remove access from (user or service account)

          principal_id: ID of the principal (user or service account) to remove access from

          resource_id: ID of the resource to unshare

          resource_type: Type of resource to unshare

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.GroupService/UnshareResourceWithPrincipal",
            body=maybe_transform(
                {
                    "principal": principal,
                    "principal_id": principal_id,
                    "resource_id": resource_id,
                    "resource_type": resource_type,
                },
                share_delete_params.ShareDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncSharesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSharesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSharesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSharesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return AsyncSharesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        principal: Principal | Omit = omit,
        principal_id: str | Omit = omit,
        resource_id: str | Omit = omit,
        resource_type: ResourceType | Omit = omit,
        role: ResourceRole | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Shares a resource directly with a principal (user or service account).

        Use this method to:

        - Grant a user or service account direct access to a runner, project, or other
          resource
        - Share resources without creating and managing groups manually

        ### Examples

        - Share a runner with a user:

          Grants admin access to a runner for a specific user.

          ```yaml
          resourceType: RESOURCE_TYPE_RUNNER
          resourceId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          principal: PRINCIPAL_USER
          principalId: "f53d2330-3795-4c5d-a1f3-453121af9c60"
          role: RESOURCE_ROLE_RUNNER_ADMIN
          ```

        - Share a runner with a service account:

          Grants user access to a runner for a service account.

          ```yaml
          resourceType: RESOURCE_TYPE_RUNNER
          resourceId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          principal: PRINCIPAL_SERVICE_ACCOUNT
          principalId: "a1b2c3d4-5678-90ab-cdef-1234567890ab"
          role: RESOURCE_ROLE_RUNNER_USER
          ```

        ### Authorization

        Requires admin role on the specific resource.

        Args:
          principal: Type of principal to share with (user or service account)

          principal_id: ID of the principal (user or service account) to share with

          resource_id: ID of the resource to share

          resource_type: Type of resource to share (runner, project, etc.)

          role: Role to grant the principal on the resource

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.GroupService/ShareResourceWithPrincipal",
            body=await async_maybe_transform(
                {
                    "principal": principal,
                    "principal_id": principal_id,
                    "resource_id": resource_id,
                    "resource_type": resource_type,
                    "role": role,
                },
                share_create_params.ShareCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def delete(
        self,
        *,
        principal: Principal | Omit = omit,
        principal_id: str | Omit = omit,
        resource_id: str | Omit = omit,
        resource_type: ResourceType | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Removes direct access for a principal (user or service account) from a resource.

        Use this method to:

        - Revoke a principal's direct access to a resource
        - Remove sharing without affecting group-based access

        ### Examples

        - Remove user access from a runner:

          Revokes a user's direct access to a runner.

          ```yaml
          resourceType: RESOURCE_TYPE_RUNNER
          resourceId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          principal: PRINCIPAL_USER
          principalId: "f53d2330-3795-4c5d-a1f3-453121af9c60"
          ```

        ### Authorization

        Requires admin role on the specific resource.

        Args:
          principal: Type of principal to remove access from (user or service account)

          principal_id: ID of the principal (user or service account) to remove access from

          resource_id: ID of the resource to unshare

          resource_type: Type of resource to unshare

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.GroupService/UnshareResourceWithPrincipal",
            body=await async_maybe_transform(
                {
                    "principal": principal,
                    "principal_id": principal_id,
                    "resource_id": resource_id,
                    "resource_type": resource_type,
                },
                share_delete_params.ShareDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class SharesResourceWithRawResponse:
    def __init__(self, shares: SharesResource) -> None:
        self._shares = shares

        self.create = to_raw_response_wrapper(
            shares.create,
        )
        self.delete = to_raw_response_wrapper(
            shares.delete,
        )


class AsyncSharesResourceWithRawResponse:
    def __init__(self, shares: AsyncSharesResource) -> None:
        self._shares = shares

        self.create = async_to_raw_response_wrapper(
            shares.create,
        )
        self.delete = async_to_raw_response_wrapper(
            shares.delete,
        )


class SharesResourceWithStreamingResponse:
    def __init__(self, shares: SharesResource) -> None:
        self._shares = shares

        self.create = to_streamed_response_wrapper(
            shares.create,
        )
        self.delete = to_streamed_response_wrapper(
            shares.delete,
        )


class AsyncSharesResourceWithStreamingResponse:
    def __init__(self, shares: AsyncSharesResource) -> None:
        self._shares = shares

        self.create = async_to_streamed_response_wrapper(
            shares.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            shares.delete,
        )
