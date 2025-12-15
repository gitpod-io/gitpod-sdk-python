# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .agent_mode import AgentMode
from .shared.subject import Subject
from .agent_code_context import AgentCodeContext

__all__ = [
    "AgentExecution",
    "Metadata",
    "Spec",
    "SpecLimits",
    "Status",
    "StatusCurrentOperation",
    "StatusCurrentOperationLlm",
    "StatusCurrentOperationToolUse",
    "StatusOutputs",
    "StatusUsedEnvironment",
]


class Metadata(BaseModel):
    """
    Metadata is data associated with this agent that's required for other
     parts of Gitpod to function
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

    creator: Optional[Subject] = None

    description: Optional[str] = None

    name: Optional[str] = None

    role: Optional[
        Literal["AGENT_EXECUTION_ROLE_UNSPECIFIED", "AGENT_EXECUTION_ROLE_DEFAULT", "AGENT_EXECUTION_ROLE_WORKFLOW"]
    ] = None
    """role is the role of the agent execution"""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
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

    workflow_action_id: Optional[str] = FieldInfo(alias="workflowActionId", default=None)
    """
    workflow_action_id is set when this agent execution was created as part of a
    workflow. Used to correlate agent executions with their parent workflow
    execution action.
    """


class SpecLimits(BaseModel):
    max_input_tokens: Optional[str] = FieldInfo(alias="maxInputTokens", default=None)

    max_iterations: Optional[str] = FieldInfo(alias="maxIterations", default=None)

    max_output_tokens: Optional[str] = FieldInfo(alias="maxOutputTokens", default=None)


class Spec(BaseModel):
    """
    Spec is the configuration of the agent that's required for the
     runner to start the agent
    """

    agent_id: Optional[str] = FieldInfo(alias="agentId", default=None)

    code_context: Optional[AgentCodeContext] = FieldInfo(alias="codeContext", default=None)

    desired_phase: Optional[
        Literal["PHASE_UNSPECIFIED", "PHASE_PENDING", "PHASE_RUNNING", "PHASE_WAITING_FOR_INPUT", "PHASE_STOPPED"]
    ] = FieldInfo(alias="desiredPhase", default=None)
    """desired_phase is the desired phase of the agent run"""

    limits: Optional[SpecLimits] = None

    mode: Optional[AgentMode] = None
    """mode is the operational mode for this agent execution"""

    session: Optional[str] = None

    spec_version: Optional[str] = FieldInfo(alias="specVersion", default=None)
    """version of the spec.

    The value of this field has no semantic meaning (e.g. don't interpret it as as a
    timestamp), but it can be used to impose a partial order. If a.spec_version <
    b.spec_version then a was the spec before b.
    """


class StatusCurrentOperationLlm(BaseModel):
    complete: Optional[bool] = None


class StatusCurrentOperationToolUse(BaseModel):
    complete: Optional[bool] = None

    tool_name: Optional[str] = FieldInfo(alias="toolName", default=None)


class StatusCurrentOperation(BaseModel):
    """current_operation is the current operation of the agent execution."""

    llm: Optional[StatusCurrentOperationLlm] = None

    retries: Optional[str] = None
    """retries is the number of times the agent run has retried one or more steps"""

    session: Optional[str] = None

    tool_use: Optional[StatusCurrentOperationToolUse] = FieldInfo(alias="toolUse", default=None)


class StatusOutputs(BaseModel):
    bool_value: Optional[bool] = FieldInfo(alias="boolValue", default=None)

    float_value: Optional[float] = FieldInfo(alias="floatValue", default=None)

    int_value: Optional[str] = FieldInfo(alias="intValue", default=None)

    string_value: Optional[str] = FieldInfo(alias="stringValue", default=None)


class StatusUsedEnvironment(BaseModel):
    created_by_agent: Optional[bool] = FieldInfo(alias="createdByAgent", default=None)

    environment_id: Optional[str] = FieldInfo(alias="environmentId", default=None)


class Status(BaseModel):
    """Status is the current status of the agent"""

    cached_creation_tokens_used: Optional[str] = FieldInfo(alias="cachedCreationTokensUsed", default=None)

    cached_input_tokens_used: Optional[str] = FieldInfo(alias="cachedInputTokensUsed", default=None)

    context_window_length: Optional[str] = FieldInfo(alias="contextWindowLength", default=None)

    conversation_url: Optional[str] = FieldInfo(alias="conversationUrl", default=None)
    """
    conversation_url is the URL to the conversation (all messages exchanged between
    the agent and the user) of the agent run.
    """

    current_activity: Optional[str] = FieldInfo(alias="currentActivity", default=None)
    """current_activity is the current activity description of the agent execution."""

    current_operation: Optional[StatusCurrentOperation] = FieldInfo(alias="currentOperation", default=None)
    """current_operation is the current operation of the agent execution."""

    failure_message: Optional[str] = FieldInfo(alias="failureMessage", default=None)
    """failure_message contains the reason the agent run failed to operate."""

    failure_reason: Optional[
        Literal[
            "AGENT_EXECUTION_FAILURE_REASON_UNSPECIFIED",
            "AGENT_EXECUTION_FAILURE_REASON_ENVIRONMENT",
            "AGENT_EXECUTION_FAILURE_REASON_SERVICE",
            "AGENT_EXECUTION_FAILURE_REASON_LLM_INTEGRATION",
            "AGENT_EXECUTION_FAILURE_REASON_INTERNAL",
            "AGENT_EXECUTION_FAILURE_REASON_AGENT_EXECUTION",
        ]
    ] = FieldInfo(alias="failureReason", default=None)
    """failure_reason contains a structured reason code for the failure."""

    input_tokens_used: Optional[str] = FieldInfo(alias="inputTokensUsed", default=None)

    iterations: Optional[str] = None

    judgement: Optional[str] = None
    """judgement is the judgement of the agent run produced by the judgement prompt."""

    outputs: Optional[Dict[str, StatusOutputs]] = None
    """
    outputs is a map of key-value pairs that can be set by the agent during
    execution. Similar to task execution outputs, but with typed values for
    structured data.
    """

    output_tokens_used: Optional[str] = FieldInfo(alias="outputTokensUsed", default=None)

    phase: Optional[
        Literal["PHASE_UNSPECIFIED", "PHASE_PENDING", "PHASE_RUNNING", "PHASE_WAITING_FOR_INPUT", "PHASE_STOPPED"]
    ] = None

    session: Optional[str] = None

    status_version: Optional[str] = FieldInfo(alias="statusVersion", default=None)
    """version of the status.

    The value of this field has no semantic meaning (e.g. don't interpret it as as a
    timestamp), but it can be used to impose a partial order. If a.status_version <
    b.status_version then a was the status before b.
    """

    supported_model: Optional[
        Literal[
            "SUPPORTED_MODEL_UNSPECIFIED",
            "SUPPORTED_MODEL_SONNET_3_5",
            "SUPPORTED_MODEL_SONNET_3_7",
            "SUPPORTED_MODEL_SONNET_3_7_EXTENDED",
            "SUPPORTED_MODEL_SONNET_4",
            "SUPPORTED_MODEL_SONNET_4_EXTENDED",
            "SUPPORTED_MODEL_SONNET_4_5",
            "SUPPORTED_MODEL_SONNET_4_5_EXTENDED",
            "SUPPORTED_MODEL_OPUS_4",
            "SUPPORTED_MODEL_OPUS_4_EXTENDED",
            "SUPPORTED_MODEL_OPUS_4_5",
            "SUPPORTED_MODEL_OPUS_4_5_EXTENDED",
            "SUPPORTED_MODEL_OPENAI_4O",
            "SUPPORTED_MODEL_OPENAI_4O_MINI",
            "SUPPORTED_MODEL_OPENAI_O1",
            "SUPPORTED_MODEL_OPENAI_O1_MINI",
        ]
    ] = FieldInfo(alias="supportedModel", default=None)
    """supported_model is the LLM model being used by the agent execution."""

    transcript_url: Optional[str] = FieldInfo(alias="transcriptUrl", default=None)
    """
    transcript_url is the URL to the LLM transcript (all messages exchanged between
    the agent and the LLM) of the agent run.
    """

    used_environments: Optional[List[StatusUsedEnvironment]] = FieldInfo(alias="usedEnvironments", default=None)
    """
    used_environments is the list of environments that were used by the agent
    execution.
    """

    warning_message: Optional[str] = FieldInfo(alias="warningMessage", default=None)
    """warning_message contains warnings, e.g. when the LLM is overloaded."""


class AgentExecution(BaseModel):
    id: Optional[str] = None
    """ID is a unique identifier of this agent run.

    No other agent run with the same name must be managed by this agent manager
    """

    metadata: Optional[Metadata] = None
    """
    Metadata is data associated with this agent that's required for other parts of
    Gitpod to function
    """

    spec: Optional[Spec] = None
    """
    Spec is the configuration of the agent that's required for the runner to start
    the agent
    """

    status: Optional[Status] = None
    """Status is the current status of the agent"""
