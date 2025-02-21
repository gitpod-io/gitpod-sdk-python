# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .subject import Subject
from ..._models import BaseModel

__all__ = ["TaskExecutionMetadata"]


class TaskExecutionMetadata(BaseModel):
    completed_at: Optional[datetime] = FieldInfo(alias="completedAt", default=None)
    """completed_at is the time the task execution was done."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """created_at is the time the task was created."""

    creator: Optional[Subject] = None
    """creator describes the principal who created/started the task run."""

    environment_id: Optional[str] = FieldInfo(alias="environmentId", default=None)
    """environment_id is the ID of the environment in which the task run is executed."""

    started_at: Optional[datetime] = FieldInfo(alias="startedAt", default=None)
    """started_at is the time the task execution actually started to run."""

    started_by: Optional[str] = FieldInfo(alias="startedBy", default=None)
    """started_by describes the trigger that started the task execution."""

    task_id: Optional[str] = FieldInfo(alias="taskId", default=None)
    """task_id is the ID of the main task being executed."""
