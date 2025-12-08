# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EnvironmentUsageRecord"]


class EnvironmentUsageRecord(BaseModel):
    """
    EnvironmentUsageRecord represents a record of an environment from start to stop.
    """

    id: Optional[str] = None
    """Environment usage record ID."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Time when the environment was created."""

    environment_class_id: Optional[str] = FieldInfo(alias="environmentClassId", default=None)
    """Environment class ID associated with the record."""

    environment_id: Optional[str] = FieldInfo(alias="environmentId", default=None)
    """Environment ID associated with the record."""

    project_id: Optional[str] = FieldInfo(alias="projectId", default=None)
    """Project ID associated with the environment (if available)."""

    runner_id: Optional[str] = FieldInfo(alias="runnerId", default=None)
    """Runner ID associated with the environment."""

    stopped_at: Optional[datetime] = FieldInfo(alias="stoppedAt", default=None)
    """Time when the environment was stopped."""

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)
    """
    User ID is the ID of the user who created the environment associated with the
    record.
    """
