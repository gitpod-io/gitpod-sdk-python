# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EnvironmentRetrieveParams"]


class EnvironmentRetrieveParams(TypedDict, total=False):
    environment_id: Required[Annotated[str, PropertyInfo(alias="environmentId")]]
    """environment_id specifies the environment to get"""
