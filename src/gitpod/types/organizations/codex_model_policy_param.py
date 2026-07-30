# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CodexModelPolicyParam"]


class CodexModelPolicyParam(TypedDict, total=False):
    """CodexModelPolicy controls per-model availability for Codex."""

    model_states: Annotated[
        Dict[
            str,
            Literal[
                "CODEX_MODEL_POLICY_STATE_UNSPECIFIED",
                "CODEX_MODEL_POLICY_STATE_ALLOWED",
                "CODEX_MODEL_POLICY_STATE_DISABLED",
            ],
        ],
        PropertyInfo(alias="modelStates"),
    ]
    """
    model_states maps CodexOpenAIModel enum names to explicit policy states. Missing
    entries are treated as allowed.
    """
