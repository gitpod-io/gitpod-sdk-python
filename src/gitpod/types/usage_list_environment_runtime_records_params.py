# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .date_range_param import DateRangeParam

__all__ = ["UsageListEnvironmentRuntimeRecordsParams", "Filter", "Pagination"]


class UsageListEnvironmentRuntimeRecordsParams(TypedDict, total=False):
    token: str

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    filter: Filter
    """Filter options."""

    pagination: Pagination
    """Pagination options."""


class Filter(TypedDict, total=False):
    """Filter options."""

    date_range: Required[Annotated[DateRangeParam, PropertyInfo(alias="dateRange")]]
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
