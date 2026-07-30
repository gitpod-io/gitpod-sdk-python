# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .co_author_tool import CoAuthorTool

__all__ = ["ToolBreakdown"]


class ToolBreakdown(BaseModel):
    """ToolBreakdown contains stats for a single AI tool (or human)."""

    commits: Optional[str] = None
    """Number of commits attributed to this tool."""

    distinct_authors: Optional[str] = FieldInfo(alias="distinctAuthors", default=None)
    """Distinct authors who used this tool."""

    lines_added: Optional[str] = FieldInfo(alias="linesAdded", default=None)
    """Lines added by this tool."""

    lines_removed: Optional[str] = FieldInfo(alias="linesRemoved", default=None)
    """Lines removed by this tool."""

    tool: Optional[CoAuthorTool] = None
    """The tool these stats are for."""
