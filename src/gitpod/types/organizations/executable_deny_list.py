# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ExecutableDenyList"]


class ExecutableDenyList(BaseModel):
    """
    ExecutableDenyList contains executables that are blocked from execution in environments.
    """

    enabled: Optional[bool] = None
    """enabled controls whether executable blocking is active"""

    executables: Optional[List[str]] = None
    """executables is the list of executable paths or names to block"""
