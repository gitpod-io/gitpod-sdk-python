# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .log_level import LogLevel
from .runner_release_channel import RunnerReleaseChannel
from .metrics_configuration_param import MetricsConfigurationParam

__all__ = ["RunnerConfigurationParam"]


class RunnerConfigurationParam(TypedDict, total=False):
    auto_update: Annotated[bool, PropertyInfo(alias="autoUpdate")]
    """auto_update indicates whether the runner should automatically update itself."""

    devcontainer_image_cache_enabled: Annotated[bool, PropertyInfo(alias="devcontainerImageCacheEnabled")]
    """
    devcontainer_image_cache_enabled controls whether the devcontainer build cache
    is enabled for this runner. Only takes effect on supported runners, currently
    only AWS EC2 and Gitpod-managed runners.
    """

    log_level: Annotated[LogLevel, PropertyInfo(alias="logLevel")]
    """log_level is the log level for the runner"""

    metrics: MetricsConfigurationParam
    """metrics contains configuration for the runner's metrics collection"""

    region: str
    """
    Region to deploy the runner in, if applicable. This is mainly used for remote
    runners, and is only a hint. The runner may be deployed in a different region.
    See the runner's status for the actual region.
    """

    release_channel: Annotated[RunnerReleaseChannel, PropertyInfo(alias="releaseChannel")]
    """The release channel the runner is on"""
