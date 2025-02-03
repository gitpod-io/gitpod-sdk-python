# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "TaskStartResponse",
    "TaskExecution",
    "TaskExecutionMetadata",
    "TaskExecutionMetadataCreator",
    "TaskExecutionSpec",
    "TaskExecutionSpecPlan",
    "TaskExecutionSpecPlanStep",
    "TaskExecutionSpecPlanStepUnionMember0",
    "TaskExecutionSpecPlanStepUnionMember0Task",
    "TaskExecutionSpecPlanStepUnionMember0TaskSpec",
    "TaskExecutionSpecPlanStepUnionMember0TaskSpecRunsOn",
    "TaskExecutionSpecPlanStepUnionMember0TaskSpecRunsOnDocker",
    "TaskExecutionSpecPlanStepUnionMember0TaskSpecRunsOnDockerDocker",
    "TaskExecutionSpecPlanStepUnionMember1",
    "TaskExecutionSpecPlanStepUnionMember1Task",
    "TaskExecutionSpecPlanStepUnionMember1TaskSpec",
    "TaskExecutionSpecPlanStepUnionMember1TaskSpecRunsOn",
    "TaskExecutionSpecPlanStepUnionMember1TaskSpecRunsOnDocker",
    "TaskExecutionSpecPlanStepUnionMember1TaskSpecRunsOnDockerDocker",
    "TaskExecutionSpecPlanStepUnionMember2",
    "TaskExecutionSpecPlanStepUnionMember2Task",
    "TaskExecutionSpecPlanStepUnionMember2TaskSpec",
    "TaskExecutionSpecPlanStepUnionMember2TaskSpecRunsOn",
    "TaskExecutionSpecPlanStepUnionMember2TaskSpecRunsOnDocker",
    "TaskExecutionSpecPlanStepUnionMember2TaskSpecRunsOnDockerDocker",
    "TaskExecutionStatus",
    "TaskExecutionStatusStep",
]


class TaskExecutionMetadataCreator(BaseModel):
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


class TaskExecutionMetadata(BaseModel):
    completed_at: Optional[datetime] = FieldInfo(alias="completedAt", default=None)
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

    creator: Optional[TaskExecutionMetadataCreator] = None
    """creator describes the principal who created/started the task run."""

    environment_id: Optional[str] = FieldInfo(alias="environmentId", default=None)
    """environment_id is the ID of the environment in which the task run is executed."""

    started_at: Optional[datetime] = FieldInfo(alias="startedAt", default=None)
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

    started_by: Optional[str] = FieldInfo(alias="startedBy", default=None)
    """started_by describes the trigger that started the task execution."""

    task_id: Optional[str] = FieldInfo(alias="taskId", default=None)
    """task_id is the ID of the main task being executed."""


class TaskExecutionSpecPlanStepUnionMember0TaskSpecRunsOnDockerDocker(BaseModel):
    environment: Optional[List[str]] = None

    image: Optional[str] = None


class TaskExecutionSpecPlanStepUnionMember0TaskSpecRunsOnDocker(BaseModel):
    docker: TaskExecutionSpecPlanStepUnionMember0TaskSpecRunsOnDockerDocker


TaskExecutionSpecPlanStepUnionMember0TaskSpecRunsOn: TypeAlias = Union[
    TaskExecutionSpecPlanStepUnionMember0TaskSpecRunsOnDocker, TaskExecutionSpecPlanStepUnionMember0TaskSpecRunsOnDocker
]


class TaskExecutionSpecPlanStepUnionMember0TaskSpec(BaseModel):
    command: Optional[str] = None
    """command contains the command the task should execute"""

    runs_on: Optional[TaskExecutionSpecPlanStepUnionMember0TaskSpecRunsOn] = FieldInfo(alias="runsOn", default=None)
    """runs_on specifies the environment the task should run on."""


class TaskExecutionSpecPlanStepUnionMember0Task(BaseModel):
    id: Optional[str] = None

    spec: Optional[TaskExecutionSpecPlanStepUnionMember0TaskSpec] = None


