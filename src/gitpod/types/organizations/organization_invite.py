# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["OrganizationInvite"]


class OrganizationInvite(BaseModel):
    invite_id: str = FieldInfo(alias="inviteId")
    """
    invite_id is the unique identifier of the invite to join the organization. Use
    JoinOrganization with this ID to join the organization.
    """
