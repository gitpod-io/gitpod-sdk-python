# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["InviteDomainsParam"]


class InviteDomainsParam(TypedDict, total=False):
    domains: List[str]
    """domains is the list of domains that are allowed to join the organization"""
