# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .billing_currency import BillingCurrency
from .enterprise_ai_token_usage import EnterpriseAITokenUsage

__all__ = ["EnterpriseAIUsage"]


class EnterpriseAIUsage(BaseModel):
    cost_microunits: Optional[str] = FieldInfo(alias="costMicrounits", default=None)

    credits: Optional[float] = None

    currency: Optional[BillingCurrency] = None

    tokens: Optional[EnterpriseAITokenUsage] = None
