# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .shared_params.subject import Subject

__all__ = ["ProjectPrebuildConfigurationParam", "Trigger", "TriggerDailySchedule"]


class TriggerDailySchedule(TypedDict, total=False):
    """
    daily_schedule triggers a prebuild once per day at the specified hour (UTC).
     The actual start time may vary slightly to distribute system load.
    """

    hour_utc: Annotated[int, PropertyInfo(alias="hourUtc")]
    """
    hour_utc is the hour of day (0-23) in UTC when the prebuild should start. The
    actual start time may be adjusted by a few minutes to balance system load.
    """


class Trigger(TypedDict, total=False):
    """trigger defines when prebuilds should be created."""

    daily_schedule: Required[Annotated[TriggerDailySchedule, PropertyInfo(alias="dailySchedule")]]
    """
    daily_schedule triggers a prebuild once per day at the specified hour (UTC). The
    actual start time may vary slightly to distribute system load.
    """


class ProjectPrebuildConfigurationParam(TypedDict, total=False):
    """
    ProjectPrebuildConfiguration defines how prebuilds are created for a project.
     Prebuilds create environment snapshots that enable faster environment startup times.
    """

    enabled: bool
    """
    enabled controls whether prebuilds are created for this project. When disabled,
    no automatic prebuilds will be triggered.
    """

    enable_jetbrains_warmup: Annotated[bool, PropertyInfo(alias="enableJetbrainsWarmup")]
    """
    enable_jetbrains_warmup controls whether JetBrains IDE warmup runs during
    prebuilds.
    """

    environment_class_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="environmentClassIds")]
    """
    environment_class_ids specifies which environment classes should have prebuilds
    created. If empty, no prebuilds are created.
    """

    executor: Subject
    """
    executor specifies who runs prebuilds for this project. The executor's SCM
    credentials are used to clone the repository. If not set, defaults to the
    project creator.
    """

    timeout: str
    """
    timeout is the maximum duration allowed for a prebuild to complete. If not
    specified, defaults to 1 hour. Must be between 5 minutes and 2 hours.
    """

    trigger: Trigger
    """trigger defines when prebuilds should be created."""
