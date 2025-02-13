# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncEnvironmentClassesPage, AsyncEnvironmentClassesPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.environments import class_list_params
from ...types.shared.environment_class import EnvironmentClass

__all__ = ["ClassesResource", "AsyncClassesResource"]


class ClassesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClassesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ClassesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClassesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return ClassesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        token: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        filter: class_list_params.Filter | NotGiven = NOT_GIVEN,
        pagination: class_list_params.Pagination | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncEnvironmentClassesPage[EnvironmentClass]:
        """
        Lists available environment classes with their specifications and resource
        limits.

        Use this method to understand what types of environments you can create and
        their capabilities. Environment classes define the compute resources and
        features available to your environments.

        ### Examples

        - List all available classes:

          Retrieves a list of all environment classes with their specifications.

          ```yaml
          {}
          ```

          buf:lint:ignore RPC_REQUEST_RESPONSE_UNIQUE

        Args:
          pagination: pagination contains the pagination options for listing environment classes

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.EnvironmentService/ListEnvironmentClasses",
            page=SyncEnvironmentClassesPage[EnvironmentClass],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                class_list_params.ClassListParams,
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
                    class_list_params.ClassListParams,
                ),
            ),
            model=EnvironmentClass,
            method="post",
        )


class AsyncClassesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClassesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncClassesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClassesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return AsyncClassesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        token: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        filter: class_list_params.Filter | NotGiven = NOT_GIVEN,
        pagination: class_list_params.Pagination | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[EnvironmentClass, AsyncEnvironmentClassesPage[EnvironmentClass]]:
        """
        Lists available environment classes with their specifications and resource
        limits.

        Use this method to understand what types of environments you can create and
        their capabilities. Environment classes define the compute resources and
        features available to your environments.

        ### Examples

        - List all available classes:

          Retrieves a list of all environment classes with their specifications.

          ```yaml
          {}
          ```

          buf:lint:ignore RPC_REQUEST_RESPONSE_UNIQUE

        Args:
          pagination: pagination contains the pagination options for listing environment classes

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.EnvironmentService/ListEnvironmentClasses",
            page=AsyncEnvironmentClassesPage[EnvironmentClass],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                class_list_params.ClassListParams,
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
                    class_list_params.ClassListParams,
                ),
            ),
            model=EnvironmentClass,
            method="post",
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
