# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared.sort_order import SortOrder

__all__ = ["BillingListEnterpriseUserCreditUsageParams", "Pagination", "Sort"]


class BillingListEnterpriseUserCreditUsageParams(TypedDict, total=False):
    organization_id: Required[Annotated[str, PropertyInfo(alias="organizationId")]]
    """organization_id is the ID of the organization to list user credit usage for."""

    token: str

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    as_of: Annotated[Union[str, datetime, None], PropertyInfo(alias="asOf", format="iso8601")]
    """
    as_of is the point in time to compute month-to-date usage up to. Defaults to now
    if not set.
    """

    pagination: Pagination

    sort: Sort
    """sort controls the ordering of results. Defaults to total credits descending."""


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


class Sort(TypedDict, total=False):
    """sort controls the ordering of results. Defaults to total credits descending."""

    field: Literal[
        "SORT_FIELD_UNSPECIFIED",
        "SORT_FIELD_USAGE",
        "SORT_FIELD_DISPLAY_NAME",
        "SORT_FIELD_BUDGET",
        "SORT_FIELD_BUDGET_USED",
    ]

    order: SortOrder
