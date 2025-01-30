# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, overload

import httpx

from ...types import (
    runner_list_params,
    runner_create_params,
    runner_delete_params,
    runner_update_params,
    runner_retrieve_params,
    runner_parse_context_url_params,
    runner_create_runner_token_params,
    runner_check_authentication_for_host_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    is_given,
    required_args,
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from .policies import (
    PoliciesResource,
    AsyncPoliciesResource,
    PoliciesResourceWithRawResponse,
    AsyncPoliciesResourceWithRawResponse,
    PoliciesResourceWithStreamingResponse,
    AsyncPoliciesResourceWithStreamingResponse,
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
from ...types.runner_list_response import RunnerListResponse
from .configurations.configurations import (
    ConfigurationsResource,
    AsyncConfigurationsResource,
    ConfigurationsResourceWithRawResponse,
    AsyncConfigurationsResourceWithRawResponse,
    ConfigurationsResourceWithStreamingResponse,
    AsyncConfigurationsResourceWithStreamingResponse,
)
from ...types.runner_create_response import RunnerCreateResponse
from ...types.runner_retrieve_response import RunnerRetrieveResponse
from ...types.runner_parse_context_url_response import RunnerParseContextURLResponse
from ...types.runner_create_runner_token_response import RunnerCreateRunnerTokenResponse
from ...types.runner_check_authentication_for_host_response import RunnerCheckAuthenticationForHostResponse

__all__ = ["RunnersResource", "AsyncRunnersResource"]


class RunnersResource(SyncAPIResource):
    @cached_property
    def configurations(self) -> ConfigurationsResource:
        return ConfigurationsResource(self._client)

    @cached_property
    def policies(self) -> PoliciesResource:
        return PoliciesResource(self._client)

    @cached_property
    def with_raw_response(self) -> RunnersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return RunnersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RunnersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return RunnersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        connect_protocol_version: Literal[1],
        kind: Literal[
            "RUNNER_KIND_UNSPECIFIED", "RUNNER_KIND_LOCAL", "RUNNER_KIND_REMOTE", "RUNNER_KIND_LOCAL_CONFIGURATION"
        ]
        | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        spec: runner_create_params.Spec | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunnerCreateResponse:
        """CreateRunner creates a new runner with the server.

        Registrations are very

        short-lived and must be renewed every 30 seconds. Runners can be registered for
        an entire organisation or a single user.

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          kind: RunnerKind represents the kind of a runner

          name: The runner name for humans

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
            "/gitpod.v1.RunnerService/CreateRunner",
            body=maybe_transform(
                {
                    "kind": kind,
                    "name": name,
                    "spec": spec,
                },
                runner_create_params.RunnerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunnerCreateResponse,
        )

    def retrieve(
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
    ) -> RunnerRetrieveResponse:
        """
        GetRunner returns a single runner.

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
            "/gitpod.v1.RunnerService/GetRunner",
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
                    runner_retrieve_params.RunnerRetrieveParams,
                ),
            ),
            cast_to=RunnerRetrieveResponse,
        )

    @overload
    def update(
        self,
        *,
        name: str,
        connect_protocol_version: Literal[1],
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        UpdateRunner updates an environment runner.

        Args:
          name: The runner's name which is shown to users

          connect_protocol_version: Define the version of the Connect protocol

          connect_timeout_ms: Define the timeout, in ms

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        *,
        spec: runner_update_params.Variant1Spec,
        connect_protocol_version: Literal[1],
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        UpdateRunner updates an environment runner.

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          connect_timeout_ms: Define the timeout, in ms

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["name", "connect_protocol_version"], ["spec", "connect_protocol_version"])
    def update(
        self,
        *,
        name: str | NotGiven = NOT_GIVEN,
        connect_protocol_version: Literal[1],
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        spec: runner_update_params.Variant1Spec | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
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
            "/gitpod.v1.RunnerService/UpdateRunner",
            body=maybe_transform(
                {
                    "name": name,
                    "spec": spec,
                },
                runner_update_params.RunnerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

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
    ) -> RunnerListResponse:
        """
        ListRunners returns all runners registered in the scope.

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
            "/gitpod.v1.RunnerService/ListRunners",
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
                    runner_list_params.RunnerListParams,
                ),
            ),
            cast_to=RunnerListResponse,
        )

    def delete(
        self,
        *,
        connect_protocol_version: Literal[1],
        force: bool | NotGiven = NOT_GIVEN,
        runner_id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        DeleteRunner deletes an environment runner.

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          force: force indicates whether the runner should be deleted forcefully. When force
              deleting a Runner, all Environments on the runner are also force deleted and
              regular Runner lifecycle is not respected. Force deleting can result in data
              loss.

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
            "/gitpod.v1.RunnerService/DeleteRunner",
            body=maybe_transform(
                {
                    "force": force,
                    "runner_id": runner_id,
                },
                runner_delete_params.RunnerDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def check_authentication_for_host(
        self,
        *,
        connect_protocol_version: Literal[1],
        host: str | NotGiven = NOT_GIVEN,
        runner_id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunnerCheckAuthenticationForHostResponse:
        """
        CheckAuthenticationForHost asks a runner if the user is authenticated against a
        particular host, e.g. an SCM system.

        If not, this function will return a URL that the user should visit to
        authenticate, or indicate that Personal Access Tokens are supported.

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
            "/gitpod.v1.RunnerService/CheckAuthenticationForHost",
            body=maybe_transform(
                {
                    "host": host,
                    "runner_id": runner_id,
                },
                runner_check_authentication_for_host_params.RunnerCheckAuthenticationForHostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunnerCheckAuthenticationForHostResponse,
        )

    def create_runner_token(
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
    ) -> RunnerCreateRunnerTokenResponse:
        """
        CreateRunnerToken returns a token that can be used to authenticate as the

        runner. Use this call to renew an outdated token - this does not expire any
        previouly issued tokens.

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
            "/gitpod.v1.RunnerService/CreateRunnerToken",
            body=maybe_transform(
                {"runner_id": runner_id}, runner_create_runner_token_params.RunnerCreateRunnerTokenParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunnerCreateRunnerTokenResponse,
        )

    def parse_context_url(
        self,
        *,
        connect_protocol_version: Literal[1],
        context_url: str | NotGiven = NOT_GIVEN,
        runner_id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunnerParseContextURLResponse:
        """
        ParseContextURL asks a runner to parse a context URL, and return the parsed
        result.

        This call returns

        - FAILED_PRECONDITION if the user requires authentication on the runner to
          access the context URL
        - PERMISSION_DENIED if the user is not allowed to access the context URL using
          the credentials they have
        - INVALID_ARGUMENT if the context URL is invalid
        - NOT_FOUND if the repository or branch indicated by the context URL does not
          exist

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
            "/gitpod.v1.RunnerService/ParseContextURL",
            body=maybe_transform(
                {
                    "context_url": context_url,
                    "runner_id": runner_id,
                },
                runner_parse_context_url_params.RunnerParseContextURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunnerParseContextURLResponse,
        )


class AsyncRunnersResource(AsyncAPIResource):
    @cached_property
    def configurations(self) -> AsyncConfigurationsResource:
        return AsyncConfigurationsResource(self._client)

    @cached_property
    def policies(self) -> AsyncPoliciesResource:
        return AsyncPoliciesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRunnersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRunnersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRunnersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return AsyncRunnersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        connect_protocol_version: Literal[1],
        kind: Literal[
            "RUNNER_KIND_UNSPECIFIED", "RUNNER_KIND_LOCAL", "RUNNER_KIND_REMOTE", "RUNNER_KIND_LOCAL_CONFIGURATION"
        ]
        | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        spec: runner_create_params.Spec | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunnerCreateResponse:
        """CreateRunner creates a new runner with the server.

        Registrations are very

        short-lived and must be renewed every 30 seconds. Runners can be registered for
        an entire organisation or a single user.

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          kind: RunnerKind represents the kind of a runner

          name: The runner name for humans

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
            "/gitpod.v1.RunnerService/CreateRunner",
            body=await async_maybe_transform(
                {
                    "kind": kind,
                    "name": name,
                    "spec": spec,
                },
                runner_create_params.RunnerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunnerCreateResponse,
        )

    async def retrieve(
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
    ) -> RunnerRetrieveResponse:
        """
        GetRunner returns a single runner.

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
            "/gitpod.v1.RunnerService/GetRunner",
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
                    runner_retrieve_params.RunnerRetrieveParams,
                ),
            ),
            cast_to=RunnerRetrieveResponse,
        )

    @overload
    async def update(
        self,
        *,
        name: str,
        connect_protocol_version: Literal[1],
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        UpdateRunner updates an environment runner.

        Args:
          name: The runner's name which is shown to users

          connect_protocol_version: Define the version of the Connect protocol

          connect_timeout_ms: Define the timeout, in ms

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        *,
        spec: runner_update_params.Variant1Spec,
        connect_protocol_version: Literal[1],
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        UpdateRunner updates an environment runner.

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          connect_timeout_ms: Define the timeout, in ms

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["name", "connect_protocol_version"], ["spec", "connect_protocol_version"])
    async def update(
        self,
        *,
        name: str | NotGiven = NOT_GIVEN,
        connect_protocol_version: Literal[1],
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        spec: runner_update_params.Variant1Spec | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
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
            "/gitpod.v1.RunnerService/UpdateRunner",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "spec": spec,
                },
                runner_update_params.RunnerUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

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
    ) -> RunnerListResponse:
        """
        ListRunners returns all runners registered in the scope.

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
            "/gitpod.v1.RunnerService/ListRunners",
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
                    runner_list_params.RunnerListParams,
                ),
            ),
            cast_to=RunnerListResponse,
        )

    async def delete(
        self,
        *,
        connect_protocol_version: Literal[1],
        force: bool | NotGiven = NOT_GIVEN,
        runner_id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        DeleteRunner deletes an environment runner.

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          force: force indicates whether the runner should be deleted forcefully. When force
              deleting a Runner, all Environments on the runner are also force deleted and
              regular Runner lifecycle is not respected. Force deleting can result in data
              loss.

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
            "/gitpod.v1.RunnerService/DeleteRunner",
            body=await async_maybe_transform(
                {
                    "force": force,
                    "runner_id": runner_id,
                },
                runner_delete_params.RunnerDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def check_authentication_for_host(
        self,
        *,
        connect_protocol_version: Literal[1],
        host: str | NotGiven = NOT_GIVEN,
        runner_id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunnerCheckAuthenticationForHostResponse:
        """
        CheckAuthenticationForHost asks a runner if the user is authenticated against a
        particular host, e.g. an SCM system.

        If not, this function will return a URL that the user should visit to
        authenticate, or indicate that Personal Access Tokens are supported.

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
            "/gitpod.v1.RunnerService/CheckAuthenticationForHost",
            body=await async_maybe_transform(
                {
                    "host": host,
                    "runner_id": runner_id,
                },
                runner_check_authentication_for_host_params.RunnerCheckAuthenticationForHostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunnerCheckAuthenticationForHostResponse,
        )

    async def create_runner_token(
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
    ) -> RunnerCreateRunnerTokenResponse:
        """
        CreateRunnerToken returns a token that can be used to authenticate as the

        runner. Use this call to renew an outdated token - this does not expire any
        previouly issued tokens.

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
            "/gitpod.v1.RunnerService/CreateRunnerToken",
            body=await async_maybe_transform(
                {"runner_id": runner_id}, runner_create_runner_token_params.RunnerCreateRunnerTokenParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunnerCreateRunnerTokenResponse,
        )

    async def parse_context_url(
        self,
        *,
        connect_protocol_version: Literal[1],
        context_url: str | NotGiven = NOT_GIVEN,
        runner_id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunnerParseContextURLResponse:
        """
        ParseContextURL asks a runner to parse a context URL, and return the parsed
        result.

        This call returns

        - FAILED_PRECONDITION if the user requires authentication on the runner to
          access the context URL
        - PERMISSION_DENIED if the user is not allowed to access the context URL using
          the credentials they have
        - INVALID_ARGUMENT if the context URL is invalid
        - NOT_FOUND if the repository or branch indicated by the context URL does not
          exist

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
            "/gitpod.v1.RunnerService/ParseContextURL",
            body=await async_maybe_transform(
                {
                    "context_url": context_url,
                    "runner_id": runner_id,
                },
                runner_parse_context_url_params.RunnerParseContextURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunnerParseContextURLResponse,
        )


