# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .environment_activity_signal_param import EnvironmentActivitySignalParam

__all__ = ["EnvironmentMarkActiveParams"]


class EnvironmentMarkActiveParams(TypedDict, total=False):
    activity_signal: Annotated[EnvironmentActivitySignalParam, PropertyInfo(alias="activitySignal")]
    """EnvironmentActivitySignal used to signal activity for an environment."""

    environment_id: Annotated[str, PropertyInfo(alias="environmentId")]
    """The ID of the environment to update activity for."""
