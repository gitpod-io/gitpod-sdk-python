# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .agent_mode import AgentMode
from .agent_code_context_param import AgentCodeContextParam

__all__ = ["AgentStartExecutionParams"]


class AgentStartExecutionParams(TypedDict, total=False):
    agent_id: Annotated[str, PropertyInfo(alias="agentId")]

    annotations: Dict[str, str]
    """
    annotations are key-value pairs for tracking external context (e.g., Linear
    session IDs, GitHub issue references). Keys should follow domain/name convention
    (e.g., "linear.app/session-id").
    """

    code_context: Annotated[AgentCodeContextParam, PropertyInfo(alias="codeContext")]

    mode: AgentMode
    """
    mode specifies the operational mode for this agent execution If not specified,
    defaults to AGENT_MODE_EXECUTION
    """

    name: str

    runner_id: Annotated[str, PropertyInfo(alias="runnerId")]
    """
    runner_id specifies a runner for this agent execution. When set, the agent
    execution is routed to this runner instead of the runner associated with the
    environment.
    """

    session_id: Annotated[str, PropertyInfo(alias="sessionId")]
    """
    session_id is the ID of the session this agent execution belongs to. If empty, a
    new session is created implicitly.
    """

    workflow_action_id: Annotated[Optional[str], PropertyInfo(alias="workflowActionId")]
    """
    workflow_action_id is an optional reference to the workflow execution action
    that created this agent execution. Used for tracking and event correlation.
    """
