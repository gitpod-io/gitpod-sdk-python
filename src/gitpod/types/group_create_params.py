# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["GroupCreateParams"]


class GroupCreateParams(TypedDict, total=False):
    description: str

    name: str

    organization_id: Annotated[str, PropertyInfo(alias="organizationId")]
