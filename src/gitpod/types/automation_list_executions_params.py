# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .shared_params.sort import Sort

__all__ = ["AutomationListExecutionsParams", "Filter", "Pagination"]


class AutomationListExecutionsParams(TypedDict, total=False):
    token: str

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    filter: Filter

    pagination: Pagination

    sort: Sort
    """sort specifies the order of results.

    When unspecified, results are sorted by operational priority (running first,
    then failed, then completed, then others). Supported sort fields: startedAt,
    finishedAt, createdAt.
    """


class Filter(TypedDict, total=False):
    has_failed_actions: Annotated[Optional[bool], PropertyInfo(alias="hasFailedActions")]

    search: str
    """
    search performs case-insensitive search across workflow execution ID and trigger
    type
    """

    status_phases: Annotated[
        List[
            Literal[
                "WORKFLOW_EXECUTION_PHASE_UNSPECIFIED",
                "WORKFLOW_EXECUTION_PHASE_PENDING",
                "WORKFLOW_EXECUTION_PHASE_RUNNING",
                "WORKFLOW_EXECUTION_PHASE_STOPPING",
                "WORKFLOW_EXECUTION_PHASE_STOPPED",
                "WORKFLOW_EXECUTION_PHASE_DELETING",
                "WORKFLOW_EXECUTION_PHASE_DELETED",
                "WORKFLOW_EXECUTION_PHASE_COMPLETED",
            ]
        ],
        PropertyInfo(alias="statusPhases"),
    ]

    workflow_execution_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="workflowExecutionIds")]

    workflow_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="workflowIds")]


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
