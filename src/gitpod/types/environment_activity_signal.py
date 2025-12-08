# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["EnvironmentActivitySignal"]


class EnvironmentActivitySignal(BaseModel):
    """EnvironmentActivitySignal used to signal activity for an environment."""

    source: Optional[str] = None
    """
    source of the activity signal, such as "VS Code", "SSH", or "Automations". It
    should be a human-readable string that describes the source of the activity
    signal.
    """

    timestamp: Optional[datetime] = None
    """
    timestamp of when the activity was observed by the source. Only reported every 5
    minutes. Zero value means no activity was observed.
    """
