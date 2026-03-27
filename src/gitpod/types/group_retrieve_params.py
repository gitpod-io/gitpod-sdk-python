# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["GroupRetrieveParams"]


class GroupRetrieveParams(TypedDict, total=False):
    id: str
    """id looks up the group by its unique ID."""

    group_id: Annotated[str, PropertyInfo(alias="groupId")]
    """Deprecated: use the group oneof instead."""

    name: str
    """name looks up the group by its name within the caller's organization."""
