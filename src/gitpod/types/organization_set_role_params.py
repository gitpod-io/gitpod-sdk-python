# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OrganizationSetRoleParams"]


class OrganizationSetRoleParams(TypedDict, total=False):
    organization_id: Annotated[str, PropertyInfo(alias="organizationId")]

    role: Literal["ORGANIZATION_ROLE_UNSPECIFIED", "ORGANIZATION_ROLE_ADMIN", "ORGANIZATION_ROLE_MEMBER"]

    user_id: Annotated[str, PropertyInfo(alias="userId")]
