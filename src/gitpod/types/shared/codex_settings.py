# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .codex_openai_model import CodexOpenAIModel
from .codex_service_tier import CodexServiceTier
from .codex_reasoning_effort import CodexReasoningEffort

__all__ = ["CodexSettings"]


class CodexSettings(BaseModel):
    """CodexSettings contains settings consumed only by the Codex app agent."""

    model: Optional[CodexOpenAIModel] = None
    """
    CodexOpenAIModel is the static allowlist of concrete OpenAI models that the
    Codex app runtime can select through Ona's Codex picker.
    """

    reasoning_effort: Optional[CodexReasoningEffort] = FieldInfo(alias="reasoningEffort", default=None)
    """
    CodexReasoningEffort is the static allowlist of reasoning efforts supported by
    the Codex app runtime.
    """

    service_tier: Optional[CodexServiceTier] = FieldInfo(alias="serviceTier", default=None)
    """
    CodexServiceTier is the static allowlist of service tiers supported by the Codex
    app runtime.
    """
