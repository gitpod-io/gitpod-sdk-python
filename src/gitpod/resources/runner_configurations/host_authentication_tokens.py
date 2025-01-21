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
from ...types.runner_configurations import (
    host_authentication_token_list_params,
    host_authentication_token_create_params,
    host_authentication_token_delete_params,
    host_authentication_token_update_params,
    host_authentication_token_retrieve_params,
)
from ...types.runner_configurations.host_authentication_token_list_response import HostAuthenticationTokenListResponse
from ...types.runner_configurations.host_authentication_token_create_response import (
    HostAuthenticationTokenCreateResponse,
)
from ...types.runner_configurations.host_authentication_token_retrieve_response import (
    HostAuthenticationTokenRetrieveResponse,
)

__all__ = ["HostAuthenticationTokensResource", "AsyncHostAuthenticationTokensResource"]


class HostAuthenticationTokensResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HostAuthenticationTokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return HostAuthenticationTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HostAuthenticationTokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return HostAuthenticationTokensResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        connect_protocol_version: Literal[1],
        id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HostAuthenticationTokenCreateResponse:
        """
        GetHostAuthenticationToken

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
            "/gitpod.v1.RunnerConfigurationService/GetHostAuthenticationToken",
            body=maybe_transform(
                {"id": id}, host_authentication_token_create_params.HostAuthenticationTokenCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HostAuthenticationTokenCreateResponse,
        )

    def retrieve(
        self,
        *,
        connect_protocol_version: Literal[1],
        base64: str | NotGiven = NOT_GIVEN,
        compression: str | NotGiven = NOT_GIVEN,
        connect: str | NotGiven = NOT_GIVEN,
        encoding: str | NotGiven = NOT_GIVEN,
        message: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HostAuthenticationTokenRetrieveResponse:
        """
        GetHostAuthenticationToken

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
        return self._get(
            "/gitpod.v1.RunnerConfigurationService/GetHostAuthenticationToken",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "base64": base64,
                        "compression": compression,
                        "connect": connect,
                        "encoding": encoding,
                        "message": message,
                    },
                    host_authentication_token_retrieve_params.HostAuthenticationTokenRetrieveParams,
                ),
            ),
            cast_to=HostAuthenticationTokenRetrieveResponse,
        )

    def update(
        self,
        *,
        body: host_authentication_token_update_params.Body,
        connect_protocol_version: Literal[1],
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        UpdateHostAuthenticationToken

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
            "/gitpod.v1.RunnerConfigurationService/UpdateHostAuthenticationToken",
            body=maybe_transform(body, host_authentication_token_update_params.HostAuthenticationTokenUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def list(
        self,
        *,
        connect_protocol_version: Literal[1],
        filter: host_authentication_token_list_params.Filter | NotGiven = NOT_GIVEN,
        pagination: host_authentication_token_list_params.Pagination | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HostAuthenticationTokenListResponse:
        """
        ListHostAuthenticationTokens

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
            "/gitpod.v1.RunnerConfigurationService/ListHostAuthenticationTokens",
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                host_authentication_token_list_params.HostAuthenticationTokenListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HostAuthenticationTokenListResponse,
        )

    def delete(
        self,
        *,
        connect_protocol_version: Literal[1],
        id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        DeleteHostAuthenticationToken

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
            "/gitpod.v1.RunnerConfigurationService/DeleteHostAuthenticationToken",
            body=maybe_transform(
                {"id": id}, host_authentication_token_delete_params.HostAuthenticationTokenDeleteParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncHostAuthenticationTokensResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHostAuthenticationTokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHostAuthenticationTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHostAuthenticationTokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return AsyncHostAuthenticationTokensResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        connect_protocol_version: Literal[1],
        id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HostAuthenticationTokenCreateResponse:
        """
        GetHostAuthenticationToken

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
            "/gitpod.v1.RunnerConfigurationService/GetHostAuthenticationToken",
            body=await async_maybe_transform(
                {"id": id}, host_authentication_token_create_params.HostAuthenticationTokenCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HostAuthenticationTokenCreateResponse,
        )

    async def retrieve(
        self,
        *,
        connect_protocol_version: Literal[1],
        base64: str | NotGiven = NOT_GIVEN,
        compression: str | NotGiven = NOT_GIVEN,
        connect: str | NotGiven = NOT_GIVEN,
        encoding: str | NotGiven = NOT_GIVEN,
        message: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HostAuthenticationTokenRetrieveResponse:
        """
        GetHostAuthenticationToken

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
        return await self._get(
            "/gitpod.v1.RunnerConfigurationService/GetHostAuthenticationToken",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "base64": base64,
                        "compression": compression,
                        "connect": connect,
                        "encoding": encoding,
                        "message": message,
                    },
                    host_authentication_token_retrieve_params.HostAuthenticationTokenRetrieveParams,
                ),
            ),
            cast_to=HostAuthenticationTokenRetrieveResponse,
        )

    async def update(
        self,
        *,
        body: host_authentication_token_update_params.Body,
        connect_protocol_version: Literal[1],
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        UpdateHostAuthenticationToken

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
            "/gitpod.v1.RunnerConfigurationService/UpdateHostAuthenticationToken",
            body=await async_maybe_transform(
                body, host_authentication_token_update_params.HostAuthenticationTokenUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def list(
        self,
        *,
        connect_protocol_version: Literal[1],
        filter: host_authentication_token_list_params.Filter | NotGiven = NOT_GIVEN,
        pagination: host_authentication_token_list_params.Pagination | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HostAuthenticationTokenListResponse:
        """
        ListHostAuthenticationTokens

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
            "/gitpod.v1.RunnerConfigurationService/ListHostAuthenticationTokens",
            body=await async_maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                host_authentication_token_list_params.HostAuthenticationTokenListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HostAuthenticationTokenListResponse,
        )

    async def delete(
        self,
        *,
        connect_protocol_version: Literal[1],
        id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        DeleteHostAuthenticationToken

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
            "/gitpod.v1.RunnerConfigurationService/DeleteHostAuthenticationToken",
            body=await async_maybe_transform(
                {"id": id}, host_authentication_token_delete_params.HostAuthenticationTokenDeleteParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class HostAuthenticationTokensResourceWithRawResponse:
    def __init__(self, host_authentication_tokens: HostAuthenticationTokensResource) -> None:
        self._host_authentication_tokens = host_authentication_tokens

        self.create = to_raw_response_wrapper(
            host_authentication_tokens.create,
        )
        self.retrieve = to_raw_response_wrapper(
            host_authentication_tokens.retrieve,
        )
        self.update = to_raw_response_wrapper(
            host_authentication_tokens.update,
        )
        self.list = to_raw_response_wrapper(
            host_authentication_tokens.list,
        )
        self.delete = to_raw_response_wrapper(
            host_authentication_tokens.delete,
        )


class AsyncHostAuthenticationTokensResourceWithRawResponse:
    def __init__(self, host_authentication_tokens: AsyncHostAuthenticationTokensResource) -> None:
        self._host_authentication_tokens = host_authentication_tokens

        self.create = async_to_raw_response_wrapper(
            host_authentication_tokens.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            host_authentication_tokens.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            host_authentication_tokens.update,
        )
        self.list = async_to_raw_response_wrapper(
            host_authentication_tokens.list,
        )
        self.delete = async_to_raw_response_wrapper(
            host_authentication_tokens.delete,
        )


class HostAuthenticationTokensResourceWithStreamingResponse:
    def __init__(self, host_authentication_tokens: HostAuthenticationTokensResource) -> None:
        self._host_authentication_tokens = host_authentication_tokens

        self.create = to_streamed_response_wrapper(
            host_authentication_tokens.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            host_authentication_tokens.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            host_authentication_tokens.update,
        )
        self.list = to_streamed_response_wrapper(
            host_authentication_tokens.list,
        )
        self.delete = to_streamed_response_wrapper(
            host_authentication_tokens.delete,
        )


class AsyncHostAuthenticationTokensResourceWithStreamingResponse:
    def __init__(self, host_authentication_tokens: AsyncHostAuthenticationTokensResource) -> None:
        self._host_authentication_tokens = host_authentication_tokens

        self.create = async_to_streamed_response_wrapper(
            host_authentication_tokens.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            host_authentication_tokens.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            host_authentication_tokens.update,
        )
        self.list = async_to_streamed_response_wrapper(
            host_authentication_tokens.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            host_authentication_tokens.delete,
        )
