# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel
from .organization_member import OrganizationMember

__all__ = ["OrganizationJoinResponse"]


class OrganizationJoinResponse(BaseModel):
    member: OrganizationMember
    """member is the member that was created by joining the organization."""
