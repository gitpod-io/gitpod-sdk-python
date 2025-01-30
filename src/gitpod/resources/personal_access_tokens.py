# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import personal_access_token_list_params, personal_access_token_delete_params
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
from ..types.personal_access_token_list_response import PersonalAccessTokenListResponse

__all__ = ["PersonalAccessTokensResource", "AsyncPersonalAccessTokensResource"]


class PersonalAccessTokensResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PersonalAccessTokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return PersonalAccessTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PersonalAccessTokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return PersonalAccessTokensResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        filter: personal_access_token_list_params.Filter | NotGiven = NOT_GIVEN,
        pagination: personal_access_token_list_params.Pagination | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PersonalAccessTokenListResponse:
        """
        ListPersonalAccessTokens

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.UserService/ListPersonalAccessTokens",
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                personal_access_token_list_params.PersonalAccessTokenListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PersonalAccessTokenListResponse,
        )

    def delete(
        self,
        *,
        personal_access_token_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        DeletePersonalAccessToken

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.UserService/DeletePersonalAccessToken",
            body=maybe_transform(
                {"personal_access_token_id": personal_access_token_id},
                personal_access_token_delete_params.PersonalAccessTokenDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncPersonalAccessTokensResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPersonalAccessTokensResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPersonalAccessTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPersonalAccessTokensResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return AsyncPersonalAccessTokensResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        filter: personal_access_token_list_params.Filter | NotGiven = NOT_GIVEN,
        pagination: personal_access_token_list_params.Pagination | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PersonalAccessTokenListResponse:
        """
        ListPersonalAccessTokens

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.UserService/ListPersonalAccessTokens",
            body=await async_maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                personal_access_token_list_params.PersonalAccessTokenListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PersonalAccessTokenListResponse,
        )

    async def delete(
        self,
        *,
        personal_access_token_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        DeletePersonalAccessToken

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.UserService/DeletePersonalAccessToken",
            body=await async_maybe_transform(
                {"personal_access_token_id": personal_access_token_id},
                personal_access_token_delete_params.PersonalAccessTokenDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class PersonalAccessTokensResourceWithRawResponse:
    def __init__(self, personal_access_tokens: PersonalAccessTokensResource) -> None:
        self._personal_access_tokens = personal_access_tokens

        self.list = to_raw_response_wrapper(
            personal_access_tokens.list,
        )
        self.delete = to_raw_response_wrapper(
            personal_access_tokens.delete,
        )


class AsyncPersonalAccessTokensResourceWithRawResponse:
    def __init__(self, personal_access_tokens: AsyncPersonalAccessTokensResource) -> None:
        self._personal_access_tokens = personal_access_tokens

        self.list = async_to_raw_response_wrapper(
            personal_access_tokens.list,
        )
        self.delete = async_to_raw_response_wrapper(
            personal_access_tokens.delete,
        )


class PersonalAccessTokensResourceWithStreamingResponse:
    def __init__(self, personal_access_tokens: PersonalAccessTokensResource) -> None:
        self._personal_access_tokens = personal_access_tokens

        self.list = to_streamed_response_wrapper(
            personal_access_tokens.list,
        )
        self.delete = to_streamed_response_wrapper(
            personal_access_tokens.delete,
        )


class AsyncPersonalAccessTokensResourceWithStreamingResponse:
    def __init__(self, personal_access_tokens: AsyncPersonalAccessTokensResource) -> None:
        self._personal_access_tokens = personal_access_tokens

        self.list = async_to_streamed_response_wrapper(
            personal_access_tokens.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            personal_access_tokens.delete,
        )
