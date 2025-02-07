# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .task_execution_phase import TaskExecutionPhase

__all__ = ["TaskExecutionStatus", "Step"]


class Step(BaseModel):
    id: Optional[str] = None
    """ID is the ID of the execution step"""

    failure_message: Optional[str] = FieldInfo(alias="failureMessage", default=None)
    """failure_message summarises why the step failed to operate.

    If this is non-empty the step has failed to operate and will likely transition
    to a failed state.
    """

    phase: Optional[TaskExecutionPhase] = None
    """phase is the current phase of the execution step"""


class TaskExecutionStatus(BaseModel):
    failure_message: Optional[str] = FieldInfo(alias="failureMessage", default=None)
    """failure_message summarises why the task execution failed to operate.

    If this is non-empty the task execution has failed to operate and will likely
    transition to a failed state.
    """

    log_url: Optional[str] = FieldInfo(alias="logUrl", default=None)
    """log_url is the URL to the logs of the task's steps.

    If this is empty, the task either has no logs or has not yet started.
    """

    phase: Optional[TaskExecutionPhase] = None
    """the phase of a task execution represents the aggregated phase of all steps."""

    status_version: Optional[str] = FieldInfo(alias="statusVersion", default=None)
    """version of the status update.

    Task executions themselves are unversioned, but their status has different
    versions. The value of this field has no semantic meaning (e.g. don't interpret
    it as as a timestamp), but it can be used to impose a partial order. If
    a.status_version < b.status_version then a was the status before b.
    """

    steps: Optional[List[Step]] = None
    """steps provides the status for each individual step of the task execution.

    If a step is missing it has not yet started.
    """
