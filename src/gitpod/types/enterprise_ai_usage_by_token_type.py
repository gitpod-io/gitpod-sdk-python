# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .enterprise_ai_usage import EnterpriseAIUsage
from .byok_rate_card_token_type import ByokRateCardTokenType

__all__ = ["EnterpriseAIUsageByTokenType"]


class EnterpriseAIUsageByTokenType(BaseModel):
    token_type: Optional[ByokRateCardTokenType] = FieldInfo(alias="tokenType", default=None)

    usage: Optional[EnterpriseAIUsage] = None
