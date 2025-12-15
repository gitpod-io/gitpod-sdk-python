# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...types import (
    RunnerKind,
    SearchMode,
    RunnerProvider,
    runner_list_params,
    runner_create_params,
    runner_delete_params,
    runner_update_params,
    runner_retrieve_params,
    runner_create_logs_token_params,
    runner_parse_context_url_params,
    runner_create_runner_token_params,
    runner_search_repositories_params,
    runner_check_authentication_for_host_params,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from .policies import (
    PoliciesResource,
    AsyncPoliciesResource,
    PoliciesResourceWithRawResponse,
    AsyncPoliciesResourceWithRawResponse,
    PoliciesResourceWithStreamingResponse,
    AsyncPoliciesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncRunnersPage, AsyncRunnersPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.runner import Runner
from ...types.runner_kind import RunnerKind
from ...types.search_mode import SearchMode
from ...types.runner_provider import RunnerProvider
from ...types.runner_spec_param import RunnerSpecParam
from .configurations.configurations import (
    ConfigurationsResource,
    AsyncConfigurationsResource,
    ConfigurationsResourceWithRawResponse,
    AsyncConfigurationsResourceWithRawResponse,
    ConfigurationsResourceWithStreamingResponse,
    AsyncConfigurationsResourceWithStreamingResponse,
)
from ...types.runner_create_response import RunnerCreateResponse
from ...types.runner_retrieve_response import RunnerRetrieveResponse
from ...types.runner_create_logs_token_response import RunnerCreateLogsTokenResponse
from ...types.runner_parse_context_url_response import RunnerParseContextURLResponse
from ...types.runner_create_runner_token_response import RunnerCreateRunnerTokenResponse
from ...types.runner_search_repositories_response import RunnerSearchRepositoriesResponse
from ...types.runner_check_authentication_for_host_response import RunnerCheckAuthenticationForHostResponse

__all__ = ["RunnersResource", "AsyncRunnersResource"]


class RunnersResource(SyncAPIResource):
    @cached_property
    def configurations(self) -> ConfigurationsResource:
        return ConfigurationsResource(self._client)

    @cached_property
    def policies(self) -> PoliciesResource:
        return PoliciesResource(self._client)

    @cached_property
    def with_raw_response(self) -> RunnersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return RunnersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RunnersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return RunnersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        kind: RunnerKind | Omit = omit,
        name: str | Omit = omit,
        provider: RunnerProvider | Omit = omit,
        runner_manager_id: str | Omit = omit,
        spec: RunnerSpecParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunnerCreateResponse:
        """Creates a new runner registration with the server.

        Registrations are very
        short-lived and must be renewed every 30 seconds.

        Use this method to:

        - Register organization runners
        - Set up runner configurations
        - Initialize runner credentials
        - Configure auto-updates

        ### Examples

        - Create cloud runner:

          Creates a new runner in AWS EC2.

          ```yaml
          name: "Production Runner"
          provider: RUNNER_PROVIDER_AWS_EC2
          spec:
            desiredPhase: RUNNER_PHASE_ACTIVE
            configuration:
              region: "us-west"
              releaseChannel: RUNNER_RELEASE_CHANNEL_STABLE
              autoUpdate: true
          ```

        - Create local runner:

          Creates a new local runner on Linux.

          ```yaml
          name: "Local Development Runner"
          provider: RUNNER_PROVIDER_LINUX_HOST
          spec:
            desiredPhase: RUNNER_PHASE_ACTIVE
            configuration:
              releaseChannel: RUNNER_RELEASE_CHANNEL_LATEST
              autoUpdate: true
          ```

        Args:
          kind: The runner's kind This field is optional and here for backwards-compatibility.
              Use the provider field instead. If provider is set, the runner's kind will be
              deduced from the provider. Only one of kind and provider must be set.

          name: The runner name for humans

          provider: The specific implementation type of the runner This field is optional for
              backwards compatibility but will be required in the future. When specified, kind
              must not be specified (will be deduced from provider)

          runner_manager_id: The runner manager id specifies the runner manager for the managed runner. This
              field is mandatory for managed runners, otheriwse should not be set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.RunnerService/CreateRunner",
            body=maybe_transform(
                {
                    "kind": kind,
                    "name": name,
                    "provider": provider,
                    "runner_manager_id": runner_manager_id,
                    "spec": spec,
                },
                runner_create_params.RunnerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunnerCreateResponse,
        )

    def retrieve(
        self,
        *,
        runner_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunnerRetrieveResponse:
        """
        Gets details about a specific runner.

        Use this method to:

        - Check runner status
        - View runner configuration
        - Monitor runner health
        - Verify runner capabilities

        ### Examples

        - Get runner details:

          Retrieves information about a specific runner.

          ```yaml
          runnerId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.RunnerService/GetRunner",
            body=maybe_transform({"runner_id": runner_id}, runner_retrieve_params.RunnerRetrieveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunnerRetrieveResponse,
        )

    def update(
        self,
        *,
        name: Optional[str] | Omit = omit,
        runner_id: str | Omit = omit,
        spec: Optional[runner_update_params.Spec] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Updates a runner's configuration.

        Use this method to:

        - Modify runner settings
        - Update release channels
        - Change runner status
        - Configure auto-update settings

        ### Examples

        - Update configuration:

          Changes runner settings.

          ```yaml
          runnerId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          name: "Updated Runner Name"
          spec:
            configuration:
              releaseChannel: RUNNER_RELEASE_CHANNEL_LATEST
              autoUpdate: true
          ```

        Args:
          name: The runner's name which is shown to users

          runner_id: runner_id specifies which runner to be updated.

              +required

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.RunnerService/UpdateRunner",
            body=maybe_transform(
                {
                    "name": name,
                    "runner_id": runner_id,
                    "spec": spec,
                },
                runner_update_params.RunnerUpdateParams,
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
        filter: runner_list_params.Filter | Omit = omit,
        pagination: runner_list_params.Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncRunnersPage[Runner]:
        """
        Lists all registered runners with optional filtering.

        Use this method to:

        - View all available runners
        - Filter by runner type
        - Monitor runner status
        - Check runner availability

        ### Examples

        - List all runners:

          Shows all runners with pagination.

          ```yaml
          pagination:
            pageSize: 20
          ```

        - Filter by provider:

          Lists only AWS EC2 runners.

          ```yaml
          filter:
            providers: ["RUNNER_PROVIDER_AWS_EC2"]
          pagination:
            pageSize: 20
          ```

        Args:
          pagination: pagination contains the pagination options for listing runners

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.RunnerService/ListRunners",
            page=SyncRunnersPage[Runner],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                runner_list_params.RunnerListParams,
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
                    runner_list_params.RunnerListParams,
                ),
            ),
            model=Runner,
            method="post",
        )

    def delete(
        self,
        *,
        force: bool | Omit = omit,
        runner_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Deletes a runner permanently.

        Use this method to:

        - Remove unused runners
        - Clean up runner registrations
        - Delete obsolete runners

        ### Examples

        - Delete runner:

          Permanently removes a runner.

          ```yaml
          runnerId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          force: force indicates whether the runner should be deleted forcefully. When force
              deleting a Runner, all Environments on the runner are also force deleted and
              regular Runner lifecycle is not respected. Force deleting can result in data
              loss.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.RunnerService/DeleteRunner",
            body=maybe_transform(
                {
                    "force": force,
                    "runner_id": runner_id,
                },
                runner_delete_params.RunnerDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def check_authentication_for_host(
        self,
        *,
        host: str | Omit = omit,
        runner_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunnerCheckAuthenticationForHostResponse:
        """
        Checks if a user is authenticated for a specific host.

        Use this method to:

        - Verify authentication status
        - Get authentication URLs
        - Check PAT support

        ### Examples

        - Check authentication:

          Verifies authentication for a host.

          ```yaml
          host: "github.com"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.RunnerService/CheckAuthenticationForHost",
            body=maybe_transform(
                {
                    "host": host,
                    "runner_id": runner_id,
                },
                runner_check_authentication_for_host_params.RunnerCheckAuthenticationForHostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunnerCheckAuthenticationForHostResponse,
        )

    def create_logs_token(
        self,
        *,
        runner_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunnerCreateLogsTokenResponse:
        """
        Creates an access token for runner logs and debug information.

        Generated tokens are valid for one hour and provide runner-specific access
        permissions. The token is scoped to a specific runner and can be used to access
        support bundles.

        ### Examples

        - Generate runner logs token:

          ```yaml
          runnerId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          runner_id: runner_id specifies the runner for which the logs token should be created.

              +required

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.RunnerService/CreateRunnerLogsToken",
            body=maybe_transform({"runner_id": runner_id}, runner_create_logs_token_params.RunnerCreateLogsTokenParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunnerCreateLogsTokenResponse,
        )

    def create_runner_token(
        self,
        *,
        runner_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunnerCreateRunnerTokenResponse:
        """
        Creates a new authentication token for a runner.

        Use this method to:

        - Generate runner credentials
        - Renew expired tokens
        - Set up runner authentication

        Note: This does not expire previously issued tokens.

        ### Examples

        - Create token:

          Creates a new token for runner authentication.

          ```yaml
          runnerId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.RunnerService/CreateRunnerToken",
            body=maybe_transform(
                {"runner_id": runner_id}, runner_create_runner_token_params.RunnerCreateRunnerTokenParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunnerCreateRunnerTokenResponse,
        )

    def parse_context_url(
        self,
        *,
        context_url: str | Omit = omit,
        runner_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunnerParseContextURLResponse:
        """
        Parses a context URL and returns the parsed result.

        Use this method to:

        - Validate context URLs
        - Check repository access
        - Verify branch existence

        Returns:

        - FAILED_PRECONDITION if authentication is required
        - PERMISSION_DENIED if access is not allowed
        - INVALID_ARGUMENT if URL is invalid
        - NOT_FOUND if repository/branch doesn't exist

        ### Examples

        - Parse URL:

          Parses and validates a context URL.

          ```yaml
          contextUrl: "https://github.com/org/repo/tree/main"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.RunnerService/ParseContextURL",
            body=maybe_transform(
                {
                    "context_url": context_url,
                    "runner_id": runner_id,
                },
                runner_parse_context_url_params.RunnerParseContextURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunnerParseContextURLResponse,
        )

    def search_repositories(
        self,
        *,
        limit: int | Omit = omit,
        pagination: runner_search_repositories_params.Pagination | Omit = omit,
        runner_id: str | Omit = omit,
        scm_host: str | Omit = omit,
        search_mode: SearchMode | Omit = omit,
        search_string: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunnerSearchRepositoriesResponse:
        """
        Searches for repositories across all authenticated SCM hosts.

        Use this method to:

        - List available repositories
        - Search repositories by name or content
        - Discover repositories for environment creation

        Returns repositories from all authenticated SCM hosts in natural sort order. If
        no repositories are found, returns an empty list.

        ### Examples

        - List all repositories:

          Returns up to 25 repositories from all authenticated hosts.

          ```yaml
          runnerId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        - Search repositories:

          Searches for repositories matching the query across all hosts.

          ```yaml
          runnerId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          searchString: "my-project"
          limit: 10
          ```

        Args:
          limit:
              Maximum number of repositories to return. Default: 25, Maximum: 100 Deprecated:
              Use pagination.page_size instead

          pagination: Pagination parameters for repository search

          scm_host: The SCM's host to retrieve repositories from

          search_mode: Search mode determines how search_string is interpreted

          search_string: Search query - interpretation depends on search_mode

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.RunnerService/SearchRepositories",
            body=maybe_transform(
                {
                    "limit": limit,
                    "pagination": pagination,
                    "runner_id": runner_id,
                    "scm_host": scm_host,
                    "search_mode": search_mode,
                    "search_string": search_string,
                },
                runner_search_repositories_params.RunnerSearchRepositoriesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunnerSearchRepositoriesResponse,
        )


class AsyncRunnersResource(AsyncAPIResource):
    @cached_property
    def configurations(self) -> AsyncConfigurationsResource:
        return AsyncConfigurationsResource(self._client)

    @cached_property
    def policies(self) -> AsyncPoliciesResource:
        return AsyncPoliciesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRunnersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRunnersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRunnersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return AsyncRunnersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        kind: RunnerKind | Omit = omit,
        name: str | Omit = omit,
        provider: RunnerProvider | Omit = omit,
        runner_manager_id: str | Omit = omit,
        spec: RunnerSpecParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunnerCreateResponse:
        """Creates a new runner registration with the server.

        Registrations are very
        short-lived and must be renewed every 30 seconds.

        Use this method to:

        - Register organization runners
        - Set up runner configurations
        - Initialize runner credentials
        - Configure auto-updates

        ### Examples

        - Create cloud runner:

          Creates a new runner in AWS EC2.

          ```yaml
          name: "Production Runner"
          provider: RUNNER_PROVIDER_AWS_EC2
          spec:
            desiredPhase: RUNNER_PHASE_ACTIVE
            configuration:
              region: "us-west"
              releaseChannel: RUNNER_RELEASE_CHANNEL_STABLE
              autoUpdate: true
          ```

        - Create local runner:

          Creates a new local runner on Linux.

          ```yaml
          name: "Local Development Runner"
          provider: RUNNER_PROVIDER_LINUX_HOST
          spec:
            desiredPhase: RUNNER_PHASE_ACTIVE
            configuration:
              releaseChannel: RUNNER_RELEASE_CHANNEL_LATEST
              autoUpdate: true
          ```

        Args:
          kind: The runner's kind This field is optional and here for backwards-compatibility.
              Use the provider field instead. If provider is set, the runner's kind will be
              deduced from the provider. Only one of kind and provider must be set.

          name: The runner name for humans

          provider: The specific implementation type of the runner This field is optional for
              backwards compatibility but will be required in the future. When specified, kind
              must not be specified (will be deduced from provider)

          runner_manager_id: The runner manager id specifies the runner manager for the managed runner. This
              field is mandatory for managed runners, otheriwse should not be set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.RunnerService/CreateRunner",
            body=await async_maybe_transform(
                {
                    "kind": kind,
                    "name": name,
                    "provider": provider,
                    "runner_manager_id": runner_manager_id,
                    "spec": spec,
                },
                runner_create_params.RunnerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunnerCreateResponse,
        )

    async def retrieve(
        self,
        *,
        runner_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunnerRetrieveResponse:
        """
        Gets details about a specific runner.

        Use this method to:

        - Check runner status
        - View runner configuration
        - Monitor runner health
        - Verify runner capabilities

        ### Examples

        - Get runner details:

          Retrieves information about a specific runner.

          ```yaml
          runnerId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.RunnerService/GetRunner",
            body=await async_maybe_transform({"runner_id": runner_id}, runner_retrieve_params.RunnerRetrieveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunnerRetrieveResponse,
        )

    async def update(
        self,
        *,
        name: Optional[str] | Omit = omit,
        runner_id: str | Omit = omit,
        spec: Optional[runner_update_params.Spec] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Updates a runner's configuration.

        Use this method to:

        - Modify runner settings
        - Update release channels
        - Change runner status
        - Configure auto-update settings

        ### Examples

        - Update configuration:

          Changes runner settings.

          ```yaml
          runnerId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          name: "Updated Runner Name"
          spec:
            configuration:
              releaseChannel: RUNNER_RELEASE_CHANNEL_LATEST
              autoUpdate: true
          ```

        Args:
          name: The runner's name which is shown to users

          runner_id: runner_id specifies which runner to be updated.

              +required

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.RunnerService/UpdateRunner",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "runner_id": runner_id,
                    "spec": spec,
                },
                runner_update_params.RunnerUpdateParams,
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
        filter: runner_list_params.Filter | Omit = omit,
        pagination: runner_list_params.Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Runner, AsyncRunnersPage[Runner]]:
        """
        Lists all registered runners with optional filtering.

        Use this method to:

        - View all available runners
        - Filter by runner type
        - Monitor runner status
        - Check runner availability

        ### Examples

        - List all runners:

          Shows all runners with pagination.

          ```yaml
          pagination:
            pageSize: 20
          ```

        - Filter by provider:

          Lists only AWS EC2 runners.

          ```yaml
          filter:
            providers: ["RUNNER_PROVIDER_AWS_EC2"]
          pagination:
            pageSize: 20
          ```

        Args:
          pagination: pagination contains the pagination options for listing runners

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.RunnerService/ListRunners",
            page=AsyncRunnersPage[Runner],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                runner_list_params.RunnerListParams,
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
                    runner_list_params.RunnerListParams,
                ),
            ),
            model=Runner,
            method="post",
        )

    async def delete(
        self,
        *,
        force: bool | Omit = omit,
        runner_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Deletes a runner permanently.

        Use this method to:

        - Remove unused runners
        - Clean up runner registrations
        - Delete obsolete runners

        ### Examples

        - Delete runner:

          Permanently removes a runner.

          ```yaml
          runnerId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          force: force indicates whether the runner should be deleted forcefully. When force
              deleting a Runner, all Environments on the runner are also force deleted and
              regular Runner lifecycle is not respected. Force deleting can result in data
              loss.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.RunnerService/DeleteRunner",
            body=await async_maybe_transform(
                {
                    "force": force,
                    "runner_id": runner_id,
                },
                runner_delete_params.RunnerDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def check_authentication_for_host(
        self,
        *,
        host: str | Omit = omit,
        runner_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunnerCheckAuthenticationForHostResponse:
        """
        Checks if a user is authenticated for a specific host.

        Use this method to:

        - Verify authentication status
        - Get authentication URLs
        - Check PAT support

        ### Examples

        - Check authentication:

          Verifies authentication for a host.

          ```yaml
          host: "github.com"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.RunnerService/CheckAuthenticationForHost",
            body=await async_maybe_transform(
                {
                    "host": host,
                    "runner_id": runner_id,
                },
                runner_check_authentication_for_host_params.RunnerCheckAuthenticationForHostParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunnerCheckAuthenticationForHostResponse,
        )

    async def create_logs_token(
        self,
        *,
        runner_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunnerCreateLogsTokenResponse:
        """
        Creates an access token for runner logs and debug information.

        Generated tokens are valid for one hour and provide runner-specific access
        permissions. The token is scoped to a specific runner and can be used to access
        support bundles.

        ### Examples

        - Generate runner logs token:

          ```yaml
          runnerId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          runner_id: runner_id specifies the runner for which the logs token should be created.

              +required

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.RunnerService/CreateRunnerLogsToken",
            body=await async_maybe_transform(
                {"runner_id": runner_id}, runner_create_logs_token_params.RunnerCreateLogsTokenParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunnerCreateLogsTokenResponse,
        )

    async def create_runner_token(
        self,
        *,
        runner_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunnerCreateRunnerTokenResponse:
        """
        Creates a new authentication token for a runner.

        Use this method to:

        - Generate runner credentials
        - Renew expired tokens
        - Set up runner authentication

        Note: This does not expire previously issued tokens.

        ### Examples

        - Create token:

          Creates a new token for runner authentication.

          ```yaml
          runnerId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.RunnerService/CreateRunnerToken",
            body=await async_maybe_transform(
                {"runner_id": runner_id}, runner_create_runner_token_params.RunnerCreateRunnerTokenParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunnerCreateRunnerTokenResponse,
        )

    async def parse_context_url(
        self,
        *,
        context_url: str | Omit = omit,
        runner_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunnerParseContextURLResponse:
        """
        Parses a context URL and returns the parsed result.

        Use this method to:

        - Validate context URLs
        - Check repository access
        - Verify branch existence

        Returns:

        - FAILED_PRECONDITION if authentication is required
        - PERMISSION_DENIED if access is not allowed
        - INVALID_ARGUMENT if URL is invalid
        - NOT_FOUND if repository/branch doesn't exist

        ### Examples

        - Parse URL:

          Parses and validates a context URL.

          ```yaml
          contextUrl: "https://github.com/org/repo/tree/main"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.RunnerService/ParseContextURL",
            body=await async_maybe_transform(
                {
                    "context_url": context_url,
                    "runner_id": runner_id,
                },
                runner_parse_context_url_params.RunnerParseContextURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunnerParseContextURLResponse,
        )

    async def search_repositories(
        self,
        *,
        limit: int | Omit = omit,
        pagination: runner_search_repositories_params.Pagination | Omit = omit,
        runner_id: str | Omit = omit,
        scm_host: str | Omit = omit,
        search_mode: SearchMode | Omit = omit,
        search_string: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunnerSearchRepositoriesResponse:
        """
        Searches for repositories across all authenticated SCM hosts.

        Use this method to:

        - List available repositories
        - Search repositories by name or content
        - Discover repositories for environment creation

        Returns repositories from all authenticated SCM hosts in natural sort order. If
        no repositories are found, returns an empty list.

        ### Examples

        - List all repositories:

          Returns up to 25 repositories from all authenticated hosts.

          ```yaml
          runnerId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        - Search repositories:

          Searches for repositories matching the query across all hosts.

          ```yaml
          runnerId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          searchString: "my-project"
          limit: 10
          ```

        Args:
          limit:
              Maximum number of repositories to return. Default: 25, Maximum: 100 Deprecated:
              Use pagination.page_size instead

          pagination: Pagination parameters for repository search

          scm_host: The SCM's host to retrieve repositories from

          search_mode: Search mode determines how search_string is interpreted

          search_string: Search query - interpretation depends on search_mode

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.RunnerService/SearchRepositories",
            body=await async_maybe_transform(
                {
                    "limit": limit,
                    "pagination": pagination,
                    "runner_id": runner_id,
                    "scm_host": scm_host,
                    "search_mode": search_mode,
                    "search_string": search_string,
                },
                runner_search_repositories_params.RunnerSearchRepositoriesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunnerSearchRepositoriesResponse,
        )


class RunnersResourceWithRawResponse:
    def __init__(self, runners: RunnersResource) -> None:
        self._runners = runners

        self.create = to_raw_response_wrapper(
            runners.create,
        )
        self.retrieve = to_raw_response_wrapper(
            runners.retrieve,
        )
        self.update = to_raw_response_wrapper(
            runners.update,
        )
        self.list = to_raw_response_wrapper(
            runners.list,
        )
        self.delete = to_raw_response_wrapper(
            runners.delete,
        )
        self.check_authentication_for_host = to_raw_response_wrapper(
            runners.check_authentication_for_host,
        )
        self.create_logs_token = to_raw_response_wrapper(
            runners.create_logs_token,
        )
        self.create_runner_token = to_raw_response_wrapper(
            runners.create_runner_token,
        )
        self.parse_context_url = to_raw_response_wrapper(
            runners.parse_context_url,
        )
        self.search_repositories = to_raw_response_wrapper(
            runners.search_repositories,
        )

    @cached_property
    def configurations(self) -> ConfigurationsResourceWithRawResponse:
        return ConfigurationsResourceWithRawResponse(self._runners.configurations)

    @cached_property
    def policies(self) -> PoliciesResourceWithRawResponse:
        return PoliciesResourceWithRawResponse(self._runners.policies)


class AsyncRunnersResourceWithRawResponse:
    def __init__(self, runners: AsyncRunnersResource) -> None:
        self._runners = runners

        self.create = async_to_raw_response_wrapper(
            runners.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            runners.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            runners.update,
        )
        self.list = async_to_raw_response_wrapper(
            runners.list,
        )
        self.delete = async_to_raw_response_wrapper(
            runners.delete,
        )
        self.check_authentication_for_host = async_to_raw_response_wrapper(
            runners.check_authentication_for_host,
        )
        self.create_logs_token = async_to_raw_response_wrapper(
            runners.create_logs_token,
        )
        self.create_runner_token = async_to_raw_response_wrapper(
            runners.create_runner_token,
        )
        self.parse_context_url = async_to_raw_response_wrapper(
            runners.parse_context_url,
        )
        self.search_repositories = async_to_raw_response_wrapper(
            runners.search_repositories,
        )

    @cached_property
    def configurations(self) -> AsyncConfigurationsResourceWithRawResponse:
        return AsyncConfigurationsResourceWithRawResponse(self._runners.configurations)

    @cached_property
    def policies(self) -> AsyncPoliciesResourceWithRawResponse:
        return AsyncPoliciesResourceWithRawResponse(self._runners.policies)


class RunnersResourceWithStreamingResponse:
    def __init__(self, runners: RunnersResource) -> None:
        self._runners = runners

        self.create = to_streamed_response_wrapper(
            runners.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            runners.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            runners.update,
        )
        self.list = to_streamed_response_wrapper(
            runners.list,
        )
        self.delete = to_streamed_response_wrapper(
            runners.delete,
        )
        self.check_authentication_for_host = to_streamed_response_wrapper(
            runners.check_authentication_for_host,
        )
        self.create_logs_token = to_streamed_response_wrapper(
            runners.create_logs_token,
        )
        self.create_runner_token = to_streamed_response_wrapper(
            runners.create_runner_token,
        )
        self.parse_context_url = to_streamed_response_wrapper(
            runners.parse_context_url,
        )
        self.search_repositories = to_streamed_response_wrapper(
            runners.search_repositories,
        )

    @cached_property
    def configurations(self) -> ConfigurationsResourceWithStreamingResponse:
        return ConfigurationsResourceWithStreamingResponse(self._runners.configurations)

    @cached_property
    def policies(self) -> PoliciesResourceWithStreamingResponse:
        return PoliciesResourceWithStreamingResponse(self._runners.policies)


class AsyncRunnersResourceWithStreamingResponse:
    def __init__(self, runners: AsyncRunnersResource) -> None:
        self._runners = runners

        self.create = async_to_streamed_response_wrapper(
            runners.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            runners.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            runners.update,
        )
        self.list = async_to_streamed_response_wrapper(
            runners.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            runners.delete,
        )
        self.check_authentication_for_host = async_to_streamed_response_wrapper(
            runners.check_authentication_for_host,
        )
        self.create_logs_token = async_to_streamed_response_wrapper(
            runners.create_logs_token,
        )
        self.create_runner_token = async_to_streamed_response_wrapper(
            runners.create_runner_token,
        )
        self.parse_context_url = async_to_streamed_response_wrapper(
            runners.parse_context_url,
        )
        self.search_repositories = async_to_streamed_response_wrapper(
            runners.search_repositories,
        )

    @cached_property
    def configurations(self) -> AsyncConfigurationsResourceWithStreamingResponse:
        return AsyncConfigurationsResourceWithStreamingResponse(self._runners.configurations)

    @cached_property
    def policies(self) -> AsyncPoliciesResourceWithStreamingResponse:
        return AsyncPoliciesResourceWithStreamingResponse(self._runners.policies)
