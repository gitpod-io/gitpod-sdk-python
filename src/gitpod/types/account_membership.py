# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.organization_role import OrganizationRole

__all__ = ["AccountMembership"]


class AccountMembership(BaseModel):
    organization_id: str = FieldInfo(alias="organizationId")
    """organization_id is the id of the organization the user is a member of"""

    organization_name: str = FieldInfo(alias="organizationName")
    """organization_name is the name of the organization the user is a member of"""

    user_id: str = FieldInfo(alias="userId")
    """user_id is the ID the user has in the organization"""

    user_role: OrganizationRole = FieldInfo(alias="userRole")
    """user_role is the role the user has in the organization"""

    organization_member_count: Optional[int] = FieldInfo(alias="organizationMemberCount", default=None)
    """
    organization_name is the member count of the organization the user is a member
    of
    """
