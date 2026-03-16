# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["UpdateWindow"]


class UpdateWindow(BaseModel):
    """
    UpdateWindow defines a daily time window (UTC) during which auto-updates are allowed.
     The window must be at least 2 hours long.
     Overnight windows are supported (e.g., start_hour=22, end_hour=4).
    """

    end_hour: Optional[int] = FieldInfo(alias="endHour", default=None)
    """
    end_hour is the end of the update window as a UTC hour (0-23). If not set,
    defaults to start_hour + 2.
    """

    start_hour: Optional[int] = FieldInfo(alias="startHour", default=None)
    """
    start_hour is the beginning of the update window as a UTC hour (0-23). +required
    """
