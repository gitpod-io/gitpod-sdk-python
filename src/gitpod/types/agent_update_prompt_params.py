# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AgentUpdatePromptParams", "Metadata", "Spec"]


class AgentUpdatePromptParams(TypedDict, total=False):
    metadata: Optional[Metadata]
    """Metadata updates"""

    prompt_id: Annotated[str, PropertyInfo(alias="promptId")]
    """The ID of the prompt to update"""

    spec: Optional[Spec]
    """Spec updates"""


class Metadata(TypedDict, total=False):
    """Metadata updates"""

    description: Optional[str]
    """A description of what the prompt does"""

    name: Optional[str]
    """The name of the prompt"""


class Spec(TypedDict, total=False):
    """Spec updates"""

    command: Optional[str]
    """The command string (unique within organization)"""

    is_command: Annotated[Optional[bool], PropertyInfo(alias="isCommand")]
    """Whether this prompt is a command"""

    is_template: Annotated[Optional[bool], PropertyInfo(alias="isTemplate")]
    """Whether this prompt is a template"""

    prompt: Optional[str]
    """The prompt content"""
