# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "WakeEventParam",
    "DevcontainerRebuild",
    "Environment",
    "LoopRetrigger",
    "LoopRetriggerUnmetCondition",
    "Timer",
]


class DevcontainerRebuild(TypedDict, total=False):
    environment_id: Annotated[str, PropertyInfo(alias="environmentId")]

    failure_message: Annotated[SequenceNotStr[str], PropertyInfo(alias="failureMessage")]

    phase: str
    """The devcontainer phase reached by the target session."""

    session_id: Annotated[str, PropertyInfo(alias="sessionId")]


class Environment(TypedDict, total=False):
    environment_id: Annotated[str, PropertyInfo(alias="environmentId")]

    failure_message: Annotated[SequenceNotStr[str], PropertyInfo(alias="failureMessage")]

    phase: str
    """The phase the environment reached (e.g. "running", "stopped", "deleted")."""


class LoopRetriggerUnmetCondition(TypedDict, total=False):
    id: str

    description: str

    expression: str

    iteration: int

    max_iterations: Annotated[int, PropertyInfo(alias="maxIterations")]

    reason: str


class LoopRetrigger(TypedDict, total=False):
    outputs: Dict[str, str]

    unmet_conditions: Annotated[Iterable[LoopRetriggerUnmetCondition], PropertyInfo(alias="unmetConditions")]


class Timer(TypedDict, total=False):
    fired_at: Annotated[Union[str, datetime], PropertyInfo(alias="firedAt", format="iso8601")]
    """The actual time the timer was evaluated as expired."""


class WakeEventParam(TypedDict, total=False):
    """
    WakeEvent is sent by the backend to wake an agent when a registered interest fires.
     Delivered via SendToAgentExecution as a new oneof variant.
    """

    devcontainer_rebuild: Annotated[DevcontainerRebuild, PropertyInfo(alias="devcontainerRebuild")]

    environment: Environment

    interest_id: Annotated[str, PropertyInfo(alias="interestId")]
    """The interest ID that fired (from WaitingInfo.Interest.id)."""

    loop_retrigger: Annotated[LoopRetrigger, PropertyInfo(alias="loopRetrigger")]

    timer: Timer