class TaskExecutionSpecPlanStepUnionMember0(BaseModel):
    service_id: str = FieldInfo(alias="serviceId")

    id: Optional[str] = None
    """ID is the ID of the execution step"""

    depends_on: Optional[List[str]] = FieldInfo(alias="dependsOn", default=None)

    label: Optional[str] = None

    task: Optional[TaskExecutionSpecPlanStepUnionMember0Task] = None


class TaskExecutionSpecPlanStepUnionMember1TaskSpecRunsOnDockerDocker(BaseModel):
    environment: Optional[List[str]] = None

    image: Optional[str] = None


class TaskExecutionSpecPlanStepUnionMember1TaskSpecRunsOnDocker(BaseModel):
    docker: TaskExecutionSpecPlanStepUnionMember1TaskSpecRunsOnDockerDocker


TaskExecutionSpecPlanStepUnionMember1TaskSpecRunsOn: TypeAlias = Union[
    TaskExecutionSpecPlanStepUnionMember1TaskSpecRunsOnDocker, TaskExecutionSpecPlanStepUnionMember1TaskSpecRunsOnDocker
]


class TaskExecutionSpecPlanStepUnionMember1TaskSpec(BaseModel):
    command: Optional[str] = None
    """command contains the command the task should execute"""

    runs_on: Optional[TaskExecutionSpecPlanStepUnionMember1TaskSpecRunsOn] = FieldInfo(alias="runsOn", default=None)
    """runs_on specifies the environment the task should run on."""


class TaskExecutionSpecPlanStepUnionMember1Task(BaseModel):
    id: Optional[str] = None

    spec: Optional[TaskExecutionSpecPlanStepUnionMember1TaskSpec] = None


class TaskExecutionSpecPlanStepUnionMember1(BaseModel):
    task: TaskExecutionSpecPlanStepUnionMember1Task

    id: Optional[str] = None
    """ID is the ID of the execution step"""

    depends_on: Optional[List[str]] = FieldInfo(alias="dependsOn", default=None)

    label: Optional[str] = None

    service_id: Optional[str] = FieldInfo(alias="serviceId", default=None)


class TaskExecutionSpecPlanStepUnionMember2TaskSpecRunsOnDockerDocker(BaseModel):
    environment: Optional[List[str]] = None

    image: Optional[str] = None


class TaskExecutionSpecPlanStepUnionMember2TaskSpecRunsOnDocker(BaseModel):
    docker: TaskExecutionSpecPlanStepUnionMember2TaskSpecRunsOnDockerDocker


TaskExecutionSpecPlanStepUnionMember2TaskSpecRunsOn: TypeAlias = Union[
    TaskExecutionSpecPlanStepUnionMember2TaskSpecRunsOnDocker, TaskExecutionSpecPlanStepUnionMember2TaskSpecRunsOnDocker
]


class TaskExecutionSpecPlanStepUnionMember2TaskSpec(BaseModel):
    command: Optional[str] = None
    """command contains the command the task should execute"""

    runs_on: Optional[TaskExecutionSpecPlanStepUnionMember2TaskSpecRunsOn] = FieldInfo(alias="runsOn", default=None)
    """runs_on specifies the environment the task should run on."""


class TaskExecutionSpecPlanStepUnionMember2Task(BaseModel):
    id: Optional[str] = None

    spec: Optional[TaskExecutionSpecPlanStepUnionMember2TaskSpec] = None


class TaskExecutionSpecPlanStepUnionMember2(BaseModel):
    id: Optional[str] = None
    """ID is the ID of the execution step"""

    depends_on: Optional[List[str]] = FieldInfo(alias="dependsOn", default=None)

    label: Optional[str] = None

    service_id: Optional[str] = FieldInfo(alias="serviceId", default=None)

    task: Optional[TaskExecutionSpecPlanStepUnionMember2Task] = None


