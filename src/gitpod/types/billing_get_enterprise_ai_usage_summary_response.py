# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .enterprise_ai_usage import EnterpriseAIUsage
from .enterprise_ai_usage_budget import EnterpriseAIUsageBudget
from .enterprise_ai_usage_by_model import EnterpriseAIUsageByModel

__all__ = ["BillingGetEnterpriseAIUsageSummaryResponse"]


class BillingGetEnterpriseAIUsageSummaryResponse(BaseModel):
    budget: Optional[EnterpriseAIUsageBudget] = None
    """budget is unset when no monthly budget applies to the organization."""

    calculated_at: Optional[datetime] = FieldInfo(alias="calculatedAt", default=None)
    """
    calculated_at is the time through which usage has been calculated. Usage after
    this timestamp may still be processing.
    """

    usage: Optional[EnterpriseAIUsage] = None

    usage_by_model: Optional[List[EnterpriseAIUsageByModel]] = FieldInfo(alias="usageByModel", default=None)
