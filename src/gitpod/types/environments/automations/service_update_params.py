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

    readiness_timeout: Annotated[str, PropertyInfo(alias="readinessTimeout")]
    """
    A Duration represents a signed, fixed-length span of time represented as a count
    of seconds and fractions of seconds at nanosecond resolution. It is independent
    of any calendar and concepts like "day" or "month". It is related to Timestamp
    in that the difference between two Timestamp values is a Duration and it can be
    added or subtracted from a Timestamp. Range is approximately +-10,000 years.

    # Examples

    Example 1: Compute Duration from two Timestamps in pseudo code.

         Timestamp start = ...;
         Timestamp end = ...;
         Duration duration = ...;

         duration.seconds = end.seconds - start.seconds;
         duration.nanos = end.nanos - start.nanos;

         if (duration.seconds < 0 && duration.nanos > 0) {
           duration.seconds += 1;
           duration.nanos -= 1000000000;
         } else if (duration.seconds > 0 && duration.nanos < 0) {
           duration.seconds -= 1;
           duration.nanos += 1000000000;
         }

    Example 2: Compute Timestamp from Timestamp + Duration in pseudo code.

         Timestamp start = ...;
         Duration duration = ...;
         Timestamp end = ...;

         end.seconds = start.seconds + duration.seconds;
         end.nanos = start.nanos + duration.nanos;

         if (end.nanos < 0) {
           end.seconds -= 1;
           end.nanos += 1000000000;
         } else if (end.nanos >= 1000000000) {
           end.seconds += 1;
           end.nanos -= 1000000000;
         }

    Example 3: Compute Duration from datetime.timedelta in Python.

         td = datetime.timedelta(days=3, minutes=10)
         duration = Duration()
         duration.FromTimedelta(td)

    # JSON Mapping

    In JSON format, the Duration type is encoded as a string rather than an object,
    where the string ends in the suffix "s" (indicating seconds) and is preceded by
    the number of seconds, with nanoseconds expressed as fractional seconds. For
    example, 3 seconds with 0 nanoseconds should be encoded in JSON format as "3s",
    while 3 seconds and 1 nanosecond should be expressed in JSON format as
    "3.000000001s", and 3 seconds and 1 microsecond should be expressed in JSON
    format as "3.000001s".
    """

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
