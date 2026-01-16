# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

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
from ...pagination import SyncScimConfigurationsPage, AsyncScimConfigurationsPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.organizations import (
    scim_configuration_list_params,
    scim_configuration_create_params,
    scim_configuration_delete_params,
    scim_configuration_update_params,
    scim_configuration_retrieve_params,
    scim_configuration_regenerate_token_params,
)
from ...types.organizations.scim_configuration import ScimConfiguration
from ...types.organizations.scim_configuration_create_response import ScimConfigurationCreateResponse
from ...types.organizations.scim_configuration_update_response import ScimConfigurationUpdateResponse
from ...types.organizations.scim_configuration_retrieve_response import ScimConfigurationRetrieveResponse
from ...types.organizations.scim_configuration_regenerate_token_response import ScimConfigurationRegenerateTokenResponse

__all__ = ["ScimConfigurationsResource", "AsyncScimConfigurationsResource"]


class ScimConfigurationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScimConfigurationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ScimConfigurationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScimConfigurationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return ScimConfigurationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        organization_id: str,
        sso_configuration_id: str,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScimConfigurationCreateResponse:
        """
        Creates a new SCIM configuration for automated user provisioning.

        Use this method to:

        - Set up SCIM 2.0 provisioning from an identity provider
        - Generate a bearer token for SCIM API authentication
        - Link SCIM provisioning to an existing SSO configuration

        ### Examples

        - Create basic SCIM configuration:

          Creates a SCIM configuration linked to an SSO provider.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          ssoConfigurationId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          organization_id: organization_id is the ID of the organization to create the SCIM configuration
              for

          sso_configuration_id: sso_configuration_id is the SSO configuration to link (required for user
              provisioning)

          name: name is a human-readable name for the SCIM configuration

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.OrganizationService/CreateSCIMConfiguration",
            body=maybe_transform(
                {
                    "organization_id": organization_id,
                    "sso_configuration_id": sso_configuration_id,
                    "name": name,
                },
                scim_configuration_create_params.ScimConfigurationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScimConfigurationCreateResponse,
        )

    def retrieve(
        self,
        *,
        scim_configuration_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScimConfigurationRetrieveResponse:
        """
        Retrieves a specific SCIM configuration.

        Use this method to:

        - View SCIM configuration details
        - Check if SCIM is enabled
        - Verify SSO linkage

        ### Examples

        - Get SCIM configuration:

          Retrieves details of a specific SCIM configuration.

          ```yaml
          scimConfigurationId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          scim_configuration_id: scim_configuration_id is the ID of the SCIM configuration to get

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.OrganizationService/GetSCIMConfiguration",
            body=maybe_transform(
                {"scim_configuration_id": scim_configuration_id},
                scim_configuration_retrieve_params.ScimConfigurationRetrieveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScimConfigurationRetrieveResponse,
        )

    def update(
        self,
        *,
        scim_configuration_id: str,
        enabled: Optional[bool] | Omit = omit,
        name: Optional[str] | Omit = omit,
        sso_configuration_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScimConfigurationUpdateResponse:
        """
        Updates a SCIM configuration.

        Use this method to:

        - Enable or disable SCIM provisioning
        - Link or unlink SSO configuration
        - Update configuration name

        ### Examples

        - Disable SCIM:

          Disables SCIM provisioning.

          ```yaml
          scimConfigurationId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          enabled: false
          ```

        - Link to SSO:

          Links SCIM configuration to an SSO provider.

          ```yaml
          scimConfigurationId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ssoConfigurationId: "f53d2330-3795-4c5d-a1f3-453121af9c60"
          ```

        Args:
          scim_configuration_id: scim_configuration_id is the ID of the SCIM configuration to update

          enabled: enabled controls whether SCIM provisioning is active

          name: name is a human-readable name for the SCIM configuration

          sso_configuration_id: sso_configuration_id is the SSO configuration to link

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.OrganizationService/UpdateSCIMConfiguration",
            body=maybe_transform(
                {
                    "scim_configuration_id": scim_configuration_id,
                    "enabled": enabled,
                    "name": name,
                    "sso_configuration_id": sso_configuration_id,
                },
                scim_configuration_update_params.ScimConfigurationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScimConfigurationUpdateResponse,
        )

    def list(
        self,
        *,
        token: str | Omit = omit,
        page_size: int | Omit = omit,
        pagination: scim_configuration_list_params.Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncScimConfigurationsPage[ScimConfiguration]:
        """
        Lists SCIM configurations for an organization.

        Use this method to:

        - View all SCIM configurations
        - Monitor provisioning status
        - Audit SCIM settings

        ### Examples

        - List SCIM configurations:

          Shows all SCIM configurations for an organization.

          ```yaml
          pagination:
            pageSize: 20
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.OrganizationService/ListSCIMConfigurations",
            page=SyncScimConfigurationsPage[ScimConfiguration],
            body=maybe_transform(
                {"pagination": pagination}, scim_configuration_list_params.ScimConfigurationListParams
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
                    scim_configuration_list_params.ScimConfigurationListParams,
                ),
            ),
            model=ScimConfiguration,
            method="post",
        )

    def delete(
        self,
        *,
        scim_configuration_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Removes a SCIM configuration from an organization.

        Use this method to:

        - Disable SCIM provisioning completely
        - Remove unused configurations
        - Clean up after migration

        ### Examples

        - Delete SCIM configuration:

          Removes a specific SCIM configuration.

          ```yaml
          scimConfigurationId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          scim_configuration_id: scim_configuration_id is the ID of the SCIM configuration to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.OrganizationService/DeleteSCIMConfiguration",
            body=maybe_transform(
                {"scim_configuration_id": scim_configuration_id},
                scim_configuration_delete_params.ScimConfigurationDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def regenerate_token(
        self,
        *,
        scim_configuration_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScimConfigurationRegenerateTokenResponse:
        """
        Regenerates the bearer token for a SCIM configuration.

        Use this method to:

        - Rotate SCIM credentials
        - Recover from token compromise
        - Update IdP configuration

        ### Examples

        - Regenerate token:

          Creates a new bearer token, invalidating the old one.

          ```yaml
          scimConfigurationId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          scim_configuration_id: scim_configuration_id is the ID of the SCIM configuration to regenerate token
              for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.OrganizationService/RegenerateSCIMToken",
            body=maybe_transform(
                {"scim_configuration_id": scim_configuration_id},
                scim_configuration_regenerate_token_params.ScimConfigurationRegenerateTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScimConfigurationRegenerateTokenResponse,
        )


class AsyncScimConfigurationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScimConfigurationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncScimConfigurationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScimConfigurationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return AsyncScimConfigurationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        organization_id: str,
        sso_configuration_id: str,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScimConfigurationCreateResponse:
        """
        Creates a new SCIM configuration for automated user provisioning.

        Use this method to:

        - Set up SCIM 2.0 provisioning from an identity provider
        - Generate a bearer token for SCIM API authentication
        - Link SCIM provisioning to an existing SSO configuration

        ### Examples

        - Create basic SCIM configuration:

          Creates a SCIM configuration linked to an SSO provider.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          ssoConfigurationId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          organization_id: organization_id is the ID of the organization to create the SCIM configuration
              for

          sso_configuration_id: sso_configuration_id is the SSO configuration to link (required for user
              provisioning)

          name: name is a human-readable name for the SCIM configuration

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.OrganizationService/CreateSCIMConfiguration",
            body=await async_maybe_transform(
                {
                    "organization_id": organization_id,
                    "sso_configuration_id": sso_configuration_id,
                    "name": name,
                },
                scim_configuration_create_params.ScimConfigurationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScimConfigurationCreateResponse,
        )

    async def retrieve(
        self,
        *,
        scim_configuration_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScimConfigurationRetrieveResponse:
        """
        Retrieves a specific SCIM configuration.

        Use this method to:

        - View SCIM configuration details
        - Check if SCIM is enabled
        - Verify SSO linkage

        ### Examples

        - Get SCIM configuration:

          Retrieves details of a specific SCIM configuration.

          ```yaml
          scimConfigurationId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          scim_configuration_id: scim_configuration_id is the ID of the SCIM configuration to get

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.OrganizationService/GetSCIMConfiguration",
            body=await async_maybe_transform(
                {"scim_configuration_id": scim_configuration_id},
                scim_configuration_retrieve_params.ScimConfigurationRetrieveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScimConfigurationRetrieveResponse,
        )

    async def update(
        self,
        *,
        scim_configuration_id: str,
        enabled: Optional[bool] | Omit = omit,
        name: Optional[str] | Omit = omit,
        sso_configuration_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScimConfigurationUpdateResponse:
        """
        Updates a SCIM configuration.

        Use this method to:

        - Enable or disable SCIM provisioning
        - Link or unlink SSO configuration
        - Update configuration name

        ### Examples

        - Disable SCIM:

          Disables SCIM provisioning.

          ```yaml
          scimConfigurationId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          enabled: false
          ```

        - Link to SSO:

          Links SCIM configuration to an SSO provider.

          ```yaml
          scimConfigurationId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ssoConfigurationId: "f53d2330-3795-4c5d-a1f3-453121af9c60"
          ```

        Args:
          scim_configuration_id: scim_configuration_id is the ID of the SCIM configuration to update

          enabled: enabled controls whether SCIM provisioning is active

          name: name is a human-readable name for the SCIM configuration

          sso_configuration_id: sso_configuration_id is the SSO configuration to link

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.OrganizationService/UpdateSCIMConfiguration",
            body=await async_maybe_transform(
                {
                    "scim_configuration_id": scim_configuration_id,
                    "enabled": enabled,
                    "name": name,
                    "sso_configuration_id": sso_configuration_id,
                },
                scim_configuration_update_params.ScimConfigurationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScimConfigurationUpdateResponse,
        )

    def list(
        self,
        *,
        token: str | Omit = omit,
        page_size: int | Omit = omit,
        pagination: scim_configuration_list_params.Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ScimConfiguration, AsyncScimConfigurationsPage[ScimConfiguration]]:
        """
        Lists SCIM configurations for an organization.

        Use this method to:

        - View all SCIM configurations
        - Monitor provisioning status
        - Audit SCIM settings

        ### Examples

        - List SCIM configurations:

          Shows all SCIM configurations for an organization.

          ```yaml
          pagination:
            pageSize: 20
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.OrganizationService/ListSCIMConfigurations",
            page=AsyncScimConfigurationsPage[ScimConfiguration],
            body=maybe_transform(
                {"pagination": pagination}, scim_configuration_list_params.ScimConfigurationListParams
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
                    scim_configuration_list_params.ScimConfigurationListParams,
                ),
            ),
            model=ScimConfiguration,
            method="post",
        )

    async def delete(
        self,
        *,
        scim_configuration_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Removes a SCIM configuration from an organization.

        Use this method to:

        - Disable SCIM provisioning completely
        - Remove unused configurations
        - Clean up after migration

        ### Examples

        - Delete SCIM configuration:

          Removes a specific SCIM configuration.

          ```yaml
          scimConfigurationId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          scim_configuration_id: scim_configuration_id is the ID of the SCIM configuration to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.OrganizationService/DeleteSCIMConfiguration",
            body=await async_maybe_transform(
                {"scim_configuration_id": scim_configuration_id},
                scim_configuration_delete_params.ScimConfigurationDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def regenerate_token(
        self,
        *,
        scim_configuration_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScimConfigurationRegenerateTokenResponse:
        """
        Regenerates the bearer token for a SCIM configuration.

        Use this method to:

        - Rotate SCIM credentials
        - Recover from token compromise
        - Update IdP configuration

        ### Examples

        - Regenerate token:

          Creates a new bearer token, invalidating the old one.

          ```yaml
          scimConfigurationId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          scim_configuration_id: scim_configuration_id is the ID of the SCIM configuration to regenerate token
              for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.OrganizationService/RegenerateSCIMToken",
            body=await async_maybe_transform(
                {"scim_configuration_id": scim_configuration_id},
                scim_configuration_regenerate_token_params.ScimConfigurationRegenerateTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScimConfigurationRegenerateTokenResponse,
        )


class ScimConfigurationsResourceWithRawResponse:
    def __init__(self, scim_configurations: ScimConfigurationsResource) -> None:
        self._scim_configurations = scim_configurations

        self.create = to_raw_response_wrapper(
            scim_configurations.create,
        )
        self.retrieve = to_raw_response_wrapper(
            scim_configurations.retrieve,
        )
        self.update = to_raw_response_wrapper(
            scim_configurations.update,
        )
        self.list = to_raw_response_wrapper(
            scim_configurations.list,
        )
        self.delete = to_raw_response_wrapper(
            scim_configurations.delete,
        )
        self.regenerate_token = to_raw_response_wrapper(
            scim_configurations.regenerate_token,
        )


class AsyncScimConfigurationsResourceWithRawResponse:
    def __init__(self, scim_configurations: AsyncScimConfigurationsResource) -> None:
        self._scim_configurations = scim_configurations

        self.create = async_to_raw_response_wrapper(
            scim_configurations.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            scim_configurations.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            scim_configurations.update,
        )
        self.list = async_to_raw_response_wrapper(
            scim_configurations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            scim_configurations.delete,
        )
        self.regenerate_token = async_to_raw_response_wrapper(
            scim_configurations.regenerate_token,
        )


class ScimConfigurationsResourceWithStreamingResponse:
    def __init__(self, scim_configurations: ScimConfigurationsResource) -> None:
        self._scim_configurations = scim_configurations

        self.create = to_streamed_response_wrapper(
            scim_configurations.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            scim_configurations.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            scim_configurations.update,
        )
        self.list = to_streamed_response_wrapper(
            scim_configurations.list,
        )
        self.delete = to_streamed_response_wrapper(
            scim_configurations.delete,
        )
        self.regenerate_token = to_streamed_response_wrapper(
            scim_configurations.regenerate_token,
        )


class AsyncScimConfigurationsResourceWithStreamingResponse:
    def __init__(self, scim_configurations: AsyncScimConfigurationsResource) -> None:
        self._scim_configurations = scim_configurations

        self.create = async_to_streamed_response_wrapper(
            scim_configurations.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            scim_configurations.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            scim_configurations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            scim_configurations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            scim_configurations.delete,
        )
        self.regenerate_token = async_to_streamed_response_wrapper(
            scim_configurations.regenerate_token,
        )
