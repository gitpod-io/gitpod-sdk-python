# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .warm_pool_phase import WarmPoolPhase

__all__ = ["WarmPoolStatus"]


class WarmPoolStatus(BaseModel):
    """
    WarmPoolStatus contains the current status of a warm pool as reported by the runner
    """

    phase: WarmPoolPhase
    """phase is the current phase of the warm pool lifecycle"""

    failure_message: Optional[str] = FieldInfo(alias="failureMessage", default=None)
    """failure_message contains details about why the warm pool is degraded or failed"""

    status_version: Optional[str] = FieldInfo(alias="statusVersion", default=None)
    """
    status_version is incremented each time the status is updated. Used for
    optimistic concurrency control.
    """
