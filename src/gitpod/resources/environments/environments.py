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
        """
        CreateEnvironment creates a new environment and starts it.

        The `class` field must be a valid environment class ID. You can find a list of
        available environment classes with the `ListEnvironmentClasses` method.

        ### Examples

        - from context URL:

          Creates an environment from a context URL, e.g. a GitHub repository.

          ```yaml
          spec:
            machine:
              class: "61000000-0000-0000-0000-000000000000"
            content:
              initializer:
                specs:
                  - contextUrl:
                      url: "https://github.com/gitpod-io/gitpod"
          ```

        - from Git repository:

          Creates an environment from a Git repository directly. While less convenient,
          this is useful if you want to specify a specific branch, commit, etc.

          ```yaml
          spec:
            machine:
              class: "61000000-0000-0000-0000-000000000000"
            content:
              initializer:
                specs:
                  - git:
                      remoteUri: "https://github.com/gitpod-io/gitpod"
                      cloneTarget: "main"
                      targetMode: "CLONE_TARGET_MODE_REMOTE_BRANCH"
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
        environment_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnvironmentRetrieveResponse:
        """
        GetEnvironment returns a single environment.

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
        UpdateEnvironment updates the environment partially.

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
        ListEnvironments returns a list of environments that match the query.

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
        """DeleteEnvironment deletes an environment.

        When the environment is running, it
        will be stopped as well. Deleted environments cannot be started again.

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
        CreateAbdStartEnvironmentFromProject creates a new environment from a project
        and starts it.

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
        CreateEnvironmentLogsToken creates a token that can be used to access the logs
        of an environment.

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
        MarkEnvironmentActive allows tools to signal activity for an environment.

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
        """StartEnvironment starts an environment.

        This function is idempotent, i.e. if the
        environment is already running no error is returned.

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
        StopEnvironment stops a running environment.

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
        """
        CreateEnvironment creates a new environment and starts it.

        The `class` field must be a valid environment class ID. You can find a list of
        available environment classes with the `ListEnvironmentClasses` method.

        ### Examples

        - from context URL:

          Creates an environment from a context URL, e.g. a GitHub repository.

          ```yaml
          spec:
            machine:
              class: "61000000-0000-0000-0000-000000000000"
            content:
              initializer:
                specs:
                  - contextUrl:
                      url: "https://github.com/gitpod-io/gitpod"
          ```

        - from Git repository:

          Creates an environment from a Git repository directly. While less convenient,
          this is useful if you want to specify a specific branch, commit, etc.

          ```yaml
          spec:
            machine:
              class: "61000000-0000-0000-0000-000000000000"
            content:
              initializer:
                specs:
                  - git:
                      remoteUri: "https://github.com/gitpod-io/gitpod"
                      cloneTarget: "main"
                      targetMode: "CLONE_TARGET_MODE_REMOTE_BRANCH"
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
        environment_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnvironmentRetrieveResponse:
        """
        GetEnvironment returns a single environment.

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
        UpdateEnvironment updates the environment partially.

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
        ListEnvironments returns a list of environments that match the query.

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
        """DeleteEnvironment deletes an environment.

        When the environment is running, it
        will be stopped as well. Deleted environments cannot be started again.

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
        CreateAbdStartEnvironmentFromProject creates a new environment from a project
        and starts it.

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
        CreateEnvironmentLogsToken creates a token that can be used to access the logs
        of an environment.

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
        MarkEnvironmentActive allows tools to signal activity for an environment.

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
        """StartEnvironment starts an environment.

        This function is idempotent, i.e. if the
        environment is already running no error is returned.

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
        StopEnvironment stops a running environment.

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
