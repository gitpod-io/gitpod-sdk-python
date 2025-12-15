# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncProjectEnvironmentClassesPage, AsyncProjectEnvironmentClassesPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.projects import environment_clase_list_params, environment_clase_update_params
from ...types.shared.project_environment_class import ProjectEnvironmentClass as SharedProjectEnvironmentClass
from ...types.shared_params.project_environment_class import (
    ProjectEnvironmentClass as SharedParamsProjectEnvironmentClass,
)

__all__ = ["EnvironmentClasesResource", "AsyncEnvironmentClasesResource"]


class EnvironmentClasesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EnvironmentClasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return EnvironmentClasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EnvironmentClasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return EnvironmentClasesResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        project_environment_classes: Iterable[SharedParamsProjectEnvironmentClass] | Omit = omit,
        project_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Updates all environment classes of a project.

        Use this method to:

        - Modify all environment classea of a project

        ### Examples

        - Update project environment classes:

          Updates all environment classes for a project.

          ```yaml
          projectId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          projectEnvironmentClasses:
            - environmentClassId: "b0e12f6c-4c67-429d-a4a6-d9838b5da041"
              order: 0
            - localRunner: true
              order: 1
          ```

        Args:
          project_id: project_id specifies the project identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.ProjectService/UpdateProjectEnvironmentClasses",
            body=maybe_transform(
                {
                    "project_environment_classes": project_environment_classes,
                    "project_id": project_id,
                },
                environment_clase_update_params.EnvironmentClaseUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def list(
        self,
        *,
        token: str | Omit = omit,
        page_size: int | Omit = omit,
        pagination: environment_clase_list_params.Pagination | Omit = omit,
        project_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncProjectEnvironmentClassesPage[SharedProjectEnvironmentClass]:
        """
        Lists environment classes of a project.

        Use this method to:

        - View all environment classes of a project

        ### Examples

        - List project environment classes:

          Shows all environment classes of a project.

          ```yaml
          projectId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          pagination:
            pageSize: 20
          ```

        Args:
          pagination: pagination contains the pagination options for listing project policies

          project_id: project_id specifies the project identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.ProjectService/ListProjectEnvironmentClasses",
            page=SyncProjectEnvironmentClassesPage[SharedProjectEnvironmentClass],
            body=maybe_transform(
                {
                    "pagination": pagination,
                    "project_id": project_id,
                },
                environment_clase_list_params.EnvironmentClaseListParams,
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
                    environment_clase_list_params.EnvironmentClaseListParams,
                ),
            ),
            model=SharedProjectEnvironmentClass,
            method="post",
        )


class AsyncEnvironmentClasesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEnvironmentClasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEnvironmentClasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEnvironmentClasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return AsyncEnvironmentClasesResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        project_environment_classes: Iterable[SharedParamsProjectEnvironmentClass] | Omit = omit,
        project_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Updates all environment classes of a project.

        Use this method to:

        - Modify all environment classea of a project

        ### Examples

        - Update project environment classes:

          Updates all environment classes for a project.

          ```yaml
          projectId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          projectEnvironmentClasses:
            - environmentClassId: "b0e12f6c-4c67-429d-a4a6-d9838b5da041"
              order: 0
            - localRunner: true
              order: 1
          ```

        Args:
          project_id: project_id specifies the project identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.ProjectService/UpdateProjectEnvironmentClasses",
            body=await async_maybe_transform(
                {
                    "project_environment_classes": project_environment_classes,
                    "project_id": project_id,
                },
                environment_clase_update_params.EnvironmentClaseUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def list(
        self,
        *,
        token: str | Omit = omit,
        page_size: int | Omit = omit,
        pagination: environment_clase_list_params.Pagination | Omit = omit,
        project_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[
        SharedProjectEnvironmentClass, AsyncProjectEnvironmentClassesPage[SharedProjectEnvironmentClass]
    ]:
        """
        Lists environment classes of a project.

        Use this method to:

        - View all environment classes of a project

        ### Examples

        - List project environment classes:

          Shows all environment classes of a project.

          ```yaml
          projectId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          pagination:
            pageSize: 20
          ```

        Args:
          pagination: pagination contains the pagination options for listing project policies

          project_id: project_id specifies the project identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.ProjectService/ListProjectEnvironmentClasses",
            page=AsyncProjectEnvironmentClassesPage[SharedProjectEnvironmentClass],
            body=maybe_transform(
                {
                    "pagination": pagination,
                    "project_id": project_id,
                },
                environment_clase_list_params.EnvironmentClaseListParams,
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
                    environment_clase_list_params.EnvironmentClaseListParams,
                ),
            ),
            model=SharedProjectEnvironmentClass,
            method="post",
        )


class EnvironmentClasesResourceWithRawResponse:
    def __init__(self, environment_clases: EnvironmentClasesResource) -> None:
        self._environment_clases = environment_clases

        self.update = to_raw_response_wrapper(
            environment_clases.update,
        )
        self.list = to_raw_response_wrapper(
            environment_clases.list,
        )


class AsyncEnvironmentClasesResourceWithRawResponse:
    def __init__(self, environment_clases: AsyncEnvironmentClasesResource) -> None:
        self._environment_clases = environment_clases

        self.update = async_to_raw_response_wrapper(
            environment_clases.update,
        )
        self.list = async_to_raw_response_wrapper(
            environment_clases.list,
        )


class EnvironmentClasesResourceWithStreamingResponse:
    def __init__(self, environment_clases: EnvironmentClasesResource) -> None:
        self._environment_clases = environment_clases

        self.update = to_streamed_response_wrapper(
            environment_clases.update,
        )
        self.list = to_streamed_response_wrapper(
            environment_clases.list,
        )


class AsyncEnvironmentClasesResourceWithStreamingResponse:
    def __init__(self, environment_clases: AsyncEnvironmentClasesResource) -> None:
        self._environment_clases = environment_clases

        self.update = async_to_streamed_response_wrapper(
            environment_clases.update,
        )
        self.list = async_to_streamed_response_wrapper(
            environment_clases.list,
        )
