# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .user_input_block_param import UserInputBlockParam

__all__ = ["AgentSendToExecutionParams"]


class AgentSendToExecutionParams(TypedDict, total=False):
    agent_execution_id: Annotated[str, PropertyInfo(alias="agentExecutionId")]

    user_input: Annotated[UserInputBlockParam, PropertyInfo(alias="userInput")]
