# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["EnvironmentPhase"]

EnvironmentPhase: TypeAlias = Literal[
    "ENVIRONMENT_PHASE_UNSPECIFIED",
    "ENVIRONMENT_PHASE_CREATING",
    "ENVIRONMENT_PHASE_STARTING",
    "ENVIRONMENT_PHASE_RUNNING",
    "ENVIRONMENT_PHASE_UPDATING",
    "ENVIRONMENT_PHASE_STOPPING",
    "ENVIRONMENT_PHASE_STOPPED",
    "ENVIRONMENT_PHASE_DELETING",
    "ENVIRONMENT_PHASE_DELETED",
]
