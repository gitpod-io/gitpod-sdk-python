# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .sort_order import SortOrder

__all__ = ["Sort"]


class Sort(BaseModel):
    field: Optional[str] = None
    """Field name to sort by, in camelCase."""

    order: Optional[SortOrder] = None
