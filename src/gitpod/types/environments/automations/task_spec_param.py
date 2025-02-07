# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo
from ...shared_params.runs_on import RunsOn

__all__ = ["TaskSpecParam"]


class TaskSpecParam(TypedDict, total=False):
    command: str
    """command contains the command the task should execute"""

    runs_on: Annotated[RunsOn, PropertyInfo(alias="runsOn")]
    """runs_on specifies the environment the task should run on."""
