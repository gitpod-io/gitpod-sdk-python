# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .daily_credit_usage import DailyCreditUsage

__all__ = ["BillingGetCreditUsageReportResponse"]


class BillingGetCreditUsageReportResponse(BaseModel):
    daily_usage: Optional[List[DailyCreditUsage]] = FieldInfo(alias="dailyUsage", default=None)
    """One entry per day in the requested date range."""

    period_start: Optional[datetime] = FieldInfo(alias="periodStart", default=None)
    """
    Start of the billing period for this organization. Used by the frontend to
    filter out months before usage tracking began.
    """

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """When the report data was last computed."""
