# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.user_status import UserStatus

__all__ = ["User"]


class User(BaseModel):
    id: str
    """id is a UUID of the user"""

    avatar_url: Optional[str] = FieldInfo(alias="avatarUrl", default=None)
    """avatar_url is a link to the user avatar"""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """created_at is the creation time"""

    email: Optional[str] = None
    """email is the user's email address"""

    name: Optional[str] = None
    """name is the full name of the user"""

    organization_id: Optional[str] = FieldInfo(alias="organizationId", default=None)
    """organization_id is the id of the organization this account is owned by.

    +optional if not set, this account is owned by the installation.
    """

    status: Optional[UserStatus] = None
    """status is the status the user is in"""
