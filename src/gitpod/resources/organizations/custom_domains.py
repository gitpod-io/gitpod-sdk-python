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
from ..._base_client import make_request_options
from ...types.organizations import (
    CustomDomainProvider,
    custom_domain_create_params,
    custom_domain_delete_params,
    custom_domain_update_params,
    custom_domain_retrieve_params,
)
from ...types.organizations.custom_domain_provider import CustomDomainProvider
from ...types.organizations.custom_domain_create_response import CustomDomainCreateResponse
from ...types.organizations.custom_domain_update_response import CustomDomainUpdateResponse
from ...types.organizations.custom_domain_retrieve_response import CustomDomainRetrieveResponse

__all__ = ["CustomDomainsResource", "AsyncCustomDomainsResource"]


class CustomDomainsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CustomDomainsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return CustomDomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomDomainsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return CustomDomainsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        domain_name: str,
        organization_id: str,
        aws_account_id: Optional[str] | Omit = omit,
        cloud_account_id: Optional[str] | Omit = omit,
        provider: CustomDomainProvider | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomDomainCreateResponse:
        """
        Creates a custom domain configuration for an organization.

        Use this method to configure custom domains for organization workspaces

        ### Examples

        - Configure AWS custom domain:

          Sets up a custom domain with AWS provider.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          domainName: "workspaces.acme-corp.com"
          provider: CUSTOM_DOMAIN_PROVIDER_AWS
          awsAccountId: "123456789012"
          ```

        Args:
          domain_name: domain_name is the custom domain name

          organization_id: organization_id is the ID of the organization to create the custom domain for

          aws_account_id: aws_account_id is the AWS account ID (deprecated: use cloud_account_id)

          cloud_account_id: cloud_account_id is the unified cloud account identifier (AWS Account ID or GCP
              Project ID)

          provider: provider is the cloud provider for this custom domain

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.OrganizationService/CreateCustomDomain",
            body=maybe_transform(
                {
                    "domain_name": domain_name,
                    "organization_id": organization_id,
                    "aws_account_id": aws_account_id,
                    "cloud_account_id": cloud_account_id,
                    "provider": provider,
                },
                custom_domain_create_params.CustomDomainCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomDomainCreateResponse,
        )

    def retrieve(
        self,
        *,
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomDomainRetrieveResponse:
        """
        Retrieves a specific custom domain configuration.

        Use this method to view custom domain details

        ### Examples

        - Get custom domain configuration:

          Retrieves details of a specific custom domain.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          ```

        Args:
          organization_id: organization_id is the ID of the organization to retrieve custom domain for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.OrganizationService/GetCustomDomain",
            body=maybe_transform(
                {"organization_id": organization_id}, custom_domain_retrieve_params.CustomDomainRetrieveParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomDomainRetrieveResponse,
        )

    def update(
        self,
        *,
        domain_name: str,
        organization_id: str,
        aws_account_id: Optional[str] | Omit = omit,
        cloud_account_id: Optional[str] | Omit = omit,
        provider: Optional[CustomDomainProvider] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomDomainUpdateResponse:
        """
        Updates custom domain configuration settings.

        Use this method to:

        - Update cloud provider settings
        - Change AWS account ID
        - Modify domain configuration

        ### Examples

        - Update AWS account ID:

          Changes the AWS account ID for the custom domain.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          domainName: "workspaces.acme-corp.com"
          awsAccountId: "987654321098"
          ```

        Args:
          domain_name: domain_name is the custom domain name

          organization_id: organization_id is the ID of the organization to update custom domain for

          aws_account_id: aws_account_id is the AWS account ID (deprecated: use cloud_account_id)

          cloud_account_id: cloud_account_id is the unified cloud account identifier (AWS Account ID or GCP
              Project ID)

          provider: provider is the cloud provider for this custom domain

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.OrganizationService/UpdateCustomDomain",
            body=maybe_transform(
                {
                    "domain_name": domain_name,
                    "organization_id": organization_id,
                    "aws_account_id": aws_account_id,
                    "cloud_account_id": cloud_account_id,
                    "provider": provider,
                },
                custom_domain_update_params.CustomDomainUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomDomainUpdateResponse,
        )

    def delete(
        self,
        *,
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Removes a custom domain configuration from an organization.

        Use this method to:

        - Disable custom domain functionality
        - Remove outdated configurations
        - Clean up unused domains

        ### Examples

        - Delete custom domain configuration:

          Removes a specific custom domain configuration.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          ```

        Args:
          organization_id: organization_id is the ID of the organization to delete custom domain for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.OrganizationService/DeleteCustomDomain",
            body=maybe_transform(
                {"organization_id": organization_id}, custom_domain_delete_params.CustomDomainDeleteParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncCustomDomainsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCustomDomainsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomDomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomDomainsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return AsyncCustomDomainsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        domain_name: str,
        organization_id: str,
        aws_account_id: Optional[str] | Omit = omit,
        cloud_account_id: Optional[str] | Omit = omit,
        provider: CustomDomainProvider | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomDomainCreateResponse:
        """
        Creates a custom domain configuration for an organization.

        Use this method to configure custom domains for organization workspaces

        ### Examples

        - Configure AWS custom domain:

          Sets up a custom domain with AWS provider.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          domainName: "workspaces.acme-corp.com"
          provider: CUSTOM_DOMAIN_PROVIDER_AWS
          awsAccountId: "123456789012"
          ```

        Args:
          domain_name: domain_name is the custom domain name

          organization_id: organization_id is the ID of the organization to create the custom domain for

          aws_account_id: aws_account_id is the AWS account ID (deprecated: use cloud_account_id)

          cloud_account_id: cloud_account_id is the unified cloud account identifier (AWS Account ID or GCP
              Project ID)

          provider: provider is the cloud provider for this custom domain

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.OrganizationService/CreateCustomDomain",
            body=await async_maybe_transform(
                {
                    "domain_name": domain_name,
                    "organization_id": organization_id,
                    "aws_account_id": aws_account_id,
                    "cloud_account_id": cloud_account_id,
                    "provider": provider,
                },
                custom_domain_create_params.CustomDomainCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomDomainCreateResponse,
        )

    async def retrieve(
        self,
        *,
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomDomainRetrieveResponse:
        """
        Retrieves a specific custom domain configuration.

        Use this method to view custom domain details

        ### Examples

        - Get custom domain configuration:

          Retrieves details of a specific custom domain.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          ```

        Args:
          organization_id: organization_id is the ID of the organization to retrieve custom domain for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.OrganizationService/GetCustomDomain",
            body=await async_maybe_transform(
                {"organization_id": organization_id}, custom_domain_retrieve_params.CustomDomainRetrieveParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomDomainRetrieveResponse,
        )

    async def update(
        self,
        *,
        domain_name: str,
        organization_id: str,
        aws_account_id: Optional[str] | Omit = omit,
        cloud_account_id: Optional[str] | Omit = omit,
        provider: Optional[CustomDomainProvider] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomDomainUpdateResponse:
        """
        Updates custom domain configuration settings.

        Use this method to:

        - Update cloud provider settings
        - Change AWS account ID
        - Modify domain configuration

        ### Examples

        - Update AWS account ID:

          Changes the AWS account ID for the custom domain.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          domainName: "workspaces.acme-corp.com"
          awsAccountId: "987654321098"
          ```

        Args:
          domain_name: domain_name is the custom domain name

          organization_id: organization_id is the ID of the organization to update custom domain for

          aws_account_id: aws_account_id is the AWS account ID (deprecated: use cloud_account_id)

          cloud_account_id: cloud_account_id is the unified cloud account identifier (AWS Account ID or GCP
              Project ID)

          provider: provider is the cloud provider for this custom domain

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.OrganizationService/UpdateCustomDomain",
            body=await async_maybe_transform(
                {
                    "domain_name": domain_name,
                    "organization_id": organization_id,
                    "aws_account_id": aws_account_id,
                    "cloud_account_id": cloud_account_id,
                    "provider": provider,
                },
                custom_domain_update_params.CustomDomainUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomDomainUpdateResponse,
        )

    async def delete(
        self,
        *,
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Removes a custom domain configuration from an organization.

        Use this method to:

        - Disable custom domain functionality
        - Remove outdated configurations
        - Clean up unused domains

        ### Examples

        - Delete custom domain configuration:

          Removes a specific custom domain configuration.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          ```

        Args:
          organization_id: organization_id is the ID of the organization to delete custom domain for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.OrganizationService/DeleteCustomDomain",
            body=await async_maybe_transform(
                {"organization_id": organization_id}, custom_domain_delete_params.CustomDomainDeleteParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class CustomDomainsResourceWithRawResponse:
    def __init__(self, custom_domains: CustomDomainsResource) -> None:
        self._custom_domains = custom_domains

        self.create = to_raw_response_wrapper(
            custom_domains.create,
        )
        self.retrieve = to_raw_response_wrapper(
            custom_domains.retrieve,
        )
        self.update = to_raw_response_wrapper(
            custom_domains.update,
        )
        self.delete = to_raw_response_wrapper(
            custom_domains.delete,
        )


class AsyncCustomDomainsResourceWithRawResponse:
    def __init__(self, custom_domains: AsyncCustomDomainsResource) -> None:
        self._custom_domains = custom_domains

        self.create = async_to_raw_response_wrapper(
            custom_domains.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            custom_domains.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            custom_domains.update,
        )
        self.delete = async_to_raw_response_wrapper(
            custom_domains.delete,
        )


class CustomDomainsResourceWithStreamingResponse:
    def __init__(self, custom_domains: CustomDomainsResource) -> None:
        self._custom_domains = custom_domains

        self.create = to_streamed_response_wrapper(
            custom_domains.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            custom_domains.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            custom_domains.update,
        )
        self.delete = to_streamed_response_wrapper(
            custom_domains.delete,
        )


class AsyncCustomDomainsResourceWithStreamingResponse:
    def __init__(self, custom_domains: AsyncCustomDomainsResource) -> None:
        self._custom_domains = custom_domains

        self.create = async_to_streamed_response_wrapper(
            custom_domains.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            custom_domains.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            custom_domains.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            custom_domains.delete,
        )
