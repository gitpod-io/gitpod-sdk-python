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

    running_instances: Optional[int] = FieldInfo(alias="runningInstances", default=None)
    """
    running_instances is the number of running warm instances in the pool, ready to
    be claimed for near-instant environment startup.
    """

    status_version: Optional[str] = FieldInfo(alias="statusVersion", default=None)
    """
    status_version is incremented each time the status is updated. Used for
    optimistic concurrency control.
    """

    stopped_instances: Optional[int] = FieldInfo(alias="stoppedInstances", default=None)
    """
    stopped_instances is the number of pre-provisioned but stopped instances in the
    pool. When a running instance is claimed, stopped instances are used to backfill
    the running pool faster than provisioning from scratch. Stopped instances only
    incur storage costs, allowing a larger total pool at lower cost than keeping all
    instances running.
    """
