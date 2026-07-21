# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.kernel_controls_action import KernelControlsAction

__all__ = ["Veto", "Exec"]


class Exec(BaseModel):
    """exec controls executable blocking"""

    action: Optional[KernelControlsAction] = None
    """action specifies what action kernel-level controls take on policy violations"""

    denylist: Optional[List[str]] = None
    """denylist is the list of executable paths or names to block"""

    enabled: Optional[bool] = None
    """enabled controls whether executable blocking is active"""


class Veto(BaseModel):
    """Veto controls kernel-level blocking mechanisms"""

    exec: Optional[Exec] = None
    """exec controls executable blocking"""
