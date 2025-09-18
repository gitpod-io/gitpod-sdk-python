# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import gateway_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncGatewaysPage, AsyncGatewaysPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.shared.gateway import Gateway

__all__ = ["GatewaysResource", "AsyncGatewaysResource"]


class GatewaysResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GatewaysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return GatewaysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GatewaysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return GatewaysResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        token: str | Omit = omit,
        page_size: int | Omit = omit,
        pagination: gateway_list_params.Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncGatewaysPage[Gateway]:
        """
        ListGateways

        Args:
          pagination: pagination contains the pagination options for listing gateways

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.GatewayService/ListGateways",
            page=SyncGatewaysPage[Gateway],
            body=maybe_transform({"pagination": pagination}, gateway_list_params.GatewayListParams),
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
                    gateway_list_params.GatewayListParams,
                ),
            ),
            model=Gateway,
            method="post",
        )


class AsyncGatewaysResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGatewaysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGatewaysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGatewaysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return AsyncGatewaysResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        token: str | Omit = omit,
        page_size: int | Omit = omit,
        pagination: gateway_list_params.Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Gateway, AsyncGatewaysPage[Gateway]]:
        """
        ListGateways

        Args:
          pagination: pagination contains the pagination options for listing gateways

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.GatewayService/ListGateways",
            page=AsyncGatewaysPage[Gateway],
            body=maybe_transform({"pagination": pagination}, gateway_list_params.GatewayListParams),
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
                    gateway_list_params.GatewayListParams,
                ),
            ),
            model=Gateway,
            method="post",
        )


class GatewaysResourceWithRawResponse:
    def __init__(self, gateways: GatewaysResource) -> None:
        self._gateways = gateways

        self.list = to_raw_response_wrapper(
            gateways.list,
        )


class AsyncGatewaysResourceWithRawResponse:
    def __init__(self, gateways: AsyncGatewaysResource) -> None:
        self._gateways = gateways

        self.list = async_to_raw_response_wrapper(
            gateways.list,
        )


class GatewaysResourceWithStreamingResponse:
    def __init__(self, gateways: GatewaysResource) -> None:
        self._gateways = gateways

        self.list = to_streamed_response_wrapper(
            gateways.list,
        )


class AsyncGatewaysResourceWithStreamingResponse:
    def __init__(self, gateways: AsyncGatewaysResource) -> None:
        self._gateways = gateways

        self.list = async_to_streamed_response_wrapper(
            gateways.list,
        )
