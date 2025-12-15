# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AgentPolicy"]


class AgentPolicy(BaseModel):
    """AgentPolicy contains agent-specific policy settings for an organization"""

    command_deny_list: List[str] = FieldInfo(alias="commandDenyList")
    """
    command_deny_list contains a list of commands that agents are not allowed to
    execute
    """

    mcp_disabled: bool = FieldInfo(alias="mcpDisabled")
    """
    mcp_disabled controls whether MCP (Model Context Protocol) is disabled for
    agents
    """

    scm_tools_disabled: bool = FieldInfo(alias="scmToolsDisabled")
    """
    scm_tools_disabled controls whether SCM (Source Control Management) tools are
    disabled for agents
    """
