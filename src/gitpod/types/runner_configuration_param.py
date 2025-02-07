# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .runner_release_channel import RunnerReleaseChannel

__all__ = ["RunnerConfigurationParam"]


class RunnerConfigurationParam(TypedDict, total=False):
    auto_update: Annotated[bool, PropertyInfo(alias="autoUpdate")]
    """auto_update indicates whether the runner should automatically update itself."""

    region: str
    """
    Region to deploy the runner in, if applicable. This is mainly used for remote
    runners, and is only a hint. The runner may be deployed in a different region.
    See the runner's status for the actual region.
    """

    release_channel: Annotated[RunnerReleaseChannel, PropertyInfo(alias="releaseChannel")]
    """The release channel the runner is on"""
