# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..shared.sort_order import SortOrder

__all__ = ["Sort"]


class Sort(TypedDict, total=False):
    field: str
    """Field name to sort by, in camelCase."""

    order: SortOrder
