# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from .resource_role import ResourceRole
from ..shared.resource_type import ResourceType

__all__ = ["RoleAssignmentCreateParams"]


class RoleAssignmentCreateParams(TypedDict, total=False):
    group_id: Annotated[str, PropertyInfo(alias="groupId")]

    resource_id: Annotated[str, PropertyInfo(alias="resourceId")]

    resource_role: Annotated[ResourceRole, PropertyInfo(alias="resourceRole")]
    """
    ResourceRole represents roles that can be assigned to groups on resources These
    map directly to the roles defined in backend/db/rule/rbac/role/role.go
    """

    resource_type: Annotated[ResourceType, PropertyInfo(alias="resourceType")]
