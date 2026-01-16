# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared.user_status import UserStatus
from .shared.organization_role import OrganizationRole

__all__ = ["OrganizationListMembersParams", "Filter", "Pagination", "Sort"]


class OrganizationListMembersParams(TypedDict, total=False):
    organization_id: Required[Annotated[str, PropertyInfo(alias="organizationId")]]
    """organization_id is the ID of the organization to list members for"""

    token: str

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    filter: Filter

    pagination: Pagination
    """pagination contains the pagination options for listing members"""

    sort: Sort
    """sort specifies the order of results.

    When unspecified, the authenticated user is returned first, followed by other
    members sorted by name ascending. When an explicit sort is specified, results
    are sorted purely by the requested field without any special handling for the
    authenticated user.
    """


class Filter(TypedDict, total=False):
    roles: List[OrganizationRole]
    """roles filters members by their organization role"""

    search: str
    """search performs case-insensitive search across member name and email"""

    statuses: List[UserStatus]
    """status filters members by their user status"""


class Pagination(TypedDict, total=False):
    """pagination contains the pagination options for listing members"""

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
    """sort specifies the order of results.

    When unspecified, the authenticated user is
     returned first, followed by other members sorted by name ascending. When an explicit
     sort is specified, results are sorted purely by the requested field without any
     special handling for the authenticated user.
    """

    field: Literal["SORT_FIELD_UNSPECIFIED", "SORT_FIELD_NAME", "SORT_FIELD_DATE_JOINED"]

    order: Literal["SORT_ORDER_UNSPECIFIED", "SORT_ORDER_ASC", "SORT_ORDER_DESC"]
