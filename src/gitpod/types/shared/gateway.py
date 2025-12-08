# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Gateway"]


class Gateway(BaseModel):
    """Gateway represents a system gateway that provides access to services"""

    name: str
    """name is the human-readable name of the gateway.

    name is unique across all gateways.
    """

    url: str
    """url of the gateway"""

    region: Optional[str] = None
    """region is the geographical region where the gateway is located"""
