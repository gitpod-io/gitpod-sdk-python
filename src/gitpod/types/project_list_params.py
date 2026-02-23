# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .sort_param import SortParam
from .runner_kind import RunnerKind

__all__ = ["ProjectListParams", "Filter", "Pagination"]


class ProjectListParams(TypedDict, total=False):
    token: str

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    filter: Filter

    pagination: Pagination
    """pagination contains the pagination options for listing organizations"""

    sort: SortParam
    """sort specifies the order of results. Defaults to popularity descending.

    Supported fields:

    - "id": Sort by project ID (UUID v7, effectively creation order). Produces a
      stable, deterministic result set suitable for consistent pagination.
    - "popularity": Sort by popularity — a precomputed score based on recent
      environment creation activity. Updated periodically by a background job.
    """


class Filter(TypedDict, total=False):
    project_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="projectIds")]
    """project_ids filters the response to only projects with these IDs"""

    runner_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="runnerIds")]
    """
    runner_ids filters the response to only projects that use environment classes
    from these runners
    """

    runner_kinds: Annotated[List[RunnerKind], PropertyInfo(alias="runnerKinds")]
    """
    runner_kinds filters the response to only projects that use environment classes
    from runners of these kinds
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
