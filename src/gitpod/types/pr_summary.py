# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PrSummary"]


class PrSummary(BaseModel):
    """PrSummary contains aggregate PR speed metrics for a date range."""

    deployment_frequency: Optional[float] = FieldInfo(alias="deploymentFrequency", default=None)
    """PRs merged to the default branch per week."""

    deployment_frequency_trend: Optional[float] = FieldInfo(alias="deploymentFrequencyTrend", default=None)
    """
    Fractional change in deployment_frequency vs previous period. Computed as
    (current - previous) / previous.
    """

    lead_time_seconds: Optional[float] = FieldInfo(alias="leadTimeSeconds", default=None)
    """Median lead time for changes in seconds (first commit → merge)."""

    lead_time_trend: Optional[float] = FieldInfo(alias="leadTimeTrend", default=None)
    """
    Fractional change in lead_time_seconds vs previous period. Computed as
    (current - previous) / previous.
    """

    prs_merged_count: Optional[str] = FieldInfo(alias="prsMergedCount", default=None)
    """Total PRs merged in the date range."""

    prs_merged_trend: Optional[float] = FieldInfo(alias="prsMergedTrend", default=None)
    """
    Fractional change in prs_merged_count vs previous period. Computed as (current -
    previous) / previous.
    """

    time_to_first_approval_seconds: Optional[float] = FieldInfo(alias="timeToFirstApprovalSeconds", default=None)
    """
    Median time to first approval in seconds. Zero when no PRs in the range had
    approvals.
    """

    time_to_first_approval_trend: Optional[float] = FieldInfo(alias="timeToFirstApprovalTrend", default=None)
    """
    Fractional change in time_to_first_approval_seconds vs previous period. Computed
    as (current - previous) / previous.
    """
