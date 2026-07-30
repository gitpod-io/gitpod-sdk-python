# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .shared_params.date_range import DateRange

__all__ = ["BillingListEnterpriseAITeamUsageParams", "Filter", "Pagination"]


class BillingListEnterpriseAITeamUsageParams(TypedDict, total=False):
    date_range: Required[Annotated[DateRange, PropertyInfo(alias="dateRange")]]
    """Date range for the team usage list.

    Both start and end dates are inclusive. Time-of-day is ignored; dates are
    truncated to midnight in the specified timezone.
    """

    organization_id: Required[Annotated[str, PropertyInfo(alias="organizationId")]]

    token: str

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    filter: Filter

    pagination: Pagination

    timezone: str
    """IANA timezone name used to bucket usage. When empty, defaults to "UTC"."""


class Filter(TypedDict, total=False):
    team_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="teamIds")]


class Pagination(TypedDict, total=False):
    token: str
    """
    Token for the next set of results that was returned as next_token of a
    PaginationResponse
    """

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
    """Page size is the maximum number of results to retrieve per page. Defaults to 25.

    Maximum 100.
    """
