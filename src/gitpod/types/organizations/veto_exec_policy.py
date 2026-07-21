# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.kernel_controls_action import KernelControlsAction

__all__ = ["VetoExecPolicy"]


class VetoExecPolicy(BaseModel):
    """
    VetoExecPolicy defines the policy for blocking or auditing executable execution in environments.
    """

    action: Optional[KernelControlsAction] = None
    """action specifies what action kernel-level controls take on policy violations"""

    enabled: Optional[bool] = None
    """enabled controls whether executable blocking is active"""

    executables: Optional[List[str]] = None
    """executables is the list of executable paths or names to block"""
