# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .enterprise_ai_usage import EnterpriseAIUsage
from .enterprise_ai_usage_by_token_type import EnterpriseAIUsageByTokenType

__all__ = ["EnterpriseAIUsageByModel"]


class EnterpriseAIUsageByModel(BaseModel):
    model: Optional[str] = None

    unpriced_usage: Optional[EnterpriseAIUsage] = FieldInfo(alias="unpricedUsage", default=None)
    """Usage excluded from spend because no matching BYOK rate was configured."""

    unpriced_usage_by_token_type: Optional[List[EnterpriseAIUsageByTokenType]] = FieldInfo(
        alias="unpricedUsageByTokenType", default=None
    )

    usage: Optional[EnterpriseAIUsage] = None

    usage_by_token_type: Optional[List[EnterpriseAIUsageByTokenType]] = FieldInfo(
        alias="usageByTokenType", default=None
    )
