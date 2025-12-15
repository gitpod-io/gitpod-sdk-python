# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["AgentListExecutionsParams", "Filter", "Pagination"]


class AgentListExecutionsParams(TypedDict, total=False):
    token: str

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    filter: Filter

    pagination: Pagination


class Filter(TypedDict, total=False):
    agent_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="agentIds")]

    creator_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="creatorIds")]

    environment_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="environmentIds")]

    project_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="projectIds")]

    roles: List[
        Literal["AGENT_EXECUTION_ROLE_UNSPECIFIED", "AGENT_EXECUTION_ROLE_DEFAULT", "AGENT_EXECUTION_ROLE_WORKFLOW"]
    ]

    status_phases: Annotated[
        List[
            Literal["PHASE_UNSPECIFIED", "PHASE_PENDING", "PHASE_RUNNING", "PHASE_WAITING_FOR_INPUT", "PHASE_STOPPED"]
        ],
        PropertyInfo(alias="statusPhases"),
    ]


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
