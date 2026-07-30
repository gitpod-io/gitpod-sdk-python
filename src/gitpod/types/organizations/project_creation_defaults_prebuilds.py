# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.subject import Subject

__all__ = ["ProjectCreationDefaultsPrebuilds", "Trigger", "TriggerDailySchedule"]


class TriggerDailySchedule(BaseModel):
    """
    daily_schedule triggers a prebuild once per day at the specified hour (UTC).
     The actual start time may vary slightly to distribute system load.
    """

    hour_utc: Optional[int] = FieldInfo(alias="hourUtc", default=None)
    """
    hour_utc is the hour of day (0-23) in UTC when the prebuild should start. The
    actual start time may be adjusted by a few minutes to balance system load.
    """


class Trigger(BaseModel):
    """trigger defines when prebuilds should be created on newly created projects."""

    daily_schedule: TriggerDailySchedule = FieldInfo(alias="dailySchedule")
    """
    daily_schedule triggers a prebuild once per day at the specified hour (UTC). The
    actual start time may vary slightly to distribute system load.
    """


class ProjectCreationDefaultsPrebuilds(BaseModel):
    """
    ProjectCreationDefaultsPrebuilds configures default prebuild settings.
     Presence of this message means prebuilds can be enabled for the default environment classes.
    """

    enable_jetbrains_warmup: Optional[bool] = FieldInfo(alias="enableJetbrainsWarmup", default=None)
    """
    enable_jetbrains_warmup controls whether JetBrains IDE warmup runs during
    prebuilds on newly created projects.
    """

    prebuild_executor: Optional[Subject] = FieldInfo(alias="prebuildExecutor", default=None)
    """
    prebuild_executor is the service account used to run prebuilds on newly created
    projects. Must be a service account (not a user).
    """

    timeout: Optional[str] = None
    """
    timeout is the maximum duration allowed for a prebuild to complete. If not
    specified, defaults to 1 hour. Must be between 5 minutes and 2 hours.
    """

    trigger: Optional[Trigger] = None
    """trigger defines when prebuilds should be created on newly created projects."""
