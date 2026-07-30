# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .credits_by_type import CreditsByType

__all__ = ["CumulativeCreditUsage"]


class CumulativeCreditUsage(BaseModel):
    """CumulativeCreditUsage contains cumulative credit consumption totals."""

    total_credits: Optional[float] = FieldInfo(alias="totalCredits", default=None)
    """Total credits consumed."""

    usage_by_type: Optional[List[CreditsByType]] = FieldInfo(alias="usageByType", default=None)
    """Credits consumed broken down by usage type."""
