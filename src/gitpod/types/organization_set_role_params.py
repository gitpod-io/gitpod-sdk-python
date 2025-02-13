# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared.organization_role import OrganizationRole

__all__ = ["OrganizationSetRoleParams"]


class OrganizationSetRoleParams(TypedDict, total=False):
    organization_id: Required[Annotated[str, PropertyInfo(alias="organizationId")]]

    user_id: Required[Annotated[str, PropertyInfo(alias="userId")]]

    role: OrganizationRole
