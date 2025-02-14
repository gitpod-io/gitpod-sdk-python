# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["JoinableOrganization"]


class JoinableOrganization(BaseModel):
    organization_id: str = FieldInfo(alias="organizationId")
    """organization_id is the id of the organization the user can join"""

    organization_name: str = FieldInfo(alias="organizationName")
    """organization_name is the name of the organization the user can join"""

    organization_member_count: Optional[int] = FieldInfo(alias="organizationMemberCount", default=None)
    """
    organization_member_count is the member count of the organization the user can
    join
    """
