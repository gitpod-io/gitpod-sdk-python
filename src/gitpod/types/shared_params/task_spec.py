# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .runs_on import RunsOn
from ..._utils import PropertyInfo

__all__ = ["TaskSpec"]


class TaskSpec(TypedDict, total=False):
    command: str
    """command contains the command the task should execute"""

    runs_on: Annotated[RunsOn, PropertyInfo(alias="runsOn")]
    """runs_on specifies the environment the task should run on."""
