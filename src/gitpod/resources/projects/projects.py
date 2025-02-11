# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...types import (
    project_list_params,
    project_create_params,
    project_delete_params,
    project_update_params,
    project_retrieve_params,
    project_create_from_environment_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .policies import (
    PoliciesResource,
    AsyncPoliciesResource,
    PoliciesResourceWithRawResponse,
    AsyncPoliciesResourceWithRawResponse,
    PoliciesResourceWithStreamingResponse,
    AsyncPoliciesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncProjectsPage, AsyncProjectsPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.project import Project
from ...types.project_create_response import ProjectCreateResponse
from ...types.project_update_response import ProjectUpdateResponse
from ...types.project_retrieve_response import ProjectRetrieveResponse
from ...types.environment_initializer_param import EnvironmentInitializerParam
from ...types.project_environment_class_param import ProjectEnvironmentClassParam
from ...types.project_create_from_environment_response import ProjectCreateFromEnvironmentResponse

__all__ = ["ProjectsResource", "AsyncProjectsResource"]


class ProjectsResource(SyncAPIResource):
    @cached_property
    def policies(self) -> PoliciesResource:
        return PoliciesResource(self._client)

    @cached_property
    def with_raw_response(self) -> ProjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ProjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return ProjectsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        environment_class: ProjectEnvironmentClassParam,
        initializer: EnvironmentInitializerParam,
        automations_file_path: str | NotGiven = NOT_GIVEN,
        devcontainer_file_path: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
        project_id: str | NotGiven = NOT_GIVEN,
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
          project_id: project_id specifies the project identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.ProjectService/GetProject",
            body=maybe_transform({"project_id": project_id}, project_retrieve_params.ProjectRetrieveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectRetrieveResponse,
        )

    def update(
        self,
        *,
        automations_file_path: Optional[str] | NotGiven = NOT_GIVEN,
        devcontainer_file_path: Optional[str] | NotGiven = NOT_GIVEN,
        environment_class: Optional[ProjectEnvironmentClassParam] | NotGiven = NOT_GIVEN,
        initializer: Optional[EnvironmentInitializerParam] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        project_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectUpdateResponse:
        """
        UpdateProject updates the properties of a Project.

        Args:
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

          initializer: EnvironmentInitializer specifies how an environment is to be initialized

          project_id: project_id specifies the project identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.ProjectService/UpdateProject",
            body=maybe_transform(
                {
                    "automations_file_path": automations_file_path,
                    "devcontainer_file_path": devcontainer_file_path,
                    "environment_class": environment_class,
                    "initializer": initializer,
                    "name": name,
                    "project_id": project_id,
                },
                project_update_params.ProjectUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectUpdateResponse,
        )

    def list(
        self,
        *,
        token: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        pagination: project_list_params.Pagination | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncProjectsPage[Project]:
        """
        ListProjects lists all projects the caller has access to.

        Args:
          pagination: pagination contains the pagination options for listing organizations

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.ProjectService/ListProjects",
            page=SyncProjectsPage[Project],
            body=maybe_transform({"pagination": pagination}, project_list_params.ProjectListParams),
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
                    project_list_params.ProjectListParams,
                ),
            ),
            model=Project,
            method="post",
        )

    def delete(
        self,
        *,
        project_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        DeleteProject deletes the specified project.

        Args:
          project_id: project_id specifies the project identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.ProjectService/DeleteProject",
            body=maybe_transform({"project_id": project_id}, project_delete_params.ProjectDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def create_from_environment(
        self,
        *,
        environment_id: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
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
          environment_id: environment_id specifies the environment identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
    def policies(self) -> AsyncPoliciesResource:
        return AsyncPoliciesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncProjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return AsyncProjectsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        environment_class: ProjectEnvironmentClassParam,
        initializer: EnvironmentInitializerParam,
        automations_file_path: str | NotGiven = NOT_GIVEN,
        devcontainer_file_path: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
        project_id: str | NotGiven = NOT_GIVEN,
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
          project_id: project_id specifies the project identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.ProjectService/GetProject",
            body=await async_maybe_transform({"project_id": project_id}, project_retrieve_params.ProjectRetrieveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectRetrieveResponse,
        )

    async def update(
        self,
        *,
        automations_file_path: Optional[str] | NotGiven = NOT_GIVEN,
        devcontainer_file_path: Optional[str] | NotGiven = NOT_GIVEN,
        environment_class: Optional[ProjectEnvironmentClassParam] | NotGiven = NOT_GIVEN,
        initializer: Optional[EnvironmentInitializerParam] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        project_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProjectUpdateResponse:
        """
        UpdateProject updates the properties of a Project.

        Args:
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

          initializer: EnvironmentInitializer specifies how an environment is to be initialized

          project_id: project_id specifies the project identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.ProjectService/UpdateProject",
            body=await async_maybe_transform(
                {
                    "automations_file_path": automations_file_path,
                    "devcontainer_file_path": devcontainer_file_path,
                    "environment_class": environment_class,
                    "initializer": initializer,
                    "name": name,
                    "project_id": project_id,
                },
                project_update_params.ProjectUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProjectUpdateResponse,
        )

    def list(
        self,
        *,
        token: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        pagination: project_list_params.Pagination | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Project, AsyncProjectsPage[Project]]:
        """
        ListProjects lists all projects the caller has access to.

        Args:
          pagination: pagination contains the pagination options for listing organizations

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.ProjectService/ListProjects",
            page=AsyncProjectsPage[Project],
            body=maybe_transform({"pagination": pagination}, project_list_params.ProjectListParams),
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
                    project_list_params.ProjectListParams,
                ),
            ),
            model=Project,
            method="post",
        )

    async def delete(
        self,
        *,
        project_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        DeleteProject deletes the specified project.

        Args:
          project_id: project_id specifies the project identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.ProjectService/DeleteProject",
            body=await async_maybe_transform({"project_id": project_id}, project_delete_params.ProjectDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def create_from_environment(
        self,
        *,
        environment_id: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
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
          environment_id: environment_id specifies the environment identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
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
        self.update = to_raw_response_wrapper(
            projects.update,
        )
        self.list = to_raw_response_wrapper(
            projects.list,
        )
        self.delete = to_raw_response_wrapper(
            projects.delete,
        )
        self.create_from_environment = to_raw_response_wrapper(
            projects.create_from_environment,
        )

    @cached_property
    def policies(self) -> PoliciesResourceWithRawResponse:
        return PoliciesResourceWithRawResponse(self._projects.policies)


class AsyncProjectsResourceWithRawResponse:
    def __init__(self, projects: AsyncProjectsResource) -> None:
        self._projects = projects

        self.create = async_to_raw_response_wrapper(
            projects.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            projects.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            projects.update,
        )
        self.list = async_to_raw_response_wrapper(
            projects.list,
        )
        self.delete = async_to_raw_response_wrapper(
            projects.delete,
        )
        self.create_from_environment = async_to_raw_response_wrapper(
            projects.create_from_environment,
        )

    @cached_property
    def policies(self) -> AsyncPoliciesResourceWithRawResponse:
        return AsyncPoliciesResourceWithRawResponse(self._projects.policies)


class ProjectsResourceWithStreamingResponse:
    def __init__(self, projects: ProjectsResource) -> None:
        self._projects = projects

        self.create = to_streamed_response_wrapper(
            projects.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            projects.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            projects.update,
        )
        self.list = to_streamed_response_wrapper(
            projects.list,
        )
        self.delete = to_streamed_response_wrapper(
            projects.delete,
        )
        self.create_from_environment = to_streamed_response_wrapper(
            projects.create_from_environment,
        )

    @cached_property
    def policies(self) -> PoliciesResourceWithStreamingResponse:
        return PoliciesResourceWithStreamingResponse(self._projects.policies)


class AsyncProjectsResourceWithStreamingResponse:
    def __init__(self, projects: AsyncProjectsResource) -> None:
        self._projects = projects

        self.create = async_to_streamed_response_wrapper(
            projects.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            projects.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            projects.update,
        )
        self.list = async_to_streamed_response_wrapper(
            projects.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            projects.delete,
        )
        self.create_from_environment = async_to_streamed_response_wrapper(
            projects.create_from_environment,
        )

    @cached_property
    def policies(self) -> AsyncPoliciesResourceWithStreamingResponse:
        return AsyncPoliciesResourceWithStreamingResponse(self._projects.policies)
