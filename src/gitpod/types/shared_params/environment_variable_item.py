# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from .environment_variable_source import EnvironmentVariableSource

__all__ = ["EnvironmentVariableItem"]


class EnvironmentVariableItem(TypedDict, total=False):
    """
    EnvironmentVariableItem represents an environment variable that can be set
     either from a literal value or from a secret reference.
    """

    name: str
    """name is the environment variable name."""

    value: str
    """value is a literal string value."""

    value_from: Annotated[EnvironmentVariableSource, PropertyInfo(alias="valueFrom")]
    """value_from specifies a source for the value."""
