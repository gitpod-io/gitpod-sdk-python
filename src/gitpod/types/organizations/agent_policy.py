# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.codex_openai_model import CodexOpenAIModel
from ..shared.codex_service_tier import CodexServiceTier
from .conversation_sharing_policy import ConversationSharingPolicy
from ..shared.codex_reasoning_effort import CodexReasoningEffort

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

    allowed_agent_ids: Optional[List[str]] = FieldInfo(alias="allowedAgentIds", default=None)
    """
    allowed_agent_ids contains the agent IDs users may select when the codex_rollout
    feature flag is enabled. Empty means all agents are allowed.
    """

    allowed_codex_models: Optional[List[CodexOpenAIModel]] = FieldInfo(alias="allowedCodexModels", default=None)
    """
    allowed_codex_models contains the Codex models users may select when the
    codex_rollout feature flag is enabled. Empty means all Codex models are allowed.
    """

    allowed_codex_reasoning_efforts: Optional[List[CodexReasoningEffort]] = FieldInfo(
        alias="allowedCodexReasoningEfforts", default=None
    )
    """
    allowed_codex_reasoning_efforts contains the Codex reasoning efforts users may
    select when the codex_rollout feature flag is enabled. Empty means all Codex
    reasoning efforts are allowed.
    """

    allowed_codex_service_tiers: Optional[List[CodexServiceTier]] = FieldInfo(
        alias="allowedCodexServiceTiers", default=None
    )
    """
    allowed_codex_service_tiers contains the Codex service tiers users may select
    when the codex_rollout feature flag is enabled. Empty means all Codex service
    tiers are allowed.
    """

    conversation_sharing_policy: Optional[ConversationSharingPolicy] = FieldInfo(
        alias="conversationSharingPolicy", default=None
    )
    """conversation_sharing_policy controls whether agent conversations can be shared"""

    max_subagents_per_environment: Optional[int] = FieldInfo(alias="maxSubagentsPerEnvironment", default=None)
    """
    max_subagents_per_environment limits the number of non-terminal sub-agents a
    parent can have running simultaneously in the same environment. Valid range:
    0-10. Zero means use the default (5).
    """

    scm_tools_allowed_group_id: Optional[str] = FieldInfo(alias="scmToolsAllowedGroupId", default=None)
    """
    scm_tools_allowed_group_id restricts SCM tools access to members of this group.
    Empty means no restriction (all users can use SCM tools if not disabled).
    """
