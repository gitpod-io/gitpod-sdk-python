# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .supported_model import SupportedModel

__all__ = ["AgentTraceModelBreakdown"]


class AgentTraceModelBreakdown(BaseModel):
    """AgentTraceModelBreakdown contains stats for a single LLM model."""

    lines_added: Optional[str] = FieldInfo(alias="linesAdded", default=None)
    """Lines added by sessions using this model."""

    lines_removed: Optional[str] = FieldInfo(alias="linesRemoved", default=None)
    """Lines removed by sessions using this model."""

    model: Optional[SupportedModel] = None
    """The model these stats are for."""

    sessions: Optional[str] = None
    """Number of sessions that used this model."""
