# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared_params.date_range import DateRange
from .credit_usage_export_group_by import CreditUsageExportGroupBy

__all__ = ["BillingGetCreditUsageExportParams"]


class BillingGetCreditUsageExportParams(TypedDict, total=False):
    date_range: Required[Annotated[DateRange, PropertyInfo(alias="dateRange")]]
    """Date range to export.

    Both start and end dates are inclusive; time-of-day is ignored. Unlike
    GetCreditUsageReport, the range may cover up to a year.
    """

    organization_id: Required[Annotated[str, PropertyInfo(alias="organizationId")]]

    group_by: Annotated[CreditUsageExportGroupBy, PropertyInfo(alias="groupBy")]
    """How to group the export data. Defaults to DAILY_SUMMARY."""
