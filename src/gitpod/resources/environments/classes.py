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
from ...types.environments import class_list_params
from ...types.environments.class_list_response import ClassListResponse

__all__ = ["ClassesResource", "AsyncClassesResource"]


class ClassesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClassesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return ClassesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClassesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return ClassesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        encoding: Literal["proto", "json"],
        connect_protocol_version: Literal[1],
        base64: bool | NotGiven = NOT_GIVEN,
        compression: Literal["identity", "gzip", "br"] | NotGiven = NOT_GIVEN,
        connect: Literal["v1"] | NotGiven = NOT_GIVEN,
        message: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClassListResponse:
        """
        ListEnvironmentClasses returns the list of environment classes with runner
        details a user is able to use based on the

        query buf:lint:ignore RPC_REQUEST_RESPONSE_UNIQUE

        Args:
          encoding: Define which encoding or 'Message-Codec' to use

          connect_protocol_version: Define the version of the Connect protocol

          base64: Specifies if the message query param is base64 encoded, which may be required
              for binary data

          compression: Which compression algorithm to use for this request

          connect: Define the version of the Connect protocol

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
            "/gitpod.v1.EnvironmentService/ListEnvironmentClasses",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "encoding": encoding,
                        "base64": base64,
                        "compression": compression,
                        "connect": connect,
                        "message": message,
                    },
                    class_list_params.ClassListParams,
                ),
            ),
            cast_to=ClassListResponse,
        )


class AsyncClassesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClassesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return AsyncClassesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClassesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return AsyncClassesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        encoding: Literal["proto", "json"],
        connect_protocol_version: Literal[1],
        base64: bool | NotGiven = NOT_GIVEN,
        compression: Literal["identity", "gzip", "br"] | NotGiven = NOT_GIVEN,
        connect: Literal["v1"] | NotGiven = NOT_GIVEN,
        message: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ClassListResponse:
        """
        ListEnvironmentClasses returns the list of environment classes with runner
        details a user is able to use based on the

        query buf:lint:ignore RPC_REQUEST_RESPONSE_UNIQUE

        Args:
          encoding: Define which encoding or 'Message-Codec' to use

          connect_protocol_version: Define the version of the Connect protocol

          base64: Specifies if the message query param is base64 encoded, which may be required
              for binary data

          compression: Which compression algorithm to use for this request

          connect: Define the version of the Connect protocol

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
            "/gitpod.v1.EnvironmentService/ListEnvironmentClasses",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "encoding": encoding,
                        "base64": base64,
                        "compression": compression,
                        "connect": connect,
                        "message": message,
                    },
                    class_list_params.ClassListParams,
                ),
            ),
            cast_to=ClassListResponse,
        )


class ClassesResourceWithRawResponse:
    def __init__(self, classes: ClassesResource) -> None:
        self._classes = classes

        self.list = to_raw_response_wrapper(
            classes.list,
        )


class AsyncClassesResourceWithRawResponse:
    def __init__(self, classes: AsyncClassesResource) -> None:
        self._classes = classes

        self.list = async_to_raw_response_wrapper(
            classes.list,
        )


class ClassesResourceWithStreamingResponse:
    def __init__(self, classes: ClassesResource) -> None:
        self._classes = classes

        self.list = to_streamed_response_wrapper(
            classes.list,
        )


class AsyncClassesResourceWithStreamingResponse:
    def __init__(self, classes: AsyncClassesResource) -> None:
        self._classes = classes

        self.list = async_to_streamed_response_wrapper(
            classes.list,
        )
