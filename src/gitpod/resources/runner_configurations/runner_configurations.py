# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...types import runner_configuration_validate_params
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
from .scm_integration import (
    ScmIntegrationResource,
    AsyncScmIntegrationResource,
    ScmIntegrationResourceWithRawResponse,
    AsyncScmIntegrationResourceWithRawResponse,
    ScmIntegrationResourceWithStreamingResponse,
    AsyncScmIntegrationResourceWithStreamingResponse,
)
from .environment_classes import (
    EnvironmentClassesResource,
    AsyncEnvironmentClassesResource,
    EnvironmentClassesResourceWithRawResponse,
    AsyncEnvironmentClassesResourceWithRawResponse,
    EnvironmentClassesResourceWithStreamingResponse,
    AsyncEnvironmentClassesResourceWithStreamingResponse,
)
from .configuration_schema import (
    ConfigurationSchemaResource,
    AsyncConfigurationSchemaResource,
    ConfigurationSchemaResourceWithRawResponse,
    AsyncConfigurationSchemaResourceWithRawResponse,
    ConfigurationSchemaResourceWithStreamingResponse,
    AsyncConfigurationSchemaResourceWithStreamingResponse,
)
from .host_authentication_tokens import (
    HostAuthenticationTokensResource,
    AsyncHostAuthenticationTokensResource,
    HostAuthenticationTokensResourceWithRawResponse,
    AsyncHostAuthenticationTokensResourceWithRawResponse,
    HostAuthenticationTokensResourceWithStreamingResponse,
    AsyncHostAuthenticationTokensResourceWithStreamingResponse,
)
from ...types.runner_configuration_validate_response import RunnerConfigurationValidateResponse

__all__ = ["RunnerConfigurationsResource", "AsyncRunnerConfigurationsResource"]


