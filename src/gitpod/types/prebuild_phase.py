# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["PrebuildPhase"]

PrebuildPhase: TypeAlias = Literal[
    "PREBUILD_PHASE_UNSPECIFIED",
    "PREBUILD_PHASE_PENDING",
    "PREBUILD_PHASE_STARTING",
    "PREBUILD_PHASE_RUNNING",
    "PREBUILD_PHASE_STOPPING",
    "PREBUILD_PHASE_SNAPSHOTTING",
    "PREBUILD_PHASE_COMPLETED",
    "PREBUILD_PHASE_FAILED",
    "PREBUILD_PHASE_CANCELLING",
    "PREBUILD_PHASE_CANCELLED",
    "PREBUILD_PHASE_DELETING",
    "PREBUILD_PHASE_DELETED",
]
