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
    """desired_size is the number of warm instances to maintain."""

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
