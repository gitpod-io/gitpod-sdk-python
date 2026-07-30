# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .time_series_point import TimeSeriesPoint

__all__ = ["UsageGetAdoptionUsageSummaryResponse"]


class UsageGetAdoptionUsageSummaryResponse(BaseModel):
    active_users_count: Optional[str] = FieldInfo(alias="activeUsersCount", default=None)
    """Count of active users in the date range."""

    active_users_trend: Optional[float] = FieldInfo(alias="activeUsersTrend", default=None)
    """
    Fractional change in active_users_count vs previous period. Computed as
    (current - previous) / previous.
    """

    env_runtime_per_user_seconds: Optional[float] = FieldInfo(alias="envRuntimePerUserSeconds", default=None)
    """Average environment runtime in seconds per active user."""

    env_runtime_per_user_trend: Optional[float] = FieldInfo(alias="envRuntimePerUserTrend", default=None)
    """
    Fractional change in env_runtime_per_user_seconds vs previous period. Computed
    as (current - previous) / previous.
    """

    power_users_count: Optional[str] = FieldInfo(alias="powerUsersCount", default=None)
    """Count of power users in the date range."""

    power_users_threshold_seconds: Optional[str] = FieldInfo(alias="powerUsersThresholdSeconds", default=None)
    """
    Threshold in seconds used to determine power users. Displayed to users so they
    understand the definition.
    """

    power_users_trend: Optional[float] = FieldInfo(alias="powerUsersTrend", default=None)
    """
    Fractional change in power_users_count vs previous period. Computed as
    (current - previous) / previous.
    """

    sessions_count: Optional[str] = FieldInfo(alias="sessionsCount", default=None)
    """Count of environment sessions (total starts) in the date range."""

    sessions_trend: Optional[float] = FieldInfo(alias="sessionsTrend", default=None)
    """
    Fractional change in sessions_count vs previous period. Computed as (current -
    previous) / previous.
    """

    sparkline: Optional[List[TimeSeriesPoint]] = None
    """Sparkline data for the card's trend line (typically ~4 weekly points)."""
