# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .cumulative_credit_usage import CumulativeCreditUsage

__all__ = ["TeamCumulativeCreditUsage"]


class TeamCumulativeCreditUsage(BaseModel):
    """
    TeamCumulativeCreditUsage contains a team's cumulative credit usage and allocation.
    """

    credit_budget: Optional[str] = FieldInfo(alias="creditBudget", default=None)
    """
    The team's credit allocation (budget) in whole credits, if set. Not set means no
    allocation has been configured for this team.
    """

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)

    team_id: Optional[str] = FieldInfo(alias="teamId", default=None)

    usage: Optional[CumulativeCreditUsage] = None
    """Cumulative credit usage for this team."""
