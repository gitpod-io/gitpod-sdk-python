# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["UpdateWindowParam"]


class UpdateWindowParam(TypedDict, total=False):
    """
    UpdateWindow defines a daily time window (UTC) during which auto-updates are allowed.
     The window must be at least 2 hours long.
     Overnight windows are supported (e.g., start_hour=22, end_hour=4).
    """

    end_hour: Annotated[Optional[int], PropertyInfo(alias="endHour")]
    """
    end_hour is the end of the update window as a UTC hour (0-23). If not set,
    defaults to start_hour + 2.
    """

    start_hour: Annotated[Optional[int], PropertyInfo(alias="startHour")]
    """
    start_hour is the beginning of the update window as a UTC hour (0-23). +required
    """
