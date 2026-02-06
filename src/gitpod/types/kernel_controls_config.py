# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .veto import Veto
from .._models import BaseModel

__all__ = ["KernelControlsConfig"]


class KernelControlsConfig(BaseModel):
    """KernelControlsConfig configures kernel-level controls for the environment"""

    veto: Optional[Veto] = None
    """veto controls blocking mechanisms"""
