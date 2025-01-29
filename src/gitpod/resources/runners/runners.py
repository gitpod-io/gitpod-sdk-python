# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...types import (
    runner_list_params,
    runner_create_params,
    runner_get_runner_params,
    runner_delete_runner_params,
    runner_update_runner_params,
    runner_parse_context_url_params,
    runner_create_runner_token_params,
    runner_check_authentication_for_host_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    is_given,
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
from ...types.runner_create_response import RunnerCreateResponse
from ...types.runner_get_runner_response import RunnerGetRunnerResponse
from ...types.runner_parse_context_url_response import RunnerParseContextURLResponse
from ...types.runner_create_runner_token_response import RunnerCreateRunnerTokenResponse
from ...types.runner_check_authentication_for_host_response import RunnerCheckAuthenticationForHostResponse

__all__ = ["RunnersResource", "AsyncRunnersResource"]


class RunnersResource(SyncAPIResource):
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

    def list(
        self,
        *,
        connect_protocol_version: Literal[1],
        filter: runner_list_params.Filter | NotGiven = NOT_GIVEN,
        pagination: runner_list_params.Pagination | NotGiven = NOT_GIVEN,
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
          connect_protocol_version: Define the version of the Connect protocol

          pagination: pagination contains the pagination options for listing runners

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
            "/gitpod.v1.RunnerService/ListRunners",
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                runner_list_params.RunnerListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunnerListResponse,
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
        particular host, e.g. an SCM system. If not, this function will return a URL
        that the user should visit to authenticate, or indicate that Personal Access
        Tokens are supported.

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
        """CreateRunnerToken returns a token that can be used to authenticate as the
        runner.

        Use this call to renew an outdated token - this does not expire any
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

    def delete_runner(
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
                runner_delete_runner_params.RunnerDeleteRunnerParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def get_runner(
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
    ) -> RunnerGetRunnerResponse:
        """
        GetRunner returns a single runner.

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
            "/gitpod.v1.RunnerService/GetRunner",
            body=maybe_transform({"runner_id": runner_id}, runner_get_runner_params.RunnerGetRunnerParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunnerGetRunnerResponse,
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

    def update_runner(
        self,
        *,
        body: runner_update_runner_params.Body,
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
            body=maybe_transform(body, runner_update_runner_params.RunnerUpdateRunnerParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncRunnersResource(AsyncAPIResource):
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

    async def list(
        self,
        *,
        connect_protocol_version: Literal[1],
        filter: runner_list_params.Filter | NotGiven = NOT_GIVEN,
        pagination: runner_list_params.Pagination | NotGiven = NOT_GIVEN,
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
          connect_protocol_version: Define the version of the Connect protocol

          pagination: pagination contains the pagination options for listing runners

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
            "/gitpod.v1.RunnerService/ListRunners",
            body=await async_maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                runner_list_params.RunnerListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunnerListResponse,
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
        particular host, e.g. an SCM system. If not, this function will return a URL
        that the user should visit to authenticate, or indicate that Personal Access
        Tokens are supported.

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
        """CreateRunnerToken returns a token that can be used to authenticate as the
        runner.

        Use this call to renew an outdated token - this does not expire any
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

    async def delete_runner(
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
                runner_delete_runner_params.RunnerDeleteRunnerParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def get_runner(
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
    ) -> RunnerGetRunnerResponse:
        """
        GetRunner returns a single runner.

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
            "/gitpod.v1.RunnerService/GetRunner",
            body=await async_maybe_transform({"runner_id": runner_id}, runner_get_runner_params.RunnerGetRunnerParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunnerGetRunnerResponse,
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

    async def update_runner(
        self,
        *,
        body: runner_update_runner_params.Body,
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
            body=await async_maybe_transform(body, runner_update_runner_params.RunnerUpdateRunnerParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class RunnersResourceWithRawResponse:
    def __init__(self, runners: RunnersResource) -> None:
        self._runners = runners

        self.create = to_raw_response_wrapper(
            runners.create,
        )
        self.list = to_raw_response_wrapper(
            runners.list,
        )
        self.check_authentication_for_host = to_raw_response_wrapper(
            runners.check_authentication_for_host,
        )
        self.create_runner_token = to_raw_response_wrapper(
            runners.create_runner_token,
        )
        self.delete_runner = to_raw_response_wrapper(
            runners.delete_runner,
        )
        self.get_runner = to_raw_response_wrapper(
            runners.get_runner,
        )
        self.parse_context_url = to_raw_response_wrapper(
            runners.parse_context_url,
        )
        self.update_runner = to_raw_response_wrapper(
            runners.update_runner,
        )

    @cached_property
    def policies(self) -> PoliciesResourceWithRawResponse:
        return PoliciesResourceWithRawResponse(self._runners.policies)


class AsyncRunnersResourceWithRawResponse:
    def __init__(self, runners: AsyncRunnersResource) -> None:
        self._runners = runners

        self.create = async_to_raw_response_wrapper(
            runners.create,
        )
        self.list = async_to_raw_response_wrapper(
            runners.list,
        )
        self.check_authentication_for_host = async_to_raw_response_wrapper(
            runners.check_authentication_for_host,
        )
        self.create_runner_token = async_to_raw_response_wrapper(
            runners.create_runner_token,
        )
        self.delete_runner = async_to_raw_response_wrapper(
            runners.delete_runner,
        )
        self.get_runner = async_to_raw_response_wrapper(
            runners.get_runner,
        )
        self.parse_context_url = async_to_raw_response_wrapper(
            runners.parse_context_url,
        )
        self.update_runner = async_to_raw_response_wrapper(
            runners.update_runner,
        )

    @cached_property
    def policies(self) -> AsyncPoliciesResourceWithRawResponse:
        return AsyncPoliciesResourceWithRawResponse(self._runners.policies)


class RunnersResourceWithStreamingResponse:
    def __init__(self, runners: RunnersResource) -> None:
        self._runners = runners

        self.create = to_streamed_response_wrapper(
            runners.create,
        )
        self.list = to_streamed_response_wrapper(
            runners.list,
        )
        self.check_authentication_for_host = to_streamed_response_wrapper(
            runners.check_authentication_for_host,
        )
        self.create_runner_token = to_streamed_response_wrapper(
            runners.create_runner_token,
        )
        self.delete_runner = to_streamed_response_wrapper(
            runners.delete_runner,
        )
        self.get_runner = to_streamed_response_wrapper(
            runners.get_runner,
        )
        self.parse_context_url = to_streamed_response_wrapper(
            runners.parse_context_url,
        )
        self.update_runner = to_streamed_response_wrapper(
            runners.update_runner,
        )

    @cached_property
    def policies(self) -> PoliciesResourceWithStreamingResponse:
        return PoliciesResourceWithStreamingResponse(self._runners.policies)


class AsyncRunnersResourceWithStreamingResponse:
    def __init__(self, runners: AsyncRunnersResource) -> None:
        self._runners = runners

        self.create = async_to_streamed_response_wrapper(
            runners.create,
        )
        self.list = async_to_streamed_response_wrapper(
            runners.list,
        )
        self.check_authentication_for_host = async_to_streamed_response_wrapper(
            runners.check_authentication_for_host,
        )
        self.create_runner_token = async_to_streamed_response_wrapper(
            runners.create_runner_token,
        )
        self.delete_runner = async_to_streamed_response_wrapper(
            runners.delete_runner,
        )
        self.get_runner = async_to_streamed_response_wrapper(
            runners.get_runner,
        )
        self.parse_context_url = async_to_streamed_response_wrapper(
            runners.parse_context_url,
        )
        self.update_runner = async_to_streamed_response_wrapper(
            runners.update_runner,
        )

    @cached_property
    def policies(self) -> AsyncPoliciesResourceWithStreamingResponse:
        return AsyncPoliciesResourceWithStreamingResponse(self._runners.policies)
