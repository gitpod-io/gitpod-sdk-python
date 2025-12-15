# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.subject import Subject

__all__ = ["ProjectPrebuildConfiguration", "Trigger", "TriggerDailySchedule"]


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
    """trigger defines when prebuilds should be created."""

    daily_schedule: TriggerDailySchedule = FieldInfo(alias="dailySchedule")
    """
    daily_schedule triggers a prebuild once per day at the specified hour (UTC). The
    actual start time may vary slightly to distribute system load.
    """


class ProjectPrebuildConfiguration(BaseModel):
    """
    ProjectPrebuildConfiguration defines how prebuilds are created for a project.
     Prebuilds create environment snapshots that enable faster environment startup times.
    """

    enabled: Optional[bool] = None
    """
    enabled controls whether prebuilds are created for this project. When disabled,
    no automatic prebuilds will be triggered.
    """

    enable_jetbrains_warmup: Optional[bool] = FieldInfo(alias="enableJetbrainsWarmup", default=None)
    """
    enable_jetbrains_warmup controls whether JetBrains IDE warmup runs during
    prebuilds.
    """

    environment_class_ids: Optional[List[str]] = FieldInfo(alias="environmentClassIds", default=None)
    """
    environment_class_ids specifies which environment classes should have prebuilds
    created. If empty, no prebuilds are created.
    """

    executor: Optional[Subject] = None
    """
    executor specifies who runs prebuilds for this project. The executor's SCM
    credentials are used to clone the repository. If not set, defaults to the
    project creator.
    """

    timeout: Optional[str] = None
    """
    timeout is the maximum duration allowed for a prebuild to complete. If not
    specified, defaults to 1 hour. Must be between 5 minutes and 2 hours.
    """

    trigger: Optional[Trigger] = None
    """trigger defines when prebuilds should be created."""
