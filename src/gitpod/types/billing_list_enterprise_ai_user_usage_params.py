# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared.sort_order import SortOrder
from .shared_params.subject import Subject
from .shared_params.date_range import DateRange

__all__ = ["BillingListEnterpriseAIUserUsageParams", "Filter", "Pagination", "Sort"]


class BillingListEnterpriseAIUserUsageParams(TypedDict, total=False):
    date_range: Required[Annotated[DateRange, PropertyInfo(alias="dateRange")]]
    """Date range for the user usage list.

    Both start and end dates are inclusive. Time-of-day is ignored; dates are
    truncated to midnight in the specified timezone.
    """

    organization_id: Required[Annotated[str, PropertyInfo(alias="organizationId")]]

    token: str

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    filter: Filter
    """Optional filter narrowing the returned user usage.

    When set to a subject, the response contains only usage for that user or service
    account.
    """

    pagination: Pagination

    sort: Sort
    """sort controls the ordering of results. Defaults to total spend descending."""

    timezone: str
    """IANA timezone name used to bucket usage. When empty, defaults to "UTC"."""


class Filter(TypedDict, total=False):
    """Optional filter narrowing the returned user usage.

    When set to a subject,
     the response contains only usage for that user or service account.
    """

    subject: Optional[Subject]
    """Restrict the user usage list to a single subject.

    The subject must be PRINCIPAL_USER or PRINCIPAL_SERVICE_ACCOUNT and belong to
    the request's organization.
    """


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
    """sort controls the ordering of results. Defaults to total spend descending."""

    field: Literal[
        "SORT_FIELD_UNSPECIFIED",
        "SORT_FIELD_USAGE",
        "SORT_FIELD_DISPLAY_NAME",
        "SORT_FIELD_BUDGET",
        "SORT_FIELD_BUDGET_USED",
    ]

    order: SortOrder
