# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .date_range_param import DateRangeParam

__all__ = ["UsageGetAdoptionUsageSummaryParams"]


class UsageGetAdoptionUsageSummaryParams(TypedDict, total=False):
    date_range: Required[Annotated[DateRangeParam, PropertyInfo(alias="dateRange")]]
    """Date range to query metrics within."""

    project_id: Annotated[str, PropertyInfo(alias="projectId")]
    """Optional project ID to filter metrics by."""

    team_id: Annotated[str, PropertyInfo(alias="teamId")]
    """Optional team ID to scope results to members of a specific team."""

    user_id: Annotated[str, PropertyInfo(alias="userId")]
    """
    Optional user ID to filter metrics for a specific user (personal insights view).
    """
