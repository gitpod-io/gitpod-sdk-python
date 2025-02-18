# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .field_value import FieldValue

__all__ = ["EnvironmentClass"]


class EnvironmentClass(TypedDict, total=False):
    id: Required[str]
    """id is the unique identifier of the environment class"""

    runner_id: Required[Annotated[str, PropertyInfo(alias="runnerId")]]
    """
    runner_id is the unique identifier of the runner the environment class belongs
    to
    """

    configuration: Iterable[FieldValue]
    """configuration describes the configuration of the environment class"""

    description: str
    """description is a human readable description of the environment class"""

    display_name: Annotated[str, PropertyInfo(alias="displayName")]
    """display_name is the human readable name of the environment class"""

    enabled: bool
    """
    enabled indicates whether the environment class can be used to create new
    environments.
    """