TaskExecutionSpecPlanStep: TypeAlias = Union[
    TaskExecutionSpecPlanStepUnionMember0, TaskExecutionSpecPlanStepUnionMember1, TaskExecutionSpecPlanStepUnionMember2
]


class TaskExecutionSpecPlan(BaseModel):
    steps: Optional[List[TaskExecutionSpecPlanStep]] = None


class TaskExecutionSpec(BaseModel):
    desired_phase: Optional[
        Literal[
            "TASK_EXECUTION_PHASE_UNSPECIFIED",
            "TASK_EXECUTION_PHASE_PENDING",
            "TASK_EXECUTION_PHASE_RUNNING",
            "TASK_EXECUTION_PHASE_SUCCEEDED",
            "TASK_EXECUTION_PHASE_FAILED",
            "TASK_EXECUTION_PHASE_STOPPED",
        ]
    ] = FieldInfo(alias="desiredPhase", default=None)
    """desired_phase is the phase the task execution should be in.

    Used to stop a running task execution early.
    """

    plan: Optional[List[TaskExecutionSpecPlan]] = None
    """plan is a list of groups of steps.

    The steps in a group are executed concurrently, while the groups are executed
    sequentially.

    The order of the groups is the order in which they are executed.
    """


class TaskExecutionStatusStep(BaseModel):
    id: Optional[str] = None
    """ID is the ID of the execution step"""

    failure_message: Optional[str] = FieldInfo(alias="failureMessage", default=None)
    """failure_message summarises why the step failed to operate. If this is non-empty

    the step has failed to operate and will likely transition to a failed state.
    """

    phase: Optional[
        Literal[
            "TASK_EXECUTION_PHASE_UNSPECIFIED",
            "TASK_EXECUTION_PHASE_PENDING",
            "TASK_EXECUTION_PHASE_RUNNING",
            "TASK_EXECUTION_PHASE_SUCCEEDED",
            "TASK_EXECUTION_PHASE_FAILED",
            "TASK_EXECUTION_PHASE_STOPPED",
        ]
    ] = None
    """phase is the current phase of the execution step"""


class TaskExecutionStatus(BaseModel):
    failure_message: Optional[str] = FieldInfo(alias="failureMessage", default=None)
    """failure_message summarises why the task execution failed to operate.

    If this is non-empty

    the task execution has failed to operate and will likely transition to a failed
    state.
    """

    log_url: Optional[str] = FieldInfo(alias="logUrl", default=None)
    """log_url is the URL to the logs of the task's steps.

    If this is empty, the task either has no logs

    or has not yet started.
    """

    phase: Optional[
        Literal[
            "TASK_EXECUTION_PHASE_UNSPECIFIED",
            "TASK_EXECUTION_PHASE_PENDING",
            "TASK_EXECUTION_PHASE_RUNNING",
            "TASK_EXECUTION_PHASE_SUCCEEDED",
            "TASK_EXECUTION_PHASE_FAILED",
            "TASK_EXECUTION_PHASE_STOPPED",
        ]
    ] = None
    """the phase of a task execution represents the aggregated phase of all steps."""

    status_version: Optional[str] = FieldInfo(alias="statusVersion", default=None)
    """version of the status update.

    Task executions themselves are unversioned, but their status has different
    versions. The value of this field has no semantic meaning (e.g. don't interpret
    it as as a timestamp), but it can be used to impose a partial order. If
    a.status_version < b.status_version then a was the status before b.
    """

    steps: Optional[List[TaskExecutionStatusStep]] = None
    """steps provides the status for each individual step of the task execution.

    If a step is missing it

    has not yet started.
    """


class TaskExecution(BaseModel):
    id: Optional[str] = None

    metadata: Optional[TaskExecutionMetadata] = None

    spec: Optional[TaskExecutionSpec] = None

    status: Optional[TaskExecutionStatus] = None


class TaskStartResponse(BaseModel):
    task_execution: Optional[TaskExecution] = FieldInfo(alias="taskExecution", default=None)
