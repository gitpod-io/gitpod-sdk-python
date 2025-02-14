# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .invite_domains_param import InviteDomainsParam

__all__ = ["OrganizationUpdateParams"]


class OrganizationUpdateParams(TypedDict, total=False):
    organization_id: Required[Annotated[str, PropertyInfo(alias="organizationId")]]
    """organization_id is the ID of the organization to update the settings for."""

    invite_domains: Annotated[Optional[InviteDomainsParam], PropertyInfo(alias="inviteDomains")]
    """invite_domains is the domain allowlist of the organization"""

    name: Optional[str]
    """name is the new name of the organization"""
