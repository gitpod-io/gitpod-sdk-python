# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["PolicyUpdateParams"]


class PolicyUpdateParams(TypedDict, total=False):
    organization_id: Required[Annotated[str, PropertyInfo(alias="organizationId")]]
    """organization_id is the ID of the organization to update policies for"""

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

    maximum_environments_per_user: Annotated[Optional[str], PropertyInfo(alias="maximumEnvironmentsPerUser")]
    """
    maximum_environments_per_user limits total environments (running or stopped) per
    user
    """

    maximum_environment_timeout: Annotated[Optional[str], PropertyInfo(alias="maximumEnvironmentTimeout")]
    """
    maximum_environment_timeout controls the maximum timeout allowed for
    environments in seconds. 0 means no limit (never). Minimum duration is 30
    minutes.
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
