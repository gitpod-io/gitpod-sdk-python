# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PatDeleteParams"]


class PatDeleteParams(TypedDict, total=False):
    personal_access_token_id: Annotated[str, PropertyInfo(alias="personalAccessTokenId")]
