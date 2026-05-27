# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .codex_openai_model import CodexOpenAIModel
from .codex_reasoning_effort import CodexReasoningEffort

__all__ = ["CodexSettingsParam"]


class CodexSettingsParam(TypedDict, total=False):
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
