# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = ["EnvironmentClassUpdateParams", "Description", "DisplayName", "Enabled"]


class Description(TypedDict, total=False):
    description: Required[str]


class DisplayName(TypedDict, total=False):
    display_name: Required[Annotated[str, PropertyInfo(alias="displayName")]]


class Enabled(TypedDict, total=False):
    enabled: Required[bool]


EnvironmentClassUpdateParams: TypeAlias = Union[Description, DisplayName, Enabled]
