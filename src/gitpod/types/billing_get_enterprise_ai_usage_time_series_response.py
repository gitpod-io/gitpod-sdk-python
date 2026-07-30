# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .daily_enterprise_ai_usage import DailyEnterpriseAIUsage

__all__ = ["BillingGetEnterpriseAIUsageTimeSeriesResponse"]


class BillingGetEnterpriseAIUsageTimeSeriesResponse(BaseModel):
    calculated_at: Optional[datetime] = FieldInfo(alias="calculatedAt", default=None)
    """
    calculated_at is the time through which usage has been calculated. Usage after
    this timestamp may still be processing.
    """

    daily_usage: Optional[List[DailyEnterpriseAIUsage]] = FieldInfo(alias="dailyUsage", default=None)
