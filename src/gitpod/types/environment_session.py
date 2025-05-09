# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EnvironmentSession"]


class EnvironmentSession(BaseModel):
    id: Optional[str] = None
    """Environment session ID."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Time when the session was created."""

    environment_class_id: Optional[str] = FieldInfo(alias="environmentClassId", default=None)
    """Environment class ID associated with the session."""

    environment_id: Optional[str] = FieldInfo(alias="environmentId", default=None)
    """Environment ID associated with the session."""

    project_id: Optional[str] = FieldInfo(alias="projectId", default=None)
    """Project ID associated with the session."""

    runner_id: Optional[str] = FieldInfo(alias="runnerId", default=None)
    """Runner ID associated with the session."""

    stopped_at: Optional[datetime] = FieldInfo(alias="stoppedAt", default=None)
    """Time when the session was stopped."""

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)
    """User ID who created the session."""
