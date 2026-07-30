# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .usage_type import UsageType

__all__ = ["CreditsByType"]


class CreditsByType(BaseModel):
    """CreditsByType contains credits consumed for a single usage type."""

    credits: Optional[float] = None

    usage_type: Optional[UsageType] = FieldInfo(alias="usageType", default=None)
    """UsageType identifies the category of usage."""
