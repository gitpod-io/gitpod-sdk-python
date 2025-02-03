# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "RunnerUpdateParams",
    "TheRunnerSNameWhichIsShownToUsers",
    "Variant1",
    "Variant1Spec",
    "Variant1SpecConfiguration",
    "Variant1SpecConfigurationConfiguration",
    "Variant1SpecConfigurationConfigurationAutoUpdateIndicatesWhetherTheRunnerShouldAutomaticallyUpdateItself",
    "Variant1SpecConfigurationConfigurationTheReleaseChannelTheRunnerIsOn",
    "Variant1SpecDesiredPhaseCanCurrentlyOnlyBeUpdatedOnLocalConfigurationRunnersToToggleWhetherLocalRunnersAreAllowedForRunningEnvironmentsInTheOrganizationSetToActiveToEnableLocalRunnersInactiveToDisableAllLocalRunnersExistingLocalRunnersAndTheirEnvironmentsWillStopAndCannotBeStartedAgainUntilTheDesiredPhaseIsSetToActiveUseThisCarefullyAsItWillAffectAllUsersInTheOrganizationWhoUseLocalRunners",
]


class TheRunnerSNameWhichIsShownToUsers(TypedDict, total=False):
    name: Required[str]
    """The runner's name which is shown to users"""

    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""


class Variant1(TypedDict, total=False):
    spec: Required[Variant1Spec]

    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""


class Variant1SpecConfigurationConfigurationAutoUpdateIndicatesWhetherTheRunnerShouldAutomaticallyUpdateItself(
    TypedDict, total=False
):
    auto_update: Required[Annotated[bool, PropertyInfo(alias="autoUpdate")]]
    """auto_update indicates whether the runner should automatically update itself."""


class Variant1SpecConfigurationConfigurationTheReleaseChannelTheRunnerIsOn(TypedDict, total=False):
    release_channel: Required[
        Annotated[
            Literal[
                "RUNNER_RELEASE_CHANNEL_UNSPECIFIED", "RUNNER_RELEASE_CHANNEL_STABLE", "RUNNER_RELEASE_CHANNEL_LATEST"
            ],
            PropertyInfo(alias="releaseChannel"),
        ]
    ]
    """The release channel the runner is on"""


Variant1SpecConfigurationConfiguration: TypeAlias = Union[
    Variant1SpecConfigurationConfigurationAutoUpdateIndicatesWhetherTheRunnerShouldAutomaticallyUpdateItself,
    Variant1SpecConfigurationConfigurationTheReleaseChannelTheRunnerIsOn,
]


class Variant1SpecConfiguration(TypedDict, total=False):
    configuration: Required[Variant1SpecConfigurationConfiguration]


class Variant1SpecDesiredPhaseCanCurrentlyOnlyBeUpdatedOnLocalConfigurationRunnersToToggleWhetherLocalRunnersAreAllowedForRunningEnvironmentsInTheOrganizationSetToActiveToEnableLocalRunnersInactiveToDisableAllLocalRunnersExistingLocalRunnersAndTheirEnvironmentsWillStopAndCannotBeStartedAgainUntilTheDesiredPhaseIsSetToActiveUseThisCarefullyAsItWillAffectAllUsersInTheOrganizationWhoUseLocalRunners(
    TypedDict, total=False
):
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


Variant1Spec: TypeAlias = Union[
    Variant1SpecConfiguration,
    Variant1SpecDesiredPhaseCanCurrentlyOnlyBeUpdatedOnLocalConfigurationRunnersToToggleWhetherLocalRunnersAreAllowedForRunningEnvironmentsInTheOrganizationSetToActiveToEnableLocalRunnersInactiveToDisableAllLocalRunnersExistingLocalRunnersAndTheirEnvironmentsWillStopAndCannotBeStartedAgainUntilTheDesiredPhaseIsSetToActiveUseThisCarefullyAsItWillAffectAllUsersInTheOrganizationWhoUseLocalRunners,
]

RunnerUpdateParams: TypeAlias = Union[TheRunnerSNameWhichIsShownToUsers, Variant1]
