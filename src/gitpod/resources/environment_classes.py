# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal

import httpx

from ..types import environment_class_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    is_given,
    maybe_transform,
    strip_not_given,
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
from ..types.environment_class_list_response import EnvironmentClassListResponse

__all__ = ["EnvironmentClassesResource", "AsyncEnvironmentClassesResource"]


class EnvironmentClassesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EnvironmentClassesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return EnvironmentClassesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EnvironmentClassesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return EnvironmentClassesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        connect_protocol_version: Literal[1],
        filter: Union[object, object] | NotGiven = NOT_GIVEN,
        pagination: environment_class_list_params.Pagination | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnvironmentClassListResponse:
        """
        ListEnvironmentClasses returns the list of environment classes with runner
        details a user is able to use based on the query buf:lint:ignore
        RPC_REQUEST_RESPONSE_UNIQUE

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          pagination: pagination contains the pagination options for listing environment classes

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
            "/gitpod.v1.EnvironmentService/ListEnvironmentClasses",
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                environment_class_list_params.EnvironmentClassListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvironmentClassListResponse,
        )


class AsyncEnvironmentClassesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEnvironmentClassesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEnvironmentClassesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEnvironmentClassesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return AsyncEnvironmentClassesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        connect_protocol_version: Literal[1],
        filter: Union[object, object] | NotGiven = NOT_GIVEN,
        pagination: environment_class_list_params.Pagination | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnvironmentClassListResponse:
        """
        ListEnvironmentClasses returns the list of environment classes with runner
        details a user is able to use based on the query buf:lint:ignore
        RPC_REQUEST_RESPONSE_UNIQUE

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          pagination: pagination contains the pagination options for listing environment classes

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
            "/gitpod.v1.EnvironmentService/ListEnvironmentClasses",
            body=await async_maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                environment_class_list_params.EnvironmentClassListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvironmentClassListResponse,
        )


class EnvironmentClassesResourceWithRawResponse:
    def __init__(self, environment_classes: EnvironmentClassesResource) -> None:
        self._environment_classes = environment_classes

        self.list = to_raw_response_wrapper(
            environment_classes.list,
        )


class AsyncEnvironmentClassesResourceWithRawResponse:
    def __init__(self, environment_classes: AsyncEnvironmentClassesResource) -> None:
        self._environment_classes = environment_classes

        self.list = async_to_raw_response_wrapper(
            environment_classes.list,
        )


class EnvironmentClassesResourceWithStreamingResponse:
    def __init__(self, environment_classes: EnvironmentClassesResource) -> None:
        self._environment_classes = environment_classes

        self.list = to_streamed_response_wrapper(
            environment_classes.list,
        )


class AsyncEnvironmentClassesResourceWithStreamingResponse:
    def __init__(self, environment_classes: AsyncEnvironmentClassesResource) -> None:
        self._environment_classes = environment_classes

        self.list = async_to_streamed_response_wrapper(
            environment_classes.list,
        )
