# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .resource_role import ResourceRole
from ..shared.resource_type import ResourceType

__all__ = ["RoleAssignment"]


class RoleAssignment(BaseModel):
    """RoleAssignment represents a role assigned to a group on a specific resource"""

    id: Optional[str] = None
    """Unique identifier for the role assignment"""

    group_id: Optional[str] = FieldInfo(alias="groupId", default=None)
    """Group identifier"""

    organization_id: Optional[str] = FieldInfo(alias="organizationId", default=None)
    """Organization identifier"""

    resource_id: Optional[str] = FieldInfo(alias="resourceId", default=None)
    """Resource identifier"""

    resource_role: Optional[ResourceRole] = FieldInfo(alias="resourceRole", default=None)
    """Role assigned to the group on this resource"""

    resource_type: Optional[ResourceType] = FieldInfo(alias="resourceType", default=None)
    """Type of resource (runner, project, environment, etc.)"""
