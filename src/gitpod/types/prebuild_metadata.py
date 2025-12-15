# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.subject import Subject
from .prebuild_trigger import PrebuildTrigger

__all__ = ["PrebuildMetadata"]


class PrebuildMetadata(BaseModel):
    """PrebuildMetadata contains metadata about the prebuild"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """created_at is when the prebuild was created"""

    creator: Subject
    """
    creator is the identity of who created the prebuild. For manual prebuilds, this
    is the user who triggered it. For scheduled prebuilds, this is the configured
    executor.
    """

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """updated_at is when the prebuild was last updated"""

    environment_class_id: Optional[str] = FieldInfo(alias="environmentClassId", default=None)
    """
    environment_class_id is the environment class used to create this prebuild.
    While the prebuild is created with a specific environment class, environments
    with different classes (e.g., smaller or larger instance sizes) can be created
    from the same prebuild, as long as they run on the same runner. If not specified
    in create requests, uses the project's default environment class.
    """

    executor: Optional[Subject] = None
    """
    executor is the identity used to run the prebuild. The executor's SCM
    credentials are used to clone the repository. If not set, the creator's identity
    is used.
    """

    organization_id: Optional[str] = FieldInfo(alias="organizationId", default=None)
    """organization_id is the ID of the organization that owns the prebuild"""

    project_id: Optional[str] = FieldInfo(alias="projectId", default=None)
    """project_id is the ID of the project this prebuild was created for"""

    triggered_by: Optional[PrebuildTrigger] = FieldInfo(alias="triggeredBy", default=None)
    """trigger describes the trigger that created this prebuild."""
