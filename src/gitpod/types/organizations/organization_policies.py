# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["OrganizationPolicies"]


class OrganizationPolicies(BaseModel):
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

    maximum_environment_timeout: Optional[str] = FieldInfo(alias="maximumEnvironmentTimeout", default=None)
    """
    maximum_environment_timeout controls the maximum timeout allowed for
    environments in seconds. 0 means no limit (never). Minimum duration is 30
    minutes.
    """
