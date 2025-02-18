# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

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
from ....pagination import SyncServicesPage, AsyncServicesPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.environments.automations import (
    service_list_params,
    service_stop_params,
    service_start_params,
    service_create_params,
    service_delete_params,
    service_update_params,
    service_retrieve_params,
)
from ....types.environments.automations.service import Service
from ....types.environments.automations.service_spec_param import ServiceSpecParam
from ....types.environments.automations.service_metadata_param import ServiceMetadataParam
from ....types.environments.automations.service_create_response import ServiceCreateResponse
from ....types.environments.automations.service_retrieve_response import ServiceRetrieveResponse

__all__ = ["ServicesResource", "AsyncServicesResource"]


class ServicesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ServicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ServicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ServicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return ServicesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        environment_id: str | NotGiven = NOT_GIVEN,
        metadata: ServiceMetadataParam | NotGiven = NOT_GIVEN,
        spec: ServiceSpecParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceCreateResponse:
        """
        Creates a new automation service for an environment.

        Use this method to:

        - Set up long-running services
        - Configure service triggers
        - Define service dependencies
        - Specify runtime environments

        ### Examples

        - Create basic service:

          Creates a simple service with start command.

          ```yaml
          environmentId: "07e03a28-65a5-4d98-b532-8ea67b188048"
          metadata:
            reference: "web-server"
            name: "Web Server"
            description: "Runs the development web server"
            triggeredBy:
              - postDevcontainerStart: true
          spec:
            commands:
              start: "npm run dev"
              ready: "curl -s http://localhost:3000"
          ```

        - Create Docker-based service:

          Creates a service running in a specific container.

          ```yaml
          environmentId: "07e03a28-65a5-4d98-b532-8ea67b188048"
          metadata:
            reference: "redis"
            name: "Redis Server"
            description: "Redis cache service"
          spec:
            commands:
              start: "redis-server"
            runsOn:
              docker:
                image: "redis:7"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.EnvironmentAutomationService/CreateService",
            body=maybe_transform(
                {
                    "environment_id": environment_id,
                    "metadata": metadata,
                    "spec": spec,
                },
                service_create_params.ServiceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceCreateResponse,
        )

    def retrieve(
        self,
        *,
        id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceRetrieveResponse:
        """
        Gets details about a specific automation service.

        Use this method to:

        - Check service status
        - View service configuration
        - Monitor service health
        - Retrieve service metadata

        ### Examples

        - Get service details:

          Retrieves information about a specific service.

          ```yaml
          id: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.EnvironmentAutomationService/GetService",
            body=maybe_transform({"id": id}, service_retrieve_params.ServiceRetrieveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceRetrieveResponse,
        )

    def update(
        self,
        *,
        id: str | NotGiven = NOT_GIVEN,
        metadata: service_update_params.Metadata | NotGiven = NOT_GIVEN,
        spec: service_update_params.Spec | NotGiven = NOT_GIVEN,
        status: service_update_params.Status | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Updates an automation service configuration.

        Use this method to:

        - Modify service commands
        - Update triggers
        - Change runtime settings
        - Adjust dependencies

        ### Examples

        - Update commands:

          Changes service start and ready commands.

          ```yaml
          id: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          spec:
            commands:
              start: "npm run start:dev"
              ready: "curl -s http://localhost:8080"
          ```

        - Update triggers:

          Modifies when the service starts.

          ```yaml
          id: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          metadata:
            triggeredBy:
              trigger:
                - postDevcontainerStart: true
                - manual: true
          ```

        Args:
          spec: Changing the spec of a service is a complex operation. The spec of a service can
              only be updated if the service is in a stopped state. If the service is running,
              it must be stopped first.

          status: Service status updates are only expected from the executing environment. As a
              client of this API you are not expected to provide this field. Updating this
              field requires the `environmentservice:update_status` permission.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.EnvironmentAutomationService/UpdateService",
            body=maybe_transform(
                {
                    "id": id,
                    "metadata": metadata,
                    "spec": spec,
                    "status": status,
                },
                service_update_params.ServiceUpdateParams,
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
        filter: service_list_params.Filter | NotGiven = NOT_GIVEN,
        pagination: service_list_params.Pagination | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncServicesPage[Service]:
        """
        Lists automation services with optional filtering.

        Use this method to:

        - View all services in an environment
        - Filter services by reference
        - Monitor service status

        ### Examples

        - List environment services:

          Shows all services for an environment.

          ```yaml
          filter:
            environmentIds: ["07e03a28-65a5-4d98-b532-8ea67b188048"]
          pagination:
            pageSize: 20
          ```

        - Filter by reference:

          Lists services matching specific references.

          ```yaml
          filter:
            references: ["web-server", "database"]
          pagination:
            pageSize: 20
          ```

        Args:
          filter: filter contains the filter options for listing services

          pagination: pagination contains the pagination options for listing services

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.EnvironmentAutomationService/ListServices",
            page=SyncServicesPage[Service],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                service_list_params.ServiceListParams,
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
                    service_list_params.ServiceListParams,
                ),
            ),
            model=Service,
            method="post",
        )

    def delete(
        self,
        *,
        id: str | NotGiven = NOT_GIVEN,
        force: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Deletes an automation service.

        This call does not block until the service is
        deleted. If the service is not stopped it will be stopped before deletion.

        Use this method to:

        - Remove unused services
        - Clean up service configurations
        - Stop and delete services

        ### Examples

        - Delete service:

          Removes a service after stopping it.

          ```yaml
          id: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          force: false
          ```

        - Force delete:

          Immediately removes a service.

          ```yaml
          id: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          force: true
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.EnvironmentAutomationService/DeleteService",
            body=maybe_transform(
                {
                    "id": id,
                    "force": force,
                },
                service_delete_params.ServiceDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def start(
        self,
        *,
        id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Starts an automation service.

        This call does not block until the service is
        started. This call will not error if the service is already running or has been
        started.

        Use this method to:

        - Start stopped services
        - Resume service operations
        - Trigger service initialization

        ### Examples

        - Start service:

          Starts a previously stopped service.

          ```yaml
          id: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.EnvironmentAutomationService/StartService",
            body=maybe_transform({"id": id}, service_start_params.ServiceStartParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def stop(
        self,
        *,
        id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Stops an automation service.

        This call does not block until the service is
        stopped. This call will not error if the service is already stopped or has been
        stopped.

        Use this method to:

        - Pause service operations
        - Gracefully stop services
        - Prepare for updates

        ### Examples

        - Stop service:

          Gracefully stops a running service.

          ```yaml
          id: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.EnvironmentAutomationService/StopService",
            body=maybe_transform({"id": id}, service_stop_params.ServiceStopParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncServicesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncServicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncServicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncServicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return AsyncServicesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        environment_id: str | NotGiven = NOT_GIVEN,
        metadata: ServiceMetadataParam | NotGiven = NOT_GIVEN,
        spec: ServiceSpecParam | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceCreateResponse:
        """
        Creates a new automation service for an environment.

        Use this method to:

        - Set up long-running services
        - Configure service triggers
        - Define service dependencies
        - Specify runtime environments

        ### Examples

        - Create basic service:

          Creates a simple service with start command.

          ```yaml
          environmentId: "07e03a28-65a5-4d98-b532-8ea67b188048"
          metadata:
            reference: "web-server"
            name: "Web Server"
            description: "Runs the development web server"
            triggeredBy:
              - postDevcontainerStart: true
          spec:
            commands:
              start: "npm run dev"
              ready: "curl -s http://localhost:3000"
          ```

        - Create Docker-based service:

          Creates a service running in a specific container.

          ```yaml
          environmentId: "07e03a28-65a5-4d98-b532-8ea67b188048"
          metadata:
            reference: "redis"
            name: "Redis Server"
            description: "Redis cache service"
          spec:
            commands:
              start: "redis-server"
            runsOn:
              docker:
                image: "redis:7"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.EnvironmentAutomationService/CreateService",
            body=await async_maybe_transform(
                {
                    "environment_id": environment_id,
                    "metadata": metadata,
                    "spec": spec,
                },
                service_create_params.ServiceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceCreateResponse,
        )

    async def retrieve(
        self,
        *,
        id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceRetrieveResponse:
        """
        Gets details about a specific automation service.

        Use this method to:

        - Check service status
        - View service configuration
        - Monitor service health
        - Retrieve service metadata

        ### Examples

        - Get service details:

          Retrieves information about a specific service.

          ```yaml
          id: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.EnvironmentAutomationService/GetService",
            body=await async_maybe_transform({"id": id}, service_retrieve_params.ServiceRetrieveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ServiceRetrieveResponse,
        )

    async def update(
        self,
        *,
        id: str | NotGiven = NOT_GIVEN,
        metadata: service_update_params.Metadata | NotGiven = NOT_GIVEN,
        spec: service_update_params.Spec | NotGiven = NOT_GIVEN,
        status: service_update_params.Status | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Updates an automation service configuration.

        Use this method to:

        - Modify service commands
        - Update triggers
        - Change runtime settings
        - Adjust dependencies

        ### Examples

        - Update commands:

          Changes service start and ready commands.

          ```yaml
          id: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          spec:
            commands:
              start: "npm run start:dev"
              ready: "curl -s http://localhost:8080"
          ```

        - Update triggers:

          Modifies when the service starts.

          ```yaml
          id: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          metadata:
            triggeredBy:
              trigger:
                - postDevcontainerStart: true
                - manual: true
          ```

        Args:
          spec: Changing the spec of a service is a complex operation. The spec of a service can
              only be updated if the service is in a stopped state. If the service is running,
              it must be stopped first.

          status: Service status updates are only expected from the executing environment. As a
              client of this API you are not expected to provide this field. Updating this
              field requires the `environmentservice:update_status` permission.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.EnvironmentAutomationService/UpdateService",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "metadata": metadata,
                    "spec": spec,
                    "status": status,
                },
                service_update_params.ServiceUpdateParams,
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
        filter: service_list_params.Filter | NotGiven = NOT_GIVEN,
        pagination: service_list_params.Pagination | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Service, AsyncServicesPage[Service]]:
        """
        Lists automation services with optional filtering.

        Use this method to:

        - View all services in an environment
        - Filter services by reference
        - Monitor service status

        ### Examples

        - List environment services:

          Shows all services for an environment.

          ```yaml
          filter:
            environmentIds: ["07e03a28-65a5-4d98-b532-8ea67b188048"]
          pagination:
            pageSize: 20
          ```

        - Filter by reference:

          Lists services matching specific references.

          ```yaml
          filter:
            references: ["web-server", "database"]
          pagination:
            pageSize: 20
          ```

        Args:
          filter: filter contains the filter options for listing services

          pagination: pagination contains the pagination options for listing services

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.EnvironmentAutomationService/ListServices",
            page=AsyncServicesPage[Service],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                service_list_params.ServiceListParams,
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
                    service_list_params.ServiceListParams,
                ),
            ),
            model=Service,
            method="post",
        )

    async def delete(
        self,
        *,
        id: str | NotGiven = NOT_GIVEN,
        force: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Deletes an automation service.

        This call does not block until the service is
        deleted. If the service is not stopped it will be stopped before deletion.

        Use this method to:

        - Remove unused services
        - Clean up service configurations
        - Stop and delete services

        ### Examples

        - Delete service:

          Removes a service after stopping it.

          ```yaml
          id: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          force: false
          ```

        - Force delete:

          Immediately removes a service.

          ```yaml
          id: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          force: true
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.EnvironmentAutomationService/DeleteService",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "force": force,
                },
                service_delete_params.ServiceDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def start(
        self,
        *,
        id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Starts an automation service.

        This call does not block until the service is
        started. This call will not error if the service is already running or has been
        started.

        Use this method to:

        - Start stopped services
        - Resume service operations
        - Trigger service initialization

        ### Examples

        - Start service:

          Starts a previously stopped service.

          ```yaml
          id: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.EnvironmentAutomationService/StartService",
            body=await async_maybe_transform({"id": id}, service_start_params.ServiceStartParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def stop(
        self,
        *,
        id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Stops an automation service.

        This call does not block until the service is
        stopped. This call will not error if the service is already stopped or has been
        stopped.

        Use this method to:

        - Pause service operations
        - Gracefully stop services
        - Prepare for updates

        ### Examples

        - Stop service:

          Gracefully stops a running service.

          ```yaml
          id: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.EnvironmentAutomationService/StopService",
            body=await async_maybe_transform({"id": id}, service_stop_params.ServiceStopParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class ServicesResourceWithRawResponse:
    def __init__(self, services: ServicesResource) -> None:
        self._services = services

        self.create = to_raw_response_wrapper(
            services.create,
        )
        self.retrieve = to_raw_response_wrapper(
            services.retrieve,
        )
        self.update = to_raw_response_wrapper(
            services.update,
        )
        self.list = to_raw_response_wrapper(
            services.list,
        )
        self.delete = to_raw_response_wrapper(
            services.delete,
        )
        self.start = to_raw_response_wrapper(
            services.start,
        )
        self.stop = to_raw_response_wrapper(
            services.stop,
        )


class AsyncServicesResourceWithRawResponse:
    def __init__(self, services: AsyncServicesResource) -> None:
        self._services = services

        self.create = async_to_raw_response_wrapper(
            services.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            services.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            services.update,
        )
        self.list = async_to_raw_response_wrapper(
            services.list,
        )
        self.delete = async_to_raw_response_wrapper(
            services.delete,
        )
        self.start = async_to_raw_response_wrapper(
            services.start,
        )
        self.stop = async_to_raw_response_wrapper(
            services.stop,
        )


class ServicesResourceWithStreamingResponse:
    def __init__(self, services: ServicesResource) -> None:
        self._services = services

        self.create = to_streamed_response_wrapper(
            services.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            services.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            services.update,
        )
        self.list = to_streamed_response_wrapper(
            services.list,
        )
        self.delete = to_streamed_response_wrapper(
            services.delete,
        )
        self.start = to_streamed_response_wrapper(
            services.start,
        )
        self.stop = to_streamed_response_wrapper(
            services.stop,
        )


class AsyncServicesResourceWithStreamingResponse:
    def __init__(self, services: AsyncServicesResource) -> None:
        self._services = services

        self.create = async_to_streamed_response_wrapper(
            services.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            services.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            services.update,
        )
        self.list = async_to_streamed_response_wrapper(
            services.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            services.delete,
        )
        self.start = async_to_streamed_response_wrapper(
            services.start,
        )
        self.stop = async_to_streamed_response_wrapper(
            services.stop,
        )
