# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .role_assignment import RoleAssignment

__all__ = ["RoleAssignmentCreateResponse"]


class RoleAssignmentCreateResponse(BaseModel):
    assignment: Optional[RoleAssignment] = None
    """RoleAssignment represents a role assigned to a group on a specific resource"""
