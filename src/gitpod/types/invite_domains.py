# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["InviteDomains"]


class InviteDomains(BaseModel):
    domains: Optional[List[str]] = None
    """domains is the list of domains that are allowed to join the organization"""
