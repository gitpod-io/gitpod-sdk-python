# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from ..shared_params.runs_on import RunsOn

__all__ = ["AutomationsFileParam", "Services", "ServicesCommands", "Tasks"]


class ServicesCommands(TypedDict, total=False):
    ready: str
    """
    ready is an optional command that is run repeatedly until it exits with a zero
    exit code. If set, the service will first go into a Starting phase, and then
    into a Running phase once the ready command exits with a zero exit code.
    """

    start: str
    """
    start is the command to start and run the service. If start exits, the service
    will transition to the following phase:

    - Stopped: if the exit code is 0
    - Failed: if the exit code is not 0 If the stop command is not set, the start
      command will receive a SIGTERM signal when the service is requested to stop.
      If it does not exit within 2 minutes, it will receive a SIGKILL signal.
    """

    stop: str
    """
    stop is an optional command that runs when the service is requested to stop. If
    set, instead of sending a SIGTERM signal to the start command, the stop command
    will be run. Once the stop command exits, the start command will receive a
    SIGKILL signal. If the stop command exits with a non-zero exit code, the service
    will transition to the Failed phase. If the stop command does not exit within 2
    minutes, a SIGKILL signal will be sent to both the start and stop commands.
    """


class Services(TypedDict, total=False):
    commands: ServicesCommands

    description: str

    name: str

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

    role: Literal["", "default", "editor", "ai-agent"]

    runs_on: Annotated[RunsOn, PropertyInfo(alias="runsOn")]

    triggered_by: Annotated[
        List[Literal["manual", "postEnvironmentStart", "postDevcontainerStart", "prebuild"]],
        PropertyInfo(alias="triggeredBy"),
    ]


class Tasks(TypedDict, total=False):
    command: str

    depends_on: Annotated[SequenceNotStr[str], PropertyInfo(alias="dependsOn")]

    description: str

    name: str

    prebuild_requires_success: Annotated[bool, PropertyInfo(alias="prebuildRequiresSuccess")]
    """
    prebuild_requires_success controls whether a non-successful outcome of this task
    should fail the prebuild. When true and the task is triggered by a prebuild
    trigger, any terminal phase other than SUCCEEDED will cause the prebuild to
    fail. Defaults to false.
    """

    runs_on: Annotated[RunsOn, PropertyInfo(alias="runsOn")]

    triggered_by: Annotated[
        List[Literal["manual", "postEnvironmentStart", "postDevcontainerStart", "prebuild"]],
        PropertyInfo(alias="triggeredBy"),
    ]


class AutomationsFileParam(TypedDict, total=False):
    """
    WARN: Do not remove any field here, as it will break reading automation yaml files. We error if there are any
     unknown fields in the yaml (to ensure the yaml is correct), but would break if we removed any fields.
     This includes marking a field as "reserved" in the proto file, this will also break reading the yaml.
    """

    services: Dict[str, Services]

    tasks: Dict[str, Tasks]
