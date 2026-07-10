# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .credits_by_type import CreditsByType
from .enterprise_ai_usage_by_model import EnterpriseAIUsageByModel

__all__ = ["UserCreditUsage"]


class UserCreditUsage(BaseModel):
    """UserCreditUsage contains a single user's credit usage, broken down by type."""

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)

    usage: Optional[List[CreditsByType]] = None

    usage_by_model: Optional[List[EnterpriseAIUsageByModel]] = FieldInfo(alias="usageByModel", default=None)
    """Intelligence usage broken down by model."""

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)
    """Empty when representing the "Others" aggregation bucket."""
