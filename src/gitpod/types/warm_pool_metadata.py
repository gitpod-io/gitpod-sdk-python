# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WarmPoolMetadata"]


class WarmPoolMetadata(BaseModel):
    """WarmPoolMetadata contains metadata about the warm pool"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """created_at is when the warm pool was created"""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """updated_at is when the warm pool was last updated"""

    environment_class_id: Optional[str] = FieldInfo(alias="environmentClassId", default=None)
    """environment_class_id is the environment class whose instances are warmed"""

    organization_id: Optional[str] = FieldInfo(alias="organizationId", default=None)
    """organization_id is the ID of the organization that owns the warm pool"""

    project_id: Optional[str] = FieldInfo(alias="projectId", default=None)
    """project_id is the ID of the project this warm pool belongs to"""

    runner_id: Optional[str] = FieldInfo(alias="runnerId", default=None)
    """
    runner_id is the runner that manages this warm pool. Derived from the
    environment class.
    """
