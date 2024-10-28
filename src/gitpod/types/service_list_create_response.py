# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ServiceListCreateResponse",
    "Pagination",
    "Service",
    "ServiceMetadata",
    "ServiceMetadataCreator",
    "ServiceSpec",
    "ServiceSpecCommands",
    "ServiceStatus",
]


class Pagination(BaseModel):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)
    """Token passed for retreiving the next set of results.

    Empty if there are no more results
    """


class ServiceMetadataCreator(BaseModel):
    id: Optional[str] = None
    """id is the UUID of the subject"""

    principal: Optional[
        Literal[
            "PRINCIPAL_UNSPECIFIED",
            "PRINCIPAL_ACCOUNT",
            "PRINCIPAL_USER",
            "PRINCIPAL_RUNNER",
            "PRINCIPAL_ENVIRONMENT",
            "PRINCIPAL_SERVICE_ACCOUNT",
        ]
    ] = None
    """Principal is the principal of the subject"""


class ServiceMetadata(BaseModel):
    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """
    A Timestamp represents a point in time independent of any time zone or local
    calendar, encoded as a count of seconds and fractions of seconds at nanosecond
    resolution. The count is relative to an epoch at UTC midnight on January 1,
    1970, in the proleptic Gregorian calendar which extends the Gregorian calendar
    backwards to year one.

    All minutes are 60 seconds long. Leap seconds are "smeared" so that no leap
    second table is needed for interpretation, using a
    [24-hour linear smear](https://developers.google.com/time/smear).

    The range is from 0001-01-01T00:00:00Z to 9999-12-31T23:59:59.999999999Z. By
    restricting to that range, we ensure that we can convert to and from
    [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) date strings.

    # Examples

    Example 1: Compute Timestamp from POSIX `time()`.

         Timestamp timestamp;
         timestamp.set_seconds(time(NULL));
         timestamp.set_nanos(0);

    Example 2: Compute Timestamp from POSIX `gettimeofday()`.

         struct timeval tv;
         gettimeofday(&tv, NULL);

         Timestamp timestamp;
         timestamp.set_seconds(tv.tv_sec);
         timestamp.set_nanos(tv.tv_usec * 1000);

    Example 3: Compute Timestamp from Win32 `GetSystemTimeAsFileTime()`.

         FILETIME ft;
         GetSystemTimeAsFileTime(&ft);
         UINT64 ticks = (((UINT64)ft.dwHighDateTime) << 32) | ft.dwLowDateTime;

         // A Windows tick is 100 nanoseconds. Windows epoch 1601-01-01T00:00:00Z
         // is 11644473600 seconds before Unix epoch 1970-01-01T00:00:00Z.
         Timestamp timestamp;
         timestamp.set_seconds((INT64) ((ticks / 10000000) - 11644473600LL));
         timestamp.set_nanos((INT32) ((ticks % 10000000) * 100));

    Example 4: Compute Timestamp from Java `System.currentTimeMillis()`.

         long millis = System.currentTimeMillis();

         Timestamp timestamp = Timestamp.newBuilder().setSeconds(millis / 1000)
             .setNanos((int) ((millis % 1000) * 1000000)).build();

    Example 5: Compute Timestamp from Java `Instant.now()`.

         Instant now = Instant.now();

         Timestamp timestamp =
             Timestamp.newBuilder().setSeconds(now.getEpochSecond())
                 .setNanos(now.getNano()).build();

    Example 6: Compute Timestamp from current time in Python.

         timestamp = Timestamp()
         timestamp.GetCurrentTime()

    # JSON Mapping

    In JSON format, the Timestamp type is encoded as a string in the
    [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format. That is, the format is
    "{year}-{month}-{day}T{hour}:{min}:{sec}[.{frac_sec}]Z" where {year} is always
    expressed using four digits while {month}, {day}, {hour}, {min}, and {sec} are
    zero-padded to two digits each. The fractional seconds, which can go up to 9
    digits (i.e. up to 1 nanosecond resolution), are optional. The "Z" suffix
    indicates the timezone ("UTC"); the timezone is required. A proto3 JSON
    serializer should always use UTC (as indicated by "Z") when printing the
    Timestamp type and a proto3 JSON parser should be able to accept both UTC and
    other timezones (as indicated by an offset).

    For example, "2017-01-15T01:30:15.01Z" encodes 15.01 seconds past 01:30 UTC on
    January 15, 2017.

    In JavaScript, one can convert a Date object to this format using the standard
    [toISOString()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date/toISOString)
    method. In Python, a standard `datetime.datetime` object can be converted to
    this format using
    [`strftime`](https://docs.python.org/2/library/time.html#time.strftime) with the
    time format spec '%Y-%m-%dT%H:%M:%S.%fZ'. Likewise, in Java, one can use the
    Joda Time's
    [`ISODateTimeFormat.dateTime()`](<http://joda-time.sourceforge.net/apidocs/org/joda/time/format/ISODateTimeFormat.html#dateTime()>)
    to obtain a formatter capable of generating timestamps in this format.
    """

    creator: Optional[ServiceMetadataCreator] = None
    """creator describes the principal who created the service."""

    description: Optional[str] = None
    """description is a user-facing description for the service.

    It can be used to provide context and documentation for the service.
    """

    name: Optional[str] = None
    """name is a user-facing name for the service.

    Unlike the reference, this field is not unique, and not referenced by the
    system. This is a short descriptive name for the service.
    """

    reference: Optional[str] = None
    """
    reference is a user-facing identifier for the service which must be unique on
    the environment. It is used to express dependencies between services, and to
    identify the service in user interactions (e.g. the CLI).
    """

    triggered_by: Optional[List[Union[object, object, object, object]]] = FieldInfo(alias="triggeredBy", default=None)
    """triggered_by is a list of trigger that start the service."""


