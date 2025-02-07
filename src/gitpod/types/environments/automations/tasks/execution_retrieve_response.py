# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel
from ....shared.task_execution import TaskExecution

__all__ = ["ExecutionRetrieveResponse"]


class ExecutionRetrieveResponse(BaseModel):
    task_execution: Optional[TaskExecution] = FieldInfo(alias="taskExecution", default=None)
