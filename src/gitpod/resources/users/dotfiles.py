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
from ...types.users import dotfile_get_params, dotfile_set_params
from ..._base_client import make_request_options
from ...types.users.dotfile_get_response import DotfileGetResponse

__all__ = ["DotfilesResource", "AsyncDotfilesResource"]


class DotfilesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DotfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return DotfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DotfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return DotfilesResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        empty: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DotfileGetResponse:
        """
        Gets the dotfiles for a user.

        Use this method to:

        - Retrieve user dotfiles

        ### Examples

        - Get dotfiles:

          Retrieves the dotfiles for the current user.

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
            "/gitpod.v1.UserService/GetDotfilesConfiguration",
            body=maybe_transform({"empty": empty}, dotfile_get_params.DotfileGetParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DotfileGetResponse,
        )

    def set(
        self,
        *,
        repository: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Sets the dotfiles configuration for a user.

        Use this method to:

        - Configure user dotfiles
        - Update dotfiles settings

        ### Examples

        - Set dotfiles configuration:

          Sets the dotfiles configuration for the current user.

          ```yaml
          { "repository": "https://github.com/gitpod-io/dotfiles" }
          ```

        - Remove dotfiles:

          Removes the dotfiles for the current user.

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
            "/gitpod.v1.UserService/SetDotfilesConfiguration",
            body=maybe_transform({"repository": repository}, dotfile_set_params.DotfileSetParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncDotfilesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDotfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDotfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDotfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return AsyncDotfilesResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        empty: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DotfileGetResponse:
        """
        Gets the dotfiles for a user.

        Use this method to:

        - Retrieve user dotfiles

        ### Examples

        - Get dotfiles:

          Retrieves the dotfiles for the current user.

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
            "/gitpod.v1.UserService/GetDotfilesConfiguration",
            body=await async_maybe_transform({"empty": empty}, dotfile_get_params.DotfileGetParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DotfileGetResponse,
        )

    async def set(
        self,
        *,
        repository: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Sets the dotfiles configuration for a user.

        Use this method to:

        - Configure user dotfiles
        - Update dotfiles settings

        ### Examples

        - Set dotfiles configuration:

          Sets the dotfiles configuration for the current user.

          ```yaml
          { "repository": "https://github.com/gitpod-io/dotfiles" }
          ```

        - Remove dotfiles:

          Removes the dotfiles for the current user.

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
            "/gitpod.v1.UserService/SetDotfilesConfiguration",
            body=await async_maybe_transform({"repository": repository}, dotfile_set_params.DotfileSetParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class DotfilesResourceWithRawResponse:
    def __init__(self, dotfiles: DotfilesResource) -> None:
        self._dotfiles = dotfiles

        self.get = to_raw_response_wrapper(
            dotfiles.get,
        )
        self.set = to_raw_response_wrapper(
            dotfiles.set,
        )


class AsyncDotfilesResourceWithRawResponse:
    def __init__(self, dotfiles: AsyncDotfilesResource) -> None:
        self._dotfiles = dotfiles

        self.get = async_to_raw_response_wrapper(
            dotfiles.get,
        )
        self.set = async_to_raw_response_wrapper(
            dotfiles.set,
        )


class DotfilesResourceWithStreamingResponse:
    def __init__(self, dotfiles: DotfilesResource) -> None:
        self._dotfiles = dotfiles

        self.get = to_streamed_response_wrapper(
            dotfiles.get,
        )
        self.set = to_streamed_response_wrapper(
            dotfiles.set,
        )


class AsyncDotfilesResourceWithStreamingResponse:
    def __init__(self, dotfiles: AsyncDotfilesResource) -> None:
        self._dotfiles = dotfiles

        self.get = async_to_streamed_response_wrapper(
            dotfiles.get,
        )
        self.set = async_to_streamed_response_wrapper(
            dotfiles.set,
        )
