# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .task_spec import TaskSpec
from .task_execution_phase import TaskExecutionPhase

__all__ = ["TaskExecutionSpec", "Plan", "PlanStep", "PlanStepTask"]


class PlanStepTask(BaseModel):
    id: Optional[str] = None

    spec: Optional[TaskSpec] = None


class PlanStep(BaseModel):
    id: Optional[str] = None
    """ID is the ID of the execution step"""

    depends_on: Optional[List[str]] = FieldInfo(alias="dependsOn", default=None)

    label: Optional[str] = None

    service_id: Optional[str] = FieldInfo(alias="serviceId", default=None)

    task: Optional[PlanStepTask] = None


class Plan(BaseModel):
    steps: Optional[List[PlanStep]] = None


class TaskExecutionSpec(BaseModel):
    desired_phase: Optional[TaskExecutionPhase] = FieldInfo(alias="desiredPhase", default=None)
    """desired_phase is the phase the task execution should be in.

    Used to stop a running task execution early.
    """

    plan: Optional[List[Plan]] = None
    """plan is a list of groups of steps.

    The steps in a group are executed concurrently, while the groups are executed
    sequentially. The order of the groups is the order in which they are executed.
    """
