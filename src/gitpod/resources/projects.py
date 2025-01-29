# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal

import httpx

from ..types import (
    project_create_params,
    project_retrieve_params,
    project_create_from_environment_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    is_given,
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
from ..types.project_create_response import ProjectCreateResponse
from ..types.project_retrieve_response import ProjectRetrieveResponse
from ..types.project_create_from_environment_response import ProjectCreateFromEnvironmentResponse

__all__ = ["ProjectsResource", "AsyncProjectsResource"]


class ProjectsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return ProjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return ProjectsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        environment_class: Union[object, object, object],
        initializer: project_create_params.Initializer,
        connect_protocol_version: Literal[1],
        automations_file_path: str | NotGiven = NOT_GIVEN,
        devcontainer_file_path: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectCreateResponse:
        """
        CreateProject creates a new Project.

        Args:
          initializer: EnvironmentInitializer specifies how an environment is to be initialized

          connect_protocol_version: Define the version of the Connect protocol

          automations_file_path: automations_file_path is the path to the automations file relative to the repo
              root path must not be absolute (start with a /):

              ```
              this.matches("^$|^[^/].*")
              ```

          devcontainer_file_path: devcontainer_file_path is the path to the devcontainer file relative to the repo
              root path must not be absolute (start with a /):

              ```
              this.matches("^$|^[^/].*")
              ```

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
            "/gitpod.v1.ProjectService/CreateProject",
            body=maybe_transform(
                {
                    "environment_class": environment_class,
                    "initializer": initializer,
                    "automations_file_path": automations_file_path,
                    "devcontainer_file_path": devcontainer_file_path,
                    "name": name,
                },
                project_create_params.ProjectCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectCreateResponse,
        )

    def retrieve(
        self,
        *,
        connect_protocol_version: Literal[1],
        project_id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectRetrieveResponse:
        """
        GetProject retrieves a single Project.

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          project_id: project_id specifies the project identifier

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
            "/gitpod.v1.ProjectService/GetProject",
            body=maybe_transform({"project_id": project_id}, project_retrieve_params.ProjectRetrieveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectRetrieveResponse,
        )

    def create_from_environment(
        self,
        *,
        connect_protocol_version: Literal[1],
        environment_id: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectCreateFromEnvironmentResponse:
        """
        CreateProject creates a new Project using an environment as template.

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          environment_id: environment_id specifies the environment identifier

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
            "/gitpod.v1.ProjectService/CreateProjectFromEnvironment",
            body=maybe_transform(
                {
                    "environment_id": environment_id,
                    "name": name,
                },
                project_create_from_environment_params.ProjectCreateFromEnvironmentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectCreateFromEnvironmentResponse,
        )


class AsyncProjectsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return AsyncProjectsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        environment_class: Union[object, object, object],
        initializer: project_create_params.Initializer,
        connect_protocol_version: Literal[1],
        automations_file_path: str | NotGiven = NOT_GIVEN,
        devcontainer_file_path: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectCreateResponse:
        """
        CreateProject creates a new Project.

        Args:
          initializer: EnvironmentInitializer specifies how an environment is to be initialized

          connect_protocol_version: Define the version of the Connect protocol

          automations_file_path: automations_file_path is the path to the automations file relative to the repo
              root path must not be absolute (start with a /):

              ```
              this.matches("^$|^[^/].*")
              ```

          devcontainer_file_path: devcontainer_file_path is the path to the devcontainer file relative to the repo
              root path must not be absolute (start with a /):

              ```
              this.matches("^$|^[^/].*")
              ```

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
            "/gitpod.v1.ProjectService/CreateProject",
            body=await async_maybe_transform(
                {
                    "environment_class": environment_class,
                    "initializer": initializer,
                    "automations_file_path": automations_file_path,
                    "devcontainer_file_path": devcontainer_file_path,
                    "name": name,
                },
                project_create_params.ProjectCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectCreateResponse,
        )

    async def retrieve(
        self,
        *,
        connect_protocol_version: Literal[1],
        project_id: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectRetrieveResponse:
        """
        GetProject retrieves a single Project.

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          project_id: project_id specifies the project identifier

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
            "/gitpod.v1.ProjectService/GetProject",
            body=await async_maybe_transform({"project_id": project_id}, project_retrieve_params.ProjectRetrieveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectRetrieveResponse,
        )

    async def create_from_environment(
        self,
        *,
        connect_protocol_version: Literal[1],
        environment_id: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        connect_timeout_ms: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectCreateFromEnvironmentResponse:
        """
        CreateProject creates a new Project using an environment as template.

        Args:
          connect_protocol_version: Define the version of the Connect protocol

          environment_id: environment_id specifies the environment identifier

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
            "/gitpod.v1.ProjectService/CreateProjectFromEnvironment",
            body=await async_maybe_transform(
                {
                    "environment_id": environment_id,
                    "name": name,
                },
                project_create_from_environment_params.ProjectCreateFromEnvironmentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectCreateFromEnvironmentResponse,
        )


class ProjectsResourceWithRawResponse:
    def __init__(self, projects: ProjectsResource) -> None:
        self._projects = projects

        self.create = to_raw_response_wrapper(
            projects.create,
        )
        self.retrieve = to_raw_response_wrapper(
            projects.retrieve,
        )
        self.create_from_environment = to_raw_response_wrapper(
            projects.create_from_environment,
        )


class AsyncProjectsResourceWithRawResponse:
    def __init__(self, projects: AsyncProjectsResource) -> None:
        self._projects = projects

        self.create = async_to_raw_response_wrapper(
            projects.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            projects.retrieve,
        )
        self.create_from_environment = async_to_raw_response_wrapper(
            projects.create_from_environment,
        )


class ProjectsResourceWithStreamingResponse:
    def __init__(self, projects: ProjectsResource) -> None:
        self._projects = projects

        self.create = to_streamed_response_wrapper(
            projects.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            projects.retrieve,
        )
        self.create_from_environment = to_streamed_response_wrapper(
            projects.create_from_environment,
        )


class AsyncProjectsResourceWithStreamingResponse:
    def __init__(self, projects: AsyncProjectsResource) -> None:
        self._projects = projects

        self.create = async_to_streamed_response_wrapper(
            projects.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            projects.retrieve,
        )
        self.create_from_environment = async_to_streamed_response_wrapper(
            projects.create_from_environment,
        )
