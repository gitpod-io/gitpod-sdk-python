# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OrganizationRetrieveParams"]


class OrganizationRetrieveParams(TypedDict, total=False):
    organization_id: Required[Annotated[str, PropertyInfo(alias="organizationId")]]
    """organization_id is the unique identifier of the Organization to retreive."""
