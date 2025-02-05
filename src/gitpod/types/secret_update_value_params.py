# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SecretUpdateValueParams"]


class SecretUpdateValueParams(TypedDict, total=False):
    secret_id: Annotated[str, PropertyInfo(alias="secretId")]

    value: str
    """value is the plaintext value of the secret"""
