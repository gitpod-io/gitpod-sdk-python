# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RequestInfoParam"]


class RequestInfoParam(TypedDict, total=False):
    """Request information (Sentry-compatible)"""

    data: str
    """Request body (truncated if large)"""

    headers: Dict[str, str]
    """Request headers"""

    method: str
    """HTTP method"""

    query_string: Annotated[Dict[str, str], PropertyInfo(alias="queryString")]
    """Query parameters"""

    url: str
    """Request URL"""
