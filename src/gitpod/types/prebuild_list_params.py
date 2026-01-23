# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .prebuild_phase import PrebuildPhase
from .prebuild_trigger import PrebuildTrigger

__all__ = ["PrebuildListParams", "Filter", "Pagination"]


class PrebuildListParams(TypedDict, total=False):
    token: str

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    filter: Filter
    """filter contains the filter options for listing prebuilds"""

    pagination: Pagination
    """pagination contains the pagination options for listing prebuilds"""


class Filter(TypedDict, total=False):
    """filter contains the filter options for listing prebuilds"""

    creator_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="creatorIds")]
    """creator_ids filters prebuilds by who created them"""

    executor_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="executorIds")]
    """executor_ids filters prebuilds by whose credentials were used to run them"""

    phases: List[PrebuildPhase]
    """phases filters prebuilds by their current phase"""

    project_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="projectIds")]
    """project_ids filters prebuilds to specific projects"""

    triggered_by: Annotated[List[PrebuildTrigger], PropertyInfo(alias="triggeredBy")]
    """triggered_by filters prebuilds by how they were triggered"""


class Pagination(TypedDict, total=False):
    """pagination contains the pagination options for listing prebuilds"""

    token: str
    """
    Token for the next set of results that was returned as next_token of a
    PaginationResponse
    """

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
    """Page size is the maximum number of results to retrieve per page. Defaults to 25.

    Maximum 100.
    """
