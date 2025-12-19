# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .group_membership import GroupMembership

__all__ = ["MembershipRetrieveResponse"]


class MembershipRetrieveResponse(BaseModel):
    member: Optional[GroupMembership] = None
    """The membership if found, nil if subject is not a member"""
