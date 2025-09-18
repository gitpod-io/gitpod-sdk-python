# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...pagination import SyncPoliciesPage, AsyncPoliciesPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.runners import (
    RunnerRole,
    policy_list_params,
    policy_create_params,
    policy_delete_params,
    policy_update_params,
)
from ...types.runners.runner_role import RunnerRole
from ...types.runners.runner_policy import RunnerPolicy
from ...types.runners.policy_create_response import PolicyCreateResponse
from ...types.runners.policy_update_response import PolicyUpdateResponse

__all__ = ["PoliciesResource", "AsyncPoliciesResource"]


class PoliciesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PoliciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return PoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PoliciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return PoliciesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        group_id: str | Omit = omit,
        role: RunnerRole | Omit = omit,
        runner_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyCreateResponse:
        """
        Creates a new policy for a runner.

        Use this method to:

        - Set up access controls
        - Define group permissions
        - Configure role-based access

        ### Examples

        - Create admin policy:

          Grants admin access to a group.

          ```yaml
          runnerId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          groupId: "f53d2330-3795-4c5d-a1f3-453121af9c60"
          role: RUNNER_ROLE_ADMIN
          ```

        Args:
          group_id: group_id specifies the group_id identifier

          runner_id: runner_id specifies the project identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.RunnerService/CreateRunnerPolicy",
            body=maybe_transform(
                {
                    "group_id": group_id,
                    "role": role,
                    "runner_id": runner_id,
                },
                policy_create_params.PolicyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyCreateResponse,
        )

    def update(
        self,
        *,
        group_id: str | Omit = omit,
        role: RunnerRole | Omit = omit,
        runner_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyUpdateResponse:
        """
        Updates an existing runner policy.

        Use this method to:

        - Modify access levels
        - Change group roles
        - Update permissions

        ### Examples

        - Update policy role:

          Changes a group's access level.

          ```yaml
          runnerId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          groupId: "f53d2330-3795-4c5d-a1f3-453121af9c60"
          role: RUNNER_ROLE_USER
          ```

        Args:
          group_id: group_id specifies the group_id identifier

          runner_id: runner_id specifies the project identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.RunnerService/UpdateRunnerPolicy",
            body=maybe_transform(
                {
                    "group_id": group_id,
                    "role": role,
                    "runner_id": runner_id,
                },
                policy_update_params.PolicyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyUpdateResponse,
        )

    def list(
        self,
        *,
        token: str | Omit = omit,
        page_size: int | Omit = omit,
        pagination: policy_list_params.Pagination | Omit = omit,
        runner_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPoliciesPage[RunnerPolicy]:
        """
        Lists policies for a runner.

        Use this method to:

        - View access controls
        - Check policy configurations
        - Audit permissions

        ### Examples

        - List policies:

          Shows all policies for a runner.

          ```yaml
          runnerId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          pagination:
            pageSize: 20
          ```

        Args:
          pagination: pagination contains the pagination options for listing project policies

          runner_id: runner_id specifies the project identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.RunnerService/ListRunnerPolicies",
            page=SyncPoliciesPage[RunnerPolicy],
            body=maybe_transform(
                {
                    "pagination": pagination,
                    "runner_id": runner_id,
                },
                policy_list_params.PolicyListParams,
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
                    policy_list_params.PolicyListParams,
                ),
            ),
            model=RunnerPolicy,
            method="post",
        )

    def delete(
        self,
        *,
        group_id: str | Omit = omit,
        runner_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Deletes a runner policy.

        Use this method to:

        - Remove access controls
        - Revoke permissions
        - Clean up policies

        ### Examples

        - Delete policy:

          Removes a group's access policy.

          ```yaml
          runnerId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          groupId: "f53d2330-3795-4c5d-a1f3-453121af9c60"
          ```

        Args:
          group_id: group_id specifies the group_id identifier

          runner_id: runner_id specifies the project identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.RunnerService/DeleteRunnerPolicy",
            body=maybe_transform(
                {
                    "group_id": group_id,
                    "runner_id": runner_id,
                },
                policy_delete_params.PolicyDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncPoliciesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPoliciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPoliciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return AsyncPoliciesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        group_id: str | Omit = omit,
        role: RunnerRole | Omit = omit,
        runner_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyCreateResponse:
        """
        Creates a new policy for a runner.

        Use this method to:

        - Set up access controls
        - Define group permissions
        - Configure role-based access

        ### Examples

        - Create admin policy:

          Grants admin access to a group.

          ```yaml
          runnerId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          groupId: "f53d2330-3795-4c5d-a1f3-453121af9c60"
          role: RUNNER_ROLE_ADMIN
          ```

        Args:
          group_id: group_id specifies the group_id identifier

          runner_id: runner_id specifies the project identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.RunnerService/CreateRunnerPolicy",
            body=await async_maybe_transform(
                {
                    "group_id": group_id,
                    "role": role,
                    "runner_id": runner_id,
                },
                policy_create_params.PolicyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyCreateResponse,
        )

    async def update(
        self,
        *,
        group_id: str | Omit = omit,
        role: RunnerRole | Omit = omit,
        runner_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyUpdateResponse:
        """
        Updates an existing runner policy.

        Use this method to:

        - Modify access levels
        - Change group roles
        - Update permissions

        ### Examples

        - Update policy role:

          Changes a group's access level.

          ```yaml
          runnerId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          groupId: "f53d2330-3795-4c5d-a1f3-453121af9c60"
          role: RUNNER_ROLE_USER
          ```

        Args:
          group_id: group_id specifies the group_id identifier

          runner_id: runner_id specifies the project identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.RunnerService/UpdateRunnerPolicy",
            body=await async_maybe_transform(
                {
                    "group_id": group_id,
                    "role": role,
                    "runner_id": runner_id,
                },
                policy_update_params.PolicyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyUpdateResponse,
        )

    def list(
        self,
        *,
        token: str | Omit = omit,
        page_size: int | Omit = omit,
        pagination: policy_list_params.Pagination | Omit = omit,
        runner_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[RunnerPolicy, AsyncPoliciesPage[RunnerPolicy]]:
        """
        Lists policies for a runner.

        Use this method to:

        - View access controls
        - Check policy configurations
        - Audit permissions

        ### Examples

        - List policies:

          Shows all policies for a runner.

          ```yaml
          runnerId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          pagination:
            pageSize: 20
          ```

        Args:
          pagination: pagination contains the pagination options for listing project policies

          runner_id: runner_id specifies the project identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.RunnerService/ListRunnerPolicies",
            page=AsyncPoliciesPage[RunnerPolicy],
            body=maybe_transform(
                {
                    "pagination": pagination,
                    "runner_id": runner_id,
                },
                policy_list_params.PolicyListParams,
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
                    policy_list_params.PolicyListParams,
                ),
            ),
            model=RunnerPolicy,
            method="post",
        )

    async def delete(
        self,
        *,
        group_id: str | Omit = omit,
        runner_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Deletes a runner policy.

        Use this method to:

        - Remove access controls
        - Revoke permissions
        - Clean up policies

        ### Examples

        - Delete policy:

          Removes a group's access policy.

          ```yaml
          runnerId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          groupId: "f53d2330-3795-4c5d-a1f3-453121af9c60"
          ```

        Args:
          group_id: group_id specifies the group_id identifier

          runner_id: runner_id specifies the project identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.RunnerService/DeleteRunnerPolicy",
            body=await async_maybe_transform(
                {
                    "group_id": group_id,
                    "runner_id": runner_id,
                },
                policy_delete_params.PolicyDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class PoliciesResourceWithRawResponse:
    def __init__(self, policies: PoliciesResource) -> None:
        self._policies = policies

        self.create = to_raw_response_wrapper(
            policies.create,
        )
        self.update = to_raw_response_wrapper(
            policies.update,
        )
        self.list = to_raw_response_wrapper(
            policies.list,
        )
        self.delete = to_raw_response_wrapper(
            policies.delete,
        )


class AsyncPoliciesResourceWithRawResponse:
    def __init__(self, policies: AsyncPoliciesResource) -> None:
        self._policies = policies

        self.create = async_to_raw_response_wrapper(
            policies.create,
        )
        self.update = async_to_raw_response_wrapper(
            policies.update,
        )
        self.list = async_to_raw_response_wrapper(
            policies.list,
        )
        self.delete = async_to_raw_response_wrapper(
            policies.delete,
        )


class PoliciesResourceWithStreamingResponse:
    def __init__(self, policies: PoliciesResource) -> None:
        self._policies = policies

        self.create = to_streamed_response_wrapper(
            policies.create,
        )
        self.update = to_streamed_response_wrapper(
            policies.update,
        )
        self.list = to_streamed_response_wrapper(
            policies.list,
        )
        self.delete = to_streamed_response_wrapper(
            policies.delete,
        )


class AsyncPoliciesResourceWithStreamingResponse:
    def __init__(self, policies: AsyncPoliciesResource) -> None:
        self._policies = policies

        self.create = async_to_streamed_response_wrapper(
            policies.create,
        )
        self.update = async_to_streamed_response_wrapper(
            policies.update,
        )
        self.list = async_to_streamed_response_wrapper(
            policies.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            policies.delete,
        )
