# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["TaskExecutionPhase"]

TaskExecutionPhase: TypeAlias = Literal[
    "TASK_EXECUTION_PHASE_UNSPECIFIED",
    "TASK_EXECUTION_PHASE_PENDING",
    "TASK_EXECUTION_PHASE_RUNNING",
    "TASK_EXECUTION_PHASE_SUCCEEDED",
    "TASK_EXECUTION_PHASE_FAILED",
    "TASK_EXECUTION_PHASE_STOPPED",
]
