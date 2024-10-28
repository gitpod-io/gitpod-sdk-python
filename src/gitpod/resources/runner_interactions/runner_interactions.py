# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal

import httpx

from ...types import (
    runner_interaction_signup_params,
    runner_interaction_mark_active_params,
    runner_interaction_update_status_params,
)
from ..._types import (
    NOT_GIVEN,
    Body,
    Query,
    Headers,
    NotGiven,
    Base64FileInput,
)
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
from .environment import (
    EnvironmentResource,
    AsyncEnvironmentResource,
    EnvironmentResourceWithRawResponse,
    AsyncEnvironmentResourceWithRawResponse,
    EnvironmentResourceWithStreamingResponse,
    AsyncEnvironmentResourceWithStreamingResponse,
)
from .environments import (
    EnvironmentsResource,
    AsyncEnvironmentsResource,
    EnvironmentsResourceWithRawResponse,
    AsyncEnvironmentsResourceWithRawResponse,
    EnvironmentsResourceWithStreamingResponse,
    AsyncEnvironmentsResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.runner_interaction_signup_response import RunnerInteractionSignupResponse

__all__ = ["RunnerInteractionsResource", "AsyncRunnerInteractionsResource"]


class RunnerInteractionsResource(SyncAPIResource):
    @cached_property
    def environment(self) -> EnvironmentResource:
        return EnvironmentResource(self._client)

    @cached_property
    def environments(self) -> EnvironmentsResource:
        return EnvironmentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> RunnerInteractionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return RunnerInteractionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RunnerInteractionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return RunnerInteractionsResourceWithStreamingResponse(self)

    def mark_active(
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
    ) -> object:
        """MarkRunnerActive marks a runner as available.

        This must be called every 30
        seconds to keep the runner active.

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          runner_id: The runner's identity

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
            "/gitpod.v1.RunnerInteractionService/MarkRunnerActive",
            body=maybe_transform(
                {"runner_id": runner_id}, runner_interaction_mark_active_params.RunnerInteractionMarkActiveParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def signup(
        self,
        *,
        connect_protocol_version: Literal[1],
        environment_classes: Iterable[runner_interaction_signup_params.EnvironmentClass] | NotGiven = NOT_GIVEN,
        public_key: Union[str, Base64FileInput] | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunnerInteractionSignupResponse:
        """Signup is called by a runner to sign up with the backend.

        This is the first call
        a runner makes.

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          environment_classes: The environment classes this runner has to offer

          public_key: The runner's public key. Must be an ECDH public key encoded in PKIX, ASN.1 DER
              format.

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
            "/gitpod.v1.RunnerInteractionService/Signup",
            body=maybe_transform(
                {
                    "environment_classes": environment_classes,
                    "public_key": public_key,
                },
                runner_interaction_signup_params.RunnerInteractionSignupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunnerInteractionSignupResponse,
        )

    def update_status(
        self,
        *,
        body: runner_interaction_update_status_params.Body,
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
        UpdateRunnerStatus updates the status of the runner.

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
            "/gitpod.v1.RunnerInteractionService/UpdateRunnerStatus",
            body=maybe_transform(body, runner_interaction_update_status_params.RunnerInteractionUpdateStatusParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncRunnerInteractionsResource(AsyncAPIResource):
    @cached_property
    def environment(self) -> AsyncEnvironmentResource:
        return AsyncEnvironmentResource(self._client)

    @cached_property
    def environments(self) -> AsyncEnvironmentsResource:
        return AsyncEnvironmentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRunnerInteractionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRunnerInteractionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRunnerInteractionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return AsyncRunnerInteractionsResourceWithStreamingResponse(self)

    async def mark_active(
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
    ) -> object:
        """MarkRunnerActive marks a runner as available.

        This must be called every 30
        seconds to keep the runner active.

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          runner_id: The runner's identity

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
            "/gitpod.v1.RunnerInteractionService/MarkRunnerActive",
            body=await async_maybe_transform(
                {"runner_id": runner_id}, runner_interaction_mark_active_params.RunnerInteractionMarkActiveParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def signup(
        self,
        *,
        connect_protocol_version: Literal[1],
        environment_classes: Iterable[runner_interaction_signup_params.EnvironmentClass] | NotGiven = NOT_GIVEN,
        public_key: Union[str, Base64FileInput] | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunnerInteractionSignupResponse:
        """Signup is called by a runner to sign up with the backend.

        This is the first call
        a runner makes.

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          environment_classes: The environment classes this runner has to offer

          public_key: The runner's public key. Must be an ECDH public key encoded in PKIX, ASN.1 DER
              format.

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
            "/gitpod.v1.RunnerInteractionService/Signup",
            body=await async_maybe_transform(
                {
                    "environment_classes": environment_classes,
                    "public_key": public_key,
                },
                runner_interaction_signup_params.RunnerInteractionSignupParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunnerInteractionSignupResponse,
        )

    async def update_status(
        self,
        *,
        body: runner_interaction_update_status_params.Body,
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
        UpdateRunnerStatus updates the status of the runner.

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
            "/gitpod.v1.RunnerInteractionService/UpdateRunnerStatus",
            body=await async_maybe_transform(
                body, runner_interaction_update_status_params.RunnerInteractionUpdateStatusParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class RunnerInteractionsResourceWithRawResponse:
    def __init__(self, runner_interactions: RunnerInteractionsResource) -> None:
        self._runner_interactions = runner_interactions

        self.mark_active = to_raw_response_wrapper(
            runner_interactions.mark_active,
        )
        self.signup = to_raw_response_wrapper(
            runner_interactions.signup,
        )
        self.update_status = to_raw_response_wrapper(
            runner_interactions.update_status,
        )

    @cached_property
    def environment(self) -> EnvironmentResourceWithRawResponse:
        return EnvironmentResourceWithRawResponse(self._runner_interactions.environment)

    @cached_property
    def environments(self) -> EnvironmentsResourceWithRawResponse:
        return EnvironmentsResourceWithRawResponse(self._runner_interactions.environments)


class AsyncRunnerInteractionsResourceWithRawResponse:
    def __init__(self, runner_interactions: AsyncRunnerInteractionsResource) -> None:
        self._runner_interactions = runner_interactions

        self.mark_active = async_to_raw_response_wrapper(
            runner_interactions.mark_active,
        )
        self.signup = async_to_raw_response_wrapper(
            runner_interactions.signup,
        )
        self.update_status = async_to_raw_response_wrapper(
            runner_interactions.update_status,
        )

    @cached_property
    def environment(self) -> AsyncEnvironmentResourceWithRawResponse:
        return AsyncEnvironmentResourceWithRawResponse(self._runner_interactions.environment)

    @cached_property
    def environments(self) -> AsyncEnvironmentsResourceWithRawResponse:
        return AsyncEnvironmentsResourceWithRawResponse(self._runner_interactions.environments)


class RunnerInteractionsResourceWithStreamingResponse:
    def __init__(self, runner_interactions: RunnerInteractionsResource) -> None:
        self._runner_interactions = runner_interactions

        self.mark_active = to_streamed_response_wrapper(
            runner_interactions.mark_active,
        )
        self.signup = to_streamed_response_wrapper(
            runner_interactions.signup,
        )
        self.update_status = to_streamed_response_wrapper(
            runner_interactions.update_status,
        )

    @cached_property
    def environment(self) -> EnvironmentResourceWithStreamingResponse:
        return EnvironmentResourceWithStreamingResponse(self._runner_interactions.environment)

    @cached_property
    def environments(self) -> EnvironmentsResourceWithStreamingResponse:
        return EnvironmentsResourceWithStreamingResponse(self._runner_interactions.environments)


class AsyncRunnerInteractionsResourceWithStreamingResponse:
    def __init__(self, runner_interactions: AsyncRunnerInteractionsResource) -> None:
        self._runner_interactions = runner_interactions

        self.mark_active = async_to_streamed_response_wrapper(
            runner_interactions.mark_active,
        )
        self.signup = async_to_streamed_response_wrapper(
            runner_interactions.signup,
        )
        self.update_status = async_to_streamed_response_wrapper(
            runner_interactions.update_status,
        )

    @cached_property
    def environment(self) -> AsyncEnvironmentResourceWithStreamingResponse:
        return AsyncEnvironmentResourceWithStreamingResponse(self._runner_interactions.environment)

    @cached_property
    def environments(self) -> AsyncEnvironmentsResourceWithStreamingResponse:
        return AsyncEnvironmentsResourceWithStreamingResponse(self._runner_interactions.environments)
