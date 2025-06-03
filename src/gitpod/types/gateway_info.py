# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .shared.gateway import Gateway

__all__ = ["GatewayInfo"]


class GatewayInfo(BaseModel):
    gateway: Optional[Gateway] = None
    """Gateway represents a system gateway that provides access to services"""

    latency: Optional[str] = None
    """latency is the round-trip time of the runner to the gateway in milliseconds."""
