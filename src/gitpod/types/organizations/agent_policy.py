# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

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

    scm_tools_allowed_group_id: Optional[str] = FieldInfo(alias="scmToolsAllowedGroupId", default=None)
    """
    scm_tools_allowed_group_id restricts SCM tools access to members of this group.
    Empty means no restriction (all users can use SCM tools if not disabled).
    """
