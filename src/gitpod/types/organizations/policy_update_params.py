# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from ..admission_level import AdmissionLevel
from .veto_exec_policy_param import VetoExecPolicyParam
from .conversation_sharing_policy import ConversationSharingPolicy

__all__ = [
    "PolicyUpdateParams",
    "AgentPolicy",
    "EditorVersionRestrictions",
    "ProjectCreationDefaults",
    "SecurityAgentPolicy",
    "SecurityAgentPolicyCrowdstrike",
]


class PolicyUpdateParams(TypedDict, total=False):
    organization_id: Required[Annotated[str, PropertyInfo(alias="organizationId")]]
    """organization_id is the ID of the organization to update policies for"""

    agent_policy: Annotated[Optional[AgentPolicy], PropertyInfo(alias="agentPolicy")]
    """agent_policy contains agent-specific policy settings"""

    allowed_editor_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="allowedEditorIds")]
    """
    allowed_editor_ids is the list of editor IDs that are allowed to be used in the
    organization
    """

    allow_local_runners: Annotated[Optional[bool], PropertyInfo(alias="allowLocalRunners")]
    """
    allow_local_runners controls whether local runners are allowed to be used in the
    organization
    """

    default_editor_id: Annotated[Optional[str], PropertyInfo(alias="defaultEditorId")]
    """
    default_editor_id is the default editor ID to be used when a user doesn't
    specify one
    """

    default_environment_image: Annotated[Optional[str], PropertyInfo(alias="defaultEnvironmentImage")]
    """
    default_environment_image is the default container image when none is defined in
    repo
    """

    delete_archived_environments_after: Annotated[Optional[str], PropertyInfo(alias="deleteArchivedEnvironmentsAfter")]
    """
    delete_archived_environments_after controls how long archived environments are
    kept before automatic deletion. 0 means no automatic deletion. Maximum duration
    is 4 weeks (2419200 seconds).
    """

    editor_version_restrictions: Annotated[
        Dict[str, EditorVersionRestrictions], PropertyInfo(alias="editorVersionRestrictions")
    ]
    """
    editor_version_restrictions restricts which editor versions can be used. Maps
    editor ID to version policy with allowed major versions.
    """

    maximum_environment_lifetime: Annotated[Optional[str], PropertyInfo(alias="maximumEnvironmentLifetime")]
    """
    maximum_environment_lifetime controls for how long environments are allowed to
    be reused. 0 means no maximum lifetime. Maximum duration is 180 days (15552000
    seconds).
    """

    maximum_environments_per_user: Annotated[Optional[str], PropertyInfo(alias="maximumEnvironmentsPerUser")]
    """
    maximum_environments_per_user limits total environments (running or stopped) per
    user
    """

    maximum_environment_timeout: Annotated[Optional[str], PropertyInfo(alias="maximumEnvironmentTimeout")]
    """
    maximum_environment_timeout controls the maximum timeout allowed for
    environments in seconds. 0 means no limit (never). Minimum duration is 30
    minutes (1800 seconds). value must be 0s (no limit) or at least 1800s (30
    minutes):

    ```
    this == duration('0s') || this >= duration('1800s')
    ```
    """

    maximum_running_environments_per_user: Annotated[
        Optional[str], PropertyInfo(alias="maximumRunningEnvironmentsPerUser")
    ]
    """
    maximum_running_environments_per_user limits simultaneously running environments
    per user
    """

    max_port_admission_level: Annotated[Optional[AdmissionLevel], PropertyInfo(alias="maxPortAdmissionLevel")]
    """
    max_port_admission_level caps the maximum admission level a user-opened port may
    use. UNSPECIFIED means no cap (any AdmissionLevel value is allowed). System
    ports (VS Code Browser, agents) are exempt. The legacy port_sharing_disabled
    field, when true, takes precedence and blocks all user-initiated port sharing.
    """

    members_create_projects: Annotated[Optional[bool], PropertyInfo(alias="membersCreateProjects")]
    """members_create_projects controls whether members can create projects"""

    members_require_projects: Annotated[Optional[bool], PropertyInfo(alias="membersRequireProjects")]
    """
    members_require_projects controls whether environments can only be created from
    projects by non-admin users
    """

    port_sharing_disabled: Annotated[Optional[bool], PropertyInfo(alias="portSharingDisabled")]
    """
    port_sharing_disabled controls whether user-initiated port sharing is disabled
    in the organization. System ports (VS Code Browser, agents) are always exempt
    from this policy.
    """

    project_creation_defaults: Annotated[
        Optional[ProjectCreationDefaults], PropertyInfo(alias="projectCreationDefaults")
    ]
    """
    project_creation_defaults contains updates to default settings applied to newly
    created projects.
    """

    require_custom_domain_access: Annotated[Optional[bool], PropertyInfo(alias="requireCustomDomainAccess")]
    """
    require_custom_domain_access controls whether users must access via custom
    domain when one is configured. When true, access via app.gitpod.io is blocked.
    """

    restrict_account_creation_to_scim: Annotated[Optional[bool], PropertyInfo(alias="restrictAccountCreationToScim")]
    """
    restrict_account_creation_to_scim controls whether account creation is
    restricted to SCIM-provisioned users only. When true and SCIM is configured for
    the organization, only users provisioned via SCIM can create accounts.
    """

    security_agent_policy: Annotated[Optional[SecurityAgentPolicy], PropertyInfo(alias="securityAgentPolicy")]
    """security_agent_policy contains security agent configuration updates"""

    veto_exec_policy: Annotated[Optional[VetoExecPolicyParam], PropertyInfo(alias="vetoExecPolicy")]
    """veto_exec_policy contains the veto exec policy for environments."""

    web_browser_disabled: Annotated[Optional[bool], PropertyInfo(alias="webBrowserDisabled")]
    """
    web_browser_disabled controls whether users can open the built-in web browser
    from environment pages. This does not affect VS Code Browser.
    """


