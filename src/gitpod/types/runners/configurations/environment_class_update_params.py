# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["EnvironmentClassUpdateParams"]


class EnvironmentClassUpdateParams(TypedDict, total=False):
    description: Optional[str]

    display_name: Annotated[Optional[str], PropertyInfo(alias="displayName")]

    enabled: Optional[bool]

    environment_class_id: Annotated[str, PropertyInfo(alias="environmentClassId")]
