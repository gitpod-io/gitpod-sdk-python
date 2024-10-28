# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["EnvironmentListParams", "Pagination"]


class EnvironmentListParams(TypedDict, total=False):
    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    environment_ids: Annotated[List[str], PropertyInfo(alias="environmentIds")]
    """An optional list of environment IDs to fetch.

    If this list is empty/not provided all environments that ought to run on the
    runner are returned.
    """

    pagination: Pagination
    """pagination contains the pagination options for listing environments"""

    runner_id: Annotated[str, PropertyInfo(alias="runnerId")]
    """The runner's identifier"""

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""


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
