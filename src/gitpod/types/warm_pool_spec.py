# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .warm_pool_phase import WarmPoolPhase

__all__ = ["WarmPoolSpec"]


class WarmPoolSpec(BaseModel):
    """WarmPoolSpec contains the desired configuration for a warm pool"""

    desired_phase: Optional[WarmPoolPhase] = FieldInfo(alias="desiredPhase", default=None)
    """
    desired_phase is the intended lifecycle phase for this warm pool. Managed by the
    API and reconciler.
    """

    desired_size: Optional[int] = FieldInfo(alias="desiredSize", default=None)
    """
    desired_size is the number of warm instances to maintain. Deprecated: Use
    min_size and max_size instead for dynamic scaling. Existing pools will be
    migrated to min_size=max_size=desired_size.
    """

    max_size: Optional[int] = FieldInfo(alias="maxSize", default=None)
    """
    max_size is the maximum number of warm instances to maintain. The pool will
    never scale above this value. Must be >= min_size and <= 20.
    """

    min_size: Optional[int] = FieldInfo(alias="minSize", default=None)
    """
    min_size is the minimum number of warm instances to maintain. The pool will
    never scale below this value. Must be >= 0 and <= max_size. Set to 0 to allow
    full scale-down.
    """

    snapshot_id: Optional[str] = FieldInfo(alias="snapshotId", default=None)
    """
    snapshot_id is the prebuild snapshot to warm up in the pool. Updated by the
    reconciler when a new prebuild completes for this project and environment class.
    Empty when no completed prebuild exists yet.
    """

    spec_version: Optional[str] = FieldInfo(alias="specVersion", default=None)
    """
    spec_version is incremented each time the spec is updated. Used for optimistic
    concurrency control.
    """
