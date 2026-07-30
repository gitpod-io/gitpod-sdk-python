# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .cumulative_credit_usage import CumulativeCreditUsage
from .user_credit_budget_usage import UserCreditBudgetUsage
from .team_cumulative_credit_usage import TeamCumulativeCreditUsage

__all__ = ["BillingGetCumulativeCreditUsageResponse"]


class BillingGetCumulativeCreditUsageResponse(BaseModel):
    org_usage: Optional[CumulativeCreditUsage] = FieldInfo(alias="orgUsage", default=None)
    """Org-wide cumulative usage, broken down by type and total."""

    period_start: Optional[datetime] = FieldInfo(alias="periodStart", default=None)
    """
    Start of the cumulative calculation period. Cumulative totals are computed from
    this date forward.
    """

    team_usage: Optional[List[TeamCumulativeCreditUsage]] = FieldInfo(alias="teamUsage", default=None)
    """
    Per-team cumulative usage with credit allocation comparison. Returns all teams
    (no top-N limit).
    """

    unteamed_usage: Optional[CumulativeCreditUsage] = FieldInfo(alias="unteamedUsage", default=None)
    """Usage by members not assigned to any team."""

    user_usage: Optional[List[UserCreditBudgetUsage]] = FieldInfo(alias="userUsage", default=None)
    """
    Per-user month-to-date usage for every user with usage in the period. The budget
    fields on each entry are populated only when a monthly budget applies to that
    user. This list is not paginated or capped; for large organizations prefer
    ListEnterpriseUserCreditUsage.
    """
