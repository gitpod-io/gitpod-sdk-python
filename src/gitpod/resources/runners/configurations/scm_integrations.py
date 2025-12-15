# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

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
        host: str | Omit = omit,
        issuer_url: Optional[str] | Omit = omit,
        oauth_client_id: Optional[str] | Omit = omit,
        oauth_plaintext_client_secret: Optional[str] | Omit = omit,
        pat: bool | Omit = omit,
        runner_id: str | Omit = omit,
        scm_id: str | Omit = omit,
        virtual_directory: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScmIntegrationCreateResponse:
        """
        Creates a new SCM integration for a runner.

        Use this method to:

        - Configure source control access
        - Set up repository integrations
        - Enable code synchronization

        ### Examples

        - Create GitHub integration:

          Sets up GitHub SCM integration.

          ```yaml
          runnerId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          scmId: "github"
          host: "github.com"
          oauthClientId: "client_id"
          oauthPlaintextClientSecret: "client_secret"
          ```

        Args:
          issuer_url: issuer_url can be set to override the authentication provider URL, if it doesn't
              match the SCM host.

          oauth_client_id: oauth_client_id is the OAuth app's client ID, if OAuth is configured. If
              configured, oauth_plaintext_client_secret must also be set.

          oauth_plaintext_client_secret: oauth_plaintext_client_secret is the OAuth app's client secret in clear text.
              This will first be encrypted with the runner's public key before being stored.

          scm_id: scm_id references the scm_id in the runner's configuration schema that this
              integration is for

          virtual_directory: virtual_directory is the virtual directory path for Azure DevOps Server (e.g.,
              "/tfs"). This field is only used for Azure DevOps Server SCM integrations and
              should be empty for other SCM types. Azure DevOps Server APIs work without
              collection when PAT scope is 'All accessible organizations'.

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
                    "issuer_url": issuer_url,
                    "oauth_client_id": oauth_client_id,
                    "oauth_plaintext_client_secret": oauth_plaintext_client_secret,
                    "pat": pat,
                    "runner_id": runner_id,
                    "scm_id": scm_id,
                    "virtual_directory": virtual_directory,
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
        id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScmIntegrationRetrieveResponse:
        """
        Gets details about a specific SCM integration.

        Use this method to:

        - View integration settings
        - Check integration status
        - Verify configuration

        ### Examples

        - Get integration details:

          Retrieves information about a specific integration.

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
        id: str | Omit = omit,
        issuer_url: Optional[str] | Omit = omit,
        oauth_client_id: Optional[str] | Omit = omit,
        oauth_plaintext_client_secret: Optional[str] | Omit = omit,
        pat: Optional[bool] | Omit = omit,
        virtual_directory: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Updates an existing SCM integration.

        Use this method to:

        - Modify integration settings
        - Update credentials
        - Change configuration

        ### Examples

        - Update integration:

          Updates OAuth credentials.

          ```yaml
          id: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          oauthClientId: "new_client_id"
          oauthPlaintextClientSecret: "new_client_secret"
          ```

        Args:
          issuer_url: issuer_url can be set to override the authentication provider URL, if it doesn't
              match the SCM host.

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

          virtual_directory: virtual_directory is the virtual directory path for Azure DevOps Server (e.g.,
              "/tfs"). This field is only used for Azure DevOps Server SCM integrations and
              should be empty for other SCM types. Azure DevOps Server APIs work without
              collection when PAT scope is 'All accessible organizations'.

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
                    "issuer_url": issuer_url,
                    "oauth_client_id": oauth_client_id,
                    "oauth_plaintext_client_secret": oauth_plaintext_client_secret,
                    "pat": pat,
                    "virtual_directory": virtual_directory,
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
        token: str | Omit = omit,
        page_size: int | Omit = omit,
        filter: scm_integration_list_params.Filter | Omit = omit,
        pagination: scm_integration_list_params.Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncIntegrationsPage[ScmIntegration]:
        """
        Lists SCM integrations for a runner.

        Use this method to:

        - View all integrations
        - Monitor integration status
        - Check available SCMs

        ### Examples

        - List integrations:

          Shows all SCM integrations.

          ```yaml
          filter:
            runnerIds: ["d2c94c27-3b76-4a42-b88c-95a85e392c68"]
          pagination:
            pageSize: 20
          ```

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
        id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Deletes an SCM integration.

        Use this method to:

        - Remove unused integrations
        - Clean up configurations
        - Revoke SCM access

        ### Examples

        - Delete integration:

          Removes an SCM integration.

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
        host: str | Omit = omit,
        issuer_url: Optional[str] | Omit = omit,
        oauth_client_id: Optional[str] | Omit = omit,
        oauth_plaintext_client_secret: Optional[str] | Omit = omit,
        pat: bool | Omit = omit,
        runner_id: str | Omit = omit,
        scm_id: str | Omit = omit,
        virtual_directory: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScmIntegrationCreateResponse:
        """
        Creates a new SCM integration for a runner.

        Use this method to:

        - Configure source control access
        - Set up repository integrations
        - Enable code synchronization

        ### Examples

        - Create GitHub integration:

          Sets up GitHub SCM integration.

          ```yaml
          runnerId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          scmId: "github"
          host: "github.com"
          oauthClientId: "client_id"
          oauthPlaintextClientSecret: "client_secret"
          ```

        Args:
          issuer_url: issuer_url can be set to override the authentication provider URL, if it doesn't
              match the SCM host.

          oauth_client_id: oauth_client_id is the OAuth app's client ID, if OAuth is configured. If
              configured, oauth_plaintext_client_secret must also be set.

          oauth_plaintext_client_secret: oauth_plaintext_client_secret is the OAuth app's client secret in clear text.
              This will first be encrypted with the runner's public key before being stored.

          scm_id: scm_id references the scm_id in the runner's configuration schema that this
              integration is for

          virtual_directory: virtual_directory is the virtual directory path for Azure DevOps Server (e.g.,
              "/tfs"). This field is only used for Azure DevOps Server SCM integrations and
              should be empty for other SCM types. Azure DevOps Server APIs work without
              collection when PAT scope is 'All accessible organizations'.

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
                    "issuer_url": issuer_url,
                    "oauth_client_id": oauth_client_id,
                    "oauth_plaintext_client_secret": oauth_plaintext_client_secret,
                    "pat": pat,
                    "runner_id": runner_id,
                    "scm_id": scm_id,
                    "virtual_directory": virtual_directory,
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
        id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ScmIntegrationRetrieveResponse:
        """
        Gets details about a specific SCM integration.

        Use this method to:

        - View integration settings
        - Check integration status
        - Verify configuration

        ### Examples

        - Get integration details:

          Retrieves information about a specific integration.

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
        id: str | Omit = omit,
        issuer_url: Optional[str] | Omit = omit,
        oauth_client_id: Optional[str] | Omit = omit,
        oauth_plaintext_client_secret: Optional[str] | Omit = omit,
        pat: Optional[bool] | Omit = omit,
        virtual_directory: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Updates an existing SCM integration.

        Use this method to:

        - Modify integration settings
        - Update credentials
        - Change configuration

        ### Examples

        - Update integration:

          Updates OAuth credentials.

          ```yaml
          id: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          oauthClientId: "new_client_id"
          oauthPlaintextClientSecret: "new_client_secret"
          ```

        Args:
          issuer_url: issuer_url can be set to override the authentication provider URL, if it doesn't
              match the SCM host.

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

          virtual_directory: virtual_directory is the virtual directory path for Azure DevOps Server (e.g.,
              "/tfs"). This field is only used for Azure DevOps Server SCM integrations and
              should be empty for other SCM types. Azure DevOps Server APIs work without
              collection when PAT scope is 'All accessible organizations'.

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
                    "issuer_url": issuer_url,
                    "oauth_client_id": oauth_client_id,
                    "oauth_plaintext_client_secret": oauth_plaintext_client_secret,
                    "pat": pat,
                    "virtual_directory": virtual_directory,
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
        token: str | Omit = omit,
        page_size: int | Omit = omit,
        filter: scm_integration_list_params.Filter | Omit = omit,
        pagination: scm_integration_list_params.Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ScmIntegration, AsyncIntegrationsPage[ScmIntegration]]:
        """
        Lists SCM integrations for a runner.

        Use this method to:

        - View all integrations
        - Monitor integration status
        - Check available SCMs

        ### Examples

        - List integrations:

          Shows all SCM integrations.

          ```yaml
          filter:
            runnerIds: ["d2c94c27-3b76-4a42-b88c-95a85e392c68"]
          pagination:
            pageSize: 20
          ```

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
        id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Deletes an SCM integration.

        Use this method to:

        - Remove unused integrations
        - Clean up configurations
        - Revoke SCM access

        ### Examples

        - Delete integration:

          Removes an SCM integration.

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
