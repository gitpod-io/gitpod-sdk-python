# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .tool_breakdown import ToolBreakdown

__all__ = ["CoAuthorSummary"]


class CoAuthorSummary(BaseModel):
    """CoAuthorSummary contains aggregate totals for a date range."""

    by_tool: Optional[List[ToolBreakdown]] = FieldInfo(alias="byTool", default=None)
    """Per-tool breakdown of contribution stats."""

    distinct_authors: Optional[str] = FieldInfo(alias="distinctAuthors", default=None)
    """Number of distinct authors (by author_hash)."""

    distinct_authors_trend: Optional[float] = FieldInfo(alias="distinctAuthorsTrend", default=None)
    """Fractional change in distinct_authors compared to the previous period."""

    total_commits: Optional[str] = FieldInfo(alias="totalCommits", default=None)
    """Total number of commits in the date range."""

    total_commits_trend: Optional[float] = FieldInfo(alias="totalCommitsTrend", default=None)
    """
    Fractional change in total_commits compared to the previous period of equal
    length. Computed as (current - previous) / previous. Zero when there is no
    previous data.
    """

    total_lines_added: Optional[str] = FieldInfo(alias="totalLinesAdded", default=None)
    """Total lines added across all commits."""

    total_lines_added_trend: Optional[float] = FieldInfo(alias="totalLinesAddedTrend", default=None)
    """Fractional change in total_lines_added compared to the previous period."""

    total_lines_removed: Optional[str] = FieldInfo(alias="totalLinesRemoved", default=None)
    """Total lines removed across all commits."""

    total_lines_removed_trend: Optional[float] = FieldInfo(alias="totalLinesRemovedTrend", default=None)
    """Fractional change in total_lines_removed compared to the previous period."""
