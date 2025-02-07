# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .project_role import ProjectRole

__all__ = ["ProjectPolicy"]


class ProjectPolicy(BaseModel):
    group_id: Optional[str] = FieldInfo(alias="groupId", default=None)

    role: Optional[ProjectRole] = None
    """role is the role assigned to the group"""
