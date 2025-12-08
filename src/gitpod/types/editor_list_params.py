# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EditorListParams", "Filter", "Pagination"]


class EditorListParams(TypedDict, total=False):
    token: str

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    filter: Filter
    """filter contains the filter options for listing editors"""

    pagination: Pagination
    """pagination contains the pagination options for listing environments"""


class Filter(TypedDict, total=False):
    """filter contains the filter options for listing editors"""

    allowed_by_policy: Annotated[bool, PropertyInfo(alias="allowedByPolicy")]
    """
    allowed_by_policy filters the response to only editors that are allowed by the
    policies enforced in the organization
    """


class Pagination(TypedDict, total=False):
    """pagination contains the pagination options for listing environments"""

    token: str
    """
    Token for the next set of results that was returned as next_token of a
    PaginationResponse
    """

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
    """Page size is the maximum number of results to retrieve per page. Defaults to 25.

    Maximum 100.
    """
