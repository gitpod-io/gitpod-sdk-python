# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "OrganizationJoinParams",
    "InviteIDIsTheUniqueIdentifierOfTheInviteToJoinTheOrganization",
    "OrganizationIDIsTheUniqueIdentifierOfTheOrganizationToJoin",
]


class InviteIDIsTheUniqueIdentifierOfTheInviteToJoinTheOrganization(TypedDict, total=False):
    invite_id: Required[Annotated[str, PropertyInfo(alias="inviteId")]]
    """invite_id is the unique identifier of the invite to join the organization."""


class OrganizationIDIsTheUniqueIdentifierOfTheOrganizationToJoin(TypedDict, total=False):
    organization_id: Required[Annotated[str, PropertyInfo(alias="organizationId")]]
    """organization_id is the unique identifier of the Organization to join."""


OrganizationJoinParams: TypeAlias = Union[
    InviteIDIsTheUniqueIdentifierOfTheInviteToJoinTheOrganization,
    OrganizationIDIsTheUniqueIdentifierOfTheOrganizationToJoin,
]
