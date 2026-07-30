# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DateRange"]


class DateRange(BaseModel):
    """DateRange specifies a time period for queries."""

    end_time: datetime = FieldInfo(alias="endTime")
    """End time of the date range (exclusive)."""

    start_time: datetime = FieldInfo(alias="startTime")
    """Start time of the date range (inclusive)."""
