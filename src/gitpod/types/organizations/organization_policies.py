# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .agent_policy import AgentPolicy
from .security_agent_policy import SecurityAgentPolicy

__all__ = ["OrganizationPolicies", "EditorVersionRestrictions"]


class EditorVersionRestrictions(BaseModel):
    """EditorVersionPolicy defines the version policy for a specific editor"""

    allowed_versions: Optional[List[str]] = FieldInfo(alias="allowedVersions", default=None)
    """
    allowed_versions lists the versions that are allowed If empty, we will use the
    latest version of the editor

    Examples for JetBrains: `["2025.2", "2025.1", "2024.3"]`
    """


class OrganizationPolicies(BaseModel):
    agent_policy: AgentPolicy = FieldInfo(alias="agentPolicy")
    """agent_policy contains agent-specific policy settings"""

    allowed_editor_ids: List[str] = FieldInfo(alias="allowedEditorIds")
    """
    allowed_editor_ids is the list of editor IDs that are allowed to be used in the
    organization
    """

    allow_local_runners: bool = FieldInfo(alias="allowLocalRunners")
    """
    allow_local_runners controls whether local runners are allowed to be used in the
    organization
    """

    default_editor_id: str = FieldInfo(alias="defaultEditorId")
    """
    default_editor_id is the default editor ID to be used when a user doesn't
    specify one
    """

    default_environment_image: str = FieldInfo(alias="defaultEnvironmentImage")
    """
    default_environment_image is the default container image when none is defined in
    repo
    """

    maximum_environments_per_user: str = FieldInfo(alias="maximumEnvironmentsPerUser")
    """
    maximum_environments_per_user limits total environments (running or stopped) per
    user
    """

    maximum_running_environments_per_user: str = FieldInfo(alias="maximumRunningEnvironmentsPerUser")
    """
    maximum_running_environments_per_user limits simultaneously running environments
    per user
    """

    members_create_projects: bool = FieldInfo(alias="membersCreateProjects")
    """members_create_projects controls whether members can create projects"""

    members_require_projects: bool = FieldInfo(alias="membersRequireProjects")
    """
    members_require_projects controls whether environments can only be created from
    projects by non-admin users
    """

    organization_id: str = FieldInfo(alias="organizationId")
    """organization_id is the ID of the organization"""

    port_sharing_disabled: bool = FieldInfo(alias="portSharingDisabled")
    """
    port_sharing_disabled controls whether port sharing is disabled in the
    organization
    """

    require_custom_domain_access: bool = FieldInfo(alias="requireCustomDomainAccess")
    """
    require_custom_domain_access controls whether users must access via custom
    domain when one is configured. When true, access via app.gitpod.io is blocked.
    """

    delete_archived_environments_after: Optional[str] = FieldInfo(alias="deleteArchivedEnvironmentsAfter", default=None)
    """
    delete_archived_environments_after controls how long archived environments are
    kept before automatic deletion. 0 means no automatic deletion. Maximum duration
    is 4 weeks (2419200 seconds).
    """

    editor_version_restrictions: Optional[Dict[str, EditorVersionRestrictions]] = FieldInfo(
        alias="editorVersionRestrictions", default=None
    )
    """
    editor_version_restrictions restricts which editor versions can be used. Maps
    editor ID to version policy, editor_version_restrictions not set means no
    restrictions. If empty or not set for an editor, we will use the latest version
    of the editor
    """

    maximum_environment_lifetime: Optional[str] = FieldInfo(alias="maximumEnvironmentLifetime", default=None)
    """
    maximum_environment_lifetime controls for how long environments are allowed to
    be reused. 0 means no maximum lifetime. Maximum duration is 180 days (15552000
    seconds).
    """

    maximum_environment_timeout: Optional[str] = FieldInfo(alias="maximumEnvironmentTimeout", default=None)
    """
    maximum_environment_timeout controls the maximum timeout allowed for
    environments in seconds. 0 means no limit (never). Minimum duration is 30
    minutes (1800 seconds).
    """

    security_agent_policy: Optional[SecurityAgentPolicy] = FieldInfo(alias="securityAgentPolicy", default=None)
    """
    security_agent_policy contains security agent configuration for the
    organization. When configured, security agents are automatically deployed to all
    environments.
    """
