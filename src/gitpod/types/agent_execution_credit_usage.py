# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .credits_by_type import CreditsByType

__all__ = ["AgentExecutionCreditUsage"]


class AgentExecutionCreditUsage(BaseModel):
    """
    AgentExecutionCreditUsage contains a single agent execution's credit usage for a day, broken down by type.
    """

    agent_execution_id: Optional[str] = FieldInfo(alias="agentExecutionId", default=None)
    """Empty when representing the "Others" aggregation bucket."""

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)

    usage: Optional[List[CreditsByType]] = None
