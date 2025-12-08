# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .log_level import LogLevel
from .runner_phase import RunnerPhase
from .runner_release_channel import RunnerReleaseChannel

__all__ = ["RunnerUpdateParams", "Spec", "SpecConfiguration", "SpecConfigurationMetrics"]


class RunnerUpdateParams(TypedDict, total=False):
    name: Optional[str]
    """The runner's name which is shown to users"""

    runner_id: Annotated[str, PropertyInfo(alias="runnerId")]
    """runner_id specifies which runner to be updated.

    +required
    """

    spec: Optional[Spec]


class SpecConfigurationMetrics(TypedDict, total=False):
    """metrics contains configuration for the runner's metrics collection"""

    enabled: Optional[bool]
    """enabled indicates whether the runner should collect metrics"""

    password: Optional[str]
    """password is the password to use for the metrics collector"""

    url: Optional[str]
    """url is the URL of the metrics collector"""

    username: Optional[str]
    """username is the username to use for the metrics collector"""


class SpecConfiguration(TypedDict, total=False):
    auto_update: Annotated[Optional[bool], PropertyInfo(alias="autoUpdate")]
    """auto_update indicates whether the runner should automatically update itself."""

    devcontainer_image_cache_enabled: Annotated[Optional[bool], PropertyInfo(alias="devcontainerImageCacheEnabled")]
    """
    devcontainer_image_cache_enabled controls whether the shared devcontainer build
    cache is enabled for this runner.
    """

    log_level: Annotated[Optional[LogLevel], PropertyInfo(alias="logLevel")]
    """log_level is the log level for the runner"""

    metrics: Optional[SpecConfigurationMetrics]
    """metrics contains configuration for the runner's metrics collection"""

    release_channel: Annotated[Optional[RunnerReleaseChannel], PropertyInfo(alias="releaseChannel")]
    """The release channel the runner is on"""


class Spec(TypedDict, total=False):
    configuration: Optional[SpecConfiguration]

    desired_phase: Annotated[Optional[RunnerPhase], PropertyInfo(alias="desiredPhase")]
    """
    desired_phase can currently only be updated on local-configuration runners, to
    toggle whether local runners are allowed for running environments in the
    organization. Set to:

    - ACTIVE to enable local runners.
    - INACTIVE to disable all local runners. Existing local runners and their
      environments will stop, and cannot be started again until the desired_phase is
      set to ACTIVE. Use this carefully, as it will affect all users in the
      organization who use local runners.
    """
