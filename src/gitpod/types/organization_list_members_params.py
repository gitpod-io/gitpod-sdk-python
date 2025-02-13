# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OrganizationListMembersParams", "Pagination"]


class OrganizationListMembersParams(TypedDict, total=False):
    organization_id: Required[Annotated[str, PropertyInfo(alias="organizationId")]]
    """organization_id is the ID of the organization to list members for"""

    token: str

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    pagination: Pagination
    """pagination contains the pagination options for listing members"""


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
