# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .wake_event_param import WakeEventParam
from .agent_message_param import AgentMessageParam
from .user_input_block_param import UserInputBlockParam
from .shared_params.codex_settings import CodexSettings

__all__ = ["AgentSendToExecutionParams"]


class AgentSendToExecutionParams(TypedDict, total=False):
    agent_execution_id: Annotated[str, PropertyInfo(alias="agentExecutionId")]

    agent_message: Annotated[AgentMessageParam, PropertyInfo(alias="agentMessage")]
    """AgentMessage is a message sent between agents (e.g.

    from a parent agent to a child agent execution, or vice versa).
    """

    codex_settings: Annotated[CodexSettings, PropertyInfo(alias="codexSettings")]
    """
    codex_settings contains per-turn desired settings for Codex app user_input
    sends.
    """

    user_input: Annotated[UserInputBlockParam, PropertyInfo(alias="userInput")]

    wake_event: Annotated[WakeEventParam, PropertyInfo(alias="wakeEvent")]
    """
    WakeEvent is sent by the backend to wake an agent when a registered interest
    fires. Delivered via SendToAgentExecution as a new oneof variant.
    """
