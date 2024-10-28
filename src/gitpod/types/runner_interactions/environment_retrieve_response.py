# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "EnvironmentRetrieveResponse",
    "Environment",
    "EnvironmentMetadata",
    "EnvironmentMetadataCreator",
    "EnvironmentSpec",
    "EnvironmentSpecAutomationsFile",
    "EnvironmentSpecContent",
    "EnvironmentSpecContentInitializer",
    "EnvironmentSpecDevcontainer",
    "EnvironmentSpecMachine",
    "EnvironmentSpecPort",
    "EnvironmentSpecSSHPublicKey",
    "EnvironmentSpecTimeout",
]


class EnvironmentMetadataCreator(BaseModel):
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


class EnvironmentMetadata(BaseModel):
    annotations: Optional[Dict[str, str]] = None
    """
    annotations are key/value pairs that gets attached to the environment.
    +internal - not yet implemented
    """

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

    creator: Optional[EnvironmentMetadataCreator] = None
    """creator is the identity of the creator of the environment"""

    name: Optional[str] = None
    """name is the name of the environment as specified by the user"""

    organization_id: Optional[str] = FieldInfo(alias="organizationId", default=None)
    """organization_id is the ID of the organization that contains the environment"""

    original_context_url: Optional[str] = FieldInfo(alias="originalContextUrl", default=None)
    """
    original_context_url is the normalized URL from which the environment was
    created
    """

    project_id: Optional[str] = FieldInfo(alias="projectId", default=None)
    """
    If the Environment was started from a project, the project_id will reference the
    project.
    """

    runner_id: Optional[str] = FieldInfo(alias="runnerId", default=None)
    """Runner is the ID of the runner that runs this environment."""


class EnvironmentSpecAutomationsFile(BaseModel):
    automations_file_path: Optional[str] = FieldInfo(alias="automationsFilePath", default=None)
    """
    automations_file_path is the path to the automations file that is applied in the
    environment, relative to the repo root.
    """

    session: Optional[str] = None


class EnvironmentSpecContentInitializer(BaseModel):
    specs: Optional[List[Union[object, object, object]]] = None


class EnvironmentSpecContent(BaseModel):
    git_email: Optional[str] = FieldInfo(alias="gitEmail", default=None)
    """The Git email address"""

    git_username: Optional[str] = FieldInfo(alias="gitUsername", default=None)
    """The Git username"""

    initializer: Optional[EnvironmentSpecContentInitializer] = None
    """EnvironmentInitializer specifies how an environment is to be initialized"""

    session: Optional[str] = None


class EnvironmentSpecDevcontainer(BaseModel):
    devcontainer_file_path: Optional[str] = FieldInfo(alias="devcontainerFilePath", default=None)
    """
    devcontainer_file_path is the path to the devcontainer file relative to the repo
    root
    """

    session: Optional[str] = None


class EnvironmentSpecMachine(BaseModel):
    class_: Optional[str] = FieldInfo(alias="class", default=None)
    """Class denotes the class of the environment we ought to start"""

    session: Optional[str] = None


class EnvironmentSpecPort(BaseModel):
    admission: Optional[
        Literal["ADMISSION_LEVEL_UNSPECIFIED", "ADMISSION_LEVEL_OWNER_ONLY", "ADMISSION_LEVEL_EVERYONE"]
    ] = None
    """Admission level describes who can access an environment instance and its ports."""

    name: Optional[str] = None
    """name of this port"""

    port: Optional[int] = None
    """port number"""


class EnvironmentSpecSSHPublicKey(BaseModel):
    id: Optional[str] = None
    """id is the unique identifier of the public key"""

    value: Optional[str] = None
    """value is the actual public key in the public key file format"""


class EnvironmentSpecTimeout(BaseModel):
    disconnected: Optional[str] = None
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


class EnvironmentSpec(BaseModel):
    admission: Optional[
        Literal["ADMISSION_LEVEL_UNSPECIFIED", "ADMISSION_LEVEL_OWNER_ONLY", "ADMISSION_LEVEL_EVERYONE"]
    ] = None
    """Admission level describes who can access an environment instance and its ports."""

    automations_file: Optional[EnvironmentSpecAutomationsFile] = FieldInfo(alias="automationsFile", default=None)
    """automations_file is the automations file spec of the environment"""

    content: Optional[EnvironmentSpecContent] = None
    """content is the content spec of the environment"""

    desired_phase: Optional[
        Literal[
            "ENVIRONMENT_PHASE_UNSPECIFIED",
            "ENVIRONMENT_PHASE_CREATING",
            "ENVIRONMENT_PHASE_STARTING",
            "ENVIRONMENT_PHASE_RUNNING",
            "ENVIRONMENT_PHASE_UPDATING",
            "ENVIRONMENT_PHASE_STOPPING",
            "ENVIRONMENT_PHASE_STOPPED",
            "ENVIRONMENT_PHASE_DELETING",
            "ENVIRONMENT_PHASE_DELETED",
        ]
    ] = FieldInfo(alias="desiredPhase", default=None)
    """Phase is the desired phase of the environment"""

    devcontainer: Optional[EnvironmentSpecDevcontainer] = None
    """devcontainer is the devcontainer spec of the environment"""

    machine: Optional[EnvironmentSpecMachine] = None
    """machine is the machine spec of the environment"""

    ports: Optional[List[EnvironmentSpecPort]] = None
    """ports is the set of ports which ought to be exposed to the internet"""

    secrets: Optional[List[Union[object, object, object, object]]] = None
    """secrets are confidential data that is mounted into the environment"""

    spec_version: Union[str, float, None] = FieldInfo(alias="specVersion", default=None)
    """version of the spec.

    The value of this field has no semantic meaning (e.g. don't interpret it as as a
    timestamp), but it can be used to impose a partial order. If a.spec_version <
    b.spec_version then a was the spec before b.
    """

    ssh_public_keys: Optional[List[EnvironmentSpecSSHPublicKey]] = FieldInfo(alias="sshPublicKeys", default=None)
    """ssh_public_keys are the public keys used to ssh into the environment"""

    timeout: Optional[EnvironmentSpecTimeout] = None
    """Timeout configures the environment timeout"""


class Environment(BaseModel):
    id: Optional[str] = None
    """ID is a unique identifier of this environment.

    No other environment with the same name must be managed by this environment
    manager
    """

    environment_access_token: Optional[str] = FieldInfo(alias="environmentAccessToken", default=None)
    """The environment's access token"""

    metadata: Optional[EnvironmentMetadata] = None
    """
    EnvironmentMetadata is data associated with an environment that's required for
    other parts of the system to function
    """

    spec: Optional[EnvironmentSpec] = None
    """
    EnvironmentSpec specifies the configuration of an environment for an environment
    start
    """


class EnvironmentRetrieveResponse(BaseModel):
    environment: Optional[Environment] = None
