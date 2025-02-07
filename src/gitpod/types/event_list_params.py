# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .resource_type import ResourceType
from .shared.principal import Principal

__all__ = ["EventListParams", "Filter", "Pagination"]


class EventListParams(TypedDict, total=False):
    token: str

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    filter: Filter

    pagination: Pagination
    """pagination contains the pagination options for listing environments"""


class Filter(TypedDict, total=False):
    actor_ids: Annotated[List[str], PropertyInfo(alias="actorIds")]

    actor_principals: Annotated[List[Principal], PropertyInfo(alias="actorPrincipals")]

    subject_ids: Annotated[List[str], PropertyInfo(alias="subjectIds")]

    subject_types: Annotated[List[ResourceType], PropertyInfo(alias="subjectTypes")]


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
