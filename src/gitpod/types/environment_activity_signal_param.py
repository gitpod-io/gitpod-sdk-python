# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EnvironmentActivitySignalParam"]


class EnvironmentActivitySignalParam(TypedDict, total=False):
    """EnvironmentActivitySignal used to signal activity for an environment."""

    source: str
    """
    source of the activity signal, such as "VS Code", "SSH", or "Automations". It
    should be a human-readable string that describes the source of the activity
    signal.
    """

    timestamp: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    timestamp of when the activity was observed by the source. Only reported every 5
    minutes. Zero value means no activity was observed.
    """
