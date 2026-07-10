# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared_params.date_range import DateRange

__all__ = ["BillingGetEnterpriseAIUsageSummaryParams"]


class BillingGetEnterpriseAIUsageSummaryParams(TypedDict, total=False):
    date_range: Required[Annotated[DateRange, PropertyInfo(alias="dateRange")]]
    """Date range for the summary.

    Both start and end dates are inclusive. Time-of-day is ignored; dates are
    truncated to midnight in the specified timezone.
    """

    organization_id: Required[Annotated[str, PropertyInfo(alias="organizationId")]]

    timezone: str
    """IANA timezone name used to bucket usage. When empty, defaults to "UTC"."""
