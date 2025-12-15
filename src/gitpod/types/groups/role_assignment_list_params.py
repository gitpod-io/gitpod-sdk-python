# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from .resource_role import ResourceRole
from ..shared.resource_type import ResourceType

__all__ = ["RoleAssignmentListParams", "Filter", "Pagination"]


class RoleAssignmentListParams(TypedDict, total=False):
    token: str

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]

    filter: Filter
    """Filter parameters"""

    pagination: Pagination
    """Pagination parameters"""


class Filter(TypedDict, total=False):
    """Filter parameters"""

    group_id: Annotated[str, PropertyInfo(alias="groupId")]
    """
    group_id filters the response to only role assignments for this specific group
    Empty string is allowed and means no filtering by group
    """

    resource_roles: Annotated[List[ResourceRole], PropertyInfo(alias="resourceRoles")]
    """
    resource_roles filters the response to only role assignments with these specific
    roles
    """

    resource_types: Annotated[List[ResourceType], PropertyInfo(alias="resourceTypes")]
    """
    resource_types filters the response to only role assignments for these resource
    types
    """

    user_id: Annotated[str, PropertyInfo(alias="userId")]
    """
    user_id filters the response to only role assignments for groups that this user
    is a member of Empty string is allowed and means no filtering by user
    """


class Pagination(TypedDict, total=False):
    """Pagination parameters"""

    token: str
    """
    Token for the next set of results that was returned as next_token of a
    PaginationResponse
    """

    page_size: Annotated[int, PropertyInfo(alias="pageSize")]
    """Page size is the maximum number of results to retrieve per page. Defaults to 25.

    Maximum 100.
    """
