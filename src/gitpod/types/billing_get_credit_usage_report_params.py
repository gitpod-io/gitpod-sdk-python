# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared_params.date_range import DateRange
from .credit_usage_report_filter_param import CreditUsageReportFilterParam

__all__ = ["BillingGetCreditUsageReportParams"]


class BillingGetCreditUsageReportParams(TypedDict, total=False):
    date_range: Required[Annotated[DateRange, PropertyInfo(alias="dateRange")]]
    """Date range for the report.

    Both start and end dates are inclusive. Time-of-day is ignored; dates are
    truncated to midnight in the specified timezone. The range must not exceed 31
    days.
    """

    organization_id: Required[Annotated[str, PropertyInfo(alias="organizationId")]]

    filter: CreditUsageReportFilterParam
    """Optional filter narrowing the returned data.

    When unset or empty, the response preserves the default behavior (top-N users +
    "Others"). See CreditUsageReportFilter for per-field response-scoping semantics.
    """

    timezone: str
    """IANA timezone name (e.g.

    "America/New_York", "Europe/Berlin") used to bucket daily usage. When empty,
    defaults to "UTC".
    """
