# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .agent_mode import AgentMode
from .agent_code_context_param import AgentCodeContextParam

__all__ = ["AgentStartExecutionParams"]


class AgentStartExecutionParams(TypedDict, total=False):
    agent_id: Annotated[str, PropertyInfo(alias="agentId")]

    code_context: Annotated[AgentCodeContextParam, PropertyInfo(alias="codeContext")]

    mode: AgentMode
    """
    mode specifies the operational mode for this agent execution If not specified,
    defaults to AGENT_MODE_EXECUTION
    """

    name: str

    workflow_action_id: Annotated[Optional[str], PropertyInfo(alias="workflowActionId")]
    """
    workflow_action_id is an optional reference to the workflow execution action
    that created this agent execution. Used for tracking and event correlation.
    """
