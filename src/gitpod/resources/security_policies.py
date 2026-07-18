# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    security_policy_list_params,
    security_policy_create_params,
    security_policy_delete_params,
    security_policy_update_params,
    security_policy_retrieve_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncSecurityPoliciesPage, AsyncSecurityPoliciesPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.security_policy import SecurityPolicy
from ..types.security_policy_create_response import SecurityPolicyCreateResponse
from ..types.security_policy_update_response import SecurityPolicyUpdateResponse
from ..types.security_policy_retrieve_response import SecurityPolicyRetrieveResponse

__all__ = ["SecurityPoliciesResource", "AsyncSecurityPoliciesResource"]


class SecurityPoliciesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SecurityPoliciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SecurityPoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SecurityPoliciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return SecurityPoliciesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        metadata: security_policy_create_params.Metadata,
        spec: security_policy_create_params.Spec,
        organization_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecurityPolicyCreateResponse:
        """
        Creates a new security policy.

        Use this method to:

        - Define environment access controls
        - Configure audited or blocked operations
        - Manage organization security posture

        ### Examples

        - Create security policy:

          Creates an audit-first Veto Exec policy with one audited bare name and one
          blocked absolute path. Creation stores an inactive definition; assigning it as
          the organization default validates materializability.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          metadata:
            name: "Veto Exec audit-first"
          spec:
            executables:
              defaultEffect: EFFECT_ALLOW
              rules:
                - path: "npx"
                  effect: EFFECT_AUDIT
                - path: "/usr/bin/curl"
                  effect: EFFECT_BLOCK
          ```

        Args:
          spec: Mandate/deploy security agents, e.g. CrowdStrike. Mandate credential
              security/proxy use. These can be modeled later as explicit fields if needed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.SecurityService/CreateSecurityPolicy",
            body=maybe_transform(
                {
                    "metadata": metadata,
                    "spec": spec,
                    "organization_id": organization_id,
                },
                security_policy_create_params.SecurityPolicyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecurityPolicyCreateResponse,
        )

    def retrieve(
        self,
        *,
        security_policy_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecurityPolicyRetrieveResponse:
        """
        Gets details about a specific security policy.

        Use this method to:

        - View security policy configuration
        - Inspect enforcement rules

        ### Examples

        - Get security policy:

          Retrieves a security policy by ID.

          ```yaml
          securityPolicyId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.SecurityService/GetSecurityPolicy",
            body=maybe_transform(
                {"security_policy_id": security_policy_id}, security_policy_retrieve_params.SecurityPolicyRetrieveParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecurityPolicyRetrieveResponse,
        )

    def update(
        self,
        *,
        metadata: security_policy_update_params.Metadata | Omit = omit,
        security_policy_id: str | Omit = omit,
        spec: security_policy_update_params.Spec | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecurityPolicyUpdateResponse:
        """
        Updates a security policy.

        Use this method to:

        - Rename a security policy
        - Change enforcement rules
        - Update auditing behavior

        ### Examples

        - Update security policy:

          Promotes one executable rule from audit to block while leaving unmatched
          executables allowed. Updating an assigned policy validates materializability;
          updating an unassigned policy only stores its spec.

          ```yaml
          securityPolicyId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          spec:
            executables:
              defaultEffect: EFFECT_ALLOW
              rules:
                - path: "npx"
                  effect: EFFECT_BLOCK
                - path: "/usr/bin/curl"
                  effect: EFFECT_BLOCK
          ```

        Args:
          spec: Mandate/deploy security agents, e.g. CrowdStrike. Mandate credential
              security/proxy use. These can be modeled later as explicit fields if needed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.SecurityService/UpdateSecurityPolicy",
            body=maybe_transform(
                {
                    "metadata": metadata,
                    "security_policy_id": security_policy_id,
                    "spec": spec,
                },
                security_policy_update_params.SecurityPolicyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecurityPolicyUpdateResponse,
        )

    def list(
        self,
        *,
        token: str | Omit = omit,
        page_size: int | Omit = omit,
        filter: security_policy_list_params.Filter | Omit = omit,
        pagination: security_policy_list_params.Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSecurityPoliciesPage[SecurityPolicy]:
        """
        Lists security policies.

        Use this method to:

        - View all security policies in an organization
        - Audit configured security controls

        ### Examples

        - List organization policies:

          Shows security policies with pagination.

          ```yaml
          filter:
            organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
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
            "/gitpod.v1.SecurityService/ListSecurityPolicies",
            page=SyncSecurityPoliciesPage[SecurityPolicy],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                security_policy_list_params.SecurityPolicyListParams,
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
                    security_policy_list_params.SecurityPolicyListParams,
                ),
            ),
            model=SecurityPolicy,
            method="post",
        )

    def delete(
        self,
        *,
        security_policy_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Deletes a security policy.

        Use this method to:

        - Remove obsolete security policies
        - Clean up unused policy definitions

        ### Examples

        - Delete security policy:

          Permanently removes a security policy.

          ```yaml
          securityPolicyId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.SecurityService/DeleteSecurityPolicy",
            body=maybe_transform(
                {"security_policy_id": security_policy_id}, security_policy_delete_params.SecurityPolicyDeleteParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncSecurityPoliciesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSecurityPoliciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSecurityPoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSecurityPoliciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return AsyncSecurityPoliciesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        metadata: security_policy_create_params.Metadata,
        spec: security_policy_create_params.Spec,
        organization_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecurityPolicyCreateResponse:
        """
        Creates a new security policy.

        Use this method to:

        - Define environment access controls
        - Configure audited or blocked operations
        - Manage organization security posture

        ### Examples

        - Create security policy:

          Creates an audit-first Veto Exec policy with one audited bare name and one
          blocked absolute path. Creation stores an inactive definition; assigning it as
          the organization default validates materializability.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          metadata:
            name: "Veto Exec audit-first"
          spec:
            executables:
              defaultEffect: EFFECT_ALLOW
              rules:
                - path: "npx"
                  effect: EFFECT_AUDIT
                - path: "/usr/bin/curl"
                  effect: EFFECT_BLOCK
          ```

        Args:
          spec: Mandate/deploy security agents, e.g. CrowdStrike. Mandate credential
              security/proxy use. These can be modeled later as explicit fields if needed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.SecurityService/CreateSecurityPolicy",
            body=await async_maybe_transform(
                {
                    "metadata": metadata,
                    "spec": spec,
                    "organization_id": organization_id,
                },
                security_policy_create_params.SecurityPolicyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecurityPolicyCreateResponse,
        )

    async def retrieve(
        self,
        *,
        security_policy_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecurityPolicyRetrieveResponse:
        """
        Gets details about a specific security policy.

        Use this method to:

        - View security policy configuration
        - Inspect enforcement rules

        ### Examples

        - Get security policy:

          Retrieves a security policy by ID.

          ```yaml
          securityPolicyId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.SecurityService/GetSecurityPolicy",
            body=await async_maybe_transform(
                {"security_policy_id": security_policy_id}, security_policy_retrieve_params.SecurityPolicyRetrieveParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecurityPolicyRetrieveResponse,
        )

    async def update(
        self,
        *,
        metadata: security_policy_update_params.Metadata | Omit = omit,
        security_policy_id: str | Omit = omit,
        spec: security_policy_update_params.Spec | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SecurityPolicyUpdateResponse:
        """
        Updates a security policy.

        Use this method to:

        - Rename a security policy
        - Change enforcement rules
        - Update auditing behavior

        ### Examples

        - Update security policy:

          Promotes one executable rule from audit to block while leaving unmatched
          executables allowed. Updating an assigned policy validates materializability;
          updating an unassigned policy only stores its spec.

          ```yaml
          securityPolicyId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          spec:
            executables:
              defaultEffect: EFFECT_ALLOW
              rules:
                - path: "npx"
                  effect: EFFECT_BLOCK
                - path: "/usr/bin/curl"
                  effect: EFFECT_BLOCK
          ```

        Args:
          spec: Mandate/deploy security agents, e.g. CrowdStrike. Mandate credential
              security/proxy use. These can be modeled later as explicit fields if needed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.SecurityService/UpdateSecurityPolicy",
            body=await async_maybe_transform(
                {
                    "metadata": metadata,
                    "security_policy_id": security_policy_id,
                    "spec": spec,
                },
                security_policy_update_params.SecurityPolicyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SecurityPolicyUpdateResponse,
        )

    def list(
        self,
        *,
        token: str | Omit = omit,
        page_size: int | Omit = omit,
        filter: security_policy_list_params.Filter | Omit = omit,
        pagination: security_policy_list_params.Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[SecurityPolicy, AsyncSecurityPoliciesPage[SecurityPolicy]]:
        """
        Lists security policies.

        Use this method to:

        - View all security policies in an organization
        - Audit configured security controls

        ### Examples

        - List organization policies:

          Shows security policies with pagination.

          ```yaml
          filter:
            organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
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
            "/gitpod.v1.SecurityService/ListSecurityPolicies",
            page=AsyncSecurityPoliciesPage[SecurityPolicy],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                security_policy_list_params.SecurityPolicyListParams,
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
                    security_policy_list_params.SecurityPolicyListParams,
                ),
            ),
            model=SecurityPolicy,
            method="post",
        )

    async def delete(
        self,
        *,
        security_policy_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Deletes a security policy.

        Use this method to:

        - Remove obsolete security policies
        - Clean up unused policy definitions

        ### Examples

        - Delete security policy:

          Permanently removes a security policy.

          ```yaml
          securityPolicyId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.SecurityService/DeleteSecurityPolicy",
            body=await async_maybe_transform(
                {"security_policy_id": security_policy_id}, security_policy_delete_params.SecurityPolicyDeleteParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class SecurityPoliciesResourceWithRawResponse:
    def __init__(self, security_policies: SecurityPoliciesResource) -> None:
        self._security_policies = security_policies

        self.create = to_raw_response_wrapper(
            security_policies.create,
        )
        self.retrieve = to_raw_response_wrapper(
            security_policies.retrieve,
        )
        self.update = to_raw_response_wrapper(
            security_policies.update,
        )
        self.list = to_raw_response_wrapper(
            security_policies.list,
        )
        self.delete = to_raw_response_wrapper(
            security_policies.delete,
        )


class AsyncSecurityPoliciesResourceWithRawResponse:
    def __init__(self, security_policies: AsyncSecurityPoliciesResource) -> None:
        self._security_policies = security_policies

        self.create = async_to_raw_response_wrapper(
            security_policies.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            security_policies.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            security_policies.update,
        )
        self.list = async_to_raw_response_wrapper(
            security_policies.list,
        )
        self.delete = async_to_raw_response_wrapper(
            security_policies.delete,
        )


class SecurityPoliciesResourceWithStreamingResponse:
    def __init__(self, security_policies: SecurityPoliciesResource) -> None:
        self._security_policies = security_policies

        self.create = to_streamed_response_wrapper(
            security_policies.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            security_policies.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            security_policies.update,
        )
        self.list = to_streamed_response_wrapper(
            security_policies.list,
        )
        self.delete = to_streamed_response_wrapper(
            security_policies.delete,
        )


class AsyncSecurityPoliciesResourceWithStreamingResponse:
    def __init__(self, security_policies: AsyncSecurityPoliciesResource) -> None:
        self._security_policies = security_policies

        self.create = async_to_streamed_response_wrapper(
            security_policies.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            security_policies.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            security_policies.update,
        )
        self.list = async_to_streamed_response_wrapper(
            security_policies.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            security_policies.delete,
        )
