# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .error_level import ErrorLevel

__all__ = ["BreadcrumbParam"]


class BreadcrumbParam(TypedDict, total=False):
    """Breadcrumb information (Sentry-compatible)"""

    category: str
    """Breadcrumb category"""

    data: Dict[str, str]
    """Additional breadcrumb data"""

    level: ErrorLevel
    """Breadcrumb level"""

    message: str
    """Breadcrumb message"""

    timestamp: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """When the breadcrumb occurred"""

    type: str
    """Breadcrumb type (e.g., "navigation", "http", "user", "error")"""
