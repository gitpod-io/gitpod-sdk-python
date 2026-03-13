# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["AutomationListExecutionActionsParams", "Filter", "Pagination"]


class AutomationListExecutionActionsParams(TypedDict, total=False):
    token: str

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    filter: Filter

    pagination: Pagination


class Filter(TypedDict, total=False):
    phases: List[
        Literal[
            "WORKFLOW_EXECUTION_ACTION_PHASE_UNSPECIFIED",
            "WORKFLOW_EXECUTION_ACTION_PHASE_PENDING",
            "WORKFLOW_EXECUTION_ACTION_PHASE_RUNNING",
            "WORKFLOW_EXECUTION_ACTION_PHASE_STOPPING",
            "WORKFLOW_EXECUTION_ACTION_PHASE_STOPPED",
            "WORKFLOW_EXECUTION_ACTION_PHASE_DELETING",
            "WORKFLOW_EXECUTION_ACTION_PHASE_DELETED",
            "WORKFLOW_EXECUTION_ACTION_PHASE_DONE",
        ]
    ]

    workflow_execution_action_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="workflowExecutionActionIds")]

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
