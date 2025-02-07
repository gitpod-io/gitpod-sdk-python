# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .shared.organization_role import OrganizationRole

__all__ = ["OrganizationSetRoleParams"]


class OrganizationSetRoleParams(TypedDict, total=False):
    organization_id: Annotated[str, PropertyInfo(alias="organizationId")]

    role: OrganizationRole

    user_id: Annotated[str, PropertyInfo(alias="userId")]
