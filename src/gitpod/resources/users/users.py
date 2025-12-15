# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .pats import (
    PatsResource,
    AsyncPatsResource,
    PatsResourceWithRawResponse,
    AsyncPatsResourceWithRawResponse,
    PatsResourceWithStreamingResponse,
    AsyncPatsResourceWithStreamingResponse,
)
from ...types import (
    user_get_user_params,
    user_delete_user_params,
    user_set_suspended_params,
    user_get_authenticated_user_params,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from .dotfiles import (
    DotfilesResource,
    AsyncDotfilesResource,
    DotfilesResourceWithRawResponse,
    AsyncDotfilesResourceWithRawResponse,
    DotfilesResourceWithStreamingResponse,
    AsyncDotfilesResourceWithStreamingResponse,
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
from ...types.user_get_user_response import UserGetUserResponse
from ...types.user_get_authenticated_user_response import UserGetAuthenticatedUserResponse

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def dotfiles(self) -> DotfilesResource:
        return DotfilesResource(self._client)

    @cached_property
    def pats(self) -> PatsResource:
        return PatsResource(self._client)

    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return UsersResourceWithStreamingResponse(self)

    def delete_user(
        self,
        *,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Deletes a user.

        If the User comes from an organization's SSO provider, the
        Account will also be deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.UserService/DeleteUser",
            body=maybe_transform({"user_id": user_id}, user_delete_user_params.UserDeleteUserParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def get_authenticated_user(
        self,
        *,
        empty: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserGetAuthenticatedUserResponse:
        """
        Gets information about the currently authenticated user.

        Use this method to:

        - Get user profile information
        - Check authentication status
        - Retrieve user settings
        - Verify account details

        ### Examples

        - Get current user:

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
            "/gitpod.v1.UserService/GetAuthenticatedUser",
            body=maybe_transform({"empty": empty}, user_get_authenticated_user_params.UserGetAuthenticatedUserParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserGetAuthenticatedUserResponse,
        )

    def get_user(
        self,
        *,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserGetUserResponse:
        """
        Gets basic information about a specific user by their ID.

        Use this method to:

        - Retrieve user profile information
        - Get user details for display purposes
        - Fetch user metadata for administrative tasks

        ### Examples

        - Get user by ID:

          Retrieves basic user information by user ID.

          ```yaml
          userId: "f53d2330-3795-4c5d-a1f3-453121af9c60"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.UserService/GetUser",
            body=maybe_transform({"user_id": user_id}, user_get_user_params.UserGetUserParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserGetUserResponse,
        )

    def set_suspended(
        self,
        *,
        suspended: bool | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Sets whether a user account is suspended.

        Use this method to:

        - Suspend problematic users
        - Reactivate suspended accounts
        - Manage user access

        ### Examples

        - Suspend user:

          Suspends a user account.

          ```yaml
          userId: "f53d2330-3795-4c5d-a1f3-453121af9c60"
          suspended: true
          ```

        - Reactivate user:

          Removes suspension from a user account.

          ```yaml
          userId: "f53d2330-3795-4c5d-a1f3-453121af9c60"
          suspended: false
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.UserService/SetSuspended",
            body=maybe_transform(
                {
                    "suspended": suspended,
                    "user_id": user_id,
                },
                user_set_suspended_params.UserSetSuspendedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def dotfiles(self) -> AsyncDotfilesResource:
        return AsyncDotfilesResource(self._client)

    @cached_property
    def pats(self) -> AsyncPatsResource:
        return AsyncPatsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return AsyncUsersResourceWithStreamingResponse(self)

    async def delete_user(
        self,
        *,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Deletes a user.

        If the User comes from an organization's SSO provider, the
        Account will also be deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.UserService/DeleteUser",
            body=await async_maybe_transform({"user_id": user_id}, user_delete_user_params.UserDeleteUserParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def get_authenticated_user(
        self,
        *,
        empty: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserGetAuthenticatedUserResponse:
        """
        Gets information about the currently authenticated user.

        Use this method to:

        - Get user profile information
        - Check authentication status
        - Retrieve user settings
        - Verify account details

        ### Examples

        - Get current user:

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
            "/gitpod.v1.UserService/GetAuthenticatedUser",
            body=await async_maybe_transform(
                {"empty": empty}, user_get_authenticated_user_params.UserGetAuthenticatedUserParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserGetAuthenticatedUserResponse,
        )

    async def get_user(
        self,
        *,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserGetUserResponse:
        """
        Gets basic information about a specific user by their ID.

        Use this method to:

        - Retrieve user profile information
        - Get user details for display purposes
        - Fetch user metadata for administrative tasks

        ### Examples

        - Get user by ID:

          Retrieves basic user information by user ID.

          ```yaml
          userId: "f53d2330-3795-4c5d-a1f3-453121af9c60"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.UserService/GetUser",
            body=await async_maybe_transform({"user_id": user_id}, user_get_user_params.UserGetUserParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserGetUserResponse,
        )

    async def set_suspended(
        self,
        *,
        suspended: bool | Omit = omit,
        user_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Sets whether a user account is suspended.

        Use this method to:

        - Suspend problematic users
        - Reactivate suspended accounts
        - Manage user access

        ### Examples

        - Suspend user:

          Suspends a user account.

          ```yaml
          userId: "f53d2330-3795-4c5d-a1f3-453121af9c60"
          suspended: true
          ```

        - Reactivate user:

          Removes suspension from a user account.

          ```yaml
          userId: "f53d2330-3795-4c5d-a1f3-453121af9c60"
          suspended: false
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.UserService/SetSuspended",
            body=await async_maybe_transform(
                {
                    "suspended": suspended,
                    "user_id": user_id,
                },
                user_set_suspended_params.UserSetSuspendedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.delete_user = to_raw_response_wrapper(
            users.delete_user,
        )
        self.get_authenticated_user = to_raw_response_wrapper(
            users.get_authenticated_user,
        )
        self.get_user = to_raw_response_wrapper(
            users.get_user,
        )
        self.set_suspended = to_raw_response_wrapper(
            users.set_suspended,
        )

    @cached_property
    def dotfiles(self) -> DotfilesResourceWithRawResponse:
        return DotfilesResourceWithRawResponse(self._users.dotfiles)

    @cached_property
    def pats(self) -> PatsResourceWithRawResponse:
        return PatsResourceWithRawResponse(self._users.pats)


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.delete_user = async_to_raw_response_wrapper(
            users.delete_user,
        )
        self.get_authenticated_user = async_to_raw_response_wrapper(
            users.get_authenticated_user,
        )
        self.get_user = async_to_raw_response_wrapper(
            users.get_user,
        )
        self.set_suspended = async_to_raw_response_wrapper(
            users.set_suspended,
        )

    @cached_property
    def dotfiles(self) -> AsyncDotfilesResourceWithRawResponse:
        return AsyncDotfilesResourceWithRawResponse(self._users.dotfiles)

    @cached_property
    def pats(self) -> AsyncPatsResourceWithRawResponse:
        return AsyncPatsResourceWithRawResponse(self._users.pats)


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.delete_user = to_streamed_response_wrapper(
            users.delete_user,
        )
        self.get_authenticated_user = to_streamed_response_wrapper(
            users.get_authenticated_user,
        )
        self.get_user = to_streamed_response_wrapper(
            users.get_user,
        )
        self.set_suspended = to_streamed_response_wrapper(
            users.set_suspended,
        )

    @cached_property
    def dotfiles(self) -> DotfilesResourceWithStreamingResponse:
        return DotfilesResourceWithStreamingResponse(self._users.dotfiles)

    @cached_property
    def pats(self) -> PatsResourceWithStreamingResponse:
        return PatsResourceWithStreamingResponse(self._users.pats)


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.delete_user = async_to_streamed_response_wrapper(
            users.delete_user,
        )
        self.get_authenticated_user = async_to_streamed_response_wrapper(
            users.get_authenticated_user,
        )
        self.get_user = async_to_streamed_response_wrapper(
            users.get_user,
        )
        self.set_suspended = async_to_streamed_response_wrapper(
            users.set_suspended,
        )

    @cached_property
    def dotfiles(self) -> AsyncDotfilesResourceWithStreamingResponse:
        return AsyncDotfilesResourceWithStreamingResponse(self._users.dotfiles)

    @cached_property
    def pats(self) -> AsyncPatsResourceWithStreamingResponse:
        return AsyncPatsResourceWithStreamingResponse(self._users.pats)
