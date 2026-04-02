# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MetricsConfigurationParam"]


class MetricsConfigurationParam(TypedDict, total=False):
    enabled: bool
    """enabled indicates whether the runner should collect metrics"""

    managed_metrics_enabled: Annotated[bool, PropertyInfo(alias="managedMetricsEnabled")]
    """
    When true, the runner pushes metrics to the management plane via
    ReportRunnerMetrics instead of directly to the remote_write endpoint.
    """

    password: str
    """password is the password to use for the metrics collector"""

    url: str
    """url is the URL of the metrics collector"""

    username: str
    """username is the username to use for the metrics collector"""
