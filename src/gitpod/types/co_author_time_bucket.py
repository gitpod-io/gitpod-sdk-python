# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .tool_breakdown import ToolBreakdown

__all__ = ["CoAuthorTimeBucket"]


class CoAuthorTimeBucket(BaseModel):
    """CoAuthorTimeBucket contains stats for a single time period."""

    ai_ratio: Optional[float] = FieldInfo(alias="aiRatio", default=None)
    """Ratio of AI-assisted lines added to total lines added (0.0–1.0)."""

    by_tool: Optional[List[ToolBreakdown]] = FieldInfo(alias="byTool", default=None)
    """Per-tool breakdown for this bucket."""

    distinct_authors: Optional[str] = FieldInfo(alias="distinctAuthors", default=None)
    """Number of distinct authors (by author_hash) in this bucket."""

    start_time: Optional[datetime] = FieldInfo(alias="startTime", default=None)
    """Start of this time bucket."""

    total_commits: Optional[str] = FieldInfo(alias="totalCommits", default=None)
    """Total number of commits in this bucket (across all tools)."""

    total_lines_added: Optional[str] = FieldInfo(alias="totalLinesAdded", default=None)
    """Total lines added in this bucket (across all tools)."""

    total_lines_removed: Optional[str] = FieldInfo(alias="totalLinesRemoved", default=None)
    """Total lines removed in this bucket (across all tools)."""
