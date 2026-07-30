# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .agent_trace_model_breakdown import AgentTraceModelBreakdown

__all__ = ["AgentTraceSummary"]


class AgentTraceSummary(BaseModel):
    """AgentTraceSummary contains aggregate totals for a date range."""

    by_model: Optional[List[AgentTraceModelBreakdown]] = FieldInfo(alias="byModel", default=None)
    """Per-model breakdown of session stats."""

    total_lines_added: Optional[str] = FieldInfo(alias="totalLinesAdded", default=None)
    """Total lines added across all sessions."""

    total_lines_added_trend: Optional[float] = FieldInfo(alias="totalLinesAddedTrend", default=None)
    """Fractional change in total_lines_added compared to the previous period."""

    total_lines_removed: Optional[str] = FieldInfo(alias="totalLinesRemoved", default=None)
    """Total lines removed across all sessions."""

    total_lines_removed_trend: Optional[float] = FieldInfo(alias="totalLinesRemovedTrend", default=None)
    """Fractional change in total_lines_removed compared to the previous period."""

    total_sessions: Optional[str] = FieldInfo(alias="totalSessions", default=None)
    """Total number of agent trace sessions in the date range."""

    total_sessions_trend: Optional[float] = FieldInfo(alias="totalSessionsTrend", default=None)
    """
    Fractional change in total_sessions compared to the previous period of equal
    length. Computed as (current - previous) / previous. Zero when there is no
    previous data.
    """
