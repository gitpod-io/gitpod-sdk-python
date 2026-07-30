# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CodexModelPolicy"]


class CodexModelPolicy(BaseModel):
    """CodexModelPolicy controls per-model availability for Codex."""

    api_model_states: Optional[
        Dict[
            str,
            Literal[
                "CODEX_MODEL_POLICY_STATE_UNSPECIFIED",
                "CODEX_MODEL_POLICY_STATE_ALLOWED",
                "CODEX_MODEL_POLICY_STATE_DISABLED",
            ],
        ]
    ] = FieldInfo(alias="modelStates", default=None)
    """
    model_states maps CodexOpenAIModel enum names to explicit policy states. Missing
    entries are treated as allowed.
    """
