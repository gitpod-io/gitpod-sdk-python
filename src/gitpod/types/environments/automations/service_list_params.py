# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ServiceListParams", "Filter", "Pagination"]


class ServiceListParams(TypedDict, total=False):
    token: str

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    filter: Filter
    """filter contains the filter options for listing services"""

    pagination: Pagination
    """pagination contains the pagination options for listing services"""


class Filter(TypedDict, total=False):
    environment_ids: Annotated[List[str], PropertyInfo(alias="environmentIds")]
    """environment_ids filters the response to only services of these environments"""

    references: List[str]
    """references filters the response to only services with these references"""

    service_ids: Annotated[List[str], PropertyInfo(alias="serviceIds")]
    """service_ids filters the response to only services with these IDs"""


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
