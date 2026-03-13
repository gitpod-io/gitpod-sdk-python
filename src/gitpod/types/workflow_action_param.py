# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .workflow_step_param import WorkflowStepParam

__all__ = ["WorkflowActionParam", "Limits", "LimitsPerExecution"]


class LimitsPerExecution(TypedDict, total=False):
    """PerExecution defines limits per execution action."""

    max_time: Annotated[str, PropertyInfo(alias="maxTime")]
    """
    Maximum time allowed for a single execution action. Use standard duration format
    (e.g., "30m" for 30 minutes, "2h" for 2 hours).
    """


class Limits(TypedDict, total=False):
    """
    Limits defines execution limits for workflow actions.
    Concurrent actions limit cannot exceed total actions limit:
    ```
    this.max_parallel <= this.max_total
    ```
    """

    max_parallel: Annotated[int, PropertyInfo(alias="maxParallel")]
    """Maximum parallel actions must be between 1 and 25:

    ```
    this >= 1 && this <= 25
    ```
    """

    max_total: Annotated[int, PropertyInfo(alias="maxTotal")]
    """Maximum total actions must be between 1 and 100:

    ```
    this >= 1 && this <= 100
    ```
    """

    per_execution: Annotated[LimitsPerExecution, PropertyInfo(alias="perExecution")]
    """PerExecution defines limits per execution action."""


class WorkflowActionParam(TypedDict, total=False):
    """WorkflowAction defines the actions to be executed in a workflow."""

    limits: Required[Limits]
    """
    Limits defines execution limits for workflow actions. Concurrent actions limit
    cannot exceed total actions limit:

    ```
    this.max_parallel <= this.max_total
    ```
    """

    steps: Iterable[WorkflowStepParam]
    """Automation must have between 1 and 50 steps:

    ```
    size(this) >= 1 && size(this) <= 50
    ```
    """
