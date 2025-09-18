# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncEnvironmentClassesPage, AsyncEnvironmentClassesPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.runners.configurations import (
    environment_class_list_params,
    environment_class_create_params,
    environment_class_update_params,
    environment_class_retrieve_params,
)
from ....types.shared.environment_class import EnvironmentClass
from ....types.shared_params.field_value import FieldValue
from ....types.runners.configurations.environment_class_create_response import EnvironmentClassCreateResponse
from ....types.runners.configurations.environment_class_retrieve_response import EnvironmentClassRetrieveResponse

__all__ = ["EnvironmentClassesResource", "AsyncEnvironmentClassesResource"]


class EnvironmentClassesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EnvironmentClassesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return EnvironmentClassesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EnvironmentClassesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return EnvironmentClassesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        configuration: Iterable[FieldValue] | Omit = omit,
        description: str | Omit = omit,
        display_name: str | Omit = omit,
        runner_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnvironmentClassCreateResponse:
        """
        Creates a new environment class for a runner.

        Use this method to:

        - Define compute resources
        - Configure environment settings
        - Set up runtime options

        ### Examples

        - Create environment class:

          Creates a new environment configuration.

          ```yaml
          runnerId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          displayName: "Large Instance"
          description: "8 CPU, 16GB RAM"
          configuration:
            - key: "cpu"
              value: "8"
            - key: "memory"
              value: "16384"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.RunnerConfigurationService/CreateEnvironmentClass",
            body=maybe_transform(
                {
                    "configuration": configuration,
                    "description": description,
                    "display_name": display_name,
                    "runner_id": runner_id,
                },
                environment_class_create_params.EnvironmentClassCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvironmentClassCreateResponse,
        )

    def retrieve(
        self,
        *,
        environment_class_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnvironmentClassRetrieveResponse:
        """
        Gets details about a specific environment class.

        Use this method to:

        - View class configuration
        - Check resource settings
        - Verify availability

        ### Examples

        - Get class details:

          Retrieves information about a specific class.

          ```yaml
          environmentClassId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.RunnerConfigurationService/GetEnvironmentClass",
            body=maybe_transform(
                {"environment_class_id": environment_class_id},
                environment_class_retrieve_params.EnvironmentClassRetrieveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvironmentClassRetrieveResponse,
        )

    def update(
        self,
        *,
        description: Optional[str] | Omit = omit,
        display_name: Optional[str] | Omit = omit,
        enabled: Optional[bool] | Omit = omit,
        environment_class_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Updates an environment class.

        Use this method to:

        - Modify class settings
        - Update resource limits
        - Change availability

        ### Examples

        - Update class:

          Changes class configuration.

          ```yaml
          environmentClassId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          displayName: "Updated Large Instance"
          description: "16 CPU, 32GB RAM"
          enabled: true
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.RunnerConfigurationService/UpdateEnvironmentClass",
            body=maybe_transform(
                {
                    "description": description,
                    "display_name": display_name,
                    "enabled": enabled,
                    "environment_class_id": environment_class_id,
                },
                environment_class_update_params.EnvironmentClassUpdateParams,
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
        filter: environment_class_list_params.Filter | Omit = omit,
        pagination: environment_class_list_params.Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncEnvironmentClassesPage[EnvironmentClass]:
        """
        Lists environment classes with optional filtering.

        Use this method to:

        - View available classes
        - Filter by capability
        - Check enabled status

        ### Examples

        - List all classes:

          Shows all environment classes.

          ```yaml
          pagination:
            pageSize: 20
          ```

        - Filter enabled classes:

          Lists only enabled environment classes.

          ```yaml
          filter:
            enabled: true
          pagination:
            pageSize: 20
          ```

          buf:lint:ignore RPC_REQUEST_RESPONSE_UNIQUE

        Args:
          pagination: pagination contains the pagination options for listing environment classes

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.RunnerConfigurationService/ListEnvironmentClasses",
            page=SyncEnvironmentClassesPage[EnvironmentClass],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                environment_class_list_params.EnvironmentClassListParams,
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
                    environment_class_list_params.EnvironmentClassListParams,
                ),
            ),
            model=EnvironmentClass,
            method="post",
        )


class AsyncEnvironmentClassesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEnvironmentClassesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEnvironmentClassesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEnvironmentClassesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return AsyncEnvironmentClassesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        configuration: Iterable[FieldValue] | Omit = omit,
        description: str | Omit = omit,
        display_name: str | Omit = omit,
        runner_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnvironmentClassCreateResponse:
        """
        Creates a new environment class for a runner.

        Use this method to:

        - Define compute resources
        - Configure environment settings
        - Set up runtime options

        ### Examples

        - Create environment class:

          Creates a new environment configuration.

          ```yaml
          runnerId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          displayName: "Large Instance"
          description: "8 CPU, 16GB RAM"
          configuration:
            - key: "cpu"
              value: "8"
            - key: "memory"
              value: "16384"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.RunnerConfigurationService/CreateEnvironmentClass",
            body=await async_maybe_transform(
                {
                    "configuration": configuration,
                    "description": description,
                    "display_name": display_name,
                    "runner_id": runner_id,
                },
                environment_class_create_params.EnvironmentClassCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvironmentClassCreateResponse,
        )

    async def retrieve(
        self,
        *,
        environment_class_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EnvironmentClassRetrieveResponse:
        """
        Gets details about a specific environment class.

        Use this method to:

        - View class configuration
        - Check resource settings
        - Verify availability

        ### Examples

        - Get class details:

          Retrieves information about a specific class.

          ```yaml
          environmentClassId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.RunnerConfigurationService/GetEnvironmentClass",
            body=await async_maybe_transform(
                {"environment_class_id": environment_class_id},
                environment_class_retrieve_params.EnvironmentClassRetrieveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvironmentClassRetrieveResponse,
        )

    async def update(
        self,
        *,
        description: Optional[str] | Omit = omit,
        display_name: Optional[str] | Omit = omit,
        enabled: Optional[bool] | Omit = omit,
        environment_class_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Updates an environment class.

        Use this method to:

        - Modify class settings
        - Update resource limits
        - Change availability

        ### Examples

        - Update class:

          Changes class configuration.

          ```yaml
          environmentClassId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          displayName: "Updated Large Instance"
          description: "16 CPU, 32GB RAM"
          enabled: true
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.RunnerConfigurationService/UpdateEnvironmentClass",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "display_name": display_name,
                    "enabled": enabled,
                    "environment_class_id": environment_class_id,
                },
                environment_class_update_params.EnvironmentClassUpdateParams,
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
        filter: environment_class_list_params.Filter | Omit = omit,
        pagination: environment_class_list_params.Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[EnvironmentClass, AsyncEnvironmentClassesPage[EnvironmentClass]]:
        """
        Lists environment classes with optional filtering.

        Use this method to:

        - View available classes
        - Filter by capability
        - Check enabled status

        ### Examples

        - List all classes:

          Shows all environment classes.

          ```yaml
          pagination:
            pageSize: 20
          ```

        - Filter enabled classes:

          Lists only enabled environment classes.

          ```yaml
          filter:
            enabled: true
          pagination:
            pageSize: 20
          ```

          buf:lint:ignore RPC_REQUEST_RESPONSE_UNIQUE

        Args:
          pagination: pagination contains the pagination options for listing environment classes

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.RunnerConfigurationService/ListEnvironmentClasses",
            page=AsyncEnvironmentClassesPage[EnvironmentClass],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                environment_class_list_params.EnvironmentClassListParams,
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
                    environment_class_list_params.EnvironmentClassListParams,
                ),
            ),
            model=EnvironmentClass,
            method="post",
        )


class EnvironmentClassesResourceWithRawResponse:
    def __init__(self, environment_classes: EnvironmentClassesResource) -> None:
        self._environment_classes = environment_classes

        self.create = to_raw_response_wrapper(
            environment_classes.create,
        )
        self.retrieve = to_raw_response_wrapper(
            environment_classes.retrieve,
        )
        self.update = to_raw_response_wrapper(
            environment_classes.update,
        )
        self.list = to_raw_response_wrapper(
            environment_classes.list,
        )


class AsyncEnvironmentClassesResourceWithRawResponse:
    def __init__(self, environment_classes: AsyncEnvironmentClassesResource) -> None:
        self._environment_classes = environment_classes

        self.create = async_to_raw_response_wrapper(
            environment_classes.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            environment_classes.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            environment_classes.update,
        )
        self.list = async_to_raw_response_wrapper(
            environment_classes.list,
        )


class EnvironmentClassesResourceWithStreamingResponse:
    def __init__(self, environment_classes: EnvironmentClassesResource) -> None:
        self._environment_classes = environment_classes

        self.create = to_streamed_response_wrapper(
            environment_classes.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            environment_classes.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            environment_classes.update,
        )
        self.list = to_streamed_response_wrapper(
            environment_classes.list,
        )


class AsyncEnvironmentClassesResourceWithStreamingResponse:
    def __init__(self, environment_classes: AsyncEnvironmentClassesResource) -> None:
        self._environment_classes = environment_classes

        self.create = async_to_streamed_response_wrapper(
            environment_classes.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            environment_classes.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            environment_classes.update,
        )
        self.list = async_to_streamed_response_wrapper(
            environment_classes.list,
        )
