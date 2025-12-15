# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AccountListLoginProvidersParams", "Filter", "Pagination"]


class AccountListLoginProvidersParams(TypedDict, total=False):
    token: str

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    filter: Filter
    """filter contains the filter options for listing login methods"""

    pagination: Pagination
    """pagination contains the pagination options for listing login methods"""


class Filter(TypedDict, total=False):
    """filter contains the filter options for listing login methods"""

    email: Optional[str]
    """email is the email address to filter SSO providers by"""

    invite_id: Annotated[Optional[str], PropertyInfo(alias="inviteId")]
    """invite_id is the ID of the invite URL the user wants to login with"""


class Pagination(TypedDict, total=False):
    """pagination contains the pagination options for listing login methods"""

    token: str
    """
    Token for the next set of results that was returned as next_token of a
    PaginationResponse
    """

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
    """Page size is the maximum number of results to retrieve per page. Defaults to 25.

    Maximum 100.
    """
