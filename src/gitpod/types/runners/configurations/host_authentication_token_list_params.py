# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["HostAuthenticationTokenListParams", "Filter", "Pagination"]


class HostAuthenticationTokenListParams(TypedDict, total=False):
    token: str

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    filter: Filter

    pagination: Pagination


class Filter(TypedDict, total=False):
    runner_id: Annotated[Optional[str], PropertyInfo(alias="runnerId")]

    subject_id: Annotated[Optional[str], PropertyInfo(alias="subjectId")]
    """Filter by subject (user or service account)"""

    user_id: Annotated[Optional[str], PropertyInfo(alias="userId")]
    """Deprecated: Use principal_id instead"""


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
