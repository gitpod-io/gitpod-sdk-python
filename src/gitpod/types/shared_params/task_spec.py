# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Annotated, TypedDict

from .runs_on import RunsOn
from ..._utils import PropertyInfo
from .environment_variable_item import EnvironmentVariableItem

__all__ = ["TaskSpec"]


class TaskSpec(TypedDict, total=False):
    command: str
    """command contains the command the task should execute"""

    env: Iterable[EnvironmentVariableItem]
    """env specifies environment variables for the task."""

    prebuild_requires_success: Annotated[bool, PropertyInfo(alias="prebuildRequiresSuccess")]
    """
    prebuild_requires_success controls whether a non-successful outcome of this task
    should fail the prebuild. When true and the task is triggered by a prebuild or
    before_snapshot trigger, any terminal phase other than SUCCEEDED (i.e. FAILED or
    STOPPED) will cause the prebuild to fail instead of just recording a warning.
    Defaults to false (existing behavior: task failures produce warnings only).
    """

    runs_on: Annotated[RunsOn, PropertyInfo(alias="runsOn")]
    """runs_on specifies the environment the task should run on."""
