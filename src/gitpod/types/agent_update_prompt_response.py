# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .prompt import Prompt
from .._models import BaseModel

__all__ = ["AgentUpdatePromptResponse"]


class AgentUpdatePromptResponse(BaseModel):
    prompt: Optional[Prompt] = None
