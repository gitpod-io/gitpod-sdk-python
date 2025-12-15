# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AccountListSSOLoginsParams", "Pagination"]


class AccountListSSOLoginsParams(TypedDict, total=False):
    email: Required[str]
    """email is the email the user wants to login with"""

    token: str

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    pagination: Pagination
    """pagination contains the pagination options for listing SSO logins"""

    return_to: Annotated[Optional[str], PropertyInfo(alias="returnTo")]
    """return_to is the URL the user will be redirected to after login"""


class Pagination(TypedDict, total=False):
    """pagination contains the pagination options for listing SSO logins"""

    token: str
    """
    Token for the next set of results that was returned as next_token of a
    PaginationResponse
    """

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
    """Page size is the maximum number of results to retrieve per page. Defaults to 25.

    Maximum 100.
    """
