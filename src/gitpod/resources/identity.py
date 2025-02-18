# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ..types import (
    identity_get_id_token_params,
    identity_exchange_token_params,
    identity_get_authenticated_identity_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.identity_get_id_token_response import IdentityGetIDTokenResponse
from ..types.identity_exchange_token_response import IdentityExchangeTokenResponse
from ..types.identity_get_authenticated_identity_response import IdentityGetAuthenticatedIdentityResponse

__all__ = ["IdentityResource", "AsyncIdentityResource"]


class IdentityResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IdentityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return IdentityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IdentityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return IdentityResourceWithStreamingResponse(self)

    def exchange_token(
        self,
        *,
        exchange_token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityExchangeTokenResponse:
        """
        Exchanges an exchange token for a new access token.

        Use this method to:

        - Convert exchange tokens to access tokens
        - Obtain new access credentials
        - Complete token exchange flows

        ### Examples

        - Exchange token:

          Trades an exchange token for an access token.

          ```yaml
          exchangeToken: "exchange-token-value"
          ```

        Args:
          exchange_token: exchange_token is the token to exchange

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.IdentityService/ExchangeToken",
            body=maybe_transform(
                {"exchange_token": exchange_token}, identity_exchange_token_params.IdentityExchangeTokenParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdentityExchangeTokenResponse,
        )

    def get_authenticated_identity(
        self,
        *,
        empty: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityGetAuthenticatedIdentityResponse:
        """
        Retrieves information about the currently authenticated identity.

        Use this method to:

        - Get current user information
        - Check authentication status
        - Retrieve organization context
        - Validate authentication principal

        ### Examples

        - Get current identity:

          Retrieves details about the authenticated user.

          ```yaml
          {}
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.IdentityService/GetAuthenticatedIdentity",
            body=maybe_transform(
                {"empty": empty}, identity_get_authenticated_identity_params.IdentityGetAuthenticatedIdentityParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdentityGetAuthenticatedIdentityResponse,
        )

    def get_id_token(
        self,
        *,
        audience: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityGetIDTokenResponse:
        """
        Gets an ID token for authenticating with other services.

        Use this method to:

        - Obtain authentication tokens for service-to-service calls
        - Access protected resources
        - Generate scoped access tokens

        ### Examples

        - Get token for single service:

          Retrieves a token for authenticating with one service.

          ```yaml
          audience:
            - "https://api.gitpod.io"
          ```

        - Get token for multiple services:

          Retrieves a token valid for multiple services.

          ```yaml
          audience:
            - "https://api.gitpod.io"
            - "https://ws.gitpod.io"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.IdentityService/GetIDToken",
            body=maybe_transform({"audience": audience}, identity_get_id_token_params.IdentityGetIDTokenParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdentityGetIDTokenResponse,
        )


class AsyncIdentityResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIdentityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIdentityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIdentityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return AsyncIdentityResourceWithStreamingResponse(self)

    async def exchange_token(
        self,
        *,
        exchange_token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityExchangeTokenResponse:
        """
        Exchanges an exchange token for a new access token.

        Use this method to:

        - Convert exchange tokens to access tokens
        - Obtain new access credentials
        - Complete token exchange flows

        ### Examples

        - Exchange token:

          Trades an exchange token for an access token.

          ```yaml
          exchangeToken: "exchange-token-value"
          ```

        Args:
          exchange_token: exchange_token is the token to exchange

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.IdentityService/ExchangeToken",
            body=await async_maybe_transform(
                {"exchange_token": exchange_token}, identity_exchange_token_params.IdentityExchangeTokenParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdentityExchangeTokenResponse,
        )

    async def get_authenticated_identity(
        self,
        *,
        empty: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityGetAuthenticatedIdentityResponse:
        """
        Retrieves information about the currently authenticated identity.

        Use this method to:

        - Get current user information
        - Check authentication status
        - Retrieve organization context
        - Validate authentication principal

        ### Examples

        - Get current identity:

          Retrieves details about the authenticated user.

          ```yaml
          {}
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.IdentityService/GetAuthenticatedIdentity",
            body=await async_maybe_transform(
                {"empty": empty}, identity_get_authenticated_identity_params.IdentityGetAuthenticatedIdentityParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdentityGetAuthenticatedIdentityResponse,
        )

    async def get_id_token(
        self,
        *,
        audience: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IdentityGetIDTokenResponse:
        """
        Gets an ID token for authenticating with other services.

        Use this method to:

        - Obtain authentication tokens for service-to-service calls
        - Access protected resources
        - Generate scoped access tokens

        ### Examples

        - Get token for single service:

          Retrieves a token for authenticating with one service.

          ```yaml
          audience:
            - "https://api.gitpod.io"
          ```

        - Get token for multiple services:

          Retrieves a token valid for multiple services.

          ```yaml
          audience:
            - "https://api.gitpod.io"
            - "https://ws.gitpod.io"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.IdentityService/GetIDToken",
            body=await async_maybe_transform(
                {"audience": audience}, identity_get_id_token_params.IdentityGetIDTokenParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IdentityGetIDTokenResponse,
        )


class IdentityResourceWithRawResponse:
    def __init__(self, identity: IdentityResource) -> None:
        self._identity = identity

        self.exchange_token = to_raw_response_wrapper(
            identity.exchange_token,
        )
        self.get_authenticated_identity = to_raw_response_wrapper(
            identity.get_authenticated_identity,
        )
        self.get_id_token = to_raw_response_wrapper(
            identity.get_id_token,
        )


class AsyncIdentityResourceWithRawResponse:
    def __init__(self, identity: AsyncIdentityResource) -> None:
        self._identity = identity

        self.exchange_token = async_to_raw_response_wrapper(
            identity.exchange_token,
        )
        self.get_authenticated_identity = async_to_raw_response_wrapper(
            identity.get_authenticated_identity,
        )
        self.get_id_token = async_to_raw_response_wrapper(
            identity.get_id_token,
        )


class IdentityResourceWithStreamingResponse:
    def __init__(self, identity: IdentityResource) -> None:
        self._identity = identity

        self.exchange_token = to_streamed_response_wrapper(
            identity.exchange_token,
        )
        self.get_authenticated_identity = to_streamed_response_wrapper(
            identity.get_authenticated_identity,
        )
        self.get_id_token = to_streamed_response_wrapper(
            identity.get_id_token,
        )


class AsyncIdentityResourceWithStreamingResponse:
    def __init__(self, identity: AsyncIdentityResource) -> None:
        self._identity = identity

        self.exchange_token = async_to_streamed_response_wrapper(
            identity.exchange_token,
        )
        self.get_authenticated_identity = async_to_streamed_response_wrapper(
            identity.get_authenticated_identity,
        )
        self.get_id_token = async_to_streamed_response_wrapper(
            identity.get_id_token,
        )