class RunnerConfigurationsResource(SyncAPIResource):
    @cached_property
    def host_authentication_tokens(self) -> HostAuthenticationTokensResource:
        return HostAuthenticationTokensResource(self._client)

    @cached_property
    def configuration_schema(self) -> ConfigurationSchemaResource:
        return ConfigurationSchemaResource(self._client)

    @cached_property
    def scm_integration(self) -> ScmIntegrationResource:
        return ScmIntegrationResource(self._client)

    @cached_property
    def environment_classes(self) -> EnvironmentClassesResource:
        return EnvironmentClassesResource(self._client)

    @cached_property
    def with_raw_response(self) -> RunnerConfigurationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return RunnerConfigurationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RunnerConfigurationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return RunnerConfigurationsResourceWithStreamingResponse(self)

    def validate(
        self,
        *,
        body: runner_configuration_validate_params.Body,
        connect_protocol_version: Literal[1],
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunnerConfigurationValidateResponse:
        """ValidateRunnerConfiguration validates a runner configuration (e.g.

        environment
        class, SCM integration) with the runner.

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
            "/gitpod.v1.RunnerConfigurationService/ValidateRunnerConfiguration",
            body=maybe_transform(body, runner_configuration_validate_params.RunnerConfigurationValidateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunnerConfigurationValidateResponse,
        )


class AsyncRunnerConfigurationsResource(AsyncAPIResource):
    @cached_property
    def host_authentication_tokens(self) -> AsyncHostAuthenticationTokensResource:
        return AsyncHostAuthenticationTokensResource(self._client)

    @cached_property
    def configuration_schema(self) -> AsyncConfigurationSchemaResource:
        return AsyncConfigurationSchemaResource(self._client)

    @cached_property
    def scm_integration(self) -> AsyncScmIntegrationResource:
        return AsyncScmIntegrationResource(self._client)

    @cached_property
    def environment_classes(self) -> AsyncEnvironmentClassesResource:
        return AsyncEnvironmentClassesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRunnerConfigurationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRunnerConfigurationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRunnerConfigurationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return AsyncRunnerConfigurationsResourceWithStreamingResponse(self)

    async def validate(
        self,
        *,
        body: runner_configuration_validate_params.Body,
        connect_protocol_version: Literal[1],
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunnerConfigurationValidateResponse:
        """ValidateRunnerConfiguration validates a runner configuration (e.g.

        environment
        class, SCM integration) with the runner.

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
            "/gitpod.v1.RunnerConfigurationService/ValidateRunnerConfiguration",
            body=await async_maybe_transform(
                body, runner_configuration_validate_params.RunnerConfigurationValidateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunnerConfigurationValidateResponse,
        )


class RunnerConfigurationsResourceWithRawResponse:
    def __init__(self, runner_configurations: RunnerConfigurationsResource) -> None:
        self._runner_configurations = runner_configurations

        self.validate = to_raw_response_wrapper(
            runner_configurations.validate,
        )

    @cached_property
    def host_authentication_tokens(self) -> HostAuthenticationTokensResourceWithRawResponse:
        return HostAuthenticationTokensResourceWithRawResponse(self._runner_configurations.host_authentication_tokens)

    @cached_property
    def configuration_schema(self) -> ConfigurationSchemaResourceWithRawResponse:
        return ConfigurationSchemaResourceWithRawResponse(self._runner_configurations.configuration_schema)

    @cached_property
    def scm_integration(self) -> ScmIntegrationResourceWithRawResponse:
        return ScmIntegrationResourceWithRawResponse(self._runner_configurations.scm_integration)

    @cached_property
    def environment_classes(self) -> EnvironmentClassesResourceWithRawResponse:
        return EnvironmentClassesResourceWithRawResponse(self._runner_configurations.environment_classes)


class AsyncRunnerConfigurationsResourceWithRawResponse:
    def __init__(self, runner_configurations: AsyncRunnerConfigurationsResource) -> None:
        self._runner_configurations = runner_configurations

        self.validate = async_to_raw_response_wrapper(
            runner_configurations.validate,
        )

    @cached_property
    def host_authentication_tokens(self) -> AsyncHostAuthenticationTokensResourceWithRawResponse:
        return AsyncHostAuthenticationTokensResourceWithRawResponse(
            self._runner_configurations.host_authentication_tokens
        )

    @cached_property
    def configuration_schema(self) -> AsyncConfigurationSchemaResourceWithRawResponse:
        return AsyncConfigurationSchemaResourceWithRawResponse(self._runner_configurations.configuration_schema)

    @cached_property
    def scm_integration(self) -> AsyncScmIntegrationResourceWithRawResponse:
        return AsyncScmIntegrationResourceWithRawResponse(self._runner_configurations.scm_integration)

    @cached_property
    def environment_classes(self) -> AsyncEnvironmentClassesResourceWithRawResponse:
        return AsyncEnvironmentClassesResourceWithRawResponse(self._runner_configurations.environment_classes)


class RunnerConfigurationsResourceWithStreamingResponse:
    def __init__(self, runner_configurations: RunnerConfigurationsResource) -> None:
        self._runner_configurations = runner_configurations

        self.validate = to_streamed_response_wrapper(
            runner_configurations.validate,
        )

    @cached_property
    def host_authentication_tokens(self) -> HostAuthenticationTokensResourceWithStreamingResponse:
        return HostAuthenticationTokensResourceWithStreamingResponse(
            self._runner_configurations.host_authentication_tokens
        )

    @cached_property
    def configuration_schema(self) -> ConfigurationSchemaResourceWithStreamingResponse:
        return ConfigurationSchemaResourceWithStreamingResponse(self._runner_configurations.configuration_schema)

    @cached_property
    def scm_integration(self) -> ScmIntegrationResourceWithStreamingResponse:
        return ScmIntegrationResourceWithStreamingResponse(self._runner_configurations.scm_integration)

    @cached_property
    def environment_classes(self) -> EnvironmentClassesResourceWithStreamingResponse:
        return EnvironmentClassesResourceWithStreamingResponse(self._runner_configurations.environment_classes)


class AsyncRunnerConfigurationsResourceWithStreamingResponse:
    def __init__(self, runner_configurations: AsyncRunnerConfigurationsResource) -> None:
        self._runner_configurations = runner_configurations

        self.validate = async_to_streamed_response_wrapper(
            runner_configurations.validate,
        )

    @cached_property
    def host_authentication_tokens(self) -> AsyncHostAuthenticationTokensResourceWithStreamingResponse:
        return AsyncHostAuthenticationTokensResourceWithStreamingResponse(
            self._runner_configurations.host_authentication_tokens
        )

    @cached_property
    def configuration_schema(self) -> AsyncConfigurationSchemaResourceWithStreamingResponse:
        return AsyncConfigurationSchemaResourceWithStreamingResponse(self._runner_configurations.configuration_schema)

    @cached_property
    def scm_integration(self) -> AsyncScmIntegrationResourceWithStreamingResponse:
        return AsyncScmIntegrationResourceWithStreamingResponse(self._runner_configurations.scm_integration)

    @cached_property
    def environment_classes(self) -> AsyncEnvironmentClassesResourceWithStreamingResponse:
        return AsyncEnvironmentClassesResourceWithStreamingResponse(self._runner_configurations.environment_classes)
