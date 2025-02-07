# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["ServicePhase"]

ServicePhase: TypeAlias = Literal[
    "SERVICE_PHASE_UNSPECIFIED",
    "SERVICE_PHASE_STARTING",
    "SERVICE_PHASE_RUNNING",
    "SERVICE_PHASE_STOPPING",
    "SERVICE_PHASE_STOPPED",
    "SERVICE_PHASE_FAILED",
    "SERVICE_PHASE_DELETED",
]