class RunnersResourceWithRawResponse:
    def __init__(self, runners: RunnersResource) -> None:
        self._runners = runners

        self.create = to_raw_response_wrapper(
            runners.create,
        )
        self.retrieve = to_raw_response_wrapper(
            runners.retrieve,
        )
        self.update = to_raw_response_wrapper(
            runners.update,
        )
        self.list = to_raw_response_wrapper(
            runners.list,
        )
        self.delete = to_raw_response_wrapper(
            runners.delete,
        )
        self.check_authentication_for_host = to_raw_response_wrapper(
            runners.check_authentication_for_host,
        )
        self.create_runner_token = to_raw_response_wrapper(
            runners.create_runner_token,
        )
        self.parse_context_url = to_raw_response_wrapper(
            runners.parse_context_url,
        )

    @cached_property
    def configurations(self) -> ConfigurationsResourceWithRawResponse:
        return ConfigurationsResourceWithRawResponse(self._runners.configurations)

    @cached_property
    def policies(self) -> PoliciesResourceWithRawResponse:
        return PoliciesResourceWithRawResponse(self._runners.policies)


class AsyncRunnersResourceWithRawResponse:
    def __init__(self, runners: AsyncRunnersResource) -> None:
        self._runners = runners

        self.create = async_to_raw_response_wrapper(
            runners.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            runners.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            runners.update,
        )
        self.list = async_to_raw_response_wrapper(
            runners.list,
        )
        self.delete = async_to_raw_response_wrapper(
            runners.delete,
        )
        self.check_authentication_for_host = async_to_raw_response_wrapper(
            runners.check_authentication_for_host,
        )
        self.create_runner_token = async_to_raw_response_wrapper(
            runners.create_runner_token,
        )
        self.parse_context_url = async_to_raw_response_wrapper(
            runners.parse_context_url,
        )

    @cached_property
    def configurations(self) -> AsyncConfigurationsResourceWithRawResponse:
        return AsyncConfigurationsResourceWithRawResponse(self._runners.configurations)

    @cached_property
    def policies(self) -> AsyncPoliciesResourceWithRawResponse:
        return AsyncPoliciesResourceWithRawResponse(self._runners.policies)


