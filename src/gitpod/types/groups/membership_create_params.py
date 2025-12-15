# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from ..shared_params.subject import Subject

__all__ = ["MembershipCreateParams"]


class MembershipCreateParams(TypedDict, total=False):
    group_id: Annotated[str, PropertyInfo(alias="groupId")]

    subject: Subject
    """Subject to add to the group"""
