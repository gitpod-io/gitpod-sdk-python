# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .workflow_step import WorkflowStep

__all__ = ["WorkflowAction", "Limits", "LimitsPerExecution"]


class LimitsPerExecution(BaseModel):
    """PerExecution defines limits per execution action."""

    max_time: Optional[str] = FieldInfo(alias="maxTime", default=None)
    """
    Maximum time allowed for a single execution action. Use standard duration format
    (e.g., "30m" for 30 minutes, "2h" for 2 hours).
    """


class Limits(BaseModel):
    """
    Limits defines execution limits for workflow actions.
    Concurrent actions limit cannot exceed total actions limit:
    ```
    this.max_parallel <= this.max_total
    ```
    """

    max_parallel: Optional[int] = FieldInfo(alias="maxParallel", default=None)
    """Maximum parallel actions must be between 1 and 25:

    ```
    this >= 1 && this <= 25
    ```
    """

    max_total: Optional[int] = FieldInfo(alias="maxTotal", default=None)
    """Maximum total actions must be between 1 and 100:

    ```
    this >= 1 && this <= 100
    ```
    """

    per_execution: Optional[LimitsPerExecution] = FieldInfo(alias="perExecution", default=None)
    """PerExecution defines limits per execution action."""


class WorkflowAction(BaseModel):
    """WorkflowAction defines the actions to be executed in a workflow."""

    limits: Limits
    """
    Limits defines execution limits for workflow actions. Concurrent actions limit
    cannot exceed total actions limit:

    ```
    this.max_parallel <= this.max_total
    ```
    """

    steps: Optional[List[WorkflowStep]] = None
    """Automation must have between 1 and 50 steps:

    ```
    size(this) >= 1 && size(this) <= 50
    ```
    """
