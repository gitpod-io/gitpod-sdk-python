# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .task_spec import TaskSpec
from ...._models import BaseModel
from .task_metadata import TaskMetadata

__all__ = ["Task"]


class Task(BaseModel):
    id: Optional[str] = None

    depends_on: Optional[List[str]] = FieldInfo(alias="dependsOn", default=None)
    """dependencies specifies the IDs of the automations this task depends on."""

    environment_id: Optional[str] = FieldInfo(alias="environmentId", default=None)

    metadata: Optional[TaskMetadata] = None

    spec: Optional[TaskSpec] = None
