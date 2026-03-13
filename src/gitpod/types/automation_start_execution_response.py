# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .workflow_execution import WorkflowExecution

__all__ = ["AutomationStartExecutionResponse"]


class AutomationStartExecutionResponse(BaseModel):
    workflow_execution: Optional[WorkflowExecution] = FieldInfo(alias="workflowExecution", default=None)
    """WorkflowExecution represents a workflow execution instance."""
