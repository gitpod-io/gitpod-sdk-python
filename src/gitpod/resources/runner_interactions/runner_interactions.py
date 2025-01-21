# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal

import httpx

from ...types import (
    runner_interaction_signup_params,
    runner_interaction_mark_active_params,
    runner_interaction_send_response_params,
    runner_interaction_update_status_params,
    runner_interaction_get_latest_version_params,
    runner_interaction_list_runner_scm_integrations_params,
    runner_interaction_list_runner_environment_classes_params,
    runner_interaction_update_runner_configuration_schema_params,
    runner_interaction_get_host_authentication_token_value_params,
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
from ...types.runner_interaction_get_latest_version_response import RunnerInteractionGetLatestVersionResponse
from ...types.runner_interaction_list_runner_scm_integrations_response import (
    RunnerInteractionListRunnerScmIntegrationsResponse,
)
from ...types.runner_interaction_list_runner_environment_classes_response import (
    RunnerInteractionListRunnerEnvironmentClassesResponse,
)
from ...types.runner_interaction_get_host_authentication_token_value_response import (
    RunnerInteractionGetHostAuthenticationTokenValueResponse,
)

__all__ = ["RunnerInteractionsResource", "AsyncRunnerInteractionsResource"]


class RunnerInteractionsResource(SyncAPIResource):
    @cached_property
    def environments(self) -> EnvironmentsResource:
        return EnvironmentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> RunnerInteractionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
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

    def get_host_authentication_token_value(
        self,
        *,
        connect_protocol_version: Literal[1],
        host: str | NotGiven = NOT_GIVEN,
        principal_id: str | NotGiven = NOT_GIVEN,
        runner_id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunnerInteractionGetHostAuthenticationTokenValueResponse:
        """
        GetRunnerHostAuthenticationToken returns an authentication token for the given
        host.

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          host: The host to get the authentication token for

          principal_id: The principal's ID to get the authentication token for

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
            "/gitpod.v1.RunnerInteractionService/GetHostAuthenticationTokenValue",
            body=maybe_transform(
                {
                    "host": host,
                    "principal_id": principal_id,
                    "runner_id": runner_id,
                },
                runner_interaction_get_host_authentication_token_value_params.RunnerInteractionGetHostAuthenticationTokenValueParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunnerInteractionGetHostAuthenticationTokenValueResponse,
        )

    def get_latest_version(
        self,
        *,
        connect_protocol_version: Literal[1],
        current_version: str | NotGiven = NOT_GIVEN,
        infrastructure_version: str | NotGiven = NOT_GIVEN,
        runner_id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunnerInteractionGetLatestVersionResponse:
        """
        GetLatestVersion returns the latest version of the runner.

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          current_version: The current version of the runner

          infrastructure_version: The version of the infrastructure

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
            "/gitpod.v1.RunnerInteractionService/GetLatestVersion",
            body=maybe_transform(
                {
                    "current_version": current_version,
                    "infrastructure_version": infrastructure_version,
                    "runner_id": runner_id,
                },
                runner_interaction_get_latest_version_params.RunnerInteractionGetLatestVersionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunnerInteractionGetLatestVersionResponse,
        )

    def list_runner_environment_classes(
        self,
        *,
        connect_protocol_version: Literal[1],
        filter: runner_interaction_list_runner_environment_classes_params.Filter | NotGiven = NOT_GIVEN,
        pagination: runner_interaction_list_runner_environment_classes_params.Pagination | NotGiven = NOT_GIVEN,
        runner_id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunnerInteractionListRunnerEnvironmentClassesResponse:
        """
        ListRunnerEnvironmentClasses returns the environment classes configured for the
        runner.

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          pagination: pagination contains the pagination options for listing environment classes

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
            "/gitpod.v1.RunnerInteractionService/ListRunnerEnvironmentClasses",
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                    "runner_id": runner_id,
                },
                runner_interaction_list_runner_environment_classes_params.RunnerInteractionListRunnerEnvironmentClassesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunnerInteractionListRunnerEnvironmentClassesResponse,
        )

    def list_runner_scm_integrations(
        self,
        *,
        connect_protocol_version: Literal[1],
        filter: runner_interaction_list_runner_scm_integrations_params.Filter | NotGiven = NOT_GIVEN,
        pagination: runner_interaction_list_runner_scm_integrations_params.Pagination | NotGiven = NOT_GIVEN,
        runner_id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunnerInteractionListRunnerScmIntegrationsResponse:
        """
        ListRunnerSCMIntegrations

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          pagination: pagination contains the pagination options for listing SCM integrations

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
            "/gitpod.v1.RunnerInteractionService/ListRunnerSCMIntegrations",
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                    "runner_id": runner_id,
                },
                runner_interaction_list_runner_scm_integrations_params.RunnerInteractionListRunnerScmIntegrationsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunnerInteractionListRunnerScmIntegrationsResponse,
        )

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

    def send_response(
        self,
        *,
        body: runner_interaction_send_response_params.Body,
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
        SendResponse sends a response to a request.

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
            "/gitpod.v1.RunnerInteractionService/SendResponse",
            body=maybe_transform(body, runner_interaction_send_response_params.RunnerInteractionSendResponseParams),
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

    def update_runner_configuration_schema(
        self,
        *,
        connect_protocol_version: Literal[1],
        config_schema: runner_interaction_update_runner_configuration_schema_params.ConfigSchema | NotGiven = NOT_GIVEN,
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
        UpdateRunnerConfigurationSchema updates the runner's configuration schema.

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          config_schema: config_schema is the schema for the runner's configuration

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
            "/gitpod.v1.RunnerInteractionService/UpdateRunnerConfigurationSchema",
            body=maybe_transform(
                {
                    "config_schema": config_schema,
                    "runner_id": runner_id,
                },
                runner_interaction_update_runner_configuration_schema_params.RunnerInteractionUpdateRunnerConfigurationSchemaParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
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
    def environments(self) -> AsyncEnvironmentsResource:
        return AsyncEnvironmentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRunnerInteractionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
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

    async def get_host_authentication_token_value(
        self,
        *,
        connect_protocol_version: Literal[1],
        host: str | NotGiven = NOT_GIVEN,
        principal_id: str | NotGiven = NOT_GIVEN,
        runner_id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunnerInteractionGetHostAuthenticationTokenValueResponse:
        """
        GetRunnerHostAuthenticationToken returns an authentication token for the given
        host.

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          host: The host to get the authentication token for

          principal_id: The principal's ID to get the authentication token for

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
            "/gitpod.v1.RunnerInteractionService/GetHostAuthenticationTokenValue",
            body=await async_maybe_transform(
                {
                    "host": host,
                    "principal_id": principal_id,
                    "runner_id": runner_id,
                },
                runner_interaction_get_host_authentication_token_value_params.RunnerInteractionGetHostAuthenticationTokenValueParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunnerInteractionGetHostAuthenticationTokenValueResponse,
        )

    async def get_latest_version(
        self,
        *,
        connect_protocol_version: Literal[1],
        current_version: str | NotGiven = NOT_GIVEN,
        infrastructure_version: str | NotGiven = NOT_GIVEN,
        runner_id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunnerInteractionGetLatestVersionResponse:
        """
        GetLatestVersion returns the latest version of the runner.

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          current_version: The current version of the runner

          infrastructure_version: The version of the infrastructure

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
            "/gitpod.v1.RunnerInteractionService/GetLatestVersion",
            body=await async_maybe_transform(
                {
                    "current_version": current_version,
                    "infrastructure_version": infrastructure_version,
                    "runner_id": runner_id,
                },
                runner_interaction_get_latest_version_params.RunnerInteractionGetLatestVersionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunnerInteractionGetLatestVersionResponse,
        )

    async def list_runner_environment_classes(
        self,
        *,
        connect_protocol_version: Literal[1],
        filter: runner_interaction_list_runner_environment_classes_params.Filter | NotGiven = NOT_GIVEN,
        pagination: runner_interaction_list_runner_environment_classes_params.Pagination | NotGiven = NOT_GIVEN,
        runner_id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunnerInteractionListRunnerEnvironmentClassesResponse:
        """
        ListRunnerEnvironmentClasses returns the environment classes configured for the
        runner.

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          pagination: pagination contains the pagination options for listing environment classes

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
            "/gitpod.v1.RunnerInteractionService/ListRunnerEnvironmentClasses",
            body=await async_maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                    "runner_id": runner_id,
                },
                runner_interaction_list_runner_environment_classes_params.RunnerInteractionListRunnerEnvironmentClassesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunnerInteractionListRunnerEnvironmentClassesResponse,
        )

    async def list_runner_scm_integrations(
        self,
        *,
        connect_protocol_version: Literal[1],
        filter: runner_interaction_list_runner_scm_integrations_params.Filter | NotGiven = NOT_GIVEN,
        pagination: runner_interaction_list_runner_scm_integrations_params.Pagination | NotGiven = NOT_GIVEN,
        runner_id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunnerInteractionListRunnerScmIntegrationsResponse:
        """
        ListRunnerSCMIntegrations

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          pagination: pagination contains the pagination options for listing SCM integrations

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
            "/gitpod.v1.RunnerInteractionService/ListRunnerSCMIntegrations",
            body=await async_maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                    "runner_id": runner_id,
                },
                runner_interaction_list_runner_scm_integrations_params.RunnerInteractionListRunnerScmIntegrationsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunnerInteractionListRunnerScmIntegrationsResponse,
        )

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

    async def send_response(
        self,
        *,
        body: runner_interaction_send_response_params.Body,
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
        SendResponse sends a response to a request.

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
            "/gitpod.v1.RunnerInteractionService/SendResponse",
            body=await async_maybe_transform(
                body, runner_interaction_send_response_params.RunnerInteractionSendResponseParams
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

    async def update_runner_configuration_schema(
        self,
        *,
        connect_protocol_version: Literal[1],
        config_schema: runner_interaction_update_runner_configuration_schema_params.ConfigSchema | NotGiven = NOT_GIVEN,
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
        UpdateRunnerConfigurationSchema updates the runner's configuration schema.

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          config_schema: config_schema is the schema for the runner's configuration

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
            "/gitpod.v1.RunnerInteractionService/UpdateRunnerConfigurationSchema",
            body=await async_maybe_transform(
                {
                    "config_schema": config_schema,
                    "runner_id": runner_id,
                },
                runner_interaction_update_runner_configuration_schema_params.RunnerInteractionUpdateRunnerConfigurationSchemaParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
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

        self.get_host_authentication_token_value = to_raw_response_wrapper(
            runner_interactions.get_host_authentication_token_value,
        )
        self.get_latest_version = to_raw_response_wrapper(
            runner_interactions.get_latest_version,
        )
        self.list_runner_environment_classes = to_raw_response_wrapper(
            runner_interactions.list_runner_environment_classes,
        )
        self.list_runner_scm_integrations = to_raw_response_wrapper(
            runner_interactions.list_runner_scm_integrations,
        )
        self.mark_active = to_raw_response_wrapper(
            runner_interactions.mark_active,
        )
        self.send_response = to_raw_response_wrapper(
            runner_interactions.send_response,
        )
        self.signup = to_raw_response_wrapper(
            runner_interactions.signup,
        )
        self.update_runner_configuration_schema = to_raw_response_wrapper(
            runner_interactions.update_runner_configuration_schema,
        )
        self.update_status = to_raw_response_wrapper(
            runner_interactions.update_status,
        )

    @cached_property
    def environments(self) -> EnvironmentsResourceWithRawResponse:
        return EnvironmentsResourceWithRawResponse(self._runner_interactions.environments)


class AsyncRunnerInteractionsResourceWithRawResponse:
    def __init__(self, runner_interactions: AsyncRunnerInteractionsResource) -> None:
        self._runner_interactions = runner_interactions

        self.get_host_authentication_token_value = async_to_raw_response_wrapper(
            runner_interactions.get_host_authentication_token_value,
        )
        self.get_latest_version = async_to_raw_response_wrapper(
            runner_interactions.get_latest_version,
        )
        self.list_runner_environment_classes = async_to_raw_response_wrapper(
            runner_interactions.list_runner_environment_classes,
        )
        self.list_runner_scm_integrations = async_to_raw_response_wrapper(
            runner_interactions.list_runner_scm_integrations,
        )
        self.mark_active = async_to_raw_response_wrapper(
            runner_interactions.mark_active,
        )
        self.send_response = async_to_raw_response_wrapper(
            runner_interactions.send_response,
        )
        self.signup = async_to_raw_response_wrapper(
            runner_interactions.signup,
        )
        self.update_runner_configuration_schema = async_to_raw_response_wrapper(
            runner_interactions.update_runner_configuration_schema,
        )
        self.update_status = async_to_raw_response_wrapper(
            runner_interactions.update_status,
        )

    @cached_property
    def environments(self) -> AsyncEnvironmentsResourceWithRawResponse:
        return AsyncEnvironmentsResourceWithRawResponse(self._runner_interactions.environments)


class RunnerInteractionsResourceWithStreamingResponse:
    def __init__(self, runner_interactions: RunnerInteractionsResource) -> None:
        self._runner_interactions = runner_interactions

        self.get_host_authentication_token_value = to_streamed_response_wrapper(
            runner_interactions.get_host_authentication_token_value,
        )
        self.get_latest_version = to_streamed_response_wrapper(
            runner_interactions.get_latest_version,
        )
        self.list_runner_environment_classes = to_streamed_response_wrapper(
            runner_interactions.list_runner_environment_classes,
        )
        self.list_runner_scm_integrations = to_streamed_response_wrapper(
            runner_interactions.list_runner_scm_integrations,
        )
        self.mark_active = to_streamed_response_wrapper(
            runner_interactions.mark_active,
        )
        self.send_response = to_streamed_response_wrapper(
            runner_interactions.send_response,
        )
        self.signup = to_streamed_response_wrapper(
            runner_interactions.signup,
        )
        self.update_runner_configuration_schema = to_streamed_response_wrapper(
            runner_interactions.update_runner_configuration_schema,
        )
        self.update_status = to_streamed_response_wrapper(
            runner_interactions.update_status,
        )

    @cached_property
    def environments(self) -> EnvironmentsResourceWithStreamingResponse:
        return EnvironmentsResourceWithStreamingResponse(self._runner_interactions.environments)


class AsyncRunnerInteractionsResourceWithStreamingResponse:
    def __init__(self, runner_interactions: AsyncRunnerInteractionsResource) -> None:
        self._runner_interactions = runner_interactions

        self.get_host_authentication_token_value = async_to_streamed_response_wrapper(
            runner_interactions.get_host_authentication_token_value,
        )
        self.get_latest_version = async_to_streamed_response_wrapper(
            runner_interactions.get_latest_version,
        )
        self.list_runner_environment_classes = async_to_streamed_response_wrapper(
            runner_interactions.list_runner_environment_classes,
        )
        self.list_runner_scm_integrations = async_to_streamed_response_wrapper(
            runner_interactions.list_runner_scm_integrations,
        )
        self.mark_active = async_to_streamed_response_wrapper(
            runner_interactions.mark_active,
        )
        self.send_response = async_to_streamed_response_wrapper(
            runner_interactions.send_response,
        )
        self.signup = async_to_streamed_response_wrapper(
            runner_interactions.signup,
        )
        self.update_runner_configuration_schema = async_to_streamed_response_wrapper(
            runner_interactions.update_runner_configuration_schema,
        )
        self.update_status = async_to_streamed_response_wrapper(
            runner_interactions.update_status,
        )

    @cached_property
    def environments(self) -> AsyncEnvironmentsResourceWithStreamingResponse:
        return AsyncEnvironmentsResourceWithStreamingResponse(self._runner_interactions.environments)
