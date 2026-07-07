# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["TimeSeriesPoint"]


class TimeSeriesPoint(BaseModel):
    time: Optional[datetime] = None
    """Timestamp for this data point."""

    value: Optional[int] = None
    """The numerical value for this data point."""
