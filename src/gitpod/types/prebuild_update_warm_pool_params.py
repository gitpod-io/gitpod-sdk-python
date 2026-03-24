# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PrebuildUpdateWarmPoolParams"]


class PrebuildUpdateWarmPoolParams(TypedDict, total=False):
    warm_pool_id: Required[Annotated[str, PropertyInfo(alias="warmPoolId")]]
    """warm_pool_id specifies the warm pool to update"""

    desired_size: Annotated[Optional[int], PropertyInfo(alias="desiredSize")]
    """desired_size updates the number of warm instances to maintain."""
