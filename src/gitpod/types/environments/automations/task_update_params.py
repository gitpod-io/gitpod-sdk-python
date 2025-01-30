# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from ...._utils import PropertyInfo

__all__ = [
    "TaskUpdateParams",
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
    "SpecCommand",
    "SpecRunsOn",
    "SpecRunsOnRunsOn",
    "SpecRunsOnRunsOnDocker",
]


class TaskUpdateParams(TypedDict, total=False):
    id: str

    depends_on: Annotated[List[str], PropertyInfo(alias="dependsOn")]
    """dependencies specifies the IDs of the automations this task depends on."""

    metadata: Metadata

    spec: Spec


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


class SpecCommand(TypedDict, total=False):
    command: Required[str]


class SpecRunsOnRunsOnDocker(TypedDict, total=False):
    environment: List[str]

    image: str


class SpecRunsOnRunsOn(TypedDict, total=False):
    docker: Required[SpecRunsOnRunsOnDocker]


class SpecRunsOn(TypedDict, total=False):
    runs_on: Required[Annotated[SpecRunsOnRunsOn, PropertyInfo(alias="runsOn")]]


Spec: TypeAlias = Union[SpecCommand, SpecRunsOn]
