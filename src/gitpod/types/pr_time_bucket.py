# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PrTimeBucket"]


class PrTimeBucket(BaseModel):
    """PrTimeBucket contains PR speed metrics for a single time period."""

    deploys: Optional[str] = None
    """Total number of deploys (merged PRs) in this bucket."""

    lead_time_seconds: Optional[float] = FieldInfo(alias="leadTimeSeconds", default=None)
    """Median lead time in seconds for PRs merged in this bucket."""

    prs_merged_count: Optional[str] = FieldInfo(alias="prsMergedCount", default=None)
    """Number of PRs merged in this bucket."""

    start_time: Optional[datetime] = FieldInfo(alias="startTime", default=None)
    """Start of this time bucket."""

    time_to_first_approval_seconds: Optional[float] = FieldInfo(alias="timeToFirstApprovalSeconds", default=None)
    """
    Median time to first approval in seconds for PRs in this bucket. Zero when no
    PRs in the bucket had approvals.
    """
