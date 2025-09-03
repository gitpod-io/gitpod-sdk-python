# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr
from .id_token_version import IDTokenVersion

__all__ = ["IdentityGetIDTokenParams"]


class IdentityGetIDTokenParams(TypedDict, total=False):
    audience: SequenceNotStr[str]

    version: IDTokenVersion
    """version is the version of the ID token."""
