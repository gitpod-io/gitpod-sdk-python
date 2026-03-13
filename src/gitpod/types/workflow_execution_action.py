# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .workflow_step import WorkflowStep
from .agent_code_context import AgentCodeContext

__all__ = [
    "WorkflowExecutionAction",
    "Metadata",
    "Spec",
    "SpecLimits",
    "Status",
    "StatusFailure",
    "StatusFailureRetry",
    "StatusStepStatus",
    "StatusStepStatusError",
    "StatusStepStatusErrorRetry",
    "StatusWarning",
    "StatusWarningRetry",
]


class Metadata(BaseModel):
    """WorkflowExecutionActionMetadata contains workflow execution action metadata."""

    action_name: Optional[str] = FieldInfo(alias="actionName", default=None)
    """
    Human-readable name for this action based on its context. Examples:
    "gitpod-io/gitpod-next" for repository context, "My Project" for project
    context. Will be empty string for actions created before this field was added.
    """

    finished_at: Optional[datetime] = FieldInfo(alias="finishedAt", default=None)
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

    started_at: Optional[datetime] = FieldInfo(alias="startedAt", default=None)
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

    workflow_execution_id: Optional[str] = FieldInfo(alias="workflowExecutionId", default=None)

    workflow_id: Optional[str] = FieldInfo(alias="workflowId", default=None)


class SpecLimits(BaseModel):
    """PerExecution defines limits per execution action."""

    max_time: Optional[str] = FieldInfo(alias="maxTime", default=None)
    """
    Maximum time allowed for a single execution action. Use standard duration format
    (e.g., "30m" for 30 minutes, "2h" for 2 hours).
    """


class Spec(BaseModel):
    """
    WorkflowExecutionActionSpec contains the specification for this execution action.
    """

    context: Optional[AgentCodeContext] = None
    """
    Context for the execution action - specifies where and how the action executes.
    This is resolved from the workflow trigger context and contains the specific
    project, repository, or agent context for this execution instance.
    """

    limits: Optional[SpecLimits] = None
    """PerExecution defines limits per execution action."""


class StatusFailureRetry(BaseModel):
    """Retry configuration. If not set, the error is considered non-retriable."""

    retriable: Optional[bool] = None
    """Whether the error is retriable."""

    retry_after: Optional[str] = FieldInfo(alias="retryAfter", default=None)
    """
    Suggested duration to wait before retrying. Only meaningful when retriable is
    true.
    """


class StatusFailure(BaseModel):
    """
    WorkflowError provides structured error information for workflow failures.
     This enables the reconciler to make informed retry decisions and the frontend
     to display actionable error messages.
    """

    code: Optional[
        Literal[
            "WORKFLOW_ERROR_CODE_UNSPECIFIED",
            "WORKFLOW_ERROR_CODE_ENVIRONMENT_ERROR",
            "WORKFLOW_ERROR_CODE_AGENT_ERROR",
        ]
    ] = None
    """Error code identifying the type of error."""

    message: Optional[str] = None
    """Human-readable error message."""

    meta: Optional[Dict[str, str]] = None
    """Additional metadata about the error. Common keys include:

    - environment_id: ID of the environment
    - task_id: ID of the task
    - service_id: ID of the service
    - workflow_id: ID of the workflow
    - workflow_execution_id: ID of the workflow execution
    """

    reason: Optional[str] = None
    """
    Reason explaining why the error occurred. Examples: "not_found", "stopped",
    "deleted", "creation_failed", "start_failed"
    """

    retry: Optional[StatusFailureRetry] = None
    """Retry configuration. If not set, the error is considered non-retriable."""


class StatusStepStatusErrorRetry(BaseModel):
    """Retry configuration. If not set, the error is considered non-retriable."""

    retriable: Optional[bool] = None
    """Whether the error is retriable."""

    retry_after: Optional[str] = FieldInfo(alias="retryAfter", default=None)
    """
    Suggested duration to wait before retrying. Only meaningful when retriable is
    true.
    """


class StatusStepStatusError(BaseModel):
    """
    Structured error that caused the step to fail.
     Provides detailed error code, message, and retry information.
    """

    code: Optional[
        Literal[
            "WORKFLOW_ERROR_CODE_UNSPECIFIED",
            "WORKFLOW_ERROR_CODE_ENVIRONMENT_ERROR",
            "WORKFLOW_ERROR_CODE_AGENT_ERROR",
        ]
    ] = None
    """Error code identifying the type of error."""

    message: Optional[str] = None
    """Human-readable error message."""

    meta: Optional[Dict[str, str]] = None
    """Additional metadata about the error. Common keys include:

    - environment_id: ID of the environment
    - task_id: ID of the task
    - service_id: ID of the service
    - workflow_id: ID of the workflow
    - workflow_execution_id: ID of the workflow execution
    """

    reason: Optional[str] = None
    """
    Reason explaining why the error occurred. Examples: "not_found", "stopped",
    "deleted", "creation_failed", "start_failed"
    """

    retry: Optional[StatusStepStatusErrorRetry] = None
    """Retry configuration. If not set, the error is considered non-retriable."""


