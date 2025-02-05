# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    account_delete_params,
    account_retrieve_params,
    account_get_sso_login_url_params,
    account_list_login_providers_params,
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
from ..pagination import SyncLoginProvidersPage, AsyncLoginProvidersPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.account_retrieve_response import AccountRetrieveResponse
from ..types.account_get_sso_login_url_response import AccountGetSSOLoginURLResponse
from ..types.account_list_login_providers_response import AccountListLoginProvidersResponse

__all__ = ["AccountsResource", "AsyncAccountsResource"]


class AccountsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/flex-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/flex-sdk-python#with_streaming_response
        """
        return AccountsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        empty: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountRetrieveResponse:
        """
        GetAccount retrieves a single Account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.AccountService/GetAccount",
            body=maybe_transform({"empty": empty}, account_retrieve_params.AccountRetrieveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountRetrieveResponse,
        )

    def delete(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """DeleteAccount deletes an Account.

        To Delete an Account, the Account must not be
        an active member of any Organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.AccountService/DeleteAccount",
            body=maybe_transform({"account_id": account_id}, account_delete_params.AccountDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def get_sso_login_url(
        self,
        *,
        return_to: str,
        email: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountGetSSOLoginURLResponse:
        """
        GetSSOLoginURL returns the URL to redirect the user to for SSO login.

        Args:
          return_to: return_to is the URL the user will be redirected to after login

          email: email is the email the user wants to login with

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.AccountService/GetSSOLoginURL",
            body=maybe_transform(
                {
                    "return_to": return_to,
                    "email": email,
                },
                account_get_sso_login_url_params.AccountGetSSOLoginURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountGetSSOLoginURLResponse,
        )

    def list_login_providers(
        self,
        *,
        token: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        filter: account_list_login_providers_params.Filter | NotGiven = NOT_GIVEN,
        pagination: account_list_login_providers_params.Pagination | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncLoginProvidersPage[AccountListLoginProvidersResponse]:
        """
        ListLoginProviders returns the list of login providers matching the provided
        filters.

        Args:
          filter: filter contains the filter options for listing login methods

          pagination: pagination contains the pagination options for listing login methods

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.AccountService/ListLoginProviders",
            page=SyncLoginProvidersPage[AccountListLoginProvidersResponse],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                account_list_login_providers_params.AccountListLoginProvidersParams,
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
                    account_list_login_providers_params.AccountListLoginProvidersParams,
                ),
            ),
            model=AccountListLoginProvidersResponse,
            method="post",
        )


class AsyncAccountsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/flex-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/flex-sdk-python#with_streaming_response
        """
        return AsyncAccountsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        empty: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountRetrieveResponse:
        """
        GetAccount retrieves a single Account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.AccountService/GetAccount",
            body=await async_maybe_transform({"empty": empty}, account_retrieve_params.AccountRetrieveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountRetrieveResponse,
        )

    async def delete(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """DeleteAccount deletes an Account.

        To Delete an Account, the Account must not be
        an active member of any Organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.AccountService/DeleteAccount",
            body=await async_maybe_transform({"account_id": account_id}, account_delete_params.AccountDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def get_sso_login_url(
        self,
        *,
        return_to: str,
        email: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountGetSSOLoginURLResponse:
        """
        GetSSOLoginURL returns the URL to redirect the user to for SSO login.

        Args:
          return_to: return_to is the URL the user will be redirected to after login

          email: email is the email the user wants to login with

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.AccountService/GetSSOLoginURL",
            body=await async_maybe_transform(
                {
                    "return_to": return_to,
                    "email": email,
                },
                account_get_sso_login_url_params.AccountGetSSOLoginURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountGetSSOLoginURLResponse,
        )

    def list_login_providers(
        self,
        *,
        token: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        filter: account_list_login_providers_params.Filter | NotGiven = NOT_GIVEN,
        pagination: account_list_login_providers_params.Pagination | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[AccountListLoginProvidersResponse, AsyncLoginProvidersPage[AccountListLoginProvidersResponse]]:
        """
        ListLoginProviders returns the list of login providers matching the provided
        filters.

        Args:
          filter: filter contains the filter options for listing login methods

          pagination: pagination contains the pagination options for listing login methods

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.AccountService/ListLoginProviders",
            page=AsyncLoginProvidersPage[AccountListLoginProvidersResponse],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                account_list_login_providers_params.AccountListLoginProvidersParams,
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
                    account_list_login_providers_params.AccountListLoginProvidersParams,
                ),
            ),
            model=AccountListLoginProvidersResponse,
            method="post",
        )


class AccountsResourceWithRawResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.retrieve = to_raw_response_wrapper(
            accounts.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            accounts.delete,
        )
        self.get_sso_login_url = to_raw_response_wrapper(
            accounts.get_sso_login_url,
        )
        self.list_login_providers = to_raw_response_wrapper(
            accounts.list_login_providers,
        )


class AsyncAccountsResourceWithRawResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.retrieve = async_to_raw_response_wrapper(
            accounts.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            accounts.delete,
        )
        self.get_sso_login_url = async_to_raw_response_wrapper(
            accounts.get_sso_login_url,
        )
        self.list_login_providers = async_to_raw_response_wrapper(
            accounts.list_login_providers,
        )


class AccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.retrieve = to_streamed_response_wrapper(
            accounts.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            accounts.delete,
        )
        self.get_sso_login_url = to_streamed_response_wrapper(
            accounts.get_sso_login_url,
        )
        self.list_login_providers = to_streamed_response_wrapper(
            accounts.list_login_providers,
        )


class AsyncAccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.retrieve = async_to_streamed_response_wrapper(
            accounts.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            accounts.delete,
        )
        self.get_sso_login_url = async_to_streamed_response_wrapper(
            accounts.get_sso_login_url,
        )
        self.list_login_providers = async_to_streamed_response_wrapper(
            accounts.list_login_providers,
        )
