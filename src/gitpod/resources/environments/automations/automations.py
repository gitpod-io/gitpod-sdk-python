# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .services import (
    ServicesResource,
    AsyncServicesResource,
    ServicesResourceWithRawResponse,
    AsyncServicesResourceWithRawResponse,
    ServicesResourceWithStreamingResponse,
    AsyncServicesResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from .tasks.tasks import (
    TasksResource,
    AsyncTasksResource,
    TasksResourceWithRawResponse,
    AsyncTasksResourceWithRawResponse,
    TasksResourceWithStreamingResponse,
    AsyncTasksResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.environments import automation_upsert_params
from ....types.environments.automations_file_param import AutomationsFileParam
from ....types.environments.automation_upsert_response import AutomationUpsertResponse

__all__ = ["AutomationsResource", "AsyncAutomationsResource"]


class AutomationsResource(SyncAPIResource):
    @cached_property
    def services(self) -> ServicesResource:
        return ServicesResource(self._client)

    @cached_property
    def tasks(self) -> TasksResource:
        return TasksResource(self._client)

    @cached_property
    def with_raw_response(self) -> AutomationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AutomationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AutomationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return AutomationsResourceWithStreamingResponse(self)

    def upsert(
        self,
        *,
        automations_file: AutomationsFileParam | NotGiven = NOT_GIVEN,
        environment_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AutomationUpsertResponse:
        """
        Upserts the automations file for the given environment.

        Use this method to:

        - Configure environment automations
        - Update automation settings
        - Manage automation files

        ### Examples

        - Update automations file:

          Updates or creates the automations configuration.

          ```yaml
          environmentId: "07e03a28-65a5-4d98-b532-8ea67b188048"
          automationsFile:
            services:
              web-server:
                name: "Web Server"
                description: "Development web server"
                commands:
                  start: "npm run dev"
                  ready: "curl -s http://localhost:3000"
                triggeredBy:
                  - postDevcontainerStart
            tasks:
              build:
                name: "Build Project"
                description: "Builds the project artifacts"
                command: "npm run build"
                triggeredBy:
                  - postEnvironmentStart
          ```

        Args:
          automations_file: WARN: Do not remove any field here, as it will break reading automation yaml
              files. We error if there are any unknown fields in the yaml (to ensure the yaml
              is correct), but would break if we removed any fields. This includes marking a
              field as "reserved" in the proto file, this will also break reading the yaml.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.EnvironmentAutomationService/UpsertAutomationsFile",
            body=maybe_transform(
                {
                    "automations_file": automations_file,
                    "environment_id": environment_id,
                },
                automation_upsert_params.AutomationUpsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutomationUpsertResponse,
        )


class AsyncAutomationsResource(AsyncAPIResource):
    @cached_property
    def services(self) -> AsyncServicesResource:
        return AsyncServicesResource(self._client)

    @cached_property
    def tasks(self) -> AsyncTasksResource:
        return AsyncTasksResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAutomationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAutomationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAutomationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return AsyncAutomationsResourceWithStreamingResponse(self)

    async def upsert(
        self,
        *,
        automations_file: AutomationsFileParam | NotGiven = NOT_GIVEN,
        environment_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AutomationUpsertResponse:
        """
        Upserts the automations file for the given environment.

        Use this method to:

        - Configure environment automations
        - Update automation settings
        - Manage automation files

        ### Examples

        - Update automations file:

          Updates or creates the automations configuration.

          ```yaml
          environmentId: "07e03a28-65a5-4d98-b532-8ea67b188048"
          automationsFile:
            services:
              web-server:
                name: "Web Server"
                description: "Development web server"
                commands:
                  start: "npm run dev"
                  ready: "curl -s http://localhost:3000"
                triggeredBy:
                  - postDevcontainerStart
            tasks:
              build:
                name: "Build Project"
                description: "Builds the project artifacts"
                command: "npm run build"
                triggeredBy:
                  - postEnvironmentStart
          ```

        Args:
          automations_file: WARN: Do not remove any field here, as it will break reading automation yaml
              files. We error if there are any unknown fields in the yaml (to ensure the yaml
              is correct), but would break if we removed any fields. This includes marking a
              field as "reserved" in the proto file, this will also break reading the yaml.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.EnvironmentAutomationService/UpsertAutomationsFile",
            body=await async_maybe_transform(
                {
                    "automations_file": automations_file,
                    "environment_id": environment_id,
                },
                automation_upsert_params.AutomationUpsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutomationUpsertResponse,
        )


class AutomationsResourceWithRawResponse:
    def __init__(self, automations: AutomationsResource) -> None:
        self._automations = automations

        self.upsert = to_raw_response_wrapper(
            automations.upsert,
        )

    @cached_property
    def services(self) -> ServicesResourceWithRawResponse:
        return ServicesResourceWithRawResponse(self._automations.services)

    @cached_property
    def tasks(self) -> TasksResourceWithRawResponse:
        return TasksResourceWithRawResponse(self._automations.tasks)


class AsyncAutomationsResourceWithRawResponse:
    def __init__(self, automations: AsyncAutomationsResource) -> None:
        self._automations = automations

        self.upsert = async_to_raw_response_wrapper(
            automations.upsert,
        )

    @cached_property
    def services(self) -> AsyncServicesResourceWithRawResponse:
        return AsyncServicesResourceWithRawResponse(self._automations.services)

    @cached_property
    def tasks(self) -> AsyncTasksResourceWithRawResponse:
        return AsyncTasksResourceWithRawResponse(self._automations.tasks)


class AutomationsResourceWithStreamingResponse:
    def __init__(self, automations: AutomationsResource) -> None:
        self._automations = automations

        self.upsert = to_streamed_response_wrapper(
            automations.upsert,
        )

    @cached_property
    def services(self) -> ServicesResourceWithStreamingResponse:
        return ServicesResourceWithStreamingResponse(self._automations.services)

    @cached_property
    def tasks(self) -> TasksResourceWithStreamingResponse:
        return TasksResourceWithStreamingResponse(self._automations.tasks)


class AsyncAutomationsResourceWithStreamingResponse:
    def __init__(self, automations: AsyncAutomationsResource) -> None:
        self._automations = automations

        self.upsert = async_to_streamed_response_wrapper(
            automations.upsert,
        )

    @cached_property
    def services(self) -> AsyncServicesResourceWithStreamingResponse:
        return AsyncServicesResourceWithStreamingResponse(self._automations.services)

    @cached_property
    def tasks(self) -> AsyncTasksResourceWithStreamingResponse:
        return AsyncTasksResourceWithStreamingResponse(self._automations.tasks)
