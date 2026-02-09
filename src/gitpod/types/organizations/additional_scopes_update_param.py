# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["AdditionalScopesUpdateParam"]


class AdditionalScopesUpdateParam(TypedDict, total=False):
    """
    AdditionalScopesUpdate wraps a list of OIDC scopes so that the update request
     can distinguish "not changing scopes" (field absent) from "clearing all scopes"
     (field present, empty list).
    """

    scopes: SequenceNotStr[str]
