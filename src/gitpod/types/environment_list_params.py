# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .runner_kind import RunnerKind
from .environment_phase import EnvironmentPhase

__all__ = ["EnvironmentListParams", "Filter", "Pagination"]


class EnvironmentListParams(TypedDict, total=False):
    token: str

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    filter: Filter

    pagination: Pagination
    """pagination contains the pagination options for listing environments"""


class Filter(TypedDict, total=False):
    creator_ids: Annotated[List[str], PropertyInfo(alias="creatorIds")]
    """
    creator_ids filters the response to only Environments created by specified
    members
    """

    project_ids: Annotated[List[str], PropertyInfo(alias="projectIds")]
    """
    project_ids filters the response to only Environments associated with the
    specified projects
    """

    runner_ids: Annotated[List[str], PropertyInfo(alias="runnerIds")]
    """
    runner_ids filters the response to only Environments running on these Runner IDs
    """

    runner_kinds: Annotated[List[RunnerKind], PropertyInfo(alias="runnerKinds")]
    """
    runner_kinds filters the response to only Environments running on these Runner
    Kinds
    """

    status_phases: Annotated[List[EnvironmentPhase], PropertyInfo(alias="statusPhases")]
    """
    actual_phases is a list of phases the environment must be in for it to be
    returned in the API call
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
