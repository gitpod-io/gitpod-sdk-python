# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = [
    "PolicyUpdateParams",
    "AgentPolicy",
    "EditorVersionRestrictions",
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
    minutes (1800 seconds).
    """

    maximum_running_environments_per_user: Annotated[
        Optional[str], PropertyInfo(alias="maximumRunningEnvironmentsPerUser")
    ]
    """
    maximum_running_environments_per_user limits simultaneously running environments
    per user
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
    port_sharing_disabled controls whether port sharing is disabled in the
    organization
    """

    require_custom_domain_access: Annotated[Optional[bool], PropertyInfo(alias="requireCustomDomainAccess")]
    """
    require_custom_domain_access controls whether users must access via custom
    domain when one is configured. When true, access via app.gitpod.io is blocked.
    """

    security_agent_policy: Annotated[Optional[SecurityAgentPolicy], PropertyInfo(alias="securityAgentPolicy")]
    """security_agent_policy contains security agent configuration updates"""


class AgentPolicy(TypedDict, total=False):
    """agent_policy contains agent-specific policy settings"""

    command_deny_list: Annotated[SequenceNotStr[str], PropertyInfo(alias="commandDenyList")]
    """
    command_deny_list contains a list of commands that agents are not allowed to
    execute
    """

    mcp_disabled: Annotated[Optional[bool], PropertyInfo(alias="mcpDisabled")]
    """
    mcp_disabled controls whether MCP (Model Context Protocol) is disabled for
    agents
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
