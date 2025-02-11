# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
    maybe_transform,
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
from ....types.shared_params.environment_class import EnvironmentClass
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

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ConfigurationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigurationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return ConfigurationsResourceWithStreamingResponse(self)

    def validate(
        self,
        *,
        environment_class: EnvironmentClass | NotGiven = NOT_GIVEN,
        runner_id: str | NotGiven = NOT_GIVEN,
        scm_integration: configuration_validate_params.ScmIntegration | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationValidateResponse:
        """ValidateRunnerConfiguration validates a runner configuration (e.g.

        environment
        class, SCM integration) with the runner.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
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
            cast_to=ConfigurationValidateResponse,
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

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConfigurationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigurationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return AsyncConfigurationsResourceWithStreamingResponse(self)

    async def validate(
        self,
        *,
        environment_class: EnvironmentClass | NotGiven = NOT_GIVEN,
        runner_id: str | NotGiven = NOT_GIVEN,
        scm_integration: configuration_validate_params.ScmIntegration | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationValidateResponse:
        """ValidateRunnerConfiguration validates a runner configuration (e.g.

        environment
        class, SCM integration) with the runner.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
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
            cast_to=ConfigurationValidateResponse,
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
