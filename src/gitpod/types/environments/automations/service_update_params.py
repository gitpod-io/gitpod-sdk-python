# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo
from .service_role import ServiceRole
from .service_phase import ServicePhase
from ...shared_params.runs_on import RunsOn
from ...shared_params.automation_trigger import AutomationTrigger
from ...shared_params.environment_variable_item import EnvironmentVariableItem

__all__ = ["ServiceUpdateParams", "Metadata", "MetadataTriggeredBy", "Spec", "SpecCommands", "Status"]


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


class MetadataTriggeredBy(TypedDict, total=False):
    trigger: Iterable[AutomationTrigger]


class Metadata(TypedDict, total=False):
    description: Optional[str]

    name: Optional[str]

    role: Optional[ServiceRole]

    triggered_by: Annotated[Optional[MetadataTriggeredBy], PropertyInfo(alias="triggeredBy")]


class SpecCommands(TypedDict, total=False):
    ready: Optional[str]

    start: Optional[str]

    stop: Optional[str]


class Spec(TypedDict, total=False):
    """Changing the spec of a service is a complex operation.

    The spec of a service
     can only be updated if the service is in a stopped state. If the service is
     running, it must be stopped first.
    """

    commands: Optional[SpecCommands]

    env: Iterable[EnvironmentVariableItem]

    runs_on: Annotated[Optional[RunsOn], PropertyInfo(alias="runsOn")]


class Status(TypedDict, total=False):
    """Service status updates are only expected from the executing environment.

    As a client
     of this API you are not expected to provide this field. Updating this field requires
     the `environmentservice:update_status` permission.
    """

    failure_message: Annotated[Optional[str], PropertyInfo(alias="failureMessage")]

    log_url: Annotated[Optional[str], PropertyInfo(alias="logUrl")]

    output: Dict[str, str]
    """setting an output field to empty string will unset it."""

    phase: Optional[ServicePhase]

    session: Optional[str]
