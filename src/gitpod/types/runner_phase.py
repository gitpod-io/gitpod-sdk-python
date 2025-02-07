# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["RunnerPhase"]

RunnerPhase: TypeAlias = Literal[
    "RUNNER_PHASE_UNSPECIFIED",
    "RUNNER_PHASE_CREATED",
    "RUNNER_PHASE_INACTIVE",
    "RUNNER_PHASE_ACTIVE",
    "RUNNER_PHASE_DELETING",
    "RUNNER_PHASE_DELETED",
    "RUNNER_PHASE_DEGRADED",
]
