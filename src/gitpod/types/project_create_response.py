# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ProjectCreateResponse",
    "Project",
    "ProjectEnvironmentClass",
    "ProjectEnvironmentClassUnionMember0",
    "ProjectEnvironmentClassUnionMember1",
    "ProjectEnvironmentClassUnionMember2",
    "ProjectInitializer",
    "ProjectInitializerSpec",
    "ProjectInitializerSpecUnionMember0",
    "ProjectInitializerSpecUnionMember0ContextURL",
    "ProjectInitializerSpecUnionMember0Git",
    "ProjectInitializerSpecUnionMember1",
    "ProjectInitializerSpecUnionMember1Git",
    "ProjectInitializerSpecUnionMember1ContextURL",
    "ProjectInitializerSpecUnionMember2",
    "ProjectInitializerSpecUnionMember2ContextURL",
    "ProjectInitializerSpecUnionMember2Git",
    "ProjectMetadata",
    "ProjectMetadataCreator",
    "ProjectUsedBy",
    "ProjectUsedBySubject",
]


class ProjectEnvironmentClassUnionMember0(BaseModel):
    environment_class_id: str = FieldInfo(alias="environmentClassId")
    """Use a fixed environment class on a given Runner.

    This cannot be a local runner's environment class.
    """

    local_runner: Optional[bool] = FieldInfo(alias="localRunner", default=None)
    """Use a local runner for the user"""


class ProjectEnvironmentClassUnionMember1(BaseModel):
    local_runner: bool = FieldInfo(alias="localRunner")
    """Use a local runner for the user"""

    environment_class_id: Optional[str] = FieldInfo(alias="environmentClassId", default=None)
    """Use a fixed environment class on a given Runner.

    This cannot be a local runner's environment class.
    """


class ProjectEnvironmentClassUnionMember2(BaseModel):
    environment_class_id: Optional[str] = FieldInfo(alias="environmentClassId", default=None)
    """Use a fixed environment class on a given Runner.

    This cannot be a local runner's environment class.
    """

    local_runner: Optional[bool] = FieldInfo(alias="localRunner", default=None)
    """Use a local runner for the user"""


ProjectEnvironmentClass: TypeAlias = Union[
    ProjectEnvironmentClassUnionMember0, ProjectEnvironmentClassUnionMember1, ProjectEnvironmentClassUnionMember2
]


class ProjectInitializerSpecUnionMember0ContextURL(BaseModel):
    url: Optional[str] = None
    """url is the URL from which the environment is created"""


class ProjectInitializerSpecUnionMember0Git(BaseModel):
    checkout_location: Optional[str] = FieldInfo(alias="checkoutLocation", default=None)
    """a path relative to the environment root in which the code will be checked out

    to
    """

    clone_target: Optional[str] = FieldInfo(alias="cloneTarget", default=None)
    """the value for the clone target mode - use depends on the target mode"""

    remote_uri: Optional[str] = FieldInfo(alias="remoteUri", default=None)
    """remote_uri is the Git remote origin"""

    target_mode: Optional[
        Literal[
            "CLONE_TARGET_MODE_UNSPECIFIED",
            "CLONE_TARGET_MODE_REMOTE_HEAD",
            "CLONE_TARGET_MODE_REMOTE_COMMIT",
            "CLONE_TARGET_MODE_REMOTE_BRANCH",
            "CLONE_TARGET_MODE_LOCAL_BRANCH",
        ]
    ] = FieldInfo(alias="targetMode", default=None)
    """CloneTargetMode is the target state in which we want to leave a GitEnvironment"""

    upstream_remote_uri: Optional[str] = FieldInfo(alias="upstreamRemoteUri", default=None)
    """upstream_Remote_uri is the fork upstream of a repository"""


class ProjectInitializerSpecUnionMember0(BaseModel):
    context_url: ProjectInitializerSpecUnionMember0ContextURL = FieldInfo(alias="contextUrl")

    git: Optional[ProjectInitializerSpecUnionMember0Git] = None


class ProjectInitializerSpecUnionMember1Git(BaseModel):
    checkout_location: Optional[str] = FieldInfo(alias="checkoutLocation", default=None)
    """a path relative to the environment root in which the code will be checked out

    to
    """

    clone_target: Optional[str] = FieldInfo(alias="cloneTarget", default=None)
    """the value for the clone target mode - use depends on the target mode"""

    remote_uri: Optional[str] = FieldInfo(alias="remoteUri", default=None)
    """remote_uri is the Git remote origin"""

    target_mode: Optional[
        Literal[
            "CLONE_TARGET_MODE_UNSPECIFIED",
            "CLONE_TARGET_MODE_REMOTE_HEAD",
            "CLONE_TARGET_MODE_REMOTE_COMMIT",
            "CLONE_TARGET_MODE_REMOTE_BRANCH",
            "CLONE_TARGET_MODE_LOCAL_BRANCH",
        ]
    ] = FieldInfo(alias="targetMode", default=None)
    """CloneTargetMode is the target state in which we want to leave a GitEnvironment"""

    upstream_remote_uri: Optional[str] = FieldInfo(alias="upstreamRemoteUri", default=None)
    """upstream_Remote_uri is the fork upstream of a repository"""


