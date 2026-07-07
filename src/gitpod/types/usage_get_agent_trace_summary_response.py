# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .time_series_point import TimeSeriesPoint
from .agent_trace_summary import AgentTraceSummary

__all__ = ["UsageGetAgentTraceSummaryResponse"]


class UsageGetAgentTraceSummaryResponse(BaseModel):
    sparkline: Optional[List[TimeSeriesPoint]] = None
    """Sparkline data for card rendering."""

    summary: Optional[AgentTraceSummary] = None
    """Summary totals and trends for the requested date range."""
