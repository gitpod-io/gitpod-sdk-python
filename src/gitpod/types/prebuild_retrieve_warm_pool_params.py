# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PrebuildRetrieveWarmPoolParams"]


class PrebuildRetrieveWarmPoolParams(TypedDict, total=False):
    warm_pool_id: Required[Annotated[str, PropertyInfo(alias="warmPoolId")]]
    """warm_pool_id specifies the warm pool to retrieve"""
