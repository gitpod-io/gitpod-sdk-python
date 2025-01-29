# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["InviteRetrieveResponse", "Invite"]


class Invite(BaseModel):
    invite_id: Optional[str] = FieldInfo(alias="inviteId", default=None)
    """invite_id is the unique identifier of the invite to join the organization.

    Use JoinOrganization with this ID to join the organization.
    """


class InviteRetrieveResponse(BaseModel):
    invite: Optional[Invite] = None
