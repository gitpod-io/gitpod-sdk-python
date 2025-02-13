# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel
from .organization_invite import OrganizationInvite

__all__ = ["InviteRetrieveResponse"]


class InviteRetrieveResponse(BaseModel):
    invite: OrganizationInvite
