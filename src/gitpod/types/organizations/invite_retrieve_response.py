# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .organization_invite import OrganizationInvite

__all__ = ["InviteRetrieveResponse"]


class InviteRetrieveResponse(BaseModel):
    invite: Optional[OrganizationInvite] = None
