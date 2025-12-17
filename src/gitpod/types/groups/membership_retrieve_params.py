# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..shared_params.subject import Subject

__all__ = ["MembershipRetrieveParams"]


class MembershipRetrieveParams(TypedDict, total=False):
    subject: Required[Subject]
    """Subject to check membership for"""

    group_id: Annotated[str, PropertyInfo(alias="groupId")]
