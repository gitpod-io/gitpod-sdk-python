# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .runs_on import RunsOn
from ..._models import BaseModel
from .environment_variable_item import EnvironmentVariableItem

__all__ = ["TaskSpec"]


class TaskSpec(BaseModel):
    command: Optional[str] = None
    """command contains the command the task should execute"""

    env: Optional[List[EnvironmentVariableItem]] = None
    """env specifies environment variables for the task."""

    prebuild_requires_success: Optional[bool] = FieldInfo(alias="prebuildRequiresSuccess", default=None)
    """
    prebuild_requires_success controls whether a non-successful outcome of this task
    should fail the prebuild. When true and the task is triggered by a prebuild or
    before_snapshot trigger, any terminal phase other than SUCCEEDED (i.e. FAILED or
    STOPPED) will cause the prebuild to fail instead of just recording a warning.
    Defaults to false (existing behavior: task failures produce warnings only).
    """

    runs_on: Optional[RunsOn] = FieldInfo(alias="runsOn", default=None)
    """runs_on specifies the environment the task should run on."""
