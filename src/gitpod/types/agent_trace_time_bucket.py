# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .agent_trace_model_breakdown import AgentTraceModelBreakdown

__all__ = ["AgentTraceTimeBucket"]


class AgentTraceTimeBucket(BaseModel):
    """AgentTraceTimeBucket contains stats for a single time period."""

    by_model: Optional[List[AgentTraceModelBreakdown]] = FieldInfo(alias="byModel", default=None)
    """Per-model breakdown for this bucket."""

    start_time: Optional[datetime] = FieldInfo(alias="startTime", default=None)
    """Start of this time bucket."""

    total_lines_added: Optional[str] = FieldInfo(alias="totalLinesAdded", default=None)
    """Total lines added in this bucket."""

    total_lines_removed: Optional[str] = FieldInfo(alias="totalLinesRemoved", default=None)
    """Total lines removed in this bucket."""

    total_sessions: Optional[str] = FieldInfo(alias="totalSessions", default=None)
    """Number of agent trace sessions in this bucket."""
