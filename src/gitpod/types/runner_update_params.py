# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .runner_phase import RunnerPhase
from .runner_release_channel import RunnerReleaseChannel

__all__ = ["RunnerUpdateParams", "Spec", "SpecConfiguration"]


class RunnerUpdateParams(TypedDict, total=False):
    name: Optional[str]
    """The runner's name which is shown to users"""

    runner_id: Annotated[str, PropertyInfo(alias="runnerId")]
    """runner_id specifies which runner to be updated.

    +required
    """

    spec: Optional[Spec]


class SpecConfiguration(TypedDict, total=False):
    auto_update: Annotated[Optional[bool], PropertyInfo(alias="autoUpdate")]
    """auto_update indicates whether the runner should automatically update itself."""

    release_channel: Annotated[Optional[RunnerReleaseChannel], PropertyInfo(alias="releaseChannel")]
    """The release channel the runner is on"""


class Spec(TypedDict, total=False):
    configuration: Optional[SpecConfiguration]

    desired_phase: Annotated[Optional[RunnerPhase], PropertyInfo(alias="desiredPhase")]
    """RunnerPhase represents the phase a runner is in"""
