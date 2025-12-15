# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["ExceptionMechanismParam"]


class ExceptionMechanismParam(TypedDict, total=False):
    """Exception mechanism information (Sentry-compatible)"""

    data: Dict[str, str]
    """Additional mechanism-specific data"""

    description: str
    """Human-readable description of the mechanism"""

    handled: bool
    """Whether the exception was handled by user code"""

    synthetic: bool
    """Whether this is a synthetic exception (created by SDK)"""

    type: str
    """Type of mechanism (e.g., "generic", "promise", "onerror")"""
