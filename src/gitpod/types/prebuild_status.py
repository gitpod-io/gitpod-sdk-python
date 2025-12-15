# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .prebuild_phase import PrebuildPhase

__all__ = ["PrebuildStatus"]


class PrebuildStatus(BaseModel):
    """PrebuildStatus contains the current status and progress of a prebuild"""

    phase: PrebuildPhase
    """phase is the current phase of the prebuild lifecycle"""

    completion_time: Optional[datetime] = FieldInfo(alias="completionTime", default=None)
    """completion_time is when the prebuild completed (successfully or with failure)"""

    environment_id: Optional[str] = FieldInfo(alias="environmentId", default=None)
    """
    environment_id is the ID of the environment used to create this prebuild. This
    field is set when the prebuild environment is created.
    """

    failure_message: Optional[str] = FieldInfo(alias="failureMessage", default=None)
    """failure_message contains details about why the prebuild failed"""

    log_url: Optional[str] = FieldInfo(alias="logUrl", default=None)
    """
    log_url provides access to prebuild logs. During prebuild execution, this
    references the environment logs. After completion, this may reference archived
    logs.
    """

    status_version: Optional[str] = FieldInfo(alias="statusVersion", default=None)
    """
    status_version is incremented each time the status is updated. Used for
    optimistic concurrency control.
    """

    warning_message: Optional[str] = FieldInfo(alias="warningMessage", default=None)
    """
    warning_message contains warnings from the prebuild environment that indicate
    something went wrong but the prebuild could still complete. For example, the
    devcontainer failed to build but the environment is still usable. These warnings
    will likely affect any environment started from this prebuild.
    """
