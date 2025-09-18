# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.runners.configurations import schema_retrieve_params
from ....types.runners.configurations.schema_retrieve_response import SchemaRetrieveResponse

__all__ = ["SchemaResource", "AsyncSchemaResource"]


class SchemaResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SchemaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SchemaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SchemaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return SchemaResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        runner_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SchemaRetrieveResponse:
        """
        Gets the latest runner configuration schema.

        Use this method to:

        - View available settings
        - Check configuration options
        - Validate configurations

        ### Examples

        - Get schema:

          Retrieves configuration schema for a runner.

          ```yaml
          runnerId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.RunnerConfigurationService/GetRunnerConfigurationSchema",
            body=maybe_transform({"runner_id": runner_id}, schema_retrieve_params.SchemaRetrieveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SchemaRetrieveResponse,
        )


class AsyncSchemaResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSchemaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSchemaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSchemaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return AsyncSchemaResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        runner_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SchemaRetrieveResponse:
        """
        Gets the latest runner configuration schema.

        Use this method to:

        - View available settings
        - Check configuration options
        - Validate configurations

        ### Examples

        - Get schema:

          Retrieves configuration schema for a runner.

          ```yaml
          runnerId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.RunnerConfigurationService/GetRunnerConfigurationSchema",
            body=await async_maybe_transform({"runner_id": runner_id}, schema_retrieve_params.SchemaRetrieveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SchemaRetrieveResponse,
        )


class SchemaResourceWithRawResponse:
    def __init__(self, schema: SchemaResource) -> None:
        self._schema = schema

        self.retrieve = to_raw_response_wrapper(
            schema.retrieve,
        )


class AsyncSchemaResourceWithRawResponse:
    def __init__(self, schema: AsyncSchemaResource) -> None:
        self._schema = schema

        self.retrieve = async_to_raw_response_wrapper(
            schema.retrieve,
        )


class SchemaResourceWithStreamingResponse:
    def __init__(self, schema: SchemaResource) -> None:
        self._schema = schema

        self.retrieve = to_streamed_response_wrapper(
            schema.retrieve,
        )


class AsyncSchemaResourceWithStreamingResponse:
    def __init__(self, schema: AsyncSchemaResource) -> None:
        self._schema = schema

        self.retrieve = async_to_streamed_response_wrapper(
            schema.retrieve,
        )
