# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["UsageListEnvironmentRuntimeRecordsParams", "Filter", "FilterDateRange", "Pagination"]


class UsageListEnvironmentRuntimeRecordsParams(TypedDict, total=False):
    token: str

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    filter: Filter
    """Filter options."""

    pagination: Pagination
    """Pagination options."""


class FilterDateRange(TypedDict, total=False):
    """Date range to query runtime records within."""

    end_time: Required[Annotated[Union[str, datetime], PropertyInfo(alias="endTime", format="iso8601")]]
    """End time of the date range (exclusive)."""

    start_time: Required[Annotated[Union[str, datetime], PropertyInfo(alias="startTime", format="iso8601")]]
    """Start time of the date range (inclusive)."""


class Filter(TypedDict, total=False):
    """Filter options."""

    date_range: Required[Annotated[FilterDateRange, PropertyInfo(alias="dateRange")]]
    """Date range to query runtime records within."""

    project_id: Annotated[str, PropertyInfo(alias="projectId")]
    """Optional project ID to filter runtime records by."""


class Pagination(TypedDict, total=False):
    """Pagination options."""

    token: str
    """
    Token for the next set of results that was returned as next_token of a
    PaginationResponse
    """

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
    """Page size is the maximum number of results to retrieve per page. Defaults to 25.

    Maximum 100.
    """