class AgentPolicy(TypedDict, total=False):
    """agent_policy contains agent-specific policy settings"""

    command_deny_list: Annotated[SequenceNotStr[str], PropertyInfo(alias="commandDenyList")]
    """
    command_deny_list contains a list of commands that agents are not allowed to
    execute
    """

    conversation_sharing_policy: Annotated[
        Optional[ConversationSharingPolicy], PropertyInfo(alias="conversationSharingPolicy")
    ]
    """conversation_sharing_policy controls whether agent conversations can be shared"""

    max_subagents_per_environment: Annotated[Optional[int], PropertyInfo(alias="maxSubagentsPerEnvironment")]
    """
    max_subagents_per_environment limits the number of non-terminal sub-agents a
    parent can have running simultaneously in the same environment. Valid range:
    0-10. Zero means use the default (5).
    """

    mcp_disabled: Annotated[Optional[bool], PropertyInfo(alias="mcpDisabled")]
    """
    mcp_disabled controls whether MCP (Model Context Protocol) is disabled for
    agents
    """

    scm_tools_allowed_group_id: Annotated[Optional[str], PropertyInfo(alias="scmToolsAllowedGroupId")]
    """
    scm_tools_allowed_group_id restricts SCM tools access to members of this group.
    Empty means no restriction (all users can use SCM tools if not disabled).
    """

    scm_tools_disabled: Annotated[Optional[bool], PropertyInfo(alias="scmToolsDisabled")]
    """
    scm_tools_disabled controls whether SCM (Source Control Management) tools are
    disabled for agents
    """


class EditorVersionRestrictions(TypedDict, total=False):
    """EditorVersionPolicy defines the version policy for a specific editor"""

    allowed_versions: Annotated[SequenceNotStr[str], PropertyInfo(alias="allowedVersions")]
    """
    allowed_versions lists the versions that are allowed If empty, we will use the
    latest version of the editor

    Examples for JetBrains: `["2025.2", "2025.1", "2024.3"]`
    """


class ProjectCreationDefaults(TypedDict, total=False):
    """
    project_creation_defaults contains updates to default settings applied to newly created projects.
    """

    insights_enabled: Annotated[Optional[bool], PropertyInfo(alias="insightsEnabled")]
    """
    insights_enabled controls whether Insights (co-author attribution) is
    automatically enabled on newly created projects.
    """


class SecurityAgentPolicyCrowdstrike(TypedDict, total=False):
    """crowdstrike contains CrowdStrike Falcon configuration updates"""

    additional_options: Annotated[Dict[str, str], PropertyInfo(alias="additionalOptions")]
    """
    additional*options contains additional FALCONCTL_OPT*\\** options as key-value
    pairs
    """

    cid_secret_id: Annotated[Optional[str], PropertyInfo(alias="cidSecretId")]
    """
    cid_secret_id references an organization secret containing the Customer ID (CID)
    """

    enabled: Optional[bool]
    """enabled controls whether CrowdStrike Falcon is deployed to environments"""

    image: Optional[str]
    """image is the CrowdStrike Falcon sensor container image reference"""

    tags: Optional[str]
    """tags are optional tags to apply to the Falcon sensor"""


class SecurityAgentPolicy(TypedDict, total=False):
    """security_agent_policy contains security agent configuration updates"""

    crowdstrike: Optional[SecurityAgentPolicyCrowdstrike]
    """crowdstrike contains CrowdStrike Falcon configuration updates"""
