# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.state import State
from .shared.subject import Subject
from .workflow_action import WorkflowAction
from .workflow_trigger_context import WorkflowTriggerContext

__all__ = [
    "WorkflowExecution",
    "Metadata",
    "Spec",
    "SpecTrigger",
    "SpecTriggerPullRequest",
    "SpecTriggerPullRequestRepository",
    "SpecTriggerTime",
    "Status",
    "StatusFailure",
    "StatusFailureRetry",
    "StatusWarning",
    "StatusWarningRetry",
]


class Metadata(BaseModel):
    """WorkflowExecutionMetadata contains workflow execution metadata."""

    creator: Optional[Subject] = None

    executor: Optional[Subject] = None

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

    workflow_id: Optional[str] = FieldInfo(alias="workflowId", default=None)


class SpecTriggerPullRequestRepository(BaseModel):
    """Repository information"""

    clone_url: Optional[str] = FieldInfo(alias="cloneUrl", default=None)

    host: Optional[str] = None

    name: Optional[str] = None

    owner: Optional[str] = None


class SpecTriggerPullRequest(BaseModel):
    """
    PullRequest represents pull request metadata from source control systems.
     This message is used across workflow triggers, executions, and agent contexts
     to maintain consistent PR information throughout the system.
    """

    id: Optional[str] = None
    """Unique identifier from the source system (e.g., "123" for GitHub PR #123)"""

    author: Optional[str] = None
    """Author name as provided by the SCM system"""

    draft: Optional[bool] = None
    """Whether this is a draft pull request"""

    from_branch: Optional[str] = FieldInfo(alias="fromBranch", default=None)
    """Source branch name (the branch being merged from)"""

    repository: Optional[SpecTriggerPullRequestRepository] = None
    """Repository information"""

    state: Optional[State] = None
    """Current state of the pull request"""

    title: Optional[str] = None
    """Pull request title"""

    to_branch: Optional[str] = FieldInfo(alias="toBranch", default=None)
    """Target branch name (the branch being merged into)"""

    url: Optional[str] = None
    """Pull request URL (e.g., "https://github.com/owner/repo/pull/123")"""


class SpecTriggerTime(BaseModel):
    """Time trigger - just the timestamp when it was triggered"""

    triggered_at: Optional[datetime] = FieldInfo(alias="triggeredAt", default=None)
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


class SpecTrigger(BaseModel):
    """WorkflowExecutionTrigger represents a workflow execution trigger instance."""

    context: WorkflowTriggerContext
    """
    Context from the workflow trigger - copied at execution time for immutability.
    This allows the reconciler to create actions without fetching the workflow
    definition.
    """

    manual: Optional[object] = None
    """Manual trigger - empty message since no additional data needed"""

    pull_request: Optional[SpecTriggerPullRequest] = FieldInfo(alias="pullRequest", default=None)
    """
    PullRequest represents pull request metadata from source control systems. This
    message is used across workflow triggers, executions, and agent contexts to
    maintain consistent PR information throughout the system.
    """

    time: Optional[SpecTriggerTime] = None
    """Time trigger - just the timestamp when it was triggered"""


class Spec(BaseModel):
    """WorkflowExecutionSpec contains the specification used for this execution."""

    action: Optional[WorkflowAction] = None
    """WorkflowAction defines the actions to be executed in a workflow."""

    report: Optional[WorkflowAction] = None
    """WorkflowAction defines the actions to be executed in a workflow."""

    trigger: Optional[SpecTrigger] = None
    """WorkflowExecutionTrigger represents a workflow execution trigger instance."""


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
    """WorkflowExecutionStatus contains the current status of a workflow execution."""

    done_action_count: Optional[int] = FieldInfo(alias="doneActionCount", default=None)

    failed_action_count: Optional[int] = FieldInfo(alias="failedActionCount", default=None)

    failures: Optional[List[StatusFailure]] = None
    """
    Structured failures that caused the workflow execution to fail. Provides
    detailed error codes, messages, and retry information.
    """

    pending_action_count: Optional[int] = FieldInfo(alias="pendingActionCount", default=None)

    phase: Optional[
        Literal[
            "WORKFLOW_EXECUTION_PHASE_UNSPECIFIED",
            "WORKFLOW_EXECUTION_PHASE_PENDING",
            "WORKFLOW_EXECUTION_PHASE_RUNNING",
            "WORKFLOW_EXECUTION_PHASE_STOPPING",
            "WORKFLOW_EXECUTION_PHASE_STOPPED",
            "WORKFLOW_EXECUTION_PHASE_DELETING",
            "WORKFLOW_EXECUTION_PHASE_DELETED",
            "WORKFLOW_EXECUTION_PHASE_COMPLETED",
        ]
    ] = None

    running_action_count: Optional[int] = FieldInfo(alias="runningActionCount", default=None)

    stopped_action_count: Optional[int] = FieldInfo(alias="stoppedActionCount", default=None)

    warnings: Optional[List[StatusWarning]] = None
    """
    Structured warnings about the workflow execution. Provides detailed warning
    codes and messages.
    """


class WorkflowExecution(BaseModel):
    """WorkflowExecution represents a workflow execution instance."""

    id: Optional[str] = None

    metadata: Optional[Metadata] = None
    """WorkflowExecutionMetadata contains workflow execution metadata."""

    spec: Optional[Spec] = None
    """WorkflowExecutionSpec contains the specification used for this execution."""

    status: Optional[Status] = None
    """WorkflowExecutionStatus contains the current status of a workflow execution."""
