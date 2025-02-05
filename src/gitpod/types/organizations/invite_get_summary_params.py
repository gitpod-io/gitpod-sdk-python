# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["InviteGetSummaryParams"]


class InviteGetSummaryParams(TypedDict, total=False):
    invite_id: Annotated[str, PropertyInfo(alias="inviteId")]
