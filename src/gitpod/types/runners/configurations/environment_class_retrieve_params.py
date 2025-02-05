# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["EnvironmentClassRetrieveParams"]


class EnvironmentClassRetrieveParams(TypedDict, total=False):
    environment_class_id: Annotated[str, PropertyInfo(alias="environmentClassId")]
