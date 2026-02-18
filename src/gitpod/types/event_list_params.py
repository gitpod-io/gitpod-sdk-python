# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .shared.principal import Principal
from .shared.resource_type import ResourceType

__all__ = ["EventListParams", "Filter", "Pagination"]


class EventListParams(TypedDict, total=False):
    token: str

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    filter: Filter

    pagination: Pagination
    """pagination contains the pagination options for listing environments"""


_FilterReservedKeywords = TypedDict(
    "_FilterReservedKeywords",
    {
        "from": Union[str, datetime, None],
    },
    total=False,
)


class Filter(_FilterReservedKeywords, total=False):
    actor_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="actorIds")]

    actor_principals: Annotated[List[Principal], PropertyInfo(alias="actorPrincipals")]

    subject_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="subjectIds")]

    subject_types: Annotated[List[ResourceType], PropertyInfo(alias="subjectTypes")]

    to: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """to filters audit logs created before this timestamp (exclusive)."""


class Pagination(TypedDict, total=False):
    """pagination contains the pagination options for listing environments"""

    token: str
    """
    Token for the next set of results that was returned as next_token of a
    PaginationResponse
    """

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
    """Page size is the maximum number of results to retrieve per page. Defaults to 25.

    Maximum 100.
    """
