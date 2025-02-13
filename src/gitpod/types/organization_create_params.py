# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OrganizationCreateParams"]


class OrganizationCreateParams(TypedDict, total=False):
    name: Required[str]
    """name is the organization name"""

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
