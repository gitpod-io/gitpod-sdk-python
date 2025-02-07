# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..shared.principal import Principal

__all__ = ["Subject"]


class Subject(TypedDict, total=False):
    id: str
    """id is the UUID of the subject"""

    principal: Principal
    """Principal is the principal of the subject"""
