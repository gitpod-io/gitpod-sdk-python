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
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
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
from .environment_clases import (
    EnvironmentClasesResource,
    AsyncEnvironmentClasesResource,
    EnvironmentClasesResourceWithRawResponse,
    AsyncEnvironmentClasesResourceWithRawResponse,
    EnvironmentClasesResourceWithStreamingResponse,
    AsyncEnvironmentClasesResourceWithStreamingResponse,
)
from ...types.project_create_response import ProjectCreateResponse
from ...types.project_update_response import ProjectUpdateResponse
from ...types.project_retrieve_response import ProjectRetrieveResponse
from ...types.environment_initializer_param import EnvironmentInitializerParam
from ...types.project_prebuild_configuration_param import ProjectPrebuildConfigurationParam
from ...types.project_create_from_environment_response import ProjectCreateFromEnvironmentResponse

__all__ = ["ProjectsResource", "AsyncProjectsResource"]


class ProjectsResource(SyncAPIResource):
    @cached_property
    def environment_clases(self) -> EnvironmentClasesResource:
        return EnvironmentClasesResource(self._client)

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
        initializer: EnvironmentInitializerParam,
        automations_file_path: str | Omit = omit,
        devcontainer_file_path: str | Omit = omit,
        name: str | Omit = omit,
        prebuild_configuration: ProjectPrebuildConfigurationParam | Omit = omit,
        technical_description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectCreateResponse:
        """
        Creates a new project with specified configuration.

        Use this method to:

        - Set up development projects
        - Configure project environments
        - Define project settings
        - Initialize project content

        ### Examples

        - Create basic project:

          Creates a project with minimal configuration.

          ```yaml
          name: "Web Application"
          initializer:
            specs:
              - git:
                  remoteUri: "https://github.com/org/repo"
          ```

        - Create project with devcontainer:

          Creates a project with custom development container.

          ```yaml
          name: "Backend Service"
          initializer:
            specs:
              - git:
                  remoteUri: "https://github.com/org/backend"
          devcontainerFilePath: ".devcontainer/devcontainer.json"
          automationsFilePath: ".gitpod/automations.yaml"
          ```

        Args:
          initializer: initializer is the content initializer

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

          prebuild_configuration: prebuild_configuration defines how prebuilds are created for this project. If
              not set, prebuilds are disabled for the project.

          technical_description: technical_description is a detailed technical description of the project This
              field is not returned by default in GetProject or ListProjects responses 8KB max

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.ProjectService/CreateProject",
            body=maybe_transform(
                {
                    "initializer": initializer,
                    "automations_file_path": automations_file_path,
                    "devcontainer_file_path": devcontainer_file_path,
                    "name": name,
                    "prebuild_configuration": prebuild_configuration,
                    "technical_description": technical_description,
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
        project_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectRetrieveResponse:
        """
        Gets details about a specific project.

        Use this method to:

        - View project configuration
        - Check project status
        - Get project metadata

        ### Examples

        - Get project details:

          Retrieves information about a specific project.

          ```yaml
          projectId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          ```

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
        automations_file_path: Optional[str] | Omit = omit,
        devcontainer_file_path: Optional[str] | Omit = omit,
        initializer: Optional[EnvironmentInitializerParam] | Omit = omit,
        name: Optional[str] | Omit = omit,
        prebuild_configuration: Optional[ProjectPrebuildConfigurationParam] | Omit = omit,
        project_id: str | Omit = omit,
        technical_description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectUpdateResponse:
        """
        Updates a project's configuration.

        Use this method to:

        - Modify project settings
        - Update environment class
        - Change project name
        - Configure initializers
        - Configure prebuild settings

        ### Examples

        - Update project name:

          Changes the project's display name.

          ```yaml
          projectId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          name: "New Project Name"
          ```

        - Enable prebuilds with daily schedule:

          Configures prebuilds to run daily at 2 AM UTC.

          ```yaml
          projectId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          prebuildConfiguration:
            enabled: true
            environmentClassIds:
              - "b0e12f6c-4c67-429d-a4a6-d9838b5da041"
            timeout: "3600s"
            trigger:
              dailySchedule:
                hourUtc: 2
          ```

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

          initializer: initializer is the content initializer

          prebuild_configuration: prebuild_configuration defines how prebuilds are created for this project. If
              not provided, the existing prebuild configuration is not modified. To disable
              prebuilds, set enabled to false.

          project_id: project_id specifies the project identifier

          technical_description: technical_description is a detailed technical description of the project This
              field is not returned by default in GetProject or ListProjects responses 8KB max

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
                    "initializer": initializer,
                    "name": name,
                    "prebuild_configuration": prebuild_configuration,
                    "project_id": project_id,
                    "technical_description": technical_description,
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
        token: str | Omit = omit,
        page_size: int | Omit = omit,
        filter: project_list_params.Filter | Omit = omit,
        pagination: project_list_params.Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncProjectsPage[Project]:
        """
        Lists projects with optional filtering.

        Use this method to:

        - View all accessible projects
        - Browse project configurations
        - Monitor project status

        ### Examples

        - List projects:

          Shows all projects with pagination.

          ```yaml
          pagination:
            pageSize: 20
          ```

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
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                project_list_params.ProjectListParams,
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
                    project_list_params.ProjectListParams,
                ),
            ),
            model=Project,
            method="post",
        )

    def delete(
        self,
        *,
        project_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Deletes a project permanently.

        Use this method to:

        - Remove unused projects
        - Clean up test projects
        - Delete obsolete configurations

        ### Examples

        - Delete project:

          Permanently removes a project.

          ```yaml
          projectId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          ```

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
        environment_id: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectCreateFromEnvironmentResponse:
        """
        Creates a new project using an existing environment as a template.

        Use this method to:

        - Clone environment configurations
        - Create projects from templates
        - Share environment setups

        ### Examples

        - Create from environment:

          Creates a project based on existing environment.

          ```yaml
          name: "Frontend Project"
          environmentId: "07e03a28-65a5-4d98-b532-8ea67b188048"
          ```

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
    def environment_clases(self) -> AsyncEnvironmentClasesResource:
        return AsyncEnvironmentClasesResource(self._client)

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
        initializer: EnvironmentInitializerParam,
        automations_file_path: str | Omit = omit,
        devcontainer_file_path: str | Omit = omit,
        name: str | Omit = omit,
        prebuild_configuration: ProjectPrebuildConfigurationParam | Omit = omit,
        technical_description: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectCreateResponse:
        """
        Creates a new project with specified configuration.

        Use this method to:

        - Set up development projects
        - Configure project environments
        - Define project settings
        - Initialize project content

        ### Examples

        - Create basic project:

          Creates a project with minimal configuration.

          ```yaml
          name: "Web Application"
          initializer:
            specs:
              - git:
                  remoteUri: "https://github.com/org/repo"
          ```

        - Create project with devcontainer:

          Creates a project with custom development container.

          ```yaml
          name: "Backend Service"
          initializer:
            specs:
              - git:
                  remoteUri: "https://github.com/org/backend"
          devcontainerFilePath: ".devcontainer/devcontainer.json"
          automationsFilePath: ".gitpod/automations.yaml"
          ```

        Args:
          initializer: initializer is the content initializer

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

          prebuild_configuration: prebuild_configuration defines how prebuilds are created for this project. If
              not set, prebuilds are disabled for the project.

          technical_description: technical_description is a detailed technical description of the project This
              field is not returned by default in GetProject or ListProjects responses 8KB max

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.ProjectService/CreateProject",
            body=await async_maybe_transform(
                {
                    "initializer": initializer,
                    "automations_file_path": automations_file_path,
                    "devcontainer_file_path": devcontainer_file_path,
                    "name": name,
                    "prebuild_configuration": prebuild_configuration,
                    "technical_description": technical_description,
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
        project_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectRetrieveResponse:
        """
        Gets details about a specific project.

        Use this method to:

        - View project configuration
        - Check project status
        - Get project metadata

        ### Examples

        - Get project details:

          Retrieves information about a specific project.

          ```yaml
          projectId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          ```

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
        automations_file_path: Optional[str] | Omit = omit,
        devcontainer_file_path: Optional[str] | Omit = omit,
        initializer: Optional[EnvironmentInitializerParam] | Omit = omit,
        name: Optional[str] | Omit = omit,
        prebuild_configuration: Optional[ProjectPrebuildConfigurationParam] | Omit = omit,
        project_id: str | Omit = omit,
        technical_description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectUpdateResponse:
        """
        Updates a project's configuration.

        Use this method to:

        - Modify project settings
        - Update environment class
        - Change project name
        - Configure initializers
        - Configure prebuild settings

        ### Examples

        - Update project name:

          Changes the project's display name.

          ```yaml
          projectId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          name: "New Project Name"
          ```

        - Enable prebuilds with daily schedule:

          Configures prebuilds to run daily at 2 AM UTC.

          ```yaml
          projectId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          prebuildConfiguration:
            enabled: true
            environmentClassIds:
              - "b0e12f6c-4c67-429d-a4a6-d9838b5da041"
            timeout: "3600s"
            trigger:
              dailySchedule:
                hourUtc: 2
          ```

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

          initializer: initializer is the content initializer

          prebuild_configuration: prebuild_configuration defines how prebuilds are created for this project. If
              not provided, the existing prebuild configuration is not modified. To disable
              prebuilds, set enabled to false.

          project_id: project_id specifies the project identifier

          technical_description: technical_description is a detailed technical description of the project This
              field is not returned by default in GetProject or ListProjects responses 8KB max

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
                    "initializer": initializer,
                    "name": name,
                    "prebuild_configuration": prebuild_configuration,
                    "project_id": project_id,
                    "technical_description": technical_description,
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
        token: str | Omit = omit,
        page_size: int | Omit = omit,
        filter: project_list_params.Filter | Omit = omit,
        pagination: project_list_params.Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Project, AsyncProjectsPage[Project]]:
        """
        Lists projects with optional filtering.

        Use this method to:

        - View all accessible projects
        - Browse project configurations
        - Monitor project status

        ### Examples

        - List projects:

          Shows all projects with pagination.

          ```yaml
          pagination:
            pageSize: 20
          ```

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
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                project_list_params.ProjectListParams,
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
                    project_list_params.ProjectListParams,
                ),
            ),
            model=Project,
            method="post",
        )

    async def delete(
        self,
        *,
        project_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Deletes a project permanently.

        Use this method to:

        - Remove unused projects
        - Clean up test projects
        - Delete obsolete configurations

        ### Examples

        - Delete project:

          Permanently removes a project.

          ```yaml
          projectId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          ```

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
        environment_id: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProjectCreateFromEnvironmentResponse:
        """
        Creates a new project using an existing environment as a template.

        Use this method to:

        - Clone environment configurations
        - Create projects from templates
        - Share environment setups

        ### Examples

        - Create from environment:

          Creates a project based on existing environment.

          ```yaml
          name: "Frontend Project"
          environmentId: "07e03a28-65a5-4d98-b532-8ea67b188048"
          ```

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
    def environment_clases(self) -> EnvironmentClasesResourceWithRawResponse:
        return EnvironmentClasesResourceWithRawResponse(self._projects.environment_clases)

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
    def environment_clases(self) -> AsyncEnvironmentClasesResourceWithRawResponse:
        return AsyncEnvironmentClasesResourceWithRawResponse(self._projects.environment_clases)

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
    def environment_clases(self) -> EnvironmentClasesResourceWithStreamingResponse:
        return EnvironmentClasesResourceWithStreamingResponse(self._projects.environment_clases)

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
    def environment_clases(self) -> AsyncEnvironmentClasesResourceWithStreamingResponse:
        return AsyncEnvironmentClasesResourceWithStreamingResponse(self._projects.environment_clases)

    @cached_property
    def policies(self) -> AsyncPoliciesResourceWithStreamingResponse:
        return AsyncPoliciesResourceWithStreamingResponse(self._projects.policies)
