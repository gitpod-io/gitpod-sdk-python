# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .credits_by_type import CreditsByType
from .team_credit_usage import TeamCreditUsage
from .user_credit_usage import UserCreditUsage
from .environment_credit_usage import EnvironmentCreditUsage
from .agent_execution_credit_usage import AgentExecutionCreditUsage
from .enterprise_ai_usage_by_model import EnterpriseAIUsageByModel

__all__ = ["DailyCreditUsage"]


class DailyCreditUsage(BaseModel):
    """DailyCreditUsage contains credit usage for a single day."""

    conversation_usage: Optional[List[AgentExecutionCreditUsage]] = FieldInfo(alias="conversationUsage", default=None)
    """
    Per-agent-execution usage for this day (top conversations + "Others"). Empty
    agent_execution_id represents the "Others" aggregation bucket.
    """

    date: Optional[datetime] = None
    """Start of the day (midnight in the requested timezone)."""

    environment_usage: Optional[List[EnvironmentCreditUsage]] = FieldInfo(alias="environmentUsage", default=None)
    """
    Per-environment usage for this day (top environments + "Others"). Empty
    environment_id represents the "Others" aggregation bucket.
    """

    org_usage: Optional[List[CreditsByType]] = FieldInfo(alias="orgUsage", default=None)
    """Org-wide usage broken down by type."""

    team_usage: Optional[List[TeamCreditUsage]] = FieldInfo(alias="teamUsage", default=None)
    """
    Per-team usage for this day (top teams + "Others"). Empty team_id represents the
    "Others" aggregation bucket.
    """

    usage_by_model: Optional[List[EnterpriseAIUsageByModel]] = FieldInfo(alias="usageByModel", default=None)
    """Org-wide intelligence usage broken down by model."""

    user_usage: Optional[List[UserCreditUsage]] = FieldInfo(alias="userUsage", default=None)
    """Per-user usage for this day (top users + "Others")."""
