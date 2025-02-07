# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .runner_release_channel import RunnerReleaseChannel

__all__ = ["RunnerConfiguration"]


class RunnerConfiguration(BaseModel):
    auto_update: Optional[bool] = FieldInfo(alias="autoUpdate", default=None)
    """auto_update indicates whether the runner should automatically update itself."""

    region: Optional[str] = None
    """
    Region to deploy the runner in, if applicable. This is mainly used for remote
    runners, and is only a hint. The runner may be deployed in a different region.
    See the runner's status for the actual region.
    """

    release_channel: Optional[RunnerReleaseChannel] = FieldInfo(alias="releaseChannel", default=None)
    """The release channel the runner is on"""
