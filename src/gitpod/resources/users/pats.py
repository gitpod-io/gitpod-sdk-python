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
from ...pagination import SyncPersonalAccessTokensPage, AsyncPersonalAccessTokensPage
from ...types.users import pat_get_params, pat_list_params, pat_delete_params
from ..._base_client import AsyncPaginator, make_request_options
from ...types.users.pat_get_response import PatGetResponse
from ...types.users.personal_access_token import PersonalAccessToken

__all__ = ["PatsResource", "AsyncPatsResource"]


class PatsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return PatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return PatsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        token: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        filter: pat_list_params.Filter | NotGiven = NOT_GIVEN,
        pagination: pat_list_params.Pagination | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncPersonalAccessTokensPage[PersonalAccessToken]:
        """
        Lists personal access tokens with optional filtering.

        Use this method to:

        - View all active tokens
        - Audit token usage
        - Manage token lifecycle

        ### Examples

        - List user tokens:

          Shows all tokens for specific users.

          ```yaml
          filter:
            userIds: ["f53d2330-3795-4c5d-a1f3-453121af9c60"]
          pagination:
            pageSize: 20
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.UserService/ListPersonalAccessTokens",
            page=SyncPersonalAccessTokensPage[PersonalAccessToken],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                pat_list_params.PatListParams,
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
                    pat_list_params.PatListParams,
                ),
            ),
            model=PersonalAccessToken,
            method="post",
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
        Deletes a personal access token.

        Use this method to:

        - Revoke token access
        - Remove unused tokens
        - Rotate credentials

        ### Examples

        - Delete token:

          Permanently revokes a token.

          ```yaml
          personalAccessTokenId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.UserService/DeletePersonalAccessToken",
            body=maybe_transform(
                {"personal_access_token_id": personal_access_token_id}, pat_delete_params.PatDeleteParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def get(
        self,
        *,
        personal_access_token_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PatGetResponse:
        """
        Gets details about a specific personal access token.

        Use this method to:

        - View token metadata
        - Check token expiration
        - Monitor token usage

        ### Examples

        - Get token details:

          Retrieves information about a specific token.

          ```yaml
          personalAccessTokenId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.UserService/GetPersonalAccessToken",
            body=maybe_transform({"personal_access_token_id": personal_access_token_id}, pat_get_params.PatGetParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PatGetResponse,
        )


class AsyncPatsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return AsyncPatsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        token: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        filter: pat_list_params.Filter | NotGiven = NOT_GIVEN,
        pagination: pat_list_params.Pagination | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[PersonalAccessToken, AsyncPersonalAccessTokensPage[PersonalAccessToken]]:
        """
        Lists personal access tokens with optional filtering.

        Use this method to:

        - View all active tokens
        - Audit token usage
        - Manage token lifecycle

        ### Examples

        - List user tokens:

          Shows all tokens for specific users.

          ```yaml
          filter:
            userIds: ["f53d2330-3795-4c5d-a1f3-453121af9c60"]
          pagination:
            pageSize: 20
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.UserService/ListPersonalAccessTokens",
            page=AsyncPersonalAccessTokensPage[PersonalAccessToken],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                pat_list_params.PatListParams,
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
                    pat_list_params.PatListParams,
                ),
            ),
            model=PersonalAccessToken,
            method="post",
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
        Deletes a personal access token.

        Use this method to:

        - Revoke token access
        - Remove unused tokens
        - Rotate credentials

        ### Examples

        - Delete token:

          Permanently revokes a token.

          ```yaml
          personalAccessTokenId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.UserService/DeletePersonalAccessToken",
            body=await async_maybe_transform(
                {"personal_access_token_id": personal_access_token_id}, pat_delete_params.PatDeleteParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def get(
        self,
        *,
        personal_access_token_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PatGetResponse:
        """
        Gets details about a specific personal access token.

        Use this method to:

        - View token metadata
        - Check token expiration
        - Monitor token usage

        ### Examples

        - Get token details:

          Retrieves information about a specific token.

          ```yaml
          personalAccessTokenId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.UserService/GetPersonalAccessToken",
            body=await async_maybe_transform(
                {"personal_access_token_id": personal_access_token_id}, pat_get_params.PatGetParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PatGetResponse,
        )


class PatsResourceWithRawResponse:
    def __init__(self, pats: PatsResource) -> None:
        self._pats = pats

        self.list = to_raw_response_wrapper(
            pats.list,
        )
        self.delete = to_raw_response_wrapper(
            pats.delete,
        )
        self.get = to_raw_response_wrapper(
            pats.get,
        )


class AsyncPatsResourceWithRawResponse:
    def __init__(self, pats: AsyncPatsResource) -> None:
        self._pats = pats

        self.list = async_to_raw_response_wrapper(
            pats.list,
        )
        self.delete = async_to_raw_response_wrapper(
            pats.delete,
        )
        self.get = async_to_raw_response_wrapper(
            pats.get,
        )


class PatsResourceWithStreamingResponse:
    def __init__(self, pats: PatsResource) -> None:
        self._pats = pats

        self.list = to_streamed_response_wrapper(
            pats.list,
        )
        self.delete = to_streamed_response_wrapper(
            pats.delete,
        )
        self.get = to_streamed_response_wrapper(
            pats.get,
        )


class AsyncPatsResourceWithStreamingResponse:
    def __init__(self, pats: AsyncPatsResource) -> None:
        self._pats = pats

        self.list = async_to_streamed_response_wrapper(
            pats.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            pats.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            pats.get,
        )
