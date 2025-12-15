# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .group_membership import GroupMembership

__all__ = ["MembershipCreateResponse"]


class MembershipCreateResponse(BaseModel):
    member: Optional[GroupMembership] = None
    """GroupMembership represents a subject's membership in a group"""
