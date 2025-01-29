# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RunnerListParams", "Filter", "Pagination"]


class RunnerListParams(TypedDict, total=False):
    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    filter: Filter

    pagination: Pagination
    """pagination contains the pagination options for listing runners"""

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""


class Filter(TypedDict, total=False):
    creator_ids: Annotated[List[str], PropertyInfo(alias="creatorIds")]
    """creator_ids filters the response to only runner created by specified users"""

    kinds: List[
        Literal["RUNNER_KIND_UNSPECIFIED", "RUNNER_KIND_LOCAL", "RUNNER_KIND_REMOTE", "RUNNER_KIND_LOCAL_CONFIGURATION"]
    ]
    """kinds filters the response to only runners of the specified kinds"""


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
