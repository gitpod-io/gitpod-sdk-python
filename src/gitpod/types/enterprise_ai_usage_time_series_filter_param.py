# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .shared_params.subject import Subject

__all__ = ["EnterpriseAIUsageTimeSeriesFilterParam"]


class EnterpriseAIUsageTimeSeriesFilterParam(TypedDict, total=False):
    subject: Optional[Subject]
    """Restrict the per-user breakdown to a single subject."""
