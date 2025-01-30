# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...types import (
    environment_list_params,
    environment_start_params,
    environment_create_params,
    environment_retrieve_params,
    environment_create_from_project_params,
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
from ..._base_client import make_request_options
from .automations.automations import (
    AutomationsResource,
    AsyncAutomationsResource,
    AutomationsResourceWithRawResponse,
    AsyncAutomationsResourceWithRawResponse,
    AutomationsResourceWithStreamingResponse,
    AsyncAutomationsResourceWithStreamingResponse,
)
from ...types.environment_list_response import EnvironmentListResponse
from ...types.environment_create_response import EnvironmentCreateResponse
from ...types.environment_retrieve_response import EnvironmentRetrieveResponse
from ...types.environment_create_from_project_response import EnvironmentCreateFromProjectResponse

__all__ = ["EnvironmentsResource", "AsyncEnvironmentsResource"]


class EnvironmentsResource(SyncAPIResource):
    @cached_property
    def automations(self) -> AutomationsResource:
        return AutomationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> EnvironmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return EnvironmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EnvironmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return EnvironmentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        spec: environment_create_params.Spec | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnvironmentCreateResponse:
        """
        CreateEnvironment creates a new environment and starts it.

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

        +return NOT_FOUND User does not have access to an environment with the given ID
        +return NOT_FOUND Environment does not exist

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

    def list(
        self,
        *,
        filter: environment_list_params.Filter | NotGiven = NOT_GIVEN,
        organization_id: str | NotGiven = NOT_GIVEN,
        pagination: environment_list_params.Pagination | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnvironmentListResponse:
        """
        ListEnvironments returns a list of environments that match the query.

        Args:
          organization_id: organization_id is the ID of the organization that contains the environments

          pagination: pagination contains the pagination options for listing environments

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.EnvironmentService/ListEnvironments",
            body=maybe_transform(
                {
                    "filter": filter,
                    "organization_id": organization_id,
                    "pagination": pagination,
                },
                environment_list_params.EnvironmentListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvironmentListResponse,
        )

    def create_from_project(
        self,
        *,
        project_id: str | NotGiven = NOT_GIVEN,
        spec: environment_create_from_project_params.Spec | NotGiven = NOT_GIVEN,
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

        This function is idempotent, i.e. if

        the environment is already running no error is returned.

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


class AsyncEnvironmentsResource(AsyncAPIResource):
    @cached_property
    def automations(self) -> AsyncAutomationsResource:
        return AsyncAutomationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEnvironmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEnvironmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEnvironmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return AsyncEnvironmentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        spec: environment_create_params.Spec | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnvironmentCreateResponse:
        """
        CreateEnvironment creates a new environment and starts it.

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

        +return NOT_FOUND User does not have access to an environment with the given ID
        +return NOT_FOUND Environment does not exist

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

    async def list(
        self,
        *,
        filter: environment_list_params.Filter | NotGiven = NOT_GIVEN,
        organization_id: str | NotGiven = NOT_GIVEN,
        pagination: environment_list_params.Pagination | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EnvironmentListResponse:
        """
        ListEnvironments returns a list of environments that match the query.

        Args:
          organization_id: organization_id is the ID of the organization that contains the environments

          pagination: pagination contains the pagination options for listing environments

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.EnvironmentService/ListEnvironments",
            body=await async_maybe_transform(
                {
                    "filter": filter,
                    "organization_id": organization_id,
                    "pagination": pagination,
                },
                environment_list_params.EnvironmentListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnvironmentListResponse,
        )

    async def create_from_project(
        self,
        *,
        project_id: str | NotGiven = NOT_GIVEN,
        spec: environment_create_from_project_params.Spec | NotGiven = NOT_GIVEN,
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

        This function is idempotent, i.e. if

        the environment is already running no error is returned.

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


class EnvironmentsResourceWithRawResponse:
    def __init__(self, environments: EnvironmentsResource) -> None:
        self._environments = environments

        self.create = to_raw_response_wrapper(
            environments.create,
        )
        self.retrieve = to_raw_response_wrapper(
            environments.retrieve,
        )
        self.list = to_raw_response_wrapper(
            environments.list,
        )
        self.create_from_project = to_raw_response_wrapper(
            environments.create_from_project,
        )
        self.start = to_raw_response_wrapper(
            environments.start,
        )

    @cached_property
    def automations(self) -> AutomationsResourceWithRawResponse:
        return AutomationsResourceWithRawResponse(self._environments.automations)


class AsyncEnvironmentsResourceWithRawResponse:
    def __init__(self, environments: AsyncEnvironmentsResource) -> None:
        self._environments = environments

        self.create = async_to_raw_response_wrapper(
            environments.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            environments.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            environments.list,
        )
        self.create_from_project = async_to_raw_response_wrapper(
            environments.create_from_project,
        )
        self.start = async_to_raw_response_wrapper(
            environments.start,
        )

    @cached_property
    def automations(self) -> AsyncAutomationsResourceWithRawResponse:
        return AsyncAutomationsResourceWithRawResponse(self._environments.automations)


class EnvironmentsResourceWithStreamingResponse:
    def __init__(self, environments: EnvironmentsResource) -> None:
        self._environments = environments

        self.create = to_streamed_response_wrapper(
            environments.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            environments.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            environments.list,
        )
        self.create_from_project = to_streamed_response_wrapper(
            environments.create_from_project,
        )
        self.start = to_streamed_response_wrapper(
            environments.start,
        )

    @cached_property
    def automations(self) -> AutomationsResourceWithStreamingResponse:
        return AutomationsResourceWithStreamingResponse(self._environments.automations)


class AsyncEnvironmentsResourceWithStreamingResponse:
    def __init__(self, environments: AsyncEnvironmentsResource) -> None:
        self._environments = environments

        self.create = async_to_streamed_response_wrapper(
            environments.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            environments.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            environments.list,
        )
        self.create_from_project = async_to_streamed_response_wrapper(
            environments.create_from_project,
        )
        self.start = async_to_streamed_response_wrapper(
            environments.start,
        )

    @cached_property
    def automations(self) -> AsyncAutomationsResourceWithStreamingResponse:
        return AsyncAutomationsResourceWithStreamingResponse(self._environments.automations)
