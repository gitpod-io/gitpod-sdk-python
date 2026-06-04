# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from ..shared.codex_openai_model import CodexOpenAIModel
from ..shared.codex_service_tier import CodexServiceTier
from ..shared.codex_reasoning_effort import CodexReasoningEffort

__all__ = ["CodexSettings"]


class CodexSettings(TypedDict, total=False):
    """CodexSettings contains settings consumed only by the Codex app agent."""

    model: CodexOpenAIModel
    """
    CodexOpenAIModel is the static allowlist of concrete OpenAI models that the
    Codex app runtime can select through Ona's Codex picker.
    """

    reasoning_effort: Annotated[CodexReasoningEffort, PropertyInfo(alias="reasoningEffort")]
    """
    CodexReasoningEffort is the static allowlist of reasoning efforts supported by
    the Codex app runtime.
    """

    service_tier: Annotated[CodexServiceTier, PropertyInfo(alias="serviceTier")]
    """
    CodexServiceTier is the static allowlist of service tiers supported by the Codex
    app runtime.
    """
