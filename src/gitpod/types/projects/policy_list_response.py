# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PolicyListResponse"]


class PolicyListResponse(BaseModel):
    group_id: Optional[str] = FieldInfo(alias="groupId", default=None)

    role: Optional[Literal["PROJECT_ROLE_UNSPECIFIED", "PROJECT_ROLE_ADMIN", "PROJECT_ROLE_USER"]] = None
    """role is the role assigned to the group"""
