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
    """
    desired_size updates the number of warm instances to maintain. Deprecated: Use
    min_size and max_size instead for dynamic scaling.
    """

    max_size: Annotated[Optional[int], PropertyInfo(alias="maxSize")]
    """
    max_size updates the maximum number of warm instances to maintain. The pool will
    never scale above this value. Must be >= min_size and <= 20.
    """

    min_size: Annotated[Optional[int], PropertyInfo(alias="minSize")]
    """
    min_size updates the minimum number of warm instances to maintain. The pool will
    never scale below this value. Must be >= 0 and <= max_size. Set to 0 to allow
    full scale-down.
    """
