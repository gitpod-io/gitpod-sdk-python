# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.subject import Subject

__all__ = ["GroupMembership"]


class GroupMembership(BaseModel):
    """GroupMembership represents a subject's membership in a group"""

    id: Optional[str] = None
    """Unique identifier for the group membership"""

    avatar_url: Optional[str] = FieldInfo(alias="avatarUrl", default=None)
    """Subject's avatar URL"""

    group_id: Optional[str] = FieldInfo(alias="groupId", default=None)
    """Group identifier"""

    name: Optional[str] = None
    """Subject's display name"""

    subject: Optional[Subject] = None
    """Subject (user, runner, environment, service account, etc.)"""
