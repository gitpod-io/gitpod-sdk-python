# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["ExecutionListParams", "Filter", "Pagination"]


class ExecutionListParams(TypedDict, total=False):
    token: str

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    filter: Filter
    """filter contains the filter options for listing task runs"""

    pagination: Pagination
    """pagination contains the pagination options for listing task runs"""


class Filter(TypedDict, total=False):
    environment_ids: Annotated[List[str], PropertyInfo(alias="environmentIds")]
    """environment_ids filters the response to only task runs of these environments"""

    phases: List[
        Literal[
            "TASK_EXECUTION_PHASE_UNSPECIFIED",
            "TASK_EXECUTION_PHASE_PENDING",
            "TASK_EXECUTION_PHASE_RUNNING",
            "TASK_EXECUTION_PHASE_SUCCEEDED",
            "TASK_EXECUTION_PHASE_FAILED",
            "TASK_EXECUTION_PHASE_STOPPED",
        ]
    ]
    """phases filters the response to only task runs in these phases"""

    task_ids: Annotated[List[str], PropertyInfo(alias="taskIds")]
    """task_ids filters the response to only task runs of these tasks"""

    task_references: Annotated[List[str], PropertyInfo(alias="taskReferences")]
    """task_references filters the response to only task runs with this reference"""


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
