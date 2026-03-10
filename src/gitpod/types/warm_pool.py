# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .warm_pool_spec import WarmPoolSpec
from .warm_pool_status import WarmPoolStatus
from .warm_pool_metadata import WarmPoolMetadata

__all__ = ["WarmPool"]


class WarmPool(BaseModel):
    """
    WarmPool maintains pre-created environment instances from a prebuild snapshot
     for near-instant environment startup.
     One warm pool exists per <project, environment_class> pair.
    """

    metadata: WarmPoolMetadata
    """metadata contains organizational and ownership information"""

    spec: WarmPoolSpec
    """spec contains the desired configuration for this warm pool"""

    status: WarmPoolStatus
    """status contains the current status reported by the runner"""

    id: Optional[str] = None
    """id is the unique identifier for the warm pool"""
