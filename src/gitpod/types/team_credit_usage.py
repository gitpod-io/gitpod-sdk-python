# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .credits_by_type import CreditsByType

__all__ = ["TeamCreditUsage"]


class TeamCreditUsage(BaseModel):
    """
    TeamCreditUsage contains a single team's credit usage for a day, broken down by type.
    """

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)

    team_id: Optional[str] = FieldInfo(alias="teamId", default=None)
    """Empty when representing the "Others" aggregation bucket."""

    usage: Optional[List[CreditsByType]] = None
