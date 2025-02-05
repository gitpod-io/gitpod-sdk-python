# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from ...._utils import PropertyInfo

__all__ = ["EnvironmentClassUpdateParams", "Variant0", "Variant1", "Variant2"]


class Variant0(TypedDict, total=False):
    description: Required[str]


class Variant1(TypedDict, total=False):
    display_name: Required[Annotated[str, PropertyInfo(alias="displayName")]]


class Variant2(TypedDict, total=False):
    enabled: Required[bool]


EnvironmentClassUpdateParams: TypeAlias = Union[Variant0, Variant1, Variant2]
