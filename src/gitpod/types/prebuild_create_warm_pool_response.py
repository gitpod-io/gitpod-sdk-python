# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .warm_pool import WarmPool

__all__ = ["PrebuildCreateWarmPoolResponse"]


class PrebuildCreateWarmPoolResponse(BaseModel):
    warm_pool: WarmPool = FieldInfo(alias="warmPool")
    """
    WarmPool maintains pre-created environment instances from a prebuild snapshot
    for near-instant environment startup. One warm pool exists per <project,
    environment_class> pair.
    """
