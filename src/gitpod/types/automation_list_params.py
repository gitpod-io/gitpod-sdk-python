# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .shared.sort_order import SortOrder

__all__ = ["AutomationListParams", "Filter", "Pagination", "Sort"]


class AutomationListParams(TypedDict, total=False):
    token: str

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    filter: Filter

    pagination: Pagination

    sort: Sort
    """sort specifies the order of results.

    When unspecified, results are sorted alphabetically by name ascending.
    """


class Filter(TypedDict, total=False):
    creator_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="creatorIds")]
    """creator_ids filters workflows by creator user IDs"""

    has_failed_execution_since: Annotated[
        Union[str, datetime], PropertyInfo(alias="hasFailedExecutionSince", format="iso8601")
    ]
    """
    has_failed_execution_since filters workflows that have at least one failed
    execution with create_time >= the specified timestamp. A failed execution is one
    that is COMPLETED with failed_action_count > 0, or STOPPED with
    failed_action_count > 0 or a non-empty failure_message. This filter is mutually
    exclusive with status_phases.
    """

    search: str
    """
    search performs case-insensitive search across workflow name, description, and
    ID
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
    """
    status_phases filters workflows by the phase of their latest execution. Only
    workflows whose most recent execution matches one of the specified phases are
    returned.
    """

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


class Sort(TypedDict, total=False):
    """sort specifies the order of results.

    When unspecified, results are sorted
     alphabetically by name ascending.
    """

    field: Literal["SORT_FIELD_UNSPECIFIED", "SORT_FIELD_NAME", "SORT_FIELD_RECENTLY_COMPLETED"]

    order: SortOrder
