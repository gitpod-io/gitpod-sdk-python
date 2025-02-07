# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .organization_member import OrganizationMember

__all__ = ["OrganizationJoinResponse"]


class OrganizationJoinResponse(BaseModel):
    member: Optional[OrganizationMember] = None
    """member is the member that was created by joining the organization."""
