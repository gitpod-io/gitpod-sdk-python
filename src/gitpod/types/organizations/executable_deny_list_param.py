# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..._types import SequenceNotStr
from .kernel_controls_action import KernelControlsAction

__all__ = ["ExecutableDenyListParam"]


class ExecutableDenyListParam(TypedDict, total=False):
    """
    ExecutableDenyList contains executables that are blocked from execution in environments.
    """

    action: KernelControlsAction
    """action specifies what action kernel-level controls take on policy violations"""

    enabled: bool
    """enabled controls whether executable blocking is active"""

    executables: SequenceNotStr[str]
    """executables is the list of executable paths or names to block"""
