# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr
from .shared.kernel_controls_action import KernelControlsAction

__all__ = ["VetoParam", "Exec"]


class Exec(TypedDict, total=False):
    """exec controls executable blocking"""

    action: KernelControlsAction
    """action specifies what action kernel-level controls take on policy violations"""

    denylist: SequenceNotStr[str]
    """denylist is the list of executable paths or names to block"""

    enabled: bool
    """enabled controls whether executable blocking is active"""


class VetoParam(TypedDict, total=False):
    """Veto controls kernel-level blocking mechanisms"""

    exec: Exec
    """exec controls executable blocking"""
