# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ...._utils import PropertyInfo

__all__ = [
    "ServiceUpdateParams",
    "Metadata",
    "MetadataDescription",
    "MetadataName",
    "MetadataTriggeredBy",
    "MetadataTriggeredByTriggeredBy",
    "MetadataTriggeredByTriggeredByTrigger",
    "MetadataTriggeredByTriggeredByTriggerManual",
    "MetadataTriggeredByTriggeredByTriggerPostDevcontainerStart",
    "MetadataTriggeredByTriggeredByTriggerPostEnvironmentStart",
    "Spec",
    "SpecCommands",
    "SpecCommandsCommands",
    "SpecCommandsCommandsReady",
    "SpecCommandsCommandsStart",
    "SpecCommandsCommandsStop",
    "SpecRunsOn",
    "SpecRunsOnRunsOn",
    "SpecRunsOnRunsOnDocker",
    "Status",
    "StatusFailureMessage",
    "StatusLogURL",
    "StatusPhase",
    "StatusSession",
]


class ServiceUpdateParams(TypedDict, total=False):
    id: str

    metadata: Metadata

    spec: Spec
    """Changing the spec of a service is a complex operation.

    The spec of a service can only be updated if the service is in a stopped state.
    If the service is running, it must be stopped first.
    """

    status: Status
    """Service status updates are only expected from the executing environment.

    As a client of this API you are not expected to provide this field. Updating
    this field requires the `environmentservice:update_status` permission.
    """


class MetadataDescription(TypedDict, total=False):
    description: Required[str]


class MetadataName(TypedDict, total=False):
    name: Required[str]


class MetadataTriggeredByTriggeredByTriggerManual(TypedDict, total=False):
    manual: Required[bool]


class MetadataTriggeredByTriggeredByTriggerPostDevcontainerStart(TypedDict, total=False):
    post_devcontainer_start: Required[Annotated[bool, PropertyInfo(alias="postDevcontainerStart")]]


class MetadataTriggeredByTriggeredByTriggerPostEnvironmentStart(TypedDict, total=False):
    post_environment_start: Required[Annotated[bool, PropertyInfo(alias="postEnvironmentStart")]]


MetadataTriggeredByTriggeredByTrigger: TypeAlias = Union[
    MetadataTriggeredByTriggeredByTriggerManual,
    MetadataTriggeredByTriggeredByTriggerPostDevcontainerStart,
    MetadataTriggeredByTriggeredByTriggerPostEnvironmentStart,
]


class MetadataTriggeredByTriggeredBy(TypedDict, total=False):
    trigger: Iterable[MetadataTriggeredByTriggeredByTrigger]


class MetadataTriggeredBy(TypedDict, total=False):
    triggered_by: Required[Annotated[MetadataTriggeredByTriggeredBy, PropertyInfo(alias="triggeredBy")]]


Metadata: TypeAlias = Union[MetadataDescription, MetadataName, MetadataTriggeredBy]


class SpecCommandsCommandsReady(TypedDict, total=False):
    ready: Required[str]


class SpecCommandsCommandsStart(TypedDict, total=False):
    start: Required[str]


class SpecCommandsCommandsStop(TypedDict, total=False):
    stop: Required[str]


SpecCommandsCommands: TypeAlias = Union[SpecCommandsCommandsReady, SpecCommandsCommandsStart, SpecCommandsCommandsStop]


class SpecCommands(TypedDict, total=False):
    commands: Required[SpecCommandsCommands]


class SpecRunsOnRunsOnDocker(TypedDict, total=False):
    environment: List[str]

    image: str


class SpecRunsOnRunsOn(TypedDict, total=False):
    docker: Required[SpecRunsOnRunsOnDocker]


class SpecRunsOn(TypedDict, total=False):
    runs_on: Required[Annotated[SpecRunsOnRunsOn, PropertyInfo(alias="runsOn")]]


Spec: TypeAlias = Union[SpecCommands, SpecRunsOn]


class StatusFailureMessage(TypedDict, total=False):
    failure_message: Required[Annotated[str, PropertyInfo(alias="failureMessage")]]


class StatusLogURL(TypedDict, total=False):
    log_url: Required[Annotated[str, PropertyInfo(alias="logUrl")]]


class StatusPhase(TypedDict, total=False):
    phase: Required[
        Literal[
            "SERVICE_PHASE_UNSPECIFIED",
            "SERVICE_PHASE_STARTING",
            "SERVICE_PHASE_RUNNING",
            "SERVICE_PHASE_STOPPING",
            "SERVICE_PHASE_STOPPED",
            "SERVICE_PHASE_FAILED",
            "SERVICE_PHASE_DELETED",
        ]
    ]


class StatusSession(TypedDict, total=False):
    session: Required[str]


Status: TypeAlias = Union[StatusFailureMessage, StatusLogURL, StatusPhase, StatusSession]
