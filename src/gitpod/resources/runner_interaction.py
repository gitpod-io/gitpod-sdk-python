# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, overload

import httpx

from ..types import (
    runner_interaction_send_response_params,
    runner_interaction_get_latest_version_params,
    runner_interaction_list_runner_scm_integrations_params,
    runner_interaction_list_runner_environment_classes_params,
    runner_interaction_update_runner_configuration_schema_params,
    runner_interaction_get_host_authentication_token_value_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    is_given,
    required_args,
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
from ..types.runner_interaction_get_latest_version_response import RunnerInteractionGetLatestVersionResponse
from ..types.runner_interaction_list_runner_scm_integrations_response import (
    RunnerInteractionListRunnerScmIntegrationsResponse,
)
from ..types.runner_interaction_list_runner_environment_classes_response import (
    RunnerInteractionListRunnerEnvironmentClassesResponse,
)
from ..types.runner_interaction_get_host_authentication_token_value_response import (
    RunnerInteractionGetHostAuthenticationTokenValueResponse,
)

__all__ = ["RunnerInteractionResource", "AsyncRunnerInteractionResource"]


class RunnerInteractionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RunnerInteractionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return RunnerInteractionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RunnerInteractionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return RunnerInteractionResourceWithStreamingResponse(self)

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

    @overload
    def send_response(
        self,
        *,
        body: object,
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
        ...

    @overload
    def send_response(
        self,
        *,
        body: object,
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
        ...

    @overload
    def send_response(
        self,
        *,
        body: object,
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
        ...

    @overload
    def send_response(
        self,
        *,
        body: object,
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
        ...

    @overload
    def send_response(
        self,
        *,
        body: object,
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
        ...

    @overload
    def send_response(
        self,
        *,
        body: object,
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
        ...

    @required_args(["body", "connect_protocol_version"])
    def send_response(
        self,
        *,
        body: object,
        connect_protocol_version: Literal[1],
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
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
            "/gitpod.v1.RunnerInteractionService/SendResponse",
            body=maybe_transform(body, runner_interaction_send_response_params.RunnerInteractionSendResponseParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
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


class AsyncRunnerInteractionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRunnerInteractionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRunnerInteractionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRunnerInteractionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return AsyncRunnerInteractionResourceWithStreamingResponse(self)

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

    @overload
    async def send_response(
        self,
        *,
        body: object,
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
        ...

    @overload
    async def send_response(
        self,
        *,
        body: object,
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
        ...

    @overload
    async def send_response(
        self,
        *,
        body: object,
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
        ...

    @overload
    async def send_response(
        self,
        *,
        body: object,
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
        ...

    @overload
    async def send_response(
        self,
        *,
        body: object,
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
        ...

    @overload
    async def send_response(
        self,
        *,
        body: object,
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
        ...

    @required_args(["body", "connect_protocol_version"])
    async def send_response(
        self,
        *,
        body: object,
        connect_protocol_version: Literal[1],
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
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
            "/gitpod.v1.RunnerInteractionService/SendResponse",
            body=await async_maybe_transform(
                body, runner_interaction_send_response_params.RunnerInteractionSendResponseParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
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


class RunnerInteractionResourceWithRawResponse:
    def __init__(self, runner_interaction: RunnerInteractionResource) -> None:
        self._runner_interaction = runner_interaction

        self.get_host_authentication_token_value = to_raw_response_wrapper(
            runner_interaction.get_host_authentication_token_value,
        )
        self.get_latest_version = to_raw_response_wrapper(
            runner_interaction.get_latest_version,
        )
        self.list_runner_environment_classes = to_raw_response_wrapper(
            runner_interaction.list_runner_environment_classes,
        )
        self.list_runner_scm_integrations = to_raw_response_wrapper(
            runner_interaction.list_runner_scm_integrations,
        )
        self.send_response = to_raw_response_wrapper(
            runner_interaction.send_response,
        )
        self.update_runner_configuration_schema = to_raw_response_wrapper(
            runner_interaction.update_runner_configuration_schema,
        )


class AsyncRunnerInteractionResourceWithRawResponse:
    def __init__(self, runner_interaction: AsyncRunnerInteractionResource) -> None:
        self._runner_interaction = runner_interaction

        self.get_host_authentication_token_value = async_to_raw_response_wrapper(
            runner_interaction.get_host_authentication_token_value,
        )
        self.get_latest_version = async_to_raw_response_wrapper(
            runner_interaction.get_latest_version,
        )
        self.list_runner_environment_classes = async_to_raw_response_wrapper(
            runner_interaction.list_runner_environment_classes,
        )
        self.list_runner_scm_integrations = async_to_raw_response_wrapper(
            runner_interaction.list_runner_scm_integrations,
        )
        self.send_response = async_to_raw_response_wrapper(
            runner_interaction.send_response,
        )
        self.update_runner_configuration_schema = async_to_raw_response_wrapper(
            runner_interaction.update_runner_configuration_schema,
        )


class RunnerInteractionResourceWithStreamingResponse:
    def __init__(self, runner_interaction: RunnerInteractionResource) -> None:
        self._runner_interaction = runner_interaction

        self.get_host_authentication_token_value = to_streamed_response_wrapper(
            runner_interaction.get_host_authentication_token_value,
        )
        self.get_latest_version = to_streamed_response_wrapper(
            runner_interaction.get_latest_version,
        )
        self.list_runner_environment_classes = to_streamed_response_wrapper(
            runner_interaction.list_runner_environment_classes,
        )
        self.list_runner_scm_integrations = to_streamed_response_wrapper(
            runner_interaction.list_runner_scm_integrations,
        )
        self.send_response = to_streamed_response_wrapper(
            runner_interaction.send_response,
        )
        self.update_runner_configuration_schema = to_streamed_response_wrapper(
            runner_interaction.update_runner_configuration_schema,
        )


class AsyncRunnerInteractionResourceWithStreamingResponse:
    def __init__(self, runner_interaction: AsyncRunnerInteractionResource) -> None:
        self._runner_interaction = runner_interaction

        self.get_host_authentication_token_value = async_to_streamed_response_wrapper(
            runner_interaction.get_host_authentication_token_value,
        )
        self.get_latest_version = async_to_streamed_response_wrapper(
            runner_interaction.get_latest_version,
        )
        self.list_runner_environment_classes = async_to_streamed_response_wrapper(
            runner_interaction.list_runner_environment_classes,
        )
        self.list_runner_scm_integrations = async_to_streamed_response_wrapper(
            runner_interaction.list_runner_scm_integrations,
        )
        self.send_response = async_to_streamed_response_wrapper(
            runner_interaction.send_response,
        )
        self.update_runner_configuration_schema = async_to_streamed_response_wrapper(
            runner_interaction.update_runner_configuration_schema,
        )
