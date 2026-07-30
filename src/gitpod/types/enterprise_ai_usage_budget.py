# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .billing_currency import BillingCurrency
from .enterprise_ai_usage import EnterpriseAIUsage
from .enterprise_ai_usage_budget_source import EnterpriseAIUsageBudgetSource

__all__ = ["EnterpriseAIUsageBudget"]


class EnterpriseAIUsageBudget(BaseModel):
    currency: Optional[BillingCurrency] = None

    monthly_cost_limit_microunits: Optional[str] = FieldInfo(alias="monthlyCostLimitMicrounits", default=None)

    monthly_credit_limit: Optional[str] = FieldInfo(alias="monthlyCreditLimit", default=None)

    month_to_date_usage: Optional[EnterpriseAIUsage] = FieldInfo(alias="monthToDateUsage", default=None)

    source: Optional[EnterpriseAIUsageBudgetSource] = None

    utilization_percent: Optional[float] = FieldInfo(alias="utilizationPercent", default=None)
