# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .workflow_execution_action import WorkflowExecutionAction

__all__ = ["AutomationRetrieveExecutionActionResponse"]


class AutomationRetrieveExecutionActionResponse(BaseModel):
    workflow_execution_action: Optional[WorkflowExecutionAction] = FieldInfo(
        alias="workflowExecutionAction", default=None
    )
    """WorkflowExecutionAction represents a workflow execution action instance."""
