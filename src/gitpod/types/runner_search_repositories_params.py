# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .search_mode import SearchMode

__all__ = ["RunnerSearchRepositoriesParams", "Pagination"]


class RunnerSearchRepositoriesParams(TypedDict, total=False):
    limit: int
    """
    Maximum number of repositories to return. Default: 25, Maximum: 100 Deprecated:
    Use pagination.page_size instead
    """

    pagination: Pagination
    """Pagination parameters for repository search"""

    runner_id: Annotated[str, PropertyInfo(alias="runnerId")]

    scm_host: Annotated[str, PropertyInfo(alias="scmHost")]
    """The SCM's host to retrieve repositories from"""

    search_mode: Annotated[SearchMode, PropertyInfo(alias="searchMode")]
    """Search mode determines how search_string is interpreted"""

    search_string: Annotated[str, PropertyInfo(alias="searchString")]
    """Search query - interpretation depends on search_mode"""


class Pagination(TypedDict, total=False):
    """Pagination parameters for repository search"""

    token: str
    """
    Token for the next set of results that was returned as next_token of a
    PaginationResponse
    """

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
    """Page size is the maximum number of results to retrieve per page. Defaults to 25.

    Maximum 100.
    """
