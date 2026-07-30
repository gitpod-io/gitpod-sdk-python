# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .billing_currency import BillingCurrency
from .enterprise_ai_usage import EnterpriseAIUsage
from .enterprise_ai_user_budget_policy_source import EnterpriseAIUserBudgetPolicySource

__all__ = ["UserCostBudgetUsage"]


class UserCostBudgetUsage(BaseModel):
    budget_source: Optional[EnterpriseAIUserBudgetPolicySource] = FieldInfo(alias="budgetSource", default=None)

    currency: Optional[BillingCurrency] = None

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)

    is_service_account: Optional[bool] = FieldInfo(alias="isServiceAccount", default=None)

    monthly_cost_limit_microunits: Optional[str] = FieldInfo(alias="monthlyCostLimitMicrounits", default=None)

    month_to_date_usage: Optional[EnterpriseAIUsage] = FieldInfo(alias="monthToDateUsage", default=None)
    """Usage within the requested date range.

    Reflects true month-to-date usage when the range starts on the first day of the
    month.
    """

    no_cap: Optional[bool] = FieldInfo(alias="noCap", default=None)

    over_budget: Optional[bool] = FieldInfo(alias="overBudget", default=None)

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)

    utilization_percent: Optional[float] = FieldInfo(alias="utilizationPercent", default=None)
