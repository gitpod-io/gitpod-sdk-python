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
from ...types.runner_configurations import configuration_schema_create_params, configuration_schema_retrieve_params
from ...types.runner_configurations.configuration_schema_create_response import ConfigurationSchemaCreateResponse
from ...types.runner_configurations.configuration_schema_retrieve_response import ConfigurationSchemaRetrieveResponse

__all__ = ["ConfigurationSchemaResource", "AsyncConfigurationSchemaResource"]


class ConfigurationSchemaResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConfigurationSchemaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return ConfigurationSchemaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigurationSchemaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return ConfigurationSchemaResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        connect_protocol_version: Literal[1],
        runner_id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationSchemaCreateResponse:
        """
        GetRunnerConfigurationSchema retrieves the latest Runner configuration schema

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
            "/gitpod.v1.RunnerConfigurationService/GetRunnerConfigurationSchema",
            body=maybe_transform(
                {"runner_id": runner_id}, configuration_schema_create_params.ConfigurationSchemaCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigurationSchemaCreateResponse,
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
    ) -> ConfigurationSchemaRetrieveResponse:
        """
        GetRunnerConfigurationSchema retrieves the latest Runner configuration schema

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
            "/gitpod.v1.RunnerConfigurationService/GetRunnerConfigurationSchema",
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
                    configuration_schema_retrieve_params.ConfigurationSchemaRetrieveParams,
                ),
            ),
            cast_to=ConfigurationSchemaRetrieveResponse,
        )


class AsyncConfigurationSchemaResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConfigurationSchemaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConfigurationSchemaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigurationSchemaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return AsyncConfigurationSchemaResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        connect_protocol_version: Literal[1],
        runner_id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationSchemaCreateResponse:
        """
        GetRunnerConfigurationSchema retrieves the latest Runner configuration schema

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
            "/gitpod.v1.RunnerConfigurationService/GetRunnerConfigurationSchema",
            body=await async_maybe_transform(
                {"runner_id": runner_id}, configuration_schema_create_params.ConfigurationSchemaCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigurationSchemaCreateResponse,
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
    ) -> ConfigurationSchemaRetrieveResponse:
        """
        GetRunnerConfigurationSchema retrieves the latest Runner configuration schema

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
            "/gitpod.v1.RunnerConfigurationService/GetRunnerConfigurationSchema",
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
                    configuration_schema_retrieve_params.ConfigurationSchemaRetrieveParams,
                ),
            ),
            cast_to=ConfigurationSchemaRetrieveResponse,
        )


class ConfigurationSchemaResourceWithRawResponse:
    def __init__(self, configuration_schema: ConfigurationSchemaResource) -> None:
        self._configuration_schema = configuration_schema

        self.create = to_raw_response_wrapper(
            configuration_schema.create,
        )
        self.retrieve = to_raw_response_wrapper(
            configuration_schema.retrieve,
        )


class AsyncConfigurationSchemaResourceWithRawResponse:
    def __init__(self, configuration_schema: AsyncConfigurationSchemaResource) -> None:
        self._configuration_schema = configuration_schema

        self.create = async_to_raw_response_wrapper(
            configuration_schema.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            configuration_schema.retrieve,
        )


class ConfigurationSchemaResourceWithStreamingResponse:
    def __init__(self, configuration_schema: ConfigurationSchemaResource) -> None:
        self._configuration_schema = configuration_schema

        self.create = to_streamed_response_wrapper(
            configuration_schema.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            configuration_schema.retrieve,
        )


class AsyncConfigurationSchemaResourceWithStreamingResponse:
    def __init__(self, configuration_schema: AsyncConfigurationSchemaResource) -> None:
        self._configuration_schema = configuration_schema

        self.create = async_to_streamed_response_wrapper(
            configuration_schema.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            configuration_schema.retrieve,
        )
