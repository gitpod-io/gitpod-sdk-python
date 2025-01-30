# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "OrganizationJoinParams",
    "InviteIDIsTheUniqueIdentifierOfTheInviteToJoinTheOrganization",
    "OrganizationIDIsTheUniqueIdentifierOfTheOrganizationToJoin",
]


class InviteIDIsTheUniqueIdentifierOfTheInviteToJoinTheOrganization(TypedDict, total=False):
    invite_id: Required[Annotated[str, PropertyInfo(alias="inviteId")]]
    """invite_id is the unique identifier of the invite to join the organization."""

    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""


class OrganizationIDIsTheUniqueIdentifierOfTheOrganizationToJoin(TypedDict, total=False):
    organization_id: Required[Annotated[str, PropertyInfo(alias="organizationId")]]
    """organization_id is the unique identifier of the Organization to join."""

    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""


OrganizationJoinParams: TypeAlias = Union[
    InviteIDIsTheUniqueIdentifierOfTheInviteToJoinTheOrganization,
    OrganizationIDIsTheUniqueIdentifierOfTheOrganizationToJoin,
]
