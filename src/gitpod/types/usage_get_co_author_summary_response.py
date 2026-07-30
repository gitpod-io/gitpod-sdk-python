# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .co_author_summary import CoAuthorSummary
from .time_series_point import TimeSeriesPoint

__all__ = ["UsageGetCoAuthorSummaryResponse"]


class UsageGetCoAuthorSummaryResponse(BaseModel):
    sparkline: Optional[List[TimeSeriesPoint]] = None
    """Sparkline data for card rendering."""

    summary: Optional[CoAuthorSummary] = None
    """Summary totals and trends for the requested date range."""
