# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .agent_trace_time_bucket import AgentTraceTimeBucket

__all__ = ["UsageGetAgentTraceTimeSeriesResponse"]


class UsageGetAgentTraceTimeSeriesResponse(BaseModel):
    time_series: Optional[List[AgentTraceTimeBucket]] = FieldInfo(alias="timeSeries", default=None)
    """Time series of agent trace stats, bucketed by the requested resolution."""
