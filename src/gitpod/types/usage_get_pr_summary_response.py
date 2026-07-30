# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .pr_summary import PrSummary
from .time_series_point import TimeSeriesPoint

__all__ = ["UsageGetPrSummaryResponse"]


class UsageGetPrSummaryResponse(BaseModel):
    sparkline: Optional[List[TimeSeriesPoint]] = None
    """Sparkline data for card rendering."""

    summary: Optional[PrSummary] = None
    """Summary totals and trends for the requested date range."""
