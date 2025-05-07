# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

from .id_token_version import IDTokenVersion

__all__ = ["IdentityGetIDTokenParams"]


class IdentityGetIDTokenParams(TypedDict, total=False):
    audience: List[str]

    version: IDTokenVersion
    """version is the version of the ID token."""
