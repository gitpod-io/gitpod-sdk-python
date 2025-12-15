# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .environment_variable_source import EnvironmentVariableSource

__all__ = ["EnvironmentVariableItem"]


class EnvironmentVariableItem(BaseModel):
    """
    EnvironmentVariableItem represents an environment variable that can be set
     either from a literal value or from a secret reference.
    """

    name: Optional[str] = None
    """name is the environment variable name."""

    value: Optional[str] = None
    """value is a literal string value."""

    value_from: Optional[EnvironmentVariableSource] = FieldInfo(alias="valueFrom", default=None)
    """value_from specifies a source for the value."""
