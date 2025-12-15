# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AgentCreatePromptParams"]


class AgentCreatePromptParams(TypedDict, total=False):
    command: str

    description: str

    is_command: Annotated[bool, PropertyInfo(alias="isCommand")]

    is_template: Annotated[bool, PropertyInfo(alias="isTemplate")]

    name: str

    prompt: str
