# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

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
from ...pagination import SyncSSOConfigurationsPage, AsyncSSOConfigurationsPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.organizations import (
    SSOConfigurationState,
    sso_configuration_list_params,
    sso_configuration_create_params,
    sso_configuration_delete_params,
    sso_configuration_update_params,
    sso_configuration_retrieve_params,
)
from ...types.organizations.sso_configuration import SSOConfiguration
from ...types.organizations.sso_configuration_state import SSOConfigurationState
from ...types.organizations.sso_configuration_create_response import SSOConfigurationCreateResponse
from ...types.organizations.sso_configuration_retrieve_response import SSOConfigurationRetrieveResponse

__all__ = ["SSOConfigurationsResource", "AsyncSSOConfigurationsResource"]


class SSOConfigurationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SSOConfigurationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SSOConfigurationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SSOConfigurationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return SSOConfigurationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        client_id: str,
        client_secret: str,
        email_domain: str,
        issuer_url: str,
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SSOConfigurationCreateResponse:
        """
        Creates or updates SSO configuration for organizational authentication.

        Use this method to:

        - Configure OIDC-based SSO providers
        - Set up built-in providers (Google, GitHub, etc.)
        - Define custom identity providers
        - Manage authentication policies

        ### Examples

        - Configure built-in Google SSO:

          Sets up SSO using Google Workspace.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          clientId: "012345678-abcdefghijklmnopqrstuvwxyz.apps.googleusercontent.com"
          clientSecret: "GOCSPX-abcdefghijklmnopqrstuvwxyz123456"
          issuerUrl: "https://accounts.google.com"
          emailDomain: "acme-corp.com"
          ```

        - Configure custom OIDC provider:

          Sets up SSO with a custom identity provider.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          clientId: "acme-corp-gitpod"
          clientSecret: "secret-token-value"
          issuerUrl: "https://sso.acme-corp.com"
          emailDomain: "acme-corp.com"
          ```

        Args:
          client_id: client_id is the client ID of the OIDC application set on the IdP

          client_secret: client_secret is the client secret of the OIDC application set on the IdP

          email_domain: email_domain is the domain that is allowed to sign in to the organization

          issuer_url: issuer_url is the URL of the IdP issuer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.OrganizationService/CreateSSOConfiguration",
            body=maybe_transform(
                {
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "email_domain": email_domain,
                    "issuer_url": issuer_url,
                    "organization_id": organization_id,
                },
                sso_configuration_create_params.SSOConfigurationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SSOConfigurationCreateResponse,
        )

    def retrieve(
        self,
        *,
        sso_configuration_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SSOConfigurationRetrieveResponse:
        """
        Retrieves a specific SSO configuration.

        Use this method to:

        - View SSO provider details
        - Check configuration status
        - Verify SSO settings

        ### Examples

        - Get SSO configuration:

          Retrieves details of a specific SSO configuration.

          ```yaml
          ssoConfigurationId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          sso_configuration_id: sso_configuration_id is the ID of the SSO configuration to get

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.OrganizationService/GetSSOConfiguration",
            body=maybe_transform(
                {"sso_configuration_id": sso_configuration_id},
                sso_configuration_retrieve_params.SSOConfigurationRetrieveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SSOConfigurationRetrieveResponse,
        )

    def update(
        self,
        *,
        sso_configuration_id: str,
        claims: Dict[str, str] | NotGiven = NOT_GIVEN,
        client_id: Optional[str] | NotGiven = NOT_GIVEN,
        client_secret: Optional[str] | NotGiven = NOT_GIVEN,
        email_domain: Optional[str] | NotGiven = NOT_GIVEN,
        issuer_url: Optional[str] | NotGiven = NOT_GIVEN,
        state: Optional[SSOConfigurationState] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Updates SSO provider settings and authentication rules.

        Use this method to:

        - Rotate client credentials
        - Update provider endpoints
        - Modify claim mappings
        - Change authentication policies
        - Toggle SSO enforcement

        ### Examples

        - Update credentials:

          Rotates client ID and secret.

          ```yaml
          ssoConfigurationId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          clientId: "new-client-id"
          clientSecret: "new-client-secret"
          ```

        - Update provider status:

          Activates or deactivates SSO provider.

          ```yaml
          ssoConfigurationId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          state: SSO_CONFIGURATION_STATE_ACTIVE
          ```

        Args:
          sso_configuration_id: sso_configuration_id is the ID of the SSO configuration to update

          claims: claims are key/value pairs that defines a mapping of claims issued by the IdP.

          client_id: client_id is the client ID of the SSO provider

          client_secret: client_secret is the client secret of the SSO provider

          issuer_url: issuer_url is the URL of the IdP issuer

          state: state is the state of the SSO configuration

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.OrganizationService/UpdateSSOConfiguration",
            body=maybe_transform(
                {
                    "sso_configuration_id": sso_configuration_id,
                    "claims": claims,
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "email_domain": email_domain,
                    "issuer_url": issuer_url,
                    "state": state,
                },
                sso_configuration_update_params.SSOConfigurationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def list(
        self,
        *,
        organization_id: str,
        token: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        pagination: sso_configuration_list_params.Pagination | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSSOConfigurationsPage[SSOConfiguration]:
        """
        Lists and filters SSO configurations for an organization.

        Use this method to:

        - View all SSO providers
        - Monitor authentication status
        - Audit security settings
        - Manage provider configurations

        ### Examples

        - List active configurations:

          Shows all active SSO providers.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          pagination:
            pageSize: 20
          ```

        - List by provider type:

          Shows custom SSO configurations.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          pagination:
            pageSize: 20
            token: "next-page-token-from-previous-response"
          ```

        Args:
          organization_id: organization_id is the ID of the organization to list SSO configurations for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.OrganizationService/ListSSOConfigurations",
            page=SyncSSOConfigurationsPage[SSOConfiguration],
            body=maybe_transform(
                {
                    "organization_id": organization_id,
                    "pagination": pagination,
                },
                sso_configuration_list_params.SSOConfigurationListParams,
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
                    sso_configuration_list_params.SSOConfigurationListParams,
                ),
            ),
            model=SSOConfiguration,
            method="post",
        )

    def delete(
        self,
        *,
        sso_configuration_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Removes an SSO configuration from an organization.

        Use this method to:

        - Disable SSO authentication
        - Remove outdated providers
        - Clean up unused configurations

        ### Examples

        - Delete SSO configuration:

          Removes a specific SSO configuration.

          ```yaml
          ssoConfigurationId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.OrganizationService/DeleteSSOConfiguration",
            body=maybe_transform(
                {"sso_configuration_id": sso_configuration_id},
                sso_configuration_delete_params.SSOConfigurationDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncSSOConfigurationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSSOConfigurationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSSOConfigurationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSSOConfigurationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return AsyncSSOConfigurationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        client_id: str,
        client_secret: str,
        email_domain: str,
        issuer_url: str,
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SSOConfigurationCreateResponse:
        """
        Creates or updates SSO configuration for organizational authentication.

        Use this method to:

        - Configure OIDC-based SSO providers
        - Set up built-in providers (Google, GitHub, etc.)
        - Define custom identity providers
        - Manage authentication policies

        ### Examples

        - Configure built-in Google SSO:

          Sets up SSO using Google Workspace.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          clientId: "012345678-abcdefghijklmnopqrstuvwxyz.apps.googleusercontent.com"
          clientSecret: "GOCSPX-abcdefghijklmnopqrstuvwxyz123456"
          issuerUrl: "https://accounts.google.com"
          emailDomain: "acme-corp.com"
          ```

        - Configure custom OIDC provider:

          Sets up SSO with a custom identity provider.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          clientId: "acme-corp-gitpod"
          clientSecret: "secret-token-value"
          issuerUrl: "https://sso.acme-corp.com"
          emailDomain: "acme-corp.com"
          ```

        Args:
          client_id: client_id is the client ID of the OIDC application set on the IdP

          client_secret: client_secret is the client secret of the OIDC application set on the IdP

          email_domain: email_domain is the domain that is allowed to sign in to the organization

          issuer_url: issuer_url is the URL of the IdP issuer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.OrganizationService/CreateSSOConfiguration",
            body=await async_maybe_transform(
                {
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "email_domain": email_domain,
                    "issuer_url": issuer_url,
                    "organization_id": organization_id,
                },
                sso_configuration_create_params.SSOConfigurationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SSOConfigurationCreateResponse,
        )

    async def retrieve(
        self,
        *,
        sso_configuration_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SSOConfigurationRetrieveResponse:
        """
        Retrieves a specific SSO configuration.

        Use this method to:

        - View SSO provider details
        - Check configuration status
        - Verify SSO settings

        ### Examples

        - Get SSO configuration:

          Retrieves details of a specific SSO configuration.

          ```yaml
          ssoConfigurationId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          sso_configuration_id: sso_configuration_id is the ID of the SSO configuration to get

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.OrganizationService/GetSSOConfiguration",
            body=await async_maybe_transform(
                {"sso_configuration_id": sso_configuration_id},
                sso_configuration_retrieve_params.SSOConfigurationRetrieveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SSOConfigurationRetrieveResponse,
        )

    async def update(
        self,
        *,
        sso_configuration_id: str,
        claims: Dict[str, str] | NotGiven = NOT_GIVEN,
        client_id: Optional[str] | NotGiven = NOT_GIVEN,
        client_secret: Optional[str] | NotGiven = NOT_GIVEN,
        email_domain: Optional[str] | NotGiven = NOT_GIVEN,
        issuer_url: Optional[str] | NotGiven = NOT_GIVEN,
        state: Optional[SSOConfigurationState] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Updates SSO provider settings and authentication rules.

        Use this method to:

        - Rotate client credentials
        - Update provider endpoints
        - Modify claim mappings
        - Change authentication policies
        - Toggle SSO enforcement

        ### Examples

        - Update credentials:

          Rotates client ID and secret.

          ```yaml
          ssoConfigurationId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          clientId: "new-client-id"
          clientSecret: "new-client-secret"
          ```

        - Update provider status:

          Activates or deactivates SSO provider.

          ```yaml
          ssoConfigurationId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          state: SSO_CONFIGURATION_STATE_ACTIVE
          ```

        Args:
          sso_configuration_id: sso_configuration_id is the ID of the SSO configuration to update

          claims: claims are key/value pairs that defines a mapping of claims issued by the IdP.

          client_id: client_id is the client ID of the SSO provider

          client_secret: client_secret is the client secret of the SSO provider

          issuer_url: issuer_url is the URL of the IdP issuer

          state: state is the state of the SSO configuration

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.OrganizationService/UpdateSSOConfiguration",
            body=await async_maybe_transform(
                {
                    "sso_configuration_id": sso_configuration_id,
                    "claims": claims,
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "email_domain": email_domain,
                    "issuer_url": issuer_url,
                    "state": state,
                },
                sso_configuration_update_params.SSOConfigurationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def list(
        self,
        *,
        organization_id: str,
        token: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        pagination: sso_configuration_list_params.Pagination | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[SSOConfiguration, AsyncSSOConfigurationsPage[SSOConfiguration]]:
        """
        Lists and filters SSO configurations for an organization.

        Use this method to:

        - View all SSO providers
        - Monitor authentication status
        - Audit security settings
        - Manage provider configurations

        ### Examples

        - List active configurations:

          Shows all active SSO providers.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          pagination:
            pageSize: 20
          ```

        - List by provider type:

          Shows custom SSO configurations.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          pagination:
            pageSize: 20
            token: "next-page-token-from-previous-response"
          ```

        Args:
          organization_id: organization_id is the ID of the organization to list SSO configurations for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.OrganizationService/ListSSOConfigurations",
            page=AsyncSSOConfigurationsPage[SSOConfiguration],
            body=maybe_transform(
                {
                    "organization_id": organization_id,
                    "pagination": pagination,
                },
                sso_configuration_list_params.SSOConfigurationListParams,
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
                    sso_configuration_list_params.SSOConfigurationListParams,
                ),
            ),
            model=SSOConfiguration,
            method="post",
        )

    async def delete(
        self,
        *,
        sso_configuration_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Removes an SSO configuration from an organization.

        Use this method to:

        - Disable SSO authentication
        - Remove outdated providers
        - Clean up unused configurations

        ### Examples

        - Delete SSO configuration:

          Removes a specific SSO configuration.

          ```yaml
          ssoConfigurationId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.OrganizationService/DeleteSSOConfiguration",
            body=await async_maybe_transform(
                {"sso_configuration_id": sso_configuration_id},
                sso_configuration_delete_params.SSOConfigurationDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class SSOConfigurationsResourceWithRawResponse:
    def __init__(self, sso_configurations: SSOConfigurationsResource) -> None:
        self._sso_configurations = sso_configurations

        self.create = to_raw_response_wrapper(
            sso_configurations.create,
        )
        self.retrieve = to_raw_response_wrapper(
            sso_configurations.retrieve,
        )
        self.update = to_raw_response_wrapper(
            sso_configurations.update,
        )
        self.list = to_raw_response_wrapper(
            sso_configurations.list,
        )
        self.delete = to_raw_response_wrapper(
            sso_configurations.delete,
        )


class AsyncSSOConfigurationsResourceWithRawResponse:
    def __init__(self, sso_configurations: AsyncSSOConfigurationsResource) -> None:
        self._sso_configurations = sso_configurations

        self.create = async_to_raw_response_wrapper(
            sso_configurations.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            sso_configurations.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            sso_configurations.update,
        )
        self.list = async_to_raw_response_wrapper(
            sso_configurations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            sso_configurations.delete,
        )


class SSOConfigurationsResourceWithStreamingResponse:
    def __init__(self, sso_configurations: SSOConfigurationsResource) -> None:
        self._sso_configurations = sso_configurations

        self.create = to_streamed_response_wrapper(
            sso_configurations.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            sso_configurations.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            sso_configurations.update,
        )
        self.list = to_streamed_response_wrapper(
            sso_configurations.list,
        )
        self.delete = to_streamed_response_wrapper(
            sso_configurations.delete,
        )


class AsyncSSOConfigurationsResourceWithStreamingResponse:
    def __init__(self, sso_configurations: AsyncSSOConfigurationsResource) -> None:
        self._sso_configurations = sso_configurations

        self.create = async_to_streamed_response_wrapper(
            sso_configurations.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            sso_configurations.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            sso_configurations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            sso_configurations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            sso_configurations.delete,
        )
