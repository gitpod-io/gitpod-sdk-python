# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .organization import Organization
from .organization_member import OrganizationMember

__all__ = ["OrganizationCreateResponse"]


class OrganizationCreateResponse(BaseModel):
    organization: Organization
    """organization is the created organization"""

    member: Optional[OrganizationMember] = None
    """member is the member that joined the org on creation.

    Only set if specified "join_organization" is "true" in the request.
    """
