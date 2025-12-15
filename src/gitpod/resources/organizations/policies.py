# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.organizations import policy_update_params, policy_retrieve_params
from ...types.organizations.policy_retrieve_response import PolicyRetrieveResponse

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
    ) -> PolicyRetrieveResponse:
        """
        Gets organization policy settings by organization ID.

        Use this method to:

        - Retrieve current policy settings for an organization
        - View resource limits and restrictions
        - Check allowed editors and other configurations

        ### Examples

        - Get organization policies:

          Retrieves policy settings for a specific organization.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          ```

        Args:
          organization_id: organization_id is the ID of the organization to retrieve policies for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.OrganizationService/GetOrganizationPolicies",
            body=maybe_transform({"organization_id": organization_id}, policy_retrieve_params.PolicyRetrieveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyRetrieveResponse,
        )

    def update(
        self,
        *,
        organization_id: str,
        agent_policy: Optional[policy_update_params.AgentPolicy] | Omit = omit,
        allowed_editor_ids: SequenceNotStr[str] | Omit = omit,
        allow_local_runners: Optional[bool] | Omit = omit,
        default_editor_id: Optional[str] | Omit = omit,
        default_environment_image: Optional[str] | Omit = omit,
        delete_archived_environments_after: Optional[str] | Omit = omit,
        editor_version_restrictions: Dict[str, policy_update_params.EditorVersionRestrictions] | Omit = omit,
        maximum_environment_lifetime: Optional[str] | Omit = omit,
        maximum_environments_per_user: Optional[str] | Omit = omit,
        maximum_environment_timeout: Optional[str] | Omit = omit,
        maximum_running_environments_per_user: Optional[str] | Omit = omit,
        members_create_projects: Optional[bool] | Omit = omit,
        members_require_projects: Optional[bool] | Omit = omit,
        port_sharing_disabled: Optional[bool] | Omit = omit,
        require_custom_domain_access: Optional[bool] | Omit = omit,
        security_agent_policy: Optional[policy_update_params.SecurityAgentPolicy] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Updates organization policy settings.

        Use this method to:

        - Configure editor restrictions
        - Set environment resource limits
        - Define project creation permissions
        - Customize default configurations

        ### Examples

        - Update editor policies:

          Restricts available editors and sets a default.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          allowedEditorIds:
            - "vscode"
            - "jetbrains"
          defaultEditorId: "vscode"
          ```

        - Set environment limits:

          Configures limits for environment usage.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          maximumEnvironmentTimeout: "3600s"
          maximumRunningEnvironmentsPerUser: "5"
          maximumEnvironmentsPerUser: "20"
          ```

        Args:
          organization_id: organization_id is the ID of the organization to update policies for

          agent_policy: agent_policy contains agent-specific policy settings

          allowed_editor_ids: allowed_editor_ids is the list of editor IDs that are allowed to be used in the
              organization

          allow_local_runners: allow_local_runners controls whether local runners are allowed to be used in the
              organization

          default_editor_id: default_editor_id is the default editor ID to be used when a user doesn't
              specify one

          default_environment_image: default_environment_image is the default container image when none is defined in
              repo

          delete_archived_environments_after: delete_archived_environments_after controls how long archived environments are
              kept before automatic deletion. 0 means no automatic deletion. Maximum duration
              is 4 weeks (2419200 seconds).

          editor_version_restrictions: editor_version_restrictions restricts which editor versions can be used. Maps
              editor ID to version policy with allowed major versions.

          maximum_environment_lifetime: maximum_environment_lifetime controls for how long environments are allowed to
              be reused. 0 means no maximum lifetime. Maximum duration is 180 days (15552000
              seconds).

          maximum_environments_per_user: maximum_environments_per_user limits total environments (running or stopped) per
              user

          maximum_environment_timeout: maximum_environment_timeout controls the maximum timeout allowed for
              environments in seconds. 0 means no limit (never). Minimum duration is 30
              minutes (1800 seconds).

          maximum_running_environments_per_user: maximum_running_environments_per_user limits simultaneously running environments
              per user

          members_create_projects: members_create_projects controls whether members can create projects

          members_require_projects: members_require_projects controls whether environments can only be created from
              projects by non-admin users

          port_sharing_disabled: port_sharing_disabled controls whether port sharing is disabled in the
              organization

          require_custom_domain_access: require_custom_domain_access controls whether users must access via custom
              domain when one is configured. When true, access via app.gitpod.io is blocked.

          security_agent_policy: security_agent_policy contains security agent configuration updates

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.OrganizationService/UpdateOrganizationPolicies",
            body=maybe_transform(
                {
                    "organization_id": organization_id,
                    "agent_policy": agent_policy,
                    "allowed_editor_ids": allowed_editor_ids,
                    "allow_local_runners": allow_local_runners,
                    "default_editor_id": default_editor_id,
                    "default_environment_image": default_environment_image,
                    "delete_archived_environments_after": delete_archived_environments_after,
                    "editor_version_restrictions": editor_version_restrictions,
                    "maximum_environment_lifetime": maximum_environment_lifetime,
                    "maximum_environments_per_user": maximum_environments_per_user,
                    "maximum_environment_timeout": maximum_environment_timeout,
                    "maximum_running_environments_per_user": maximum_running_environments_per_user,
                    "members_create_projects": members_create_projects,
                    "members_require_projects": members_require_projects,
                    "port_sharing_disabled": port_sharing_disabled,
                    "require_custom_domain_access": require_custom_domain_access,
                    "security_agent_policy": security_agent_policy,
                },
                policy_update_params.PolicyUpdateParams,
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
    ) -> PolicyRetrieveResponse:
        """
        Gets organization policy settings by organization ID.

        Use this method to:

        - Retrieve current policy settings for an organization
        - View resource limits and restrictions
        - Check allowed editors and other configurations

        ### Examples

        - Get organization policies:

          Retrieves policy settings for a specific organization.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          ```

        Args:
          organization_id: organization_id is the ID of the organization to retrieve policies for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.OrganizationService/GetOrganizationPolicies",
            body=await async_maybe_transform(
                {"organization_id": organization_id}, policy_retrieve_params.PolicyRetrieveParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyRetrieveResponse,
        )

    async def update(
        self,
        *,
        organization_id: str,
        agent_policy: Optional[policy_update_params.AgentPolicy] | Omit = omit,
        allowed_editor_ids: SequenceNotStr[str] | Omit = omit,
        allow_local_runners: Optional[bool] | Omit = omit,
        default_editor_id: Optional[str] | Omit = omit,
        default_environment_image: Optional[str] | Omit = omit,
        delete_archived_environments_after: Optional[str] | Omit = omit,
        editor_version_restrictions: Dict[str, policy_update_params.EditorVersionRestrictions] | Omit = omit,
        maximum_environment_lifetime: Optional[str] | Omit = omit,
        maximum_environments_per_user: Optional[str] | Omit = omit,
        maximum_environment_timeout: Optional[str] | Omit = omit,
        maximum_running_environments_per_user: Optional[str] | Omit = omit,
        members_create_projects: Optional[bool] | Omit = omit,
        members_require_projects: Optional[bool] | Omit = omit,
        port_sharing_disabled: Optional[bool] | Omit = omit,
        require_custom_domain_access: Optional[bool] | Omit = omit,
        security_agent_policy: Optional[policy_update_params.SecurityAgentPolicy] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Updates organization policy settings.

        Use this method to:

        - Configure editor restrictions
        - Set environment resource limits
        - Define project creation permissions
        - Customize default configurations

        ### Examples

        - Update editor policies:

          Restricts available editors and sets a default.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          allowedEditorIds:
            - "vscode"
            - "jetbrains"
          defaultEditorId: "vscode"
          ```

        - Set environment limits:

          Configures limits for environment usage.

          ```yaml
          organizationId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          maximumEnvironmentTimeout: "3600s"
          maximumRunningEnvironmentsPerUser: "5"
          maximumEnvironmentsPerUser: "20"
          ```

        Args:
          organization_id: organization_id is the ID of the organization to update policies for

          agent_policy: agent_policy contains agent-specific policy settings

          allowed_editor_ids: allowed_editor_ids is the list of editor IDs that are allowed to be used in the
              organization

          allow_local_runners: allow_local_runners controls whether local runners are allowed to be used in the
              organization

          default_editor_id: default_editor_id is the default editor ID to be used when a user doesn't
              specify one

          default_environment_image: default_environment_image is the default container image when none is defined in
              repo

          delete_archived_environments_after: delete_archived_environments_after controls how long archived environments are
              kept before automatic deletion. 0 means no automatic deletion. Maximum duration
              is 4 weeks (2419200 seconds).

          editor_version_restrictions: editor_version_restrictions restricts which editor versions can be used. Maps
              editor ID to version policy with allowed major versions.

          maximum_environment_lifetime: maximum_environment_lifetime controls for how long environments are allowed to
              be reused. 0 means no maximum lifetime. Maximum duration is 180 days (15552000
              seconds).

          maximum_environments_per_user: maximum_environments_per_user limits total environments (running or stopped) per
              user

          maximum_environment_timeout: maximum_environment_timeout controls the maximum timeout allowed for
              environments in seconds. 0 means no limit (never). Minimum duration is 30
              minutes (1800 seconds).

          maximum_running_environments_per_user: maximum_running_environments_per_user limits simultaneously running environments
              per user

          members_create_projects: members_create_projects controls whether members can create projects

          members_require_projects: members_require_projects controls whether environments can only be created from
              projects by non-admin users

          port_sharing_disabled: port_sharing_disabled controls whether port sharing is disabled in the
              organization

          require_custom_domain_access: require_custom_domain_access controls whether users must access via custom
              domain when one is configured. When true, access via app.gitpod.io is blocked.

          security_agent_policy: security_agent_policy contains security agent configuration updates

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.OrganizationService/UpdateOrganizationPolicies",
            body=await async_maybe_transform(
                {
                    "organization_id": organization_id,
                    "agent_policy": agent_policy,
                    "allowed_editor_ids": allowed_editor_ids,
                    "allow_local_runners": allow_local_runners,
                    "default_editor_id": default_editor_id,
                    "default_environment_image": default_environment_image,
                    "delete_archived_environments_after": delete_archived_environments_after,
                    "editor_version_restrictions": editor_version_restrictions,
                    "maximum_environment_lifetime": maximum_environment_lifetime,
                    "maximum_environments_per_user": maximum_environments_per_user,
                    "maximum_environment_timeout": maximum_environment_timeout,
                    "maximum_running_environments_per_user": maximum_running_environments_per_user,
                    "members_create_projects": members_create_projects,
                    "members_require_projects": members_require_projects,
                    "port_sharing_disabled": port_sharing_disabled,
                    "require_custom_domain_access": require_custom_domain_access,
                    "security_agent_policy": security_agent_policy,
                },
                policy_update_params.PolicyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class PoliciesResourceWithRawResponse:
    def __init__(self, policies: PoliciesResource) -> None:
        self._policies = policies

        self.retrieve = to_raw_response_wrapper(
            policies.retrieve,
        )
        self.update = to_raw_response_wrapper(
            policies.update,
        )


class AsyncPoliciesResourceWithRawResponse:
    def __init__(self, policies: AsyncPoliciesResource) -> None:
        self._policies = policies

        self.retrieve = async_to_raw_response_wrapper(
            policies.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            policies.update,
        )


class PoliciesResourceWithStreamingResponse:
    def __init__(self, policies: PoliciesResource) -> None:
        self._policies = policies

        self.retrieve = to_streamed_response_wrapper(
            policies.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            policies.update,
        )


class AsyncPoliciesResourceWithStreamingResponse:
    def __init__(self, policies: AsyncPoliciesResource) -> None:
        self._policies = policies

        self.retrieve = async_to_streamed_response_wrapper(
            policies.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            policies.update,
        )
