# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ...shared.runs_on import RunsOn

__all__ = ["TaskSpec"]


class TaskSpec(BaseModel):
    command: Optional[str] = None
    """command contains the command the task should execute"""

    runs_on: Optional[RunsOn] = FieldInfo(alias="runsOn", default=None)
    """runs_on specifies the environment the task should run on."""
