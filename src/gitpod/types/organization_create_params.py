# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OrganizationCreateParams"]


class OrganizationCreateParams(TypedDict, total=False):
    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    invite_accounts_with_matching_domain: Annotated[bool, PropertyInfo(alias="inviteAccountsWithMatchingDomain")]
    """
    Should other Accounts with the same domain be automatically invited to the
    organization?
    """

    join_organization: Annotated[bool, PropertyInfo(alias="joinOrganization")]
    """
    join_organization decides whether the Identity issuing this request joins the
    org on creation
    """

    name: str
    """name is the organization name"""

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""
