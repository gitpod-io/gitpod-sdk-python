# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .cumulative_credit_usage import CumulativeCreditUsage
from .enterprise_ai_usage_by_model import EnterpriseAIUsageByModel
from .enterprise_ai_user_budget_policy_source import EnterpriseAIUserBudgetPolicySource

__all__ = ["UserCreditBudgetUsage"]


class UserCreditBudgetUsage(BaseModel):
    budget_source: Optional[EnterpriseAIUserBudgetPolicySource] = FieldInfo(alias="budgetSource", default=None)

    credit_budget: Optional[str] = FieldInfo(alias="creditBudget", default=None)

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)

    is_service_account: Optional[bool] = FieldInfo(alias="isServiceAccount", default=None)
    """
    True when user_id refers to a service account rather than a human user. The
    dashboard uses this to mark non-human accounts in admin tables.
    """

    month_to_date_usage: Optional[CumulativeCreditUsage] = FieldInfo(alias="monthToDateUsage", default=None)
    """CumulativeCreditUsage contains cumulative credit consumption totals."""

    no_cap: Optional[bool] = FieldInfo(alias="noCap", default=None)

    over_budget: Optional[bool] = FieldInfo(alias="overBudget", default=None)

    usage_by_model: Optional[List[EnterpriseAIUsageByModel]] = FieldInfo(alias="usageByModel", default=None)
    """Month-to-date intelligence usage broken down by model."""

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)

    utilization_percent: Optional[float] = FieldInfo(alias="utilizationPercent", default=None)
