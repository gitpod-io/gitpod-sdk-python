# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

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
from ....pagination import SyncIntegrationsPage, AsyncIntegrationsPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.runners.configurations import (
    scm_integration_list_params,
    scm_integration_create_params,
    scm_integration_delete_params,
    scm_integration_update_params,
    scm_integration_retrieve_params,
)
from ....types.runners.configurations.scm_integration import ScmIntegration
from ....types.runners.configurations.scm_integration_create_response import ScmIntegrationCreateResponse
from ....types.runners.configurations.scm_integration_retrieve_response import ScmIntegrationRetrieveResponse

__all__ = ["ScmIntegrationsResource", "AsyncScmIntegrationsResource"]


class ScmIntegrationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScmIntegrationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ScmIntegrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScmIntegrationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return ScmIntegrationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        host: str | NotGiven = NOT_GIVEN,
        oauth_client_id: Optional[str] | NotGiven = NOT_GIVEN,
        oauth_plaintext_client_secret: Optional[str] | NotGiven = NOT_GIVEN,
        pat: bool | NotGiven = NOT_GIVEN,
        runner_id: str | NotGiven = NOT_GIVEN,
        scm_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScmIntegrationCreateResponse:
        """
        CreateSCMIntegration creates a new SCM integration on a runner.

        Args:
          oauth_client_id: oauth_client_id is the OAuth app's client ID, if OAuth is configured. If
              configured, oauth_plaintext_client_secret must also be set.

          oauth_plaintext_client_secret: oauth_plaintext_client_secret is the OAuth app's client secret in clear text.
              This will first be encrypted with the runner's public key before being stored.

          scm_id: scm_id references the scm_id in the runner's configuration schema that this
              integration is for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.RunnerConfigurationService/CreateSCMIntegration",
            body=maybe_transform(
                {
                    "host": host,
                    "oauth_client_id": oauth_client_id,
                    "oauth_plaintext_client_secret": oauth_plaintext_client_secret,
                    "pat": pat,
                    "runner_id": runner_id,
                    "scm_id": scm_id,
                },
                scm_integration_create_params.ScmIntegrationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScmIntegrationCreateResponse,
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
    ) -> ScmIntegrationRetrieveResponse:
        """
        GetSCMIntegration returns a single SCM integration configured for a runner.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.RunnerConfigurationService/GetSCMIntegration",
            body=maybe_transform({"id": id}, scm_integration_retrieve_params.ScmIntegrationRetrieveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScmIntegrationRetrieveResponse,
        )

    def update(
        self,
        *,
        id: str | NotGiven = NOT_GIVEN,
        oauth_client_id: Optional[str] | NotGiven = NOT_GIVEN,
        oauth_plaintext_client_secret: Optional[str] | NotGiven = NOT_GIVEN,
        pat: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        UpdateSCMIntegration updates an existing SCM integration on a runner.

        Args:
          oauth_client_id: oauth_client_id can be set to update the OAuth app's client ID. If an empty
              string is set, the OAuth configuration will be removed (regardless of whether a
              client secret is set), and any existing Host Authentication Tokens for the SCM
              integration's runner and host that were created using the OAuth app will be
              deleted. This might lead to users being unable to access their repositories
              until they re-authenticate.

          oauth_plaintext_client_secret: oauth_plaintext_client_secret can be set to update the OAuth app's client
              secret. The cleartext secret will be encrypted with the runner's public key
              before being stored.

          pat: pat can be set to enable or disable Personal Access Tokens support. When
              disabling PATs, any existing Host Authentication Tokens for the SCM
              integration's runner and host that were created using a PAT will be deleted.
              This might lead to users being unable to access their repositories until they
              re-authenticate.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.RunnerConfigurationService/UpdateSCMIntegration",
            body=maybe_transform(
                {
                    "id": id,
                    "oauth_client_id": oauth_client_id,
                    "oauth_plaintext_client_secret": oauth_plaintext_client_secret,
                    "pat": pat,
                },
                scm_integration_update_params.ScmIntegrationUpdateParams,
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
        filter: scm_integration_list_params.Filter | NotGiven = NOT_GIVEN,
        pagination: scm_integration_list_params.Pagination | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncIntegrationsPage[ScmIntegration]:
        """
        ListSCMIntegrations returns all SCM integrations configured for a runner.

        Args:
          pagination: pagination contains the pagination options for listing scm integrations

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.RunnerConfigurationService/ListSCMIntegrations",
            page=SyncIntegrationsPage[ScmIntegration],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                scm_integration_list_params.ScmIntegrationListParams,
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
                    scm_integration_list_params.ScmIntegrationListParams,
                ),
            ),
            model=ScmIntegration,
            method="post",
        )

    def delete(
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
        """
        DeleteSCMIntegration deletes an existing SCM integration on a runner.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.RunnerConfigurationService/DeleteSCMIntegration",
            body=maybe_transform({"id": id}, scm_integration_delete_params.ScmIntegrationDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncScmIntegrationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScmIntegrationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncScmIntegrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScmIntegrationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return AsyncScmIntegrationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        host: str | NotGiven = NOT_GIVEN,
        oauth_client_id: Optional[str] | NotGiven = NOT_GIVEN,
        oauth_plaintext_client_secret: Optional[str] | NotGiven = NOT_GIVEN,
        pat: bool | NotGiven = NOT_GIVEN,
        runner_id: str | NotGiven = NOT_GIVEN,
        scm_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScmIntegrationCreateResponse:
        """
        CreateSCMIntegration creates a new SCM integration on a runner.

        Args:
          oauth_client_id: oauth_client_id is the OAuth app's client ID, if OAuth is configured. If
              configured, oauth_plaintext_client_secret must also be set.

          oauth_plaintext_client_secret: oauth_plaintext_client_secret is the OAuth app's client secret in clear text.
              This will first be encrypted with the runner's public key before being stored.

          scm_id: scm_id references the scm_id in the runner's configuration schema that this
              integration is for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.RunnerConfigurationService/CreateSCMIntegration",
            body=await async_maybe_transform(
                {
                    "host": host,
                    "oauth_client_id": oauth_client_id,
                    "oauth_plaintext_client_secret": oauth_plaintext_client_secret,
                    "pat": pat,
                    "runner_id": runner_id,
                    "scm_id": scm_id,
                },
                scm_integration_create_params.ScmIntegrationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScmIntegrationCreateResponse,
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
    ) -> ScmIntegrationRetrieveResponse:
        """
        GetSCMIntegration returns a single SCM integration configured for a runner.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.RunnerConfigurationService/GetSCMIntegration",
            body=await async_maybe_transform({"id": id}, scm_integration_retrieve_params.ScmIntegrationRetrieveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScmIntegrationRetrieveResponse,
        )

    async def update(
        self,
        *,
        id: str | NotGiven = NOT_GIVEN,
        oauth_client_id: Optional[str] | NotGiven = NOT_GIVEN,
        oauth_plaintext_client_secret: Optional[str] | NotGiven = NOT_GIVEN,
        pat: Optional[bool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        UpdateSCMIntegration updates an existing SCM integration on a runner.

        Args:
          oauth_client_id: oauth_client_id can be set to update the OAuth app's client ID. If an empty
              string is set, the OAuth configuration will be removed (regardless of whether a
              client secret is set), and any existing Host Authentication Tokens for the SCM
              integration's runner and host that were created using the OAuth app will be
              deleted. This might lead to users being unable to access their repositories
              until they re-authenticate.

          oauth_plaintext_client_secret: oauth_plaintext_client_secret can be set to update the OAuth app's client
              secret. The cleartext secret will be encrypted with the runner's public key
              before being stored.

          pat: pat can be set to enable or disable Personal Access Tokens support. When
              disabling PATs, any existing Host Authentication Tokens for the SCM
              integration's runner and host that were created using a PAT will be deleted.
              This might lead to users being unable to access their repositories until they
              re-authenticate.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.RunnerConfigurationService/UpdateSCMIntegration",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "oauth_client_id": oauth_client_id,
                    "oauth_plaintext_client_secret": oauth_plaintext_client_secret,
                    "pat": pat,
                },
                scm_integration_update_params.ScmIntegrationUpdateParams,
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
        filter: scm_integration_list_params.Filter | NotGiven = NOT_GIVEN,
        pagination: scm_integration_list_params.Pagination | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ScmIntegration, AsyncIntegrationsPage[ScmIntegration]]:
        """
        ListSCMIntegrations returns all SCM integrations configured for a runner.

        Args:
          pagination: pagination contains the pagination options for listing scm integrations

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.RunnerConfigurationService/ListSCMIntegrations",
            page=AsyncIntegrationsPage[ScmIntegration],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                scm_integration_list_params.ScmIntegrationListParams,
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
                    scm_integration_list_params.ScmIntegrationListParams,
                ),
            ),
            model=ScmIntegration,
            method="post",
        )

    async def delete(
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
        """
        DeleteSCMIntegration deletes an existing SCM integration on a runner.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.RunnerConfigurationService/DeleteSCMIntegration",
            body=await async_maybe_transform({"id": id}, scm_integration_delete_params.ScmIntegrationDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class ScmIntegrationsResourceWithRawResponse:
    def __init__(self, scm_integrations: ScmIntegrationsResource) -> None:
        self._scm_integrations = scm_integrations

        self.create = to_raw_response_wrapper(
            scm_integrations.create,
        )
        self.retrieve = to_raw_response_wrapper(
            scm_integrations.retrieve,
        )
        self.update = to_raw_response_wrapper(
            scm_integrations.update,
        )
        self.list = to_raw_response_wrapper(
            scm_integrations.list,
        )
        self.delete = to_raw_response_wrapper(
            scm_integrations.delete,
        )


class AsyncScmIntegrationsResourceWithRawResponse:
    def __init__(self, scm_integrations: AsyncScmIntegrationsResource) -> None:
        self._scm_integrations = scm_integrations

        self.create = async_to_raw_response_wrapper(
            scm_integrations.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            scm_integrations.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            scm_integrations.update,
        )
        self.list = async_to_raw_response_wrapper(
            scm_integrations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            scm_integrations.delete,
        )


class ScmIntegrationsResourceWithStreamingResponse:
    def __init__(self, scm_integrations: ScmIntegrationsResource) -> None:
        self._scm_integrations = scm_integrations

        self.create = to_streamed_response_wrapper(
            scm_integrations.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            scm_integrations.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            scm_integrations.update,
        )
        self.list = to_streamed_response_wrapper(
            scm_integrations.list,
        )
        self.delete = to_streamed_response_wrapper(
            scm_integrations.delete,
        )


class AsyncScmIntegrationsResourceWithStreamingResponse:
    def __init__(self, scm_integrations: AsyncScmIntegrationsResource) -> None:
        self._scm_integrations = scm_integrations

        self.create = async_to_streamed_response_wrapper(
            scm_integrations.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            scm_integrations.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            scm_integrations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            scm_integrations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            scm_integrations.delete,
        )
