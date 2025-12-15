# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .agent_execution import AgentExecution

__all__ = ["AgentRetrieveExecutionResponse"]


class AgentRetrieveExecutionResponse(BaseModel):
    agent_execution: Optional[AgentExecution] = FieldInfo(alias="agentExecution", default=None)
