# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...pagination import SyncDomainVerificationsPage, AsyncDomainVerificationsPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.organizations import (
    domain_verification_list_params,
    domain_verification_create_params,
    domain_verification_delete_params,
    domain_verification_verify_params,
    domain_verification_retrieve_params,
)
from ...types.organizations.domain_verification import DomainVerification
from ...types.organizations.domain_verification_create_response import DomainVerificationCreateResponse
from ...types.organizations.domain_verification_verify_response import DomainVerificationVerifyResponse
from ...types.organizations.domain_verification_retrieve_response import DomainVerificationRetrieveResponse

__all__ = ["DomainVerificationsResource", "AsyncDomainVerificationsResource"]


class DomainVerificationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DomainVerificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return DomainVerificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DomainVerificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return DomainVerificationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        domain: str,
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DomainVerificationCreateResponse:
        """
        Initiates domain verification process to enable organization features.

        Use this method to:

        - Start domain ownership verification
        - Enable automatic team joining
        - Set up SSO restrictions
        - Configure email-based policies

        ### Examples

        - Verify primary domain:

          Starts verification for main company domain.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          domain: "acme-corp.com"
          ```

        - Verify subsidiary domain:

          Adds verification for additional company domain.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          domain: "acme-subsidiary.com"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.OrganizationService/CreateDomainVerification",
            body=maybe_transform(
                {
                    "domain": domain,
                    "organization_id": organization_id,
                },
                domain_verification_create_params.DomainVerificationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DomainVerificationCreateResponse,
        )

    def retrieve(
        self,
        *,
        domain_verification_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DomainVerificationRetrieveResponse:
        """
        Retrieves the status of a domain verification request.

        Use this method to:

        - Check verification progress
        - View verification requirements
        - Monitor domain status

        ### Examples

        - Get verification status:

          Checks the current state of a domain verification.

          ```yaml
          domainVerificationId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.OrganizationService/GetDomainVerification",
            body=maybe_transform(
                {"domain_verification_id": domain_verification_id},
                domain_verification_retrieve_params.DomainVerificationRetrieveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DomainVerificationRetrieveResponse,
        )

    def list(
        self,
        *,
        organization_id: str,
        token: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        pagination: domain_verification_list_params.Pagination | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncDomainVerificationsPage[DomainVerification]:
        """
        Lists and monitors domain verification status across an organization.

        Use this method to:

        - Track verification progress
        - View all verified domains
        - Monitor pending verifications
        - Audit domain settings

        ### Examples

        - List all verifications:

          Shows all domain verifications regardless of status.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          pagination:
            pageSize: 20
          ```

        - List with pagination:

          Retrieves next page of verifications.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          pagination:
            pageSize: 20
            token: "next-page-token-from-previous-response"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.OrganizationService/ListDomainVerifications",
            page=SyncDomainVerificationsPage[DomainVerification],
            body=maybe_transform(
                {
                    "organization_id": organization_id,
                    "pagination": pagination,
                },
                domain_verification_list_params.DomainVerificationListParams,
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
                    domain_verification_list_params.DomainVerificationListParams,
                ),
            ),
            model=DomainVerification,
            method="post",
        )

    def delete(
        self,
        *,
        domain_verification_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Removes a domain verification request.

        Use this method to:

        - Cancel pending verifications
        - Remove verified domains
        - Clean up unused domain records

        ### Examples

        - Delete verification:

          Removes a domain verification request.

          ```yaml
          domainVerificationId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.OrganizationService/DeleteDomainVerification",
            body=maybe_transform(
                {"domain_verification_id": domain_verification_id},
                domain_verification_delete_params.DomainVerificationDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def verify(
        self,
        *,
        domain_verification_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DomainVerificationVerifyResponse:
        """
        Verifies domain ownership for an organization.

        Use this method to:

        - Complete domain verification process
        - Enable domain-based features
        - Validate DNS configuration

        ### Examples

        - Verify domain ownership:

          Verifies ownership after DNS records are configured.

          ```yaml
          domainVerificationId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.OrganizationService/VerifyDomain",
            body=maybe_transform(
                {"domain_verification_id": domain_verification_id},
                domain_verification_verify_params.DomainVerificationVerifyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DomainVerificationVerifyResponse,
        )


class AsyncDomainVerificationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDomainVerificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDomainVerificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDomainVerificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return AsyncDomainVerificationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        domain: str,
        organization_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DomainVerificationCreateResponse:
        """
        Initiates domain verification process to enable organization features.

        Use this method to:

        - Start domain ownership verification
        - Enable automatic team joining
        - Set up SSO restrictions
        - Configure email-based policies

        ### Examples

        - Verify primary domain:

          Starts verification for main company domain.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          domain: "acme-corp.com"
          ```

        - Verify subsidiary domain:

          Adds verification for additional company domain.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          domain: "acme-subsidiary.com"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.OrganizationService/CreateDomainVerification",
            body=await async_maybe_transform(
                {
                    "domain": domain,
                    "organization_id": organization_id,
                },
                domain_verification_create_params.DomainVerificationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DomainVerificationCreateResponse,
        )

    async def retrieve(
        self,
        *,
        domain_verification_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DomainVerificationRetrieveResponse:
        """
        Retrieves the status of a domain verification request.

        Use this method to:

        - Check verification progress
        - View verification requirements
        - Monitor domain status

        ### Examples

        - Get verification status:

          Checks the current state of a domain verification.

          ```yaml
          domainVerificationId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.OrganizationService/GetDomainVerification",
            body=await async_maybe_transform(
                {"domain_verification_id": domain_verification_id},
                domain_verification_retrieve_params.DomainVerificationRetrieveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DomainVerificationRetrieveResponse,
        )

    def list(
        self,
        *,
        organization_id: str,
        token: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        pagination: domain_verification_list_params.Pagination | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[DomainVerification, AsyncDomainVerificationsPage[DomainVerification]]:
        """
        Lists and monitors domain verification status across an organization.

        Use this method to:

        - Track verification progress
        - View all verified domains
        - Monitor pending verifications
        - Audit domain settings

        ### Examples

        - List all verifications:

          Shows all domain verifications regardless of status.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          pagination:
            pageSize: 20
          ```

        - List with pagination:

          Retrieves next page of verifications.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          pagination:
            pageSize: 20
            token: "next-page-token-from-previous-response"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.OrganizationService/ListDomainVerifications",
            page=AsyncDomainVerificationsPage[DomainVerification],
            body=maybe_transform(
                {
                    "organization_id": organization_id,
                    "pagination": pagination,
                },
                domain_verification_list_params.DomainVerificationListParams,
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
                    domain_verification_list_params.DomainVerificationListParams,
                ),
            ),
            model=DomainVerification,
            method="post",
        )

    async def delete(
        self,
        *,
        domain_verification_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Removes a domain verification request.

        Use this method to:

        - Cancel pending verifications
        - Remove verified domains
        - Clean up unused domain records

        ### Examples

        - Delete verification:

          Removes a domain verification request.

          ```yaml
          domainVerificationId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.OrganizationService/DeleteDomainVerification",
            body=await async_maybe_transform(
                {"domain_verification_id": domain_verification_id},
                domain_verification_delete_params.DomainVerificationDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def verify(
        self,
        *,
        domain_verification_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DomainVerificationVerifyResponse:
        """
        Verifies domain ownership for an organization.

        Use this method to:

        - Complete domain verification process
        - Enable domain-based features
        - Validate DNS configuration

        ### Examples

        - Verify domain ownership:

          Verifies ownership after DNS records are configured.

          ```yaml
          domainVerificationId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.OrganizationService/VerifyDomain",
            body=await async_maybe_transform(
                {"domain_verification_id": domain_verification_id},
                domain_verification_verify_params.DomainVerificationVerifyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DomainVerificationVerifyResponse,
        )


class DomainVerificationsResourceWithRawResponse:
    def __init__(self, domain_verifications: DomainVerificationsResource) -> None:
        self._domain_verifications = domain_verifications

        self.create = to_raw_response_wrapper(
            domain_verifications.create,
        )
        self.retrieve = to_raw_response_wrapper(
            domain_verifications.retrieve,
        )
        self.list = to_raw_response_wrapper(
            domain_verifications.list,
        )
        self.delete = to_raw_response_wrapper(
            domain_verifications.delete,
        )
        self.verify = to_raw_response_wrapper(
            domain_verifications.verify,
        )


class AsyncDomainVerificationsResourceWithRawResponse:
    def __init__(self, domain_verifications: AsyncDomainVerificationsResource) -> None:
        self._domain_verifications = domain_verifications

        self.create = async_to_raw_response_wrapper(
            domain_verifications.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            domain_verifications.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            domain_verifications.list,
        )
        self.delete = async_to_raw_response_wrapper(
            domain_verifications.delete,
        )
        self.verify = async_to_raw_response_wrapper(
            domain_verifications.verify,
        )


class DomainVerificationsResourceWithStreamingResponse:
    def __init__(self, domain_verifications: DomainVerificationsResource) -> None:
        self._domain_verifications = domain_verifications

        self.create = to_streamed_response_wrapper(
            domain_verifications.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            domain_verifications.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            domain_verifications.list,
        )
        self.delete = to_streamed_response_wrapper(
            domain_verifications.delete,
        )
        self.verify = to_streamed_response_wrapper(
            domain_verifications.verify,
        )


class AsyncDomainVerificationsResourceWithStreamingResponse:
    def __init__(self, domain_verifications: AsyncDomainVerificationsResource) -> None:
        self._domain_verifications = domain_verifications

        self.create = async_to_streamed_response_wrapper(
            domain_verifications.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            domain_verifications.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            domain_verifications.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            domain_verifications.delete,
        )
        self.verify = async_to_streamed_response_wrapper(
            domain_verifications.verify,
        )
