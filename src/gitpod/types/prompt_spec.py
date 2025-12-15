# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PromptSpec"]


class PromptSpec(BaseModel):
    command: Optional[str] = None
    """command is the unique command string within the organization"""

    is_command: Optional[bool] = FieldInfo(alias="isCommand", default=None)
    """is_command indicates if this prompt is a command"""

    is_template: Optional[bool] = FieldInfo(alias="isTemplate", default=None)
    """is_template indicates if this prompt is a template"""

    prompt: Optional[str] = None
    """prompt is the content of the prompt"""
