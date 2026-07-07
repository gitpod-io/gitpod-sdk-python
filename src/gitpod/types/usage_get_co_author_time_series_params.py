# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .resolution import Resolution
from .date_range_param import DateRangeParam

__all__ = ["UsageGetCoAuthorTimeSeriesParams"]


class UsageGetCoAuthorTimeSeriesParams(TypedDict, total=False):
    date_range: Required[Annotated[DateRangeParam, PropertyInfo(alias="dateRange")]]
    """Date range to query within."""

    project_id: Annotated[str, PropertyInfo(alias="projectId")]
    """Optional project ID to scope results."""

    resolution: Resolution
    """Time resolution for the series data."""

    team_id: Annotated[str, PropertyInfo(alias="teamId")]
    """
    Optional team ID to scope results to a specific team. Mutually exclusive with
    user_id.
    """

    user_id: Annotated[str, PropertyInfo(alias="userId")]
    """
    Optional user ID to scope results to a specific user. Mutually exclusive with
    team_id.
    """
