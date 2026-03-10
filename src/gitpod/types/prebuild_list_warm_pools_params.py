# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["PrebuildListWarmPoolsParams", "Filter", "Pagination"]


class PrebuildListWarmPoolsParams(TypedDict, total=False):
    token: str

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    filter: Filter
    """filter contains the filter options for listing warm pools"""

    pagination: Pagination
    """pagination contains the pagination options for listing warm pools"""


class Filter(TypedDict, total=False):
    """filter contains the filter options for listing warm pools"""

    environment_class_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="environmentClassIds")]
    """environment_class_ids filters warm pools to specific environment classes"""

    project_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="projectIds")]
    """project_ids filters warm pools to specific projects"""


class Pagination(TypedDict, total=False):
    """pagination contains the pagination options for listing warm pools"""

    token: str
    """
    Token for the next set of results that was returned as next_token of a
    PaginationResponse
    """

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
    """Page size is the maximum number of results to retrieve per page. Defaults to 25.

    Maximum 100.
    """
