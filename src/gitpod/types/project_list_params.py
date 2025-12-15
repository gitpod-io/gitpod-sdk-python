# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ProjectListParams", "Filter", "Pagination"]


class ProjectListParams(TypedDict, total=False):
    token: str

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    filter: Filter

    pagination: Pagination
    """pagination contains the pagination options for listing organizations"""


class Filter(TypedDict, total=False):
    project_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="projectIds")]
    """project_ids filters the response to only projects with these IDs"""

    runner_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="runnerIds")]
    """
    runner_ids filters the response to only projects that use environment classes
    from these runners
    """

    search: str
    """
    search performs case-insensitive search across project name, project ID, and
    repository name
    """


class Pagination(TypedDict, total=False):
    """pagination contains the pagination options for listing organizations"""

    token: str
    """
    Token for the next set of results that was returned as next_token of a
    PaginationResponse
    """

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
    """Page size is the maximum number of results to retrieve per page. Defaults to 25.

    Maximum 100.
    """
