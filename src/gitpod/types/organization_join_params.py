# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OrganizationJoinParams"]


class OrganizationJoinParams(TypedDict, total=False):
    invite_id: Annotated[str, PropertyInfo(alias="inviteId")]
    """invite_id is the unique identifier of the invite to join the organization."""

    organization_id: Annotated[str, PropertyInfo(alias="organizationId")]
    """organization_id is the unique identifier of the Organization to join."""
