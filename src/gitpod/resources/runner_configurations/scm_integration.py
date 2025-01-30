# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, overload

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    is_given,
    required_args,
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
from ...types.runner_configurations import scm_integration_create_params
from ...types.runner_configurations.scm_integration_create_response import ScmIntegrationCreateResponse

__all__ = ["ScmIntegrationResource", "AsyncScmIntegrationResource"]


class ScmIntegrationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScmIntegrationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return ScmIntegrationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScmIntegrationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return ScmIntegrationResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        oauth_client_id: str,
        connect_protocol_version: Literal[1],
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScmIntegrationCreateResponse:
        """
        CreateSCMIntegration creates a new SCM integration on a runner.

        Args:
          oauth_client_id: oauth_client_id is the OAuth app's client ID, if OAuth is configured.

              If configured, oauth_plaintext_client_secret must also be set.

          connect_protocol_version: Define the version of the Connect protocol

          connect_timeout_ms: Define the timeout, in ms

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        oauth_plaintext_client_secret: str,
        connect_protocol_version: Literal[1],
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScmIntegrationCreateResponse:
        """
        CreateSCMIntegration creates a new SCM integration on a runner.

        Args:
          oauth_plaintext_client_secret: oauth_plaintext_client_secret is the OAuth app's client secret in clear text.

              This will first be encrypted with the runner's public key before being stored.

          connect_protocol_version: Define the version of the Connect protocol

          connect_timeout_ms: Define the timeout, in ms

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["oauth_client_id", "connect_protocol_version"], ["oauth_plaintext_client_secret", "connect_protocol_version"]
    )
    def create(
        self,
        *,
        oauth_client_id: str | NotGiven = NOT_GIVEN,
        connect_protocol_version: Literal[1],
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        oauth_plaintext_client_secret: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScmIntegrationCreateResponse:
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
            "/gitpod.v1.RunnerConfigurationService/CreateSCMIntegration",
            body=maybe_transform(
                {
                    "oauth_client_id": oauth_client_id,
                    "oauth_plaintext_client_secret": oauth_plaintext_client_secret,
                },
                scm_integration_create_params.ScmIntegrationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScmIntegrationCreateResponse,
        )


class AsyncScmIntegrationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScmIntegrationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return AsyncScmIntegrationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScmIntegrationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return AsyncScmIntegrationResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        oauth_client_id: str,
        connect_protocol_version: Literal[1],
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScmIntegrationCreateResponse:
        """
        CreateSCMIntegration creates a new SCM integration on a runner.

        Args:
          oauth_client_id: oauth_client_id is the OAuth app's client ID, if OAuth is configured.

              If configured, oauth_plaintext_client_secret must also be set.

          connect_protocol_version: Define the version of the Connect protocol

          connect_timeout_ms: Define the timeout, in ms

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        oauth_plaintext_client_secret: str,
        connect_protocol_version: Literal[1],
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScmIntegrationCreateResponse:
        """
        CreateSCMIntegration creates a new SCM integration on a runner.

        Args:
          oauth_plaintext_client_secret: oauth_plaintext_client_secret is the OAuth app's client secret in clear text.

              This will first be encrypted with the runner's public key before being stored.

          connect_protocol_version: Define the version of the Connect protocol

          connect_timeout_ms: Define the timeout, in ms

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["oauth_client_id", "connect_protocol_version"], ["oauth_plaintext_client_secret", "connect_protocol_version"]
    )
    async def create(
        self,
        *,
        oauth_client_id: str | NotGiven = NOT_GIVEN,
        connect_protocol_version: Literal[1],
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        oauth_plaintext_client_secret: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScmIntegrationCreateResponse:
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
            "/gitpod.v1.RunnerConfigurationService/CreateSCMIntegration",
            body=await async_maybe_transform(
                {
                    "oauth_client_id": oauth_client_id,
                    "oauth_plaintext_client_secret": oauth_plaintext_client_secret,
                },
                scm_integration_create_params.ScmIntegrationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScmIntegrationCreateResponse,
        )


class ScmIntegrationResourceWithRawResponse:
    def __init__(self, scm_integration: ScmIntegrationResource) -> None:
        self._scm_integration = scm_integration

        self.create = to_raw_response_wrapper(
            scm_integration.create,
        )


class AsyncScmIntegrationResourceWithRawResponse:
    def __init__(self, scm_integration: AsyncScmIntegrationResource) -> None:
        self._scm_integration = scm_integration

        self.create = async_to_raw_response_wrapper(
            scm_integration.create,
        )


class ScmIntegrationResourceWithStreamingResponse:
    def __init__(self, scm_integration: ScmIntegrationResource) -> None:
        self._scm_integration = scm_integration

        self.create = to_streamed_response_wrapper(
            scm_integration.create,
        )


class AsyncScmIntegrationResourceWithStreamingResponse:
    def __init__(self, scm_integration: AsyncScmIntegrationResource) -> None:
        self._scm_integration = scm_integration

        self.create = async_to_streamed_response_wrapper(
            scm_integration.create,
        )
