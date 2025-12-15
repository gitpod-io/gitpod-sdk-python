# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AgentRetrieveExecutionParams"]


class AgentRetrieveExecutionParams(TypedDict, total=False):
    agent_execution_id: Annotated[str, PropertyInfo(alias="agentExecutionId")]
