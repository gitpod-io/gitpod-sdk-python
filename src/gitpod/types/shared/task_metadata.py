# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .subject import Subject
from ..._models import BaseModel
from .automation_trigger import AutomationTrigger

__all__ = ["TaskMetadata"]


class TaskMetadata(BaseModel):
    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """created_at is the time the task was created."""

    creator: Optional[Subject] = None
    """creator describes the principal who created the task."""

    description: Optional[str] = None
    """description is a user-facing description for the task.

    It can be used to provide context and documentation for the task.
    """

    name: Optional[str] = None
    """name is a user-facing name for the task.

    Unlike the reference, this field is not unique, and not referenced by the
    system. This is a short descriptive name for the task.
    """

    reference: Optional[str] = None
    """
    reference is a user-facing identifier for the task which must be unique on the
    environment. It is used to express dependencies between tasks, and to identify
    the task in user interactions (e.g. the CLI).
    """

    triggered_by: Optional[List[AutomationTrigger]] = FieldInfo(alias="triggeredBy", default=None)
    """triggered_by is a list of trigger that start the task."""
