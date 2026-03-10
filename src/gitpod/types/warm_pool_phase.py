# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["WarmPoolPhase"]

WarmPoolPhase: TypeAlias = Literal[
    "WARM_POOL_PHASE_UNSPECIFIED",
    "WARM_POOL_PHASE_PENDING",
    "WARM_POOL_PHASE_READY",
    "WARM_POOL_PHASE_DEGRADED",
    "WARM_POOL_PHASE_DELETING",
    "WARM_POOL_PHASE_DELETED",
]
