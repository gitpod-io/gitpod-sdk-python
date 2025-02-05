# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "OrganizationUpdateParams",
    "InviteDomainsIsTheDomainAllowlistOfTheOrganization",
    "InviteDomainsIsTheDomainAllowlistOfTheOrganizationInviteDomains",
    "NameIsTheNewNameOfTheOrganization",
]


class InviteDomainsIsTheDomainAllowlistOfTheOrganization(TypedDict, total=False):
    invite_domains: Required[
        Annotated[InviteDomainsIsTheDomainAllowlistOfTheOrganizationInviteDomains, PropertyInfo(alias="inviteDomains")]
    ]
    """invite_domains is the domain allowlist of the organization"""


class InviteDomainsIsTheDomainAllowlistOfTheOrganizationInviteDomains(TypedDict, total=False):
    domains: List[str]
    """domains is the list of domains that are allowed to join the organization"""


class NameIsTheNewNameOfTheOrganization(TypedDict, total=False):
    name: Required[str]
    """name is the new name of the organization"""


OrganizationUpdateParams: TypeAlias = Union[
    InviteDomainsIsTheDomainAllowlistOfTheOrganization, NameIsTheNewNameOfTheOrganization
]
