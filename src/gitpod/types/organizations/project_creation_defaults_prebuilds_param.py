# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..shared_params.subject import Subject

__all__ = ["ProjectCreationDefaultsPrebuildsParam", "Trigger", "TriggerDailySchedule"]


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
    """trigger defines when prebuilds should be created on newly created projects."""

    daily_schedule: Required[Annotated[TriggerDailySchedule, PropertyInfo(alias="dailySchedule")]]
    """
    daily_schedule triggers a prebuild once per day at the specified hour (UTC). The
    actual start time may vary slightly to distribute system load.
    """


class ProjectCreationDefaultsPrebuildsParam(TypedDict, total=False):
    """
    ProjectCreationDefaultsPrebuilds configures default prebuild settings.
     Presence of this message means prebuilds can be enabled for the default environment classes.
    """

    enable_jetbrains_warmup: Annotated[bool, PropertyInfo(alias="enableJetbrainsWarmup")]
    """
    enable_jetbrains_warmup controls whether JetBrains IDE warmup runs during
    prebuilds on newly created projects.
    """

    prebuild_executor: Annotated[Subject, PropertyInfo(alias="prebuildExecutor")]
    """
    prebuild_executor is the service account used to run prebuilds on newly created
    projects. Must be a service account (not a user).
    """

    timeout: str
    """
    timeout is the maximum duration allowed for a prebuild to complete. If not
    specified, defaults to 1 hour. Must be between 5 minutes and 2 hours.
    """

    trigger: Trigger
    """trigger defines when prebuilds should be created on newly created projects."""
