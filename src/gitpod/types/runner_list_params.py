# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RunnerListParams", "Filter", "Pagination"]


class RunnerListParams(TypedDict, total=False):
    token: str

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    filter: Filter

    pagination: Pagination
    """pagination contains the pagination options for listing runners"""


class Filter(TypedDict, total=False):
    creator_ids: Annotated[List[str], PropertyInfo(alias="creatorIds")]
    """creator_ids filters the response to only runner created by specified users"""

    kinds: List[
        Literal["RUNNER_KIND_UNSPECIFIED", "RUNNER_KIND_LOCAL", "RUNNER_KIND_REMOTE", "RUNNER_KIND_LOCAL_CONFIGURATION"]
    ]
    """kinds filters the response to only runners of the specified kinds"""

    providers: List[
        Literal[
            "RUNNER_PROVIDER_UNSPECIFIED",
            "RUNNER_PROVIDER_AWS_EC2",
            "RUNNER_PROVIDER_LINUX_HOST",
            "RUNNER_PROVIDER_DESKTOP_MAC",
        ]
    ]
    """providers filters the response to only runners of the specified providers"""


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
