# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .enterprise_ai_usage import EnterpriseAIUsage
from .enterprise_ai_usage_budget import EnterpriseAIUsageBudget
from .enterprise_ai_usage_by_token_type import EnterpriseAIUsageByTokenType

__all__ = ["TeamEnterpriseAIUsage"]


class TeamEnterpriseAIUsage(BaseModel):
    budget: Optional[EnterpriseAIUsageBudget] = None
    """budget is unset when no monthly budget applies to this team."""

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)

    team_id: Optional[str] = FieldInfo(alias="teamId", default=None)

    usage: Optional[EnterpriseAIUsage] = None

    usage_by_token_type: Optional[List[EnterpriseAIUsageByTokenType]] = FieldInfo(
        alias="usageByTokenType", default=None
    )
