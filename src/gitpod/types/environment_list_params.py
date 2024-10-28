# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EnvironmentListParams", "Filter", "Pagination"]


class EnvironmentListParams(TypedDict, total=False):
    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    filter: Filter

    organization_id: Annotated[str, PropertyInfo(alias="organizationId")]
    """organization_id is the ID of the organization that contains the environments"""

    pagination: Pagination
    """pagination contains the pagination options for listing environments"""

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""


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

    status_phases: Annotated[
        List[
            Literal[
                "ENVIRONMENT_PHASE_UNSPECIFIED",
                "ENVIRONMENT_PHASE_CREATING",
                "ENVIRONMENT_PHASE_STARTING",
                "ENVIRONMENT_PHASE_RUNNING",
                "ENVIRONMENT_PHASE_UPDATING",
                "ENVIRONMENT_PHASE_STOPPING",
                "ENVIRONMENT_PHASE_STOPPED",
                "ENVIRONMENT_PHASE_DELETING",
                "ENVIRONMENT_PHASE_DELETED",
            ]
        ],
        PropertyInfo(alias="statusPhases"),
    ]
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
