# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast
from typing_extensions import Literal, overload

import httpx

from .schema import (
    SchemaResource,
    AsyncSchemaResource,
    SchemaResourceWithRawResponse,
    AsyncSchemaResourceWithRawResponse,
    SchemaResourceWithStreamingResponse,
    AsyncSchemaResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    is_given,
    required_args,
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.runners import configuration_validate_params
from .scm_integrations import (
    ScmIntegrationsResource,
    AsyncScmIntegrationsResource,
    ScmIntegrationsResourceWithRawResponse,
    AsyncScmIntegrationsResourceWithRawResponse,
    ScmIntegrationsResourceWithStreamingResponse,
    AsyncScmIntegrationsResourceWithStreamingResponse,
)
from .environment_classes import (
    EnvironmentClassesResource,
    AsyncEnvironmentClassesResource,
    EnvironmentClassesResourceWithRawResponse,
    AsyncEnvironmentClassesResourceWithRawResponse,
    EnvironmentClassesResourceWithStreamingResponse,
    AsyncEnvironmentClassesResourceWithStreamingResponse,
)
from .host_authentication_tokens import (
    HostAuthenticationTokensResource,
    AsyncHostAuthenticationTokensResource,
    HostAuthenticationTokensResourceWithRawResponse,
    AsyncHostAuthenticationTokensResourceWithRawResponse,
    HostAuthenticationTokensResourceWithStreamingResponse,
    AsyncHostAuthenticationTokensResourceWithStreamingResponse,
)
from ....types.runners.configuration_validate_response import ConfigurationValidateResponse

__all__ = ["ConfigurationsResource", "AsyncConfigurationsResource"]


class ConfigurationsResource(SyncAPIResource):
    @cached_property
    def environment_classes(self) -> EnvironmentClassesResource:
        return EnvironmentClassesResource(self._client)

    @cached_property
    def host_authentication_tokens(self) -> HostAuthenticationTokensResource:
        return HostAuthenticationTokensResource(self._client)

    @cached_property
    def schema(self) -> SchemaResource:
        return SchemaResource(self._client)

    @cached_property
    def scm_integrations(self) -> ScmIntegrationsResource:
        return ScmIntegrationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ConfigurationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return ConfigurationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigurationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return ConfigurationsResourceWithStreamingResponse(self)

    @overload
    def validate(
        self,
        *,
        environment_class: configuration_validate_params.Variant0EnvironmentClass,
        connect_protocol_version: Literal[1],
        runner_id: str | NotGiven = NOT_GIVEN,
        scm_integration: configuration_validate_params.Variant0ScmIntegration | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationValidateResponse:
        """ValidateRunnerConfiguration validates a runner configuration (e.g.

        environment
        class, SCM integration)

        with the runner.

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
    def validate(
        self,
        *,
        scm_integration: configuration_validate_params.Variant1ScmIntegration,
        connect_protocol_version: Literal[1],
        environment_class: configuration_validate_params.Variant1EnvironmentClass | NotGiven = NOT_GIVEN,
        runner_id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationValidateResponse:
        """ValidateRunnerConfiguration validates a runner configuration (e.g.

        environment
        class, SCM integration)

        with the runner.

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
    def validate(
        self,
        *,
        connect_protocol_version: Literal[1],
        environment_class: configuration_validate_params.Variant2EnvironmentClass | NotGiven = NOT_GIVEN,
        runner_id: str | NotGiven = NOT_GIVEN,
        scm_integration: configuration_validate_params.Variant2ScmIntegration | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationValidateResponse:
        """ValidateRunnerConfiguration validates a runner configuration (e.g.

        environment
        class, SCM integration)

        with the runner.

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          connect_timeout_ms: Define the timeout, in ms

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["environment_class", "connect_protocol_version"],
        ["scm_integration", "connect_protocol_version"],
        ["connect_protocol_version"],
    )
    def validate(
        self,
        *,
        environment_class: configuration_validate_params.Variant0EnvironmentClass | NotGiven = NOT_GIVEN,
        connect_protocol_version: Literal[1],
        runner_id: str | NotGiven = NOT_GIVEN,
        scm_integration: configuration_validate_params.Variant0ScmIntegration | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationValidateResponse:
        extra_headers = {
            **strip_not_given(
                {
                    "Connect-Protocol-Version": str(connect_protocol_version),
                    "Connect-Timeout-Ms": str(connect_timeout_ms) if is_given(connect_timeout_ms) else NOT_GIVEN,
                }
            ),
            **(extra_headers or {}),
        }
        return cast(
            ConfigurationValidateResponse,
            self._post(
                "/gitpod.v1.RunnerConfigurationService/ValidateRunnerConfiguration",
                body=maybe_transform(
                    {
                        "environment_class": environment_class,
                        "runner_id": runner_id,
                        "scm_integration": scm_integration,
                    },
                    configuration_validate_params.ConfigurationValidateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ConfigurationValidateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncConfigurationsResource(AsyncAPIResource):
    @cached_property
    def environment_classes(self) -> AsyncEnvironmentClassesResource:
        return AsyncEnvironmentClassesResource(self._client)

    @cached_property
    def host_authentication_tokens(self) -> AsyncHostAuthenticationTokensResource:
        return AsyncHostAuthenticationTokensResource(self._client)

    @cached_property
    def schema(self) -> AsyncSchemaResource:
        return AsyncSchemaResource(self._client)

    @cached_property
    def scm_integrations(self) -> AsyncScmIntegrationsResource:
        return AsyncScmIntegrationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncConfigurationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConfigurationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigurationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return AsyncConfigurationsResourceWithStreamingResponse(self)

    @overload
    async def validate(
        self,
        *,
        environment_class: configuration_validate_params.Variant0EnvironmentClass,
        connect_protocol_version: Literal[1],
        runner_id: str | NotGiven = NOT_GIVEN,
        scm_integration: configuration_validate_params.Variant0ScmIntegration | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationValidateResponse:
        """ValidateRunnerConfiguration validates a runner configuration (e.g.

        environment
        class, SCM integration)

        with the runner.

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
    async def validate(
        self,
        *,
        scm_integration: configuration_validate_params.Variant1ScmIntegration,
        connect_protocol_version: Literal[1],
        environment_class: configuration_validate_params.Variant1EnvironmentClass | NotGiven = NOT_GIVEN,
        runner_id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationValidateResponse:
        """ValidateRunnerConfiguration validates a runner configuration (e.g.

        environment
        class, SCM integration)

        with the runner.

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
    async def validate(
        self,
        *,
        connect_protocol_version: Literal[1],
        environment_class: configuration_validate_params.Variant2EnvironmentClass | NotGiven = NOT_GIVEN,
        runner_id: str | NotGiven = NOT_GIVEN,
        scm_integration: configuration_validate_params.Variant2ScmIntegration | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationValidateResponse:
        """ValidateRunnerConfiguration validates a runner configuration (e.g.

        environment
        class, SCM integration)

        with the runner.

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          connect_timeout_ms: Define the timeout, in ms

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["environment_class", "connect_protocol_version"],
        ["scm_integration", "connect_protocol_version"],
        ["connect_protocol_version"],
    )
    async def validate(
        self,
        *,
        environment_class: configuration_validate_params.Variant0EnvironmentClass | NotGiven = NOT_GIVEN,
        connect_protocol_version: Literal[1],
        runner_id: str | NotGiven = NOT_GIVEN,
        scm_integration: configuration_validate_params.Variant0ScmIntegration | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationValidateResponse:
        extra_headers = {
            **strip_not_given(
                {
                    "Connect-Protocol-Version": str(connect_protocol_version),
                    "Connect-Timeout-Ms": str(connect_timeout_ms) if is_given(connect_timeout_ms) else NOT_GIVEN,
                }
            ),
            **(extra_headers or {}),
        }
        return cast(
            ConfigurationValidateResponse,
            await self._post(
                "/gitpod.v1.RunnerConfigurationService/ValidateRunnerConfiguration",
                body=await async_maybe_transform(
                    {
                        "environment_class": environment_class,
                        "runner_id": runner_id,
                        "scm_integration": scm_integration,
                    },
                    configuration_validate_params.ConfigurationValidateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, ConfigurationValidateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class ConfigurationsResourceWithRawResponse:
    def __init__(self, configurations: ConfigurationsResource) -> None:
        self._configurations = configurations

        self.validate = to_raw_response_wrapper(
            configurations.validate,
        )

    @cached_property
    def environment_classes(self) -> EnvironmentClassesResourceWithRawResponse:
        return EnvironmentClassesResourceWithRawResponse(self._configurations.environment_classes)

    @cached_property
    def host_authentication_tokens(self) -> HostAuthenticationTokensResourceWithRawResponse:
        return HostAuthenticationTokensResourceWithRawResponse(self._configurations.host_authentication_tokens)

    @cached_property
    def schema(self) -> SchemaResourceWithRawResponse:
        return SchemaResourceWithRawResponse(self._configurations.schema)

    @cached_property
    def scm_integrations(self) -> ScmIntegrationsResourceWithRawResponse:
        return ScmIntegrationsResourceWithRawResponse(self._configurations.scm_integrations)


class AsyncConfigurationsResourceWithRawResponse:
    def __init__(self, configurations: AsyncConfigurationsResource) -> None:
        self._configurations = configurations

        self.validate = async_to_raw_response_wrapper(
            configurations.validate,
        )

    @cached_property
    def environment_classes(self) -> AsyncEnvironmentClassesResourceWithRawResponse:
        return AsyncEnvironmentClassesResourceWithRawResponse(self._configurations.environment_classes)

    @cached_property
    def host_authentication_tokens(self) -> AsyncHostAuthenticationTokensResourceWithRawResponse:
        return AsyncHostAuthenticationTokensResourceWithRawResponse(self._configurations.host_authentication_tokens)

    @cached_property
    def schema(self) -> AsyncSchemaResourceWithRawResponse:
        return AsyncSchemaResourceWithRawResponse(self._configurations.schema)

    @cached_property
    def scm_integrations(self) -> AsyncScmIntegrationsResourceWithRawResponse:
        return AsyncScmIntegrationsResourceWithRawResponse(self._configurations.scm_integrations)


class ConfigurationsResourceWithStreamingResponse:
    def __init__(self, configurations: ConfigurationsResource) -> None:
        self._configurations = configurations

        self.validate = to_streamed_response_wrapper(
            configurations.validate,
        )

    @cached_property
    def environment_classes(self) -> EnvironmentClassesResourceWithStreamingResponse:
        return EnvironmentClassesResourceWithStreamingResponse(self._configurations.environment_classes)

    @cached_property
    def host_authentication_tokens(self) -> HostAuthenticationTokensResourceWithStreamingResponse:
        return HostAuthenticationTokensResourceWithStreamingResponse(self._configurations.host_authentication_tokens)

    @cached_property
    def schema(self) -> SchemaResourceWithStreamingResponse:
        return SchemaResourceWithStreamingResponse(self._configurations.schema)

    @cached_property
    def scm_integrations(self) -> ScmIntegrationsResourceWithStreamingResponse:
        return ScmIntegrationsResourceWithStreamingResponse(self._configurations.scm_integrations)


class AsyncConfigurationsResourceWithStreamingResponse:
    def __init__(self, configurations: AsyncConfigurationsResource) -> None:
        self._configurations = configurations

        self.validate = async_to_streamed_response_wrapper(
            configurations.validate,
        )

    @cached_property
    def environment_classes(self) -> AsyncEnvironmentClassesResourceWithStreamingResponse:
        return AsyncEnvironmentClassesResourceWithStreamingResponse(self._configurations.environment_classes)

    @cached_property
    def host_authentication_tokens(self) -> AsyncHostAuthenticationTokensResourceWithStreamingResponse:
        return AsyncHostAuthenticationTokensResourceWithStreamingResponse(
            self._configurations.host_authentication_tokens
        )

    @cached_property
    def schema(self) -> AsyncSchemaResourceWithStreamingResponse:
        return AsyncSchemaResourceWithStreamingResponse(self._configurations.schema)

    @cached_property
    def scm_integrations(self) -> AsyncScmIntegrationsResourceWithStreamingResponse:
        return AsyncScmIntegrationsResourceWithStreamingResponse(self._configurations.scm_integrations)
