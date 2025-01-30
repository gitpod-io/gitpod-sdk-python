# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EnvironmentClassListParams", "Filter", "Pagination"]


class EnvironmentClassListParams(TypedDict, total=False):
    filter: Filter

    pagination: Pagination
    """pagination contains the pagination options for listing environment classes"""


class Filter(TypedDict, total=False):
    enabled: Required[bool]
    """enabled filters the response to only enabled or disabled environment classes.

    If not set, all environment classes are returned.
    """


class Pagination(TypedDict, total=False):
    token: str
    """Token for the next set of results that was returned as next_token of a

    PaginationResponse
    """

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
    """Page size is the maximum number of results to retrieve per page. Defaults to 25.

    Maximum 100.
    """