class ServiceSpecCommands(BaseModel):
    ready: Optional[str] = None
    """
    ready is an optional command that is run repeatedly until it exits with a zero
    exit code. If set, the service will first go into a Starting phase, and then
    into a Running phase once the ready command exits with a zero exit code.
    """

    start: Optional[str] = None
    """
    start is the command to start and run the service. If start exits, the service
    will transition to the following phase:

    - Stopped: if the exit code is 0
    - Failed: if the exit code is not 0 If the stop command is not set, the start
      command will receive a SIGTERM signal when the service is requested to stop.
      If it does not exit within 2 minutes, it will receive a SIGKILL signal.
    """

    stop: Optional[str] = None
    """
    stop is an optional command that runs when the service is requested to stop. If
    set, instead of sending a SIGTERM signal to the start command, the stop command
    will be run. Once the stop command exits, the start command will receive a
    SIGKILL signal. If the stop command exits with a non-zero exit code, the service
    will transition to the Failed phase. If the stop command does not exit within 2
    minutes, a SIGKILL signal will be sent to both the start and stop commands.
    """


class ServiceSpec(BaseModel):
    commands: Optional[ServiceSpecCommands] = None
    """
    commands contains the commands to start, stop and check the readiness of the
    service
    """

    desired_phase: Optional[
        Literal[
            "SERVICE_PHASE_UNSPECIFIED",
            "SERVICE_PHASE_STARTING",
            "SERVICE_PHASE_RUNNING",
            "SERVICE_PHASE_STOPPING",
            "SERVICE_PHASE_STOPPED",
            "SERVICE_PHASE_FAILED",
            "SERVICE_PHASE_DELETED",
        ]
    ] = FieldInfo(alias="desiredPhase", default=None)
    """Phase is the desired phase of the environment"""

    session: Optional[str] = None
    """session should be changed to trigger a restart of the service.

    If a service exits it will not be restarted until the session is changed.
    """

    spec_version: Union[str, float, None] = FieldInfo(alias="specVersion", default=None)
    """version of the spec.

    The value of this field has no semantic meaning (e.g. don't interpret it as as a
    timestamp), but it can be used to impose a partial order. If a.spec_version <
    b.spec_version then a was the spec before b.
    """


class ServiceStatus(BaseModel):
    failure_message: Optional[str] = FieldInfo(alias="failureMessage", default=None)
    """failure_message summarises why the environment failed to operate.

    If this is non-empty the environment has failed to operate and will likely
    transition to a stopped state.
    """

    log_url: Optional[str] = FieldInfo(alias="logUrl", default=None)
    """
    environment_url contains the URL at which the environment can be accessed. This
    field is only set if the environment is running.
    """

    phase: Optional[
        Literal[
            "SERVICE_PHASE_UNSPECIFIED",
            "SERVICE_PHASE_STARTING",
            "SERVICE_PHASE_RUNNING",
            "SERVICE_PHASE_STOPPING",
            "SERVICE_PHASE_STOPPED",
            "SERVICE_PHASE_FAILED",
            "SERVICE_PHASE_DELETED",
        ]
    ] = None
    """
    the phase of an environment is a simple, high-level summary of where the
    environment is in its lifecycle
    """

    session: Optional[str] = None
    """session is the current session of the service."""

    status_version: Union[str, float, None] = FieldInfo(alias="statusVersion", default=None)
    """version of the status update.

    Environment instances themselves are unversioned, but their statuus has
    different versions. The value of this field has no semantic meaning (e.g. don't
    interpret it as as a timestemp), but it can be used to impose a partial order.
    If a.status_version < b.status_version then a was the status before b.
    """


class Service(BaseModel):
    id: Optional[str] = None

    environment_id: Optional[str] = FieldInfo(alias="environmentId", default=None)

    metadata: Optional[ServiceMetadata] = None

    spec: Optional[ServiceSpec] = None

    status: Optional[ServiceStatus] = None


class ServiceListCreateResponse(BaseModel):
    pagination: Optional[Pagination] = None

    services: Optional[List[Service]] = None
