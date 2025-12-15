# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["GroupUpdateParams"]


class GroupUpdateParams(TypedDict, total=False):
    description: str

    group_id: Annotated[str, PropertyInfo(alias="groupId")]

    name: str
