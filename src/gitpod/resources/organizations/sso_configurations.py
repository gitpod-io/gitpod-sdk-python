# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, overload

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    required_args,
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
from ...types.organizations import (
    sso_configuration_list_params,
    sso_configuration_create_params,
    sso_configuration_delete_params,
    sso_configuration_update_params,
    sso_configuration_retrieve_params,
)
from ...types.organizations.sso_configuration_list_response import SSOConfigurationListResponse
from ...types.organizations.sso_configuration_create_response import SSOConfigurationCreateResponse
from ...types.organizations.sso_configuration_retrieve_response import SSOConfigurationRetrieveResponse

__all__ = ["SSOConfigurationsResource", "AsyncSSOConfigurationsResource"]


class SSOConfigurationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SSOConfigurationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return SSOConfigurationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SSOConfigurationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return SSOConfigurationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        client_id: str | NotGiven = NOT_GIVEN,
        client_secret: str | NotGiven = NOT_GIVEN,
        email_domain: str | NotGiven = NOT_GIVEN,
        issuer_url: str | NotGiven = NOT_GIVEN,
        organization_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SSOConfigurationCreateResponse:
        """
        CreateSSOConfiguration creates a new SSO configuration for the organization.

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
        sso_configuration_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SSOConfigurationRetrieveResponse:
        """
        GetSSOConfiguration returns an SSO configuration.

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

    @overload
    def update(
        self,
        *,
        client_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        UpdateSSOConfiguration updates the SSO configuration for the organization.

        Args:
          client_id: client_id is the client ID of the SSO provider

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        *,
        client_secret: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        UpdateSSOConfiguration updates the SSO configuration for the organization.

        Args:
          client_secret: client_secret is the client secret of the SSO provider

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        *,
        email_domain: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        UpdateSSOConfiguration updates the SSO configuration for the organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        *,
        issuer_url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        UpdateSSOConfiguration updates the SSO configuration for the organization.

        Args:
          issuer_url: issuer_url is the URL of the IdP issuer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        *,
        state: Literal[
            "SSO_CONFIGURATION_STATE_UNSPECIFIED", "SSO_CONFIGURATION_STATE_INACTIVE", "SSO_CONFIGURATION_STATE_ACTIVE"
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        UpdateSSOConfiguration updates the SSO configuration for the organization.

        Args:
          state: state is the state of the SSO configuration

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["client_id"], ["client_secret"], ["email_domain"], ["issuer_url"], ["state"])
    def update(
        self,
        *,
        client_id: str | NotGiven = NOT_GIVEN,
        client_secret: str | NotGiven = NOT_GIVEN,
        email_domain: str | NotGiven = NOT_GIVEN,
        issuer_url: str | NotGiven = NOT_GIVEN,
        state: Literal[
            "SSO_CONFIGURATION_STATE_UNSPECIFIED", "SSO_CONFIGURATION_STATE_INACTIVE", "SSO_CONFIGURATION_STATE_ACTIVE"
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        return self._post(
            "/gitpod.v1.OrganizationService/UpdateSSOConfiguration",
            body=maybe_transform(
                {
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
        token: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        organization_id: str | NotGiven = NOT_GIVEN,
        pagination: sso_configuration_list_params.Pagination | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SSOConfigurationListResponse:
        """
        ListSSOConfigurations lists all SSO configurations matching provided filters.

        Args:
          organization_id: organization_id is the ID of the organization to list SSO configurations for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.OrganizationService/ListSSOConfigurations",
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
            cast_to=SSOConfigurationListResponse,
        )

    def delete(
        self,
        *,
        sso_configuration_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        DeleteSSOConfiguration deletes an SSO configuration.

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

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSSOConfigurationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSSOConfigurationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/gitpod-python#with_streaming_response
        """
        return AsyncSSOConfigurationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        client_id: str | NotGiven = NOT_GIVEN,
        client_secret: str | NotGiven = NOT_GIVEN,
        email_domain: str | NotGiven = NOT_GIVEN,
        issuer_url: str | NotGiven = NOT_GIVEN,
        organization_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SSOConfigurationCreateResponse:
        """
        CreateSSOConfiguration creates a new SSO configuration for the organization.

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
        sso_configuration_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SSOConfigurationRetrieveResponse:
        """
        GetSSOConfiguration returns an SSO configuration.

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

    @overload
    async def update(
        self,
        *,
        client_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        UpdateSSOConfiguration updates the SSO configuration for the organization.

        Args:
          client_id: client_id is the client ID of the SSO provider

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        *,
        client_secret: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        UpdateSSOConfiguration updates the SSO configuration for the organization.

        Args:
          client_secret: client_secret is the client secret of the SSO provider

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        *,
        email_domain: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        UpdateSSOConfiguration updates the SSO configuration for the organization.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        *,
        issuer_url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        UpdateSSOConfiguration updates the SSO configuration for the organization.

        Args:
          issuer_url: issuer_url is the URL of the IdP issuer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        *,
        state: Literal[
            "SSO_CONFIGURATION_STATE_UNSPECIFIED", "SSO_CONFIGURATION_STATE_INACTIVE", "SSO_CONFIGURATION_STATE_ACTIVE"
        ],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        UpdateSSOConfiguration updates the SSO configuration for the organization.

        Args:
          state: state is the state of the SSO configuration

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["client_id"], ["client_secret"], ["email_domain"], ["issuer_url"], ["state"])
    async def update(
        self,
        *,
        client_id: str | NotGiven = NOT_GIVEN,
        client_secret: str | NotGiven = NOT_GIVEN,
        email_domain: str | NotGiven = NOT_GIVEN,
        issuer_url: str | NotGiven = NOT_GIVEN,
        state: Literal[
            "SSO_CONFIGURATION_STATE_UNSPECIFIED", "SSO_CONFIGURATION_STATE_INACTIVE", "SSO_CONFIGURATION_STATE_ACTIVE"
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        return await self._post(
            "/gitpod.v1.OrganizationService/UpdateSSOConfiguration",
            body=await async_maybe_transform(
                {
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

    async def list(
        self,
        *,
        token: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        organization_id: str | NotGiven = NOT_GIVEN,
        pagination: sso_configuration_list_params.Pagination | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SSOConfigurationListResponse:
        """
        ListSSOConfigurations lists all SSO configurations matching provided filters.

        Args:
          organization_id: organization_id is the ID of the organization to list SSO configurations for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.OrganizationService/ListSSOConfigurations",
            body=await async_maybe_transform(
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
                query=await async_maybe_transform(
                    {
                        "token": token,
                        "page_size": page_size,
                    },
                    sso_configuration_list_params.SSOConfigurationListParams,
                ),
            ),
            cast_to=SSOConfigurationListResponse,
        )

    async def delete(
        self,
        *,
        sso_configuration_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        DeleteSSOConfiguration deletes an SSO configuration.

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
