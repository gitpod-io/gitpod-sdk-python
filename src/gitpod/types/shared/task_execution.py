# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .task_execution_spec import TaskExecutionSpec
from .task_execution_status import TaskExecutionStatus
from .task_execution_metadata import TaskExecutionMetadata

__all__ = ["TaskExecution"]


class TaskExecution(BaseModel):
    id: str

    metadata: Optional[TaskExecutionMetadata] = None

    spec: Optional[TaskExecutionSpec] = None

    status: Optional[TaskExecutionStatus] = None
