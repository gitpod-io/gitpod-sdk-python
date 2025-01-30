# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "RunnerUpdateRunnerParams",
    "Name",
    "Spec",
    "SpecSpec",
    "SpecSpecConfiguration",
    "SpecSpecConfigurationConfiguration",
    "SpecSpecConfigurationConfigurationAutoUpdate",
    "SpecSpecConfigurationConfigurationReleaseChannel",
    "SpecSpecDesiredPhase",
]


class Name(TypedDict, total=False):
    name: Required[str]
    """The runner's name which is shown to users"""

    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""


class Spec(TypedDict, total=False):
    spec: Required[SpecSpec]

    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""


class SpecSpecConfigurationConfigurationAutoUpdate(TypedDict, total=False):
    auto_update: Required[Annotated[bool, PropertyInfo(alias="autoUpdate")]]
    """auto_update indicates whether the runner should automatically update itself."""


class SpecSpecConfigurationConfigurationReleaseChannel(TypedDict, total=False):
    release_channel: Required[
        Annotated[
            Literal[
                "RUNNER_RELEASE_CHANNEL_UNSPECIFIED", "RUNNER_RELEASE_CHANNEL_STABLE", "RUNNER_RELEASE_CHANNEL_LATEST"
            ],
            PropertyInfo(alias="releaseChannel"),
        ]
    ]
    """The release channel the runner is on"""


SpecSpecConfigurationConfiguration: TypeAlias = Union[
    SpecSpecConfigurationConfigurationAutoUpdate, SpecSpecConfigurationConfigurationReleaseChannel
]


class SpecSpecConfiguration(TypedDict, total=False):
    configuration: Required[SpecSpecConfigurationConfiguration]


class SpecSpecDesiredPhase(TypedDict, total=False):
    desired_phase: Required[
        Annotated[
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
    ]
    """RunnerPhase represents the phase a runner is in"""


SpecSpec: TypeAlias = Union[SpecSpecConfiguration, SpecSpecDesiredPhase]

RunnerUpdateRunnerParams: TypeAlias = Union[Name, Spec]
