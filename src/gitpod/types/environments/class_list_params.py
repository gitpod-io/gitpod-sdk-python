# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from ..runner_kind import RunnerKind
from ..runner_provider import RunnerProvider

__all__ = ["ClassListParams", "Filter", "Pagination"]


class ClassListParams(TypedDict, total=False):
    token: str

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    filter: Filter

    pagination: Pagination
    """pagination contains the pagination options for listing environment classes"""


class Filter(TypedDict, total=False):
    can_create_environments: Annotated[Optional[bool], PropertyInfo(alias="canCreateEnvironments")]
    """
    can_create_environments filters the response to only environment classes that
    can be used to create new environments by the caller. Unlike enabled, which
    indicates general availability, this ensures the caller only sees environment
    classes they are allowed to use.
    """

    enabled: Optional[bool]
    """
    enabled filters the response to only enabled or disabled environment classes. If
    not set, all environment classes are returned.
    """

    runner_ids: Annotated[List[str], PropertyInfo(alias="runnerIds")]
    """runner_ids filters the response to only EnvironmentClasses of these Runner IDs"""

    runner_kinds: Annotated[List[RunnerKind], PropertyInfo(alias="runnerKinds")]
    """
    runner_kind filters the response to only environment classes from runners of
    these kinds.
    """

    runner_providers: Annotated[List[RunnerProvider], PropertyInfo(alias="runnerProviders")]
    """
    runner_providers filters the response to only environment classes from runners
    of these providers.
    """


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
