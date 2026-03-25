# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MetricsConfiguration"]


class MetricsConfiguration(BaseModel):
    enabled: Optional[bool] = None
    """enabled indicates whether the runner should collect metrics"""

    managed_metrics_enabled: Optional[bool] = FieldInfo(alias="managedMetricsEnabled", default=None)
    """
    When true, the runner pushes metrics to the management plane via
    ReportRunnerMetrics instead of directly to the remote_write endpoint.
    """

    password: Optional[str] = None
    """password is the password to use for the metrics collector"""

    url: Optional[str] = None
    """url is the URL of the metrics collector"""

    username: Optional[str] = None
    """username is the username to use for the metrics collector"""
