# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EditorRetrieveParams"]


class EditorRetrieveParams(TypedDict, total=False):
    id: Required[str]
    """id is the ID of the editor to get"""
