# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .prompt_spec import PromptSpec
from .prompt_metadata import PromptMetadata

__all__ = ["Prompt"]


class Prompt(BaseModel):
    id: Optional[str] = None

    metadata: Optional[PromptMetadata] = None

    spec: Optional[PromptSpec] = None