class RunnersResourceWithStreamingResponse:
    def __init__(self, runners: RunnersResource) -> None:
        self._runners = runners

        self.create = to_streamed_response_wrapper(
            runners.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            runners.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            runners.update,
        )
        self.list = to_streamed_response_wrapper(
            runners.list,
        )
        self.delete = to_streamed_response_wrapper(
            runners.delete,
        )
        self.check_authentication_for_host = to_streamed_response_wrapper(
            runners.check_authentication_for_host,
        )
        self.create_runner_token = to_streamed_response_wrapper(
            runners.create_runner_token,
        )
        self.parse_context_url = to_streamed_response_wrapper(
            runners.parse_context_url,
        )

    @cached_property
    def configurations(self) -> ConfigurationsResourceWithStreamingResponse:
        return ConfigurationsResourceWithStreamingResponse(self._runners.configurations)

    @cached_property
    def policies(self) -> PoliciesResourceWithStreamingResponse:
        return PoliciesResourceWithStreamingResponse(self._runners.policies)


class AsyncRunnersResourceWithStreamingResponse:
    def __init__(self, runners: AsyncRunnersResource) -> None:
        self._runners = runners

        self.create = async_to_streamed_response_wrapper(
            runners.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            runners.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            runners.update,
        )
        self.list = async_to_streamed_response_wrapper(
            runners.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            runners.delete,
        )
        self.check_authentication_for_host = async_to_streamed_response_wrapper(
            runners.check_authentication_for_host,
        )
        self.create_runner_token = async_to_streamed_response_wrapper(
            runners.create_runner_token,
        )
        self.parse_context_url = async_to_streamed_response_wrapper(
            runners.parse_context_url,
        )

    @cached_property
    def configurations(self) -> AsyncConfigurationsResourceWithStreamingResponse:
        return AsyncConfigurationsResourceWithStreamingResponse(self._runners.configurations)

    @cached_property
    def policies(self) -> AsyncPoliciesResourceWithStreamingResponse:
        return AsyncPoliciesResourceWithStreamingResponse(self._runners.policies)
