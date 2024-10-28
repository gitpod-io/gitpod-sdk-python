# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RunnerCreateParams", "Spec", "SpecConfiguration"]


class RunnerCreateParams(TypedDict, total=False):
    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    kind: Literal["RUNNER_KIND_UNSPECIFIED", "RUNNER_KIND_LOCAL", "RUNNER_KIND_REMOTE"]
    """RunnerKind represents the kind of a runner"""

    name: str
    """The runner name for humans"""

    spec: Spec

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""


class SpecConfiguration(TypedDict, total=False):
    auto_update: Annotated[bool, PropertyInfo(alias="autoUpdate")]
    """auto_update indicates whether the runner should automatically update itself."""

    region: str
    """
    Region to deploy the runner in, if applicable. This is mainly used for remote
    runners, and is only a hint. The runner may be deployed in a different region.
    See the runner's status for the actual region.
    """

    release_channel: Annotated[
        Literal["RUNNER_RELEASE_CHANNEL_UNSPECIFIED", "RUNNER_RELEASE_CHANNEL_STABLE", "RUNNER_RELEASE_CHANNEL_LATEST"],
        PropertyInfo(alias="releaseChannel"),
    ]
    """The release channel the runner is on"""


class Spec(TypedDict, total=False):
    configuration: SpecConfiguration
    """The runner's configuration"""

    desired_phase: Annotated[
        Literal[
            "RUNNER_PHASE_UNSPECIFIED",
            "RUNNER_PHASE_CREATED",
            "RUNNER_PHASE_INACTIVE",
            "RUNNER_PHASE_ACTIVE",
            "RUNNER_PHASE_DELETING",
            "RUNNER_PHASE_DELETED",
            "RUNNER_PHASE_DEGRADED",
        ],
        PropertyInfo(alias="desiredPhase"),
    ]
    """RunnerPhase represents the phase a runner is in"""
