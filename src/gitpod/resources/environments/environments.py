# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...types import (
    environment_list_params,
    environment_stop_params,
    environment_start_params,
    environment_create_params,
    environment_delete_params,
    environment_update_params,
    environment_retrieve_params,
    environment_mark_active_params,
    environment_create_logs_token_params,
    environment_create_from_project_params,
)
from .classes import (
    ClassesResource,
    AsyncClassesResource,
    ClassesResourceWithRawResponse,
    AsyncClassesResourceWithRawResponse,
    ClassesResourceWithStreamingResponse,
    AsyncClassesResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
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
from ...pagination import SyncEnvironmentsPage, AsyncEnvironmentsPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.environment import Environment
from .automations.automations import (
    AutomationsResource,
    AsyncAutomationsResource,
    AutomationsResourceWithRawResponse,
    AsyncAutomationsResourceWithRawResponse,
    AutomationsResourceWithStreamingResponse,
    AsyncAutomationsResourceWithStreamingResponse,
)
from ...types.environment_spec_param import EnvironmentSpecParam
from ...types.environment_create_response import EnvironmentCreateResponse
from ...types.environment_retrieve_response import EnvironmentRetrieveResponse
from ...types.environment_activity_signal_param import EnvironmentActivitySignalParam
from ...types.environment_create_logs_token_response import EnvironmentCreateLogsTokenResponse
from ...types.environment_create_from_project_response import EnvironmentCreateFromProjectResponse

__all__ = ["EnvironmentsResource", "AsyncEnvironmentsResource"]


class EnvironmentsResource(SyncAPIResource):
    @cached_property
    def automations(self) -> AutomationsResource:
        return AutomationsResource(self._client)

    @cached_property
    def classes(self) -> ClassesResource:
        return ClassesResource(self._client)

    @cached_property
    def with_raw_response(self) -> EnvironmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return EnvironmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EnvironmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return EnvironmentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        spec: EnvironmentSpecParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnvironmentCreateResponse:
        """Creates a development environment from a context URL (e.g.

        Git repository) and
        starts it.

        The `class` field must be a valid environment class ID. You can find a list of
        available environment classes with the `ListEnvironmentClasses` method.

        ### Examples

        - Create from context URL:

          Creates an environment from a Git repository URL with default settings.

          ```yaml
          spec:
            machine:
              class: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
            content:
              initializer:
                specs:
                  - contextUrl:
                      url: "https://github.com/gitpod-io/gitpod"
          ```

        - Create from Git repository:

          Creates an environment from a Git repository with specific branch targeting.

          ```yaml
          spec:
            machine:
              class: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
            content:
              initializer:
                specs:
                  - git:
                      remoteUri: "https://github.com/gitpod-io/gitpod"
                      cloneTarget: "main"
                      targetMode: "CLONE_TARGET_MODE_REMOTE_BRANCH"
          ```

        - Create with custom timeout and ports:

          Creates an environment with custom inactivity timeout and exposed port
          configuration.

          ```yaml
          spec:
            machine:
              class: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
            content:
              initializer:
                specs:
                  - contextUrl:
                      url: "https://github.com/gitpod-io/gitpod"
            timeout:
              disconnected: "7200s" # 2 hours in seconds
            ports:
              - port: 3000
                admission: "ADMISSION_LEVEL_EVERYONE"
                name: "Web App"
          ```

        Args:
          spec: EnvironmentSpec specifies the configuration of an environment for an environment
              start

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.EnvironmentService/CreateEnvironment",
            body=maybe_transform({"spec": spec}, environment_create_params.EnvironmentCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvironmentCreateResponse,
        )

    def retrieve(
        self,
        *,
        environment_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnvironmentRetrieveResponse:
        """
        Gets details about a specific environment including its status, configuration,
        and context URL.

        Use this method to:

        - Check if an environment is ready to use
        - Get connection details for IDE and exposed ports
        - Monitor environment health and resource usage
        - Debug environment setup issues

        ### Examples

        - Get environment details:

          Retrieves detailed information about a specific environment using its unique
          identifier.

          ```yaml
          environmentId: "07e03a28-65a5-4d98-b532-8ea67b188048"
          ```

        Args:
          environment_id: environment_id specifies the environment to get

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.EnvironmentService/GetEnvironment",
            body=maybe_transform(
                {"environment_id": environment_id}, environment_retrieve_params.EnvironmentRetrieveParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvironmentRetrieveResponse,
        )

    def update(
        self,
        *,
        environment_id: str | NotGiven = NOT_GIVEN,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        spec: Optional[environment_update_params.Spec] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Updates an environment's configuration while it is running.

        Updates are limited to:

        - Git credentials (username, email)
        - SSH public keys
        - Content initialization
        - Port configurations
        - Automation files
        - Environment timeouts

        ### Examples

        - Update Git credentials:

          Updates the Git configuration for the environment.

          ```yaml
          environmentId: "07e03a28-65a5-4d98-b532-8ea67b188048"
          spec:
            content:
              gitUsername: "example-user"
              gitEmail: "user@example.com"
          ```

        - Add SSH public key:

          Adds a new SSH public key for authentication.

          ```yaml
          environmentId: "07e03a28-65a5-4d98-b532-8ea67b188048"
          spec:
            sshPublicKeys:
              - id: "0194b7c1-c954-718d-91a4-9a742aa5fc11"
                value: "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAI..."
          ```

        - Update content session:

          Updates the content session identifier for the environment.

          ```yaml
          environmentId: "07e03a28-65a5-4d98-b532-8ea67b188048"
          spec:
            content:
              session: "0194b7c1-c954-718d-91a4-9a742aa5fc11"
          ```

        Note: Machine class changes require stopping the environment and creating a new
        one.

        Args:
          environment_id: environment_id specifies which environment should be updated.

              +required

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.EnvironmentService/UpdateEnvironment",
            body=maybe_transform(
                {
                    "environment_id": environment_id,
                    "metadata": metadata,
                    "spec": spec,
                },
                environment_update_params.EnvironmentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def list(
        self,
        *,
        token: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        filter: environment_list_params.Filter | NotGiven = NOT_GIVEN,
        pagination: environment_list_params.Pagination | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncEnvironmentsPage[Environment]:
        """
        Lists all environments matching the specified criteria.

        Use this method to find and monitor environments across your organization.
        Results are ordered by creation time with newest environments first.

        ### Examples

        - List running environments for a project:

          Retrieves all running environments for a specific project with pagination.

          ```yaml
          filter:
            statusPhases: ["ENVIRONMENT_PHASE_RUNNING"]
            projectIds: ["b0e12f6c-4c67-429d-a4a6-d9838b5da047"]
          pagination:
            pageSize: 10
          ```

        - List all environments for a specific runner:

          Filters environments by runner ID and creator ID.

          ```yaml
          filter:
            runnerIds: ["e6aa9c54-89d3-42c1-ac31-bd8d8f1concentrate"]
            creatorIds: ["f53d2330-3795-4c5d-a1f3-453121af9c60"]
          ```

        - List stopped and deleted environments:

          Retrieves all environments in stopped or deleted state.

          ```yaml
          filter:
            statusPhases: ["ENVIRONMENT_PHASE_STOPPED", "ENVIRONMENT_PHASE_DELETED"]
          ```

        Args:
          pagination: pagination contains the pagination options for listing environments

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.EnvironmentService/ListEnvironments",
            page=SyncEnvironmentsPage[Environment],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                environment_list_params.EnvironmentListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "token": token,
                        "page_size": page_size,
                    },
                    environment_list_params.EnvironmentListParams,
                ),
            ),
            model=Environment,
            method="post",
        )

    def delete(
        self,
        *,
        environment_id: str | NotGiven = NOT_GIVEN,
        force: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Permanently deletes an environment.

        Running environments are automatically stopped before deletion. If force is
        true, the environment is deleted immediately without graceful shutdown.

        ### Examples

        - Delete with graceful shutdown:

          Deletes an environment after gracefully stopping it.

          ```yaml
          environmentId: "07e03a28-65a5-4d98-b532-8ea67b188048"
          force: false
          ```

        - Force delete:

          Immediately deletes an environment without waiting for graceful shutdown.

          ```yaml
          environmentId: "07e03a28-65a5-4d98-b532-8ea67b188048"
          force: true
          ```

        Args:
          environment_id: environment_id specifies the environment that is going to delete.

              +required

          force: force indicates whether the environment should be deleted forcefully When force
              deleting an Environment, the Environment is removed immediately and environment
              lifecycle is not respected. Force deleting can result in data loss on the
              environment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.EnvironmentService/DeleteEnvironment",
            body=maybe_transform(
                {
                    "environment_id": environment_id,
                    "force": force,
                },
                environment_delete_params.EnvironmentDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def create_from_project(
        self,
        *,
        project_id: str | NotGiven = NOT_GIVEN,
        spec: EnvironmentSpecParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnvironmentCreateFromProjectResponse:
        """
        Creates an environment from an existing project configuration and starts it.

        This method uses project settings as defaults but allows overriding specific
        configurations. Project settings take precedence over default configurations,
        while custom specifications in the request override project settings.

        ### Examples

        - Create with project defaults:

          Creates an environment using all default settings from the project
          configuration.

          ```yaml
          projectId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          ```

        - Create with custom compute resources:

          Creates an environment from project with custom machine class and timeout
          settings.

          ```yaml
          projectId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          spec:
            machine:
              class: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
            timeout:
              disconnected: "14400s" # 4 hours in seconds
          ```

        Args:
          spec: EnvironmentSpec specifies the configuration of an environment for an environment
              start

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.EnvironmentService/CreateEnvironmentFromProject",
            body=maybe_transform(
                {
                    "project_id": project_id,
                    "spec": spec,
                },
                environment_create_from_project_params.EnvironmentCreateFromProjectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvironmentCreateFromProjectResponse,
        )

    def create_logs_token(
        self,
        *,
        environment_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnvironmentCreateLogsTokenResponse:
        """
        Creates an access token for retrieving environment logs.

        Generated tokens are valid for one hour and provide read-only access to the
        environment's logs.

        ### Examples

        - Generate logs token:

          Creates a temporary access token for retrieving environment logs.

          ```yaml
          environmentId: "07e03a28-65a5-4d98-b532-8ea67b188048"
          ```

        Args:
          environment_id: environment_id specifies the environment for which the logs token should be
              created.

              +required

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.EnvironmentService/CreateEnvironmentLogsToken",
            body=maybe_transform(
                {"environment_id": environment_id},
                environment_create_logs_token_params.EnvironmentCreateLogsTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvironmentCreateLogsTokenResponse,
        )

    def mark_active(
        self,
        *,
        activity_signal: EnvironmentActivitySignalParam | NotGiven = NOT_GIVEN,
        environment_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Records environment activity to prevent automatic shutdown.

        Activity signals should be sent every 5 minutes while the environment is
        actively being used. The source must be between 3-80 characters.

        ### Examples

        - Signal VS Code activity:

          Records VS Code editor activity to prevent environment shutdown.

          ```yaml
          environmentId: "07e03a28-65a5-4d98-b532-8ea67b188048"
          activitySignal:
            source: "VS Code"
            timestamp: "2025-02-12T14:30:00Z"
          ```

        Args:
          activity_signal: EnvironmentActivitySignal used to signal activity for an environment.

          environment_id: The ID of the environment to update activity for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.EnvironmentService/MarkEnvironmentActive",
            body=maybe_transform(
                {
                    "activity_signal": activity_signal,
                    "environment_id": environment_id,
                },
                environment_mark_active_params.EnvironmentMarkActiveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def start(
        self,
        *,
        environment_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Starts a stopped environment.

        Use this method to resume work on a previously stopped environment. The
        environment retains its configuration and workspace content from when it was
        stopped.

        ### Examples

        - Start an environment:

          Resumes a previously stopped environment with its existing configuration.

          ```yaml
          environmentId: "07e03a28-65a5-4d98-b532-8ea67b188048"
          ```

        Args:
          environment_id: environment_id specifies which environment should be started.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.EnvironmentService/StartEnvironment",
            body=maybe_transform({"environment_id": environment_id}, environment_start_params.EnvironmentStartParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def stop(
        self,
        *,
        environment_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Stops a running environment.

        Use this method to pause work while preserving the environment's state. The
        environment can be resumed later using StartEnvironment.

        ### Examples

        - Stop an environment:

          Gracefully stops a running environment while preserving its state.

          ```yaml
          environmentId: "07e03a28-65a5-4d98-b532-8ea67b188048"
          ```

        Args:
          environment_id: environment_id specifies which environment should be stopped.

              +required

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.EnvironmentService/StopEnvironment",
            body=maybe_transform({"environment_id": environment_id}, environment_stop_params.EnvironmentStopParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncEnvironmentsResource(AsyncAPIResource):
    @cached_property
    def automations(self) -> AsyncAutomationsResource:
        return AsyncAutomationsResource(self._client)

    @cached_property
    def classes(self) -> AsyncClassesResource:
        return AsyncClassesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEnvironmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEnvironmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEnvironmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return AsyncEnvironmentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        spec: EnvironmentSpecParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnvironmentCreateResponse:
        """Creates a development environment from a context URL (e.g.

        Git repository) and
        starts it.

        The `class` field must be a valid environment class ID. You can find a list of
        available environment classes with the `ListEnvironmentClasses` method.

        ### Examples

        - Create from context URL:

          Creates an environment from a Git repository URL with default settings.

          ```yaml
          spec:
            machine:
              class: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
            content:
              initializer:
                specs:
                  - contextUrl:
                      url: "https://github.com/gitpod-io/gitpod"
          ```

        - Create from Git repository:

          Creates an environment from a Git repository with specific branch targeting.

          ```yaml
          spec:
            machine:
              class: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
            content:
              initializer:
                specs:
                  - git:
                      remoteUri: "https://github.com/gitpod-io/gitpod"
                      cloneTarget: "main"
                      targetMode: "CLONE_TARGET_MODE_REMOTE_BRANCH"
          ```

        - Create with custom timeout and ports:

          Creates an environment with custom inactivity timeout and exposed port
          configuration.

          ```yaml
          spec:
            machine:
              class: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
            content:
              initializer:
                specs:
                  - contextUrl:
                      url: "https://github.com/gitpod-io/gitpod"
            timeout:
              disconnected: "7200s" # 2 hours in seconds
            ports:
              - port: 3000
                admission: "ADMISSION_LEVEL_EVERYONE"
                name: "Web App"
          ```

        Args:
          spec: EnvironmentSpec specifies the configuration of an environment for an environment
              start

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.EnvironmentService/CreateEnvironment",
            body=await async_maybe_transform({"spec": spec}, environment_create_params.EnvironmentCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvironmentCreateResponse,
        )

    async def retrieve(
        self,
        *,
        environment_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnvironmentRetrieveResponse:
        """
        Gets details about a specific environment including its status, configuration,
        and context URL.

        Use this method to:

        - Check if an environment is ready to use
        - Get connection details for IDE and exposed ports
        - Monitor environment health and resource usage
        - Debug environment setup issues

        ### Examples

        - Get environment details:

          Retrieves detailed information about a specific environment using its unique
          identifier.

          ```yaml
          environmentId: "07e03a28-65a5-4d98-b532-8ea67b188048"
          ```

        Args:
          environment_id: environment_id specifies the environment to get

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.EnvironmentService/GetEnvironment",
            body=await async_maybe_transform(
                {"environment_id": environment_id}, environment_retrieve_params.EnvironmentRetrieveParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvironmentRetrieveResponse,
        )

    async def update(
        self,
        *,
        environment_id: str | NotGiven = NOT_GIVEN,
        metadata: Optional[object] | NotGiven = NOT_GIVEN,
        spec: Optional[environment_update_params.Spec] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Updates an environment's configuration while it is running.

        Updates are limited to:

        - Git credentials (username, email)
        - SSH public keys
        - Content initialization
        - Port configurations
        - Automation files
        - Environment timeouts

        ### Examples

        - Update Git credentials:

          Updates the Git configuration for the environment.

          ```yaml
          environmentId: "07e03a28-65a5-4d98-b532-8ea67b188048"
          spec:
            content:
              gitUsername: "example-user"
              gitEmail: "user@example.com"
          ```

        - Add SSH public key:

          Adds a new SSH public key for authentication.

          ```yaml
          environmentId: "07e03a28-65a5-4d98-b532-8ea67b188048"
          spec:
            sshPublicKeys:
              - id: "0194b7c1-c954-718d-91a4-9a742aa5fc11"
                value: "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAI..."
          ```

        - Update content session:

          Updates the content session identifier for the environment.

          ```yaml
          environmentId: "07e03a28-65a5-4d98-b532-8ea67b188048"
          spec:
            content:
              session: "0194b7c1-c954-718d-91a4-9a742aa5fc11"
          ```

        Note: Machine class changes require stopping the environment and creating a new
        one.

        Args:
          environment_id: environment_id specifies which environment should be updated.

              +required

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.EnvironmentService/UpdateEnvironment",
            body=await async_maybe_transform(
                {
                    "environment_id": environment_id,
                    "metadata": metadata,
                    "spec": spec,
                },
                environment_update_params.EnvironmentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def list(
        self,
        *,
        token: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        filter: environment_list_params.Filter | NotGiven = NOT_GIVEN,
        pagination: environment_list_params.Pagination | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Environment, AsyncEnvironmentsPage[Environment]]:
        """
        Lists all environments matching the specified criteria.

        Use this method to find and monitor environments across your organization.
        Results are ordered by creation time with newest environments first.

        ### Examples

        - List running environments for a project:

          Retrieves all running environments for a specific project with pagination.

          ```yaml
          filter:
            statusPhases: ["ENVIRONMENT_PHASE_RUNNING"]
            projectIds: ["b0e12f6c-4c67-429d-a4a6-d9838b5da047"]
          pagination:
            pageSize: 10
          ```

        - List all environments for a specific runner:

          Filters environments by runner ID and creator ID.

          ```yaml
          filter:
            runnerIds: ["e6aa9c54-89d3-42c1-ac31-bd8d8f1concentrate"]
            creatorIds: ["f53d2330-3795-4c5d-a1f3-453121af9c60"]
          ```

        - List stopped and deleted environments:

          Retrieves all environments in stopped or deleted state.

          ```yaml
          filter:
            statusPhases: ["ENVIRONMENT_PHASE_STOPPED", "ENVIRONMENT_PHASE_DELETED"]
          ```

        Args:
          pagination: pagination contains the pagination options for listing environments

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.EnvironmentService/ListEnvironments",
            page=AsyncEnvironmentsPage[Environment],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                environment_list_params.EnvironmentListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "token": token,
                        "page_size": page_size,
                    },
                    environment_list_params.EnvironmentListParams,
                ),
            ),
            model=Environment,
            method="post",
        )

    async def delete(
        self,
        *,
        environment_id: str | NotGiven = NOT_GIVEN,
        force: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Permanently deletes an environment.

        Running environments are automatically stopped before deletion. If force is
        true, the environment is deleted immediately without graceful shutdown.

        ### Examples

        - Delete with graceful shutdown:

          Deletes an environment after gracefully stopping it.

          ```yaml
          environmentId: "07e03a28-65a5-4d98-b532-8ea67b188048"
          force: false
          ```

        - Force delete:

          Immediately deletes an environment without waiting for graceful shutdown.

          ```yaml
          environmentId: "07e03a28-65a5-4d98-b532-8ea67b188048"
          force: true
          ```

        Args:
          environment_id: environment_id specifies the environment that is going to delete.

              +required

          force: force indicates whether the environment should be deleted forcefully When force
              deleting an Environment, the Environment is removed immediately and environment
              lifecycle is not respected. Force deleting can result in data loss on the
              environment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.EnvironmentService/DeleteEnvironment",
            body=await async_maybe_transform(
                {
                    "environment_id": environment_id,
                    "force": force,
                },
                environment_delete_params.EnvironmentDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def create_from_project(
        self,
        *,
        project_id: str | NotGiven = NOT_GIVEN,
        spec: EnvironmentSpecParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnvironmentCreateFromProjectResponse:
        """
        Creates an environment from an existing project configuration and starts it.

        This method uses project settings as defaults but allows overriding specific
        configurations. Project settings take precedence over default configurations,
        while custom specifications in the request override project settings.

        ### Examples

        - Create with project defaults:

          Creates an environment using all default settings from the project
          configuration.

          ```yaml
          projectId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          ```

        - Create with custom compute resources:

          Creates an environment from project with custom machine class and timeout
          settings.

          ```yaml
          projectId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          spec:
            machine:
              class: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
            timeout:
              disconnected: "14400s" # 4 hours in seconds
          ```

        Args:
          spec: EnvironmentSpec specifies the configuration of an environment for an environment
              start

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.EnvironmentService/CreateEnvironmentFromProject",
            body=await async_maybe_transform(
                {
                    "project_id": project_id,
                    "spec": spec,
                },
                environment_create_from_project_params.EnvironmentCreateFromProjectParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvironmentCreateFromProjectResponse,
        )

    async def create_logs_token(
        self,
        *,
        environment_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnvironmentCreateLogsTokenResponse:
        """
        Creates an access token for retrieving environment logs.

        Generated tokens are valid for one hour and provide read-only access to the
        environment's logs.

        ### Examples

        - Generate logs token:

          Creates a temporary access token for retrieving environment logs.

          ```yaml
          environmentId: "07e03a28-65a5-4d98-b532-8ea67b188048"
          ```

        Args:
          environment_id: environment_id specifies the environment for which the logs token should be
              created.

              +required

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.EnvironmentService/CreateEnvironmentLogsToken",
            body=await async_maybe_transform(
                {"environment_id": environment_id},
                environment_create_logs_token_params.EnvironmentCreateLogsTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvironmentCreateLogsTokenResponse,
        )

    async def mark_active(
        self,
        *,
        activity_signal: EnvironmentActivitySignalParam | NotGiven = NOT_GIVEN,
        environment_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Records environment activity to prevent automatic shutdown.

        Activity signals should be sent every 5 minutes while the environment is
        actively being used. The source must be between 3-80 characters.

        ### Examples

        - Signal VS Code activity:

          Records VS Code editor activity to prevent environment shutdown.

          ```yaml
          environmentId: "07e03a28-65a5-4d98-b532-8ea67b188048"
          activitySignal:
            source: "VS Code"
            timestamp: "2025-02-12T14:30:00Z"
          ```

        Args:
          activity_signal: EnvironmentActivitySignal used to signal activity for an environment.

          environment_id: The ID of the environment to update activity for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.EnvironmentService/MarkEnvironmentActive",
            body=await async_maybe_transform(
                {
                    "activity_signal": activity_signal,
                    "environment_id": environment_id,
                },
                environment_mark_active_params.EnvironmentMarkActiveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def start(
        self,
        *,
        environment_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Starts a stopped environment.

        Use this method to resume work on a previously stopped environment. The
        environment retains its configuration and workspace content from when it was
        stopped.

        ### Examples

        - Start an environment:

          Resumes a previously stopped environment with its existing configuration.

          ```yaml
          environmentId: "07e03a28-65a5-4d98-b532-8ea67b188048"
          ```

        Args:
          environment_id: environment_id specifies which environment should be started.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.EnvironmentService/StartEnvironment",
            body=await async_maybe_transform(
                {"environment_id": environment_id}, environment_start_params.EnvironmentStartParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def stop(
        self,
        *,
        environment_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Stops a running environment.

        Use this method to pause work while preserving the environment's state. The
        environment can be resumed later using StartEnvironment.

        ### Examples

        - Stop an environment:

          Gracefully stops a running environment while preserving its state.

          ```yaml
          environmentId: "07e03a28-65a5-4d98-b532-8ea67b188048"
          ```

        Args:
          environment_id: environment_id specifies which environment should be stopped.

              +required

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.EnvironmentService/StopEnvironment",
            body=await async_maybe_transform(
                {"environment_id": environment_id}, environment_stop_params.EnvironmentStopParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class EnvironmentsResourceWithRawResponse:
    def __init__(self, environments: EnvironmentsResource) -> None:
        self._environments = environments

        self.create = to_raw_response_wrapper(
            environments.create,
        )
        self.retrieve = to_raw_response_wrapper(
            environments.retrieve,
        )
        self.update = to_raw_response_wrapper(
            environments.update,
        )
        self.list = to_raw_response_wrapper(
            environments.list,
        )
        self.delete = to_raw_response_wrapper(
            environments.delete,
        )
        self.create_from_project = to_raw_response_wrapper(
            environments.create_from_project,
        )
        self.create_logs_token = to_raw_response_wrapper(
            environments.create_logs_token,
        )
        self.mark_active = to_raw_response_wrapper(
            environments.mark_active,
        )
        self.start = to_raw_response_wrapper(
            environments.start,
        )
        self.stop = to_raw_response_wrapper(
            environments.stop,
        )

    @cached_property
    def automations(self) -> AutomationsResourceWithRawResponse:
        return AutomationsResourceWithRawResponse(self._environments.automations)

    @cached_property
    def classes(self) -> ClassesResourceWithRawResponse:
        return ClassesResourceWithRawResponse(self._environments.classes)


class AsyncEnvironmentsResourceWithRawResponse:
    def __init__(self, environments: AsyncEnvironmentsResource) -> None:
        self._environments = environments

        self.create = async_to_raw_response_wrapper(
            environments.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            environments.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            environments.update,
        )
        self.list = async_to_raw_response_wrapper(
            environments.list,
        )
        self.delete = async_to_raw_response_wrapper(
            environments.delete,
        )
        self.create_from_project = async_to_raw_response_wrapper(
            environments.create_from_project,
        )
        self.create_logs_token = async_to_raw_response_wrapper(
            environments.create_logs_token,
        )
        self.mark_active = async_to_raw_response_wrapper(
            environments.mark_active,
        )
        self.start = async_to_raw_response_wrapper(
            environments.start,
        )
        self.stop = async_to_raw_response_wrapper(
            environments.stop,
        )

    @cached_property
    def automations(self) -> AsyncAutomationsResourceWithRawResponse:
        return AsyncAutomationsResourceWithRawResponse(self._environments.automations)

    @cached_property
    def classes(self) -> AsyncClassesResourceWithRawResponse:
        return AsyncClassesResourceWithRawResponse(self._environments.classes)


class EnvironmentsResourceWithStreamingResponse:
    def __init__(self, environments: EnvironmentsResource) -> None:
        self._environments = environments

        self.create = to_streamed_response_wrapper(
            environments.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            environments.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            environments.update,
        )
        self.list = to_streamed_response_wrapper(
            environments.list,
        )
        self.delete = to_streamed_response_wrapper(
            environments.delete,
        )
        self.create_from_project = to_streamed_response_wrapper(
            environments.create_from_project,
        )
        self.create_logs_token = to_streamed_response_wrapper(
            environments.create_logs_token,
        )
        self.mark_active = to_streamed_response_wrapper(
            environments.mark_active,
        )
        self.start = to_streamed_response_wrapper(
            environments.start,
        )
        self.stop = to_streamed_response_wrapper(
            environments.stop,
        )

    @cached_property
    def automations(self) -> AutomationsResourceWithStreamingResponse:
        return AutomationsResourceWithStreamingResponse(self._environments.automations)

    @cached_property
    def classes(self) -> ClassesResourceWithStreamingResponse:
        return ClassesResourceWithStreamingResponse(self._environments.classes)


class AsyncEnvironmentsResourceWithStreamingResponse:
    def __init__(self, environments: AsyncEnvironmentsResource) -> None:
        self._environments = environments

        self.create = async_to_streamed_response_wrapper(
            environments.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            environments.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            environments.update,
        )
        self.list = async_to_streamed_response_wrapper(
            environments.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            environments.delete,
        )
        self.create_from_project = async_to_streamed_response_wrapper(
            environments.create_from_project,
        )
        self.create_logs_token = async_to_streamed_response_wrapper(
            environments.create_logs_token,
        )
        self.mark_active = async_to_streamed_response_wrapper(
            environments.mark_active,
        )
        self.start = async_to_streamed_response_wrapper(
            environments.start,
        )
        self.stop = async_to_streamed_response_wrapper(
            environments.stop,
        )

    @cached_property
    def automations(self) -> AsyncAutomationsResourceWithStreamingResponse:
        return AsyncAutomationsResourceWithStreamingResponse(self._environments.automations)

    @cached_property
    def classes(self) -> AsyncClassesResourceWithStreamingResponse:
        return AsyncClassesResourceWithStreamingResponse(self._environments.classes)