class StatusStepStatus(BaseModel):
    """
    WorkflowExecutionActionStepStatus represents the status of a single step execution.
    """

    error: Optional[StatusStepStatusError] = None
    """
    Structured error that caused the step to fail. Provides detailed error code,
    message, and retry information.
    """

    finished_at: Optional[datetime] = FieldInfo(alias="finishedAt", default=None)
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

    phase: Optional[
        Literal[
            "STEP_PHASE_UNSPECIFIED",
            "STEP_PHASE_PENDING",
            "STEP_PHASE_RUNNING",
            "STEP_PHASE_DONE",
            "STEP_PHASE_FAILED",
            "STEP_PHASE_CANCELLED",
        ]
    ] = None

    started_at: Optional[datetime] = FieldInfo(alias="startedAt", default=None)
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

    step: Optional[WorkflowStep] = None
    """
    The step definition captured at execution time for immutability. This ensures
    the UI shows the correct step even if the workflow definition changes.
    """

    step_index: Optional[int] = FieldInfo(alias="stepIndex", default=None)
    """Index of the step in the workflow action steps array"""


class StatusWarningRetry(BaseModel):
    """Retry configuration. If not set, the error is considered non-retriable."""

    retriable: Optional[bool] = None
    """Whether the error is retriable."""

    retry_after: Optional[str] = FieldInfo(alias="retryAfter", default=None)
    """
    Suggested duration to wait before retrying. Only meaningful when retriable is
    true.
    """


class StatusWarning(BaseModel):
    """
    WorkflowError provides structured error information for workflow failures.
     This enables the reconciler to make informed retry decisions and the frontend
     to display actionable error messages.
    """

    code: Optional[
        Literal[
            "WORKFLOW_ERROR_CODE_UNSPECIFIED",
            "WORKFLOW_ERROR_CODE_ENVIRONMENT_ERROR",
            "WORKFLOW_ERROR_CODE_AGENT_ERROR",
        ]
    ] = None
    """Error code identifying the type of error."""

    message: Optional[str] = None
    """Human-readable error message."""

    meta: Optional[Dict[str, str]] = None
    """Additional metadata about the error. Common keys include:

    - environment_id: ID of the environment
    - task_id: ID of the task
    - service_id: ID of the service
    - workflow_id: ID of the workflow
    - workflow_execution_id: ID of the workflow execution
    """

    reason: Optional[str] = None
    """
    Reason explaining why the error occurred. Examples: "not_found", "stopped",
    "deleted", "creation_failed", "start_failed"
    """

    retry: Optional[StatusWarningRetry] = None
    """Retry configuration. If not set, the error is considered non-retriable."""


class Status(BaseModel):
    """
    WorkflowExecutionActionStatus contains the current status of a workflow execution action.
    """

    agent_execution_id: Optional[str] = FieldInfo(alias="agentExecutionId", default=None)

    environment_id: Optional[str] = FieldInfo(alias="environmentId", default=None)

    failures: Optional[List[StatusFailure]] = None
    """
    Structured failures that caused the workflow execution action to fail. Provides
    detailed error codes, messages, and retry information.
    """

    phase: Optional[
        Literal[
            "WORKFLOW_EXECUTION_ACTION_PHASE_UNSPECIFIED",
            "WORKFLOW_EXECUTION_ACTION_PHASE_PENDING",
            "WORKFLOW_EXECUTION_ACTION_PHASE_RUNNING",
            "WORKFLOW_EXECUTION_ACTION_PHASE_STOPPING",
            "WORKFLOW_EXECUTION_ACTION_PHASE_STOPPED",
            "WORKFLOW_EXECUTION_ACTION_PHASE_DELETING",
            "WORKFLOW_EXECUTION_ACTION_PHASE_DELETED",
            "WORKFLOW_EXECUTION_ACTION_PHASE_DONE",
        ]
    ] = None
    """WorkflowExecutionActionPhase defines the phases of workflow execution action."""

    step_statuses: Optional[List[StatusStepStatus]] = FieldInfo(alias="stepStatuses", default=None)
    """Step-level progress tracking"""

    warnings: Optional[List[StatusWarning]] = None
    """
    Structured warnings about the workflow execution action. Provides detailed
    warning codes and messages.
    """


class WorkflowExecutionAction(BaseModel):
    """WorkflowExecutionAction represents a workflow execution action instance."""

    id: Optional[str] = None

    metadata: Optional[Metadata] = None
    """WorkflowExecutionActionMetadata contains workflow execution action metadata."""

    spec: Optional[Spec] = None
    """
    WorkflowExecutionActionSpec contains the specification for this execution
    action.
    """

    status: Optional[Status] = None
    """
    WorkflowExecutionActionStatus contains the current status of a workflow
    execution action.
    """
