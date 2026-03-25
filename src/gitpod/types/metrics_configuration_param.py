# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["MetricsConfigurationParam"]


class MetricsConfigurationParam(TypedDict, total=False):
    enabled: bool
    """enabled indicates whether the runner should collect metrics"""

    password: str
    """password is the password to use for the metrics collector"""

    url: str
    """url is the URL of the metrics collector"""

    username: str
    """username is the username to use for the metrics collector"""
