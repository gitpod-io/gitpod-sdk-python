# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo
from ...shared_params.runs_on import RunsOn
from ...shared_params.automation_trigger import AutomationTrigger

__all__ = ["TaskUpdateParams", "Metadata", "MetadataTriggeredBy", "Spec"]


class TaskUpdateParams(TypedDict, total=False):
    id: str

    depends_on: Annotated[List[str], PropertyInfo(alias="dependsOn")]
    """dependencies specifies the IDs of the automations this task depends on."""

    metadata: Metadata

    spec: Spec


class MetadataTriggeredBy(TypedDict, total=False):
    trigger: Iterable[AutomationTrigger]


class Metadata(TypedDict, total=False):
    description: Optional[str]

    name: Optional[str]

    triggered_by: Annotated[Optional[MetadataTriggeredBy], PropertyInfo(alias="triggeredBy")]


class Spec(TypedDict, total=False):
    command: Optional[str]

    runs_on: Annotated[Optional[RunsOn], PropertyInfo(alias="runsOn")]
