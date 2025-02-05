# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from ...._utils import PropertyInfo

__all__ = ["HostAuthenticationTokenListParams", "Filter", "FilterRunnerID", "FilterUserID", "Pagination"]


class HostAuthenticationTokenListParams(TypedDict, total=False):
    token: str

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    filter: Filter

    pagination: Pagination


class FilterRunnerID(TypedDict, total=False):
    runner_id: Required[Annotated[str, PropertyInfo(alias="runnerId")]]


class FilterUserID(TypedDict, total=False):
    user_id: Required[Annotated[str, PropertyInfo(alias="userId")]]


Filter: TypeAlias = Union[FilterRunnerID, FilterUserID]


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