class ProjectInitializerSpecUnionMember1ContextURL(BaseModel):
    url: Optional[str] = None
    """url is the URL from which the environment is created"""


class ProjectInitializerSpecUnionMember1(BaseModel):
    git: ProjectInitializerSpecUnionMember1Git

    context_url: Optional[ProjectInitializerSpecUnionMember1ContextURL] = FieldInfo(alias="contextUrl", default=None)


class ProjectInitializerSpecUnionMember2ContextURL(BaseModel):
    url: Optional[str] = None
    """url is the URL from which the environment is created"""


class ProjectInitializerSpecUnionMember2Git(BaseModel):
    checkout_location: Optional[str] = FieldInfo(alias="checkoutLocation", default=None)
    """a path relative to the environment root in which the code will be checked out

    to
    """

    clone_target: Optional[str] = FieldInfo(alias="cloneTarget", default=None)
    """the value for the clone target mode - use depends on the target mode"""

    remote_uri: Optional[str] = FieldInfo(alias="remoteUri", default=None)
    """remote_uri is the Git remote origin"""

    target_mode: Optional[
        Literal[
            "CLONE_TARGET_MODE_UNSPECIFIED",
            "CLONE_TARGET_MODE_REMOTE_HEAD",
            "CLONE_TARGET_MODE_REMOTE_COMMIT",
            "CLONE_TARGET_MODE_REMOTE_BRANCH",
            "CLONE_TARGET_MODE_LOCAL_BRANCH",
        ]
    ] = FieldInfo(alias="targetMode", default=None)
    """CloneTargetMode is the target state in which we want to leave a GitEnvironment"""

    upstream_remote_uri: Optional[str] = FieldInfo(alias="upstreamRemoteUri", default=None)
    """upstream_Remote_uri is the fork upstream of a repository"""


class ProjectInitializerSpecUnionMember2(BaseModel):
    context_url: Optional[ProjectInitializerSpecUnionMember2ContextURL] = FieldInfo(alias="contextUrl", default=None)

    git: Optional[ProjectInitializerSpecUnionMember2Git] = None


ProjectInitializerSpec: TypeAlias = Union[
    ProjectInitializerSpecUnionMember0, ProjectInitializerSpecUnionMember1, ProjectInitializerSpecUnionMember2
]


class ProjectInitializer(BaseModel):
    specs: Optional[List[ProjectInitializerSpec]] = None


class ProjectMetadataCreator(BaseModel):
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


class ProjectMetadata(BaseModel):
    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """A Timestamp represents a point in time independent of any time zone or local

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

    creator: Optional[ProjectMetadataCreator] = None
    """creator is the identity of the project creator"""

    name: Optional[str] = None
    """name is the human readable name of the project"""

    organization_id: Optional[str] = FieldInfo(alias="organizationId", default=None)
    """organization_id is the ID of the organization that contains the environment"""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """A Timestamp represents a point in time independent of any time zone or local

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


class ProjectUsedBySubject(BaseModel):
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


class ProjectUsedBy(BaseModel):
    subjects: Optional[List[ProjectUsedBySubject]] = None
    """
    Subjects are the 10 most recent subjects who have used the project to create an
    environment
    """

    total_subjects: Optional[int] = FieldInfo(alias="totalSubjects", default=None)
    """Total number of unique subjects who have used the project"""


class Project(BaseModel):
    environment_class: ProjectEnvironmentClass = FieldInfo(alias="environmentClass")

    id: Optional[str] = None
    """id is the unique identifier for the project"""

    automations_file_path: Optional[str] = FieldInfo(alias="automationsFilePath", default=None)
    """
    automations_file_path is the path to the automations file relative to the repo
    root
    """

    devcontainer_file_path: Optional[str] = FieldInfo(alias="devcontainerFilePath", default=None)
    """
    devcontainer_file_path is the path to the devcontainer file relative to the repo
    root
    """

    initializer: Optional[ProjectInitializer] = None
    """EnvironmentInitializer specifies how an environment is to be initialized"""

    metadata: Optional[ProjectMetadata] = None

    used_by: Optional[ProjectUsedBy] = FieldInfo(alias="usedBy", default=None)


class ProjectCreateResponse(BaseModel):
    project: Optional[Project] = None
