# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["GroupListParams", "Filter", "Pagination"]


class GroupListParams(TypedDict, total=False):
    token: str

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    filter: Filter
    """filter contains options for filtering the list of groups."""

    pagination: Pagination
    """pagination contains the pagination options for listing groups"""


class Filter(TypedDict, total=False):
    """filter contains options for filtering the list of groups."""

    direct_share: Annotated[Optional[bool], PropertyInfo(alias="directShare")]
    """
    direct_share filters groups by their direct_share flag. When set, only groups
    matching this value are returned.
    """

    group_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="groupIds")]
    """group_ids filters the response to only groups with the specified IDs"""

    search: str
    """search performs case-insensitive search across group name, description, and ID"""

    system_managed: Annotated[Optional[bool], PropertyInfo(alias="systemManaged")]
    """
    system_managed filters groups by their system_managed flag. When set, only
    groups matching this value are returned.
    """


class Pagination(TypedDict, total=False):
    """pagination contains the pagination options for listing groups"""

    token: str
    """
    Token for the next set of results that was returned as next_token of a
    PaginationResponse
    """

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
    """Page size is the maximum number of results to retrieve per page. Defaults to 25.

    Maximum 100.
    """
