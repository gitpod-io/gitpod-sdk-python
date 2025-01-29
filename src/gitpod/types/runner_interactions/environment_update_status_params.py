# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "EnvironmentUpdateStatusParams",
    "Status",
    "StatusActivitySignal",
    "StatusAutomationsFile",
    "StatusContent",
    "StatusContentGit",
    "StatusContentGitChangedFile",
    "StatusDevcontainer",
    "StatusEnvironmentURLs",
    "StatusEnvironmentURLsPort",
    "StatusEnvironmentURLsSSH",
    "StatusMachine",
    "StatusMachineVersions",
    "StatusRunnerAck",
    "StatusSecret",
    "StatusSSHPublicKey",
]


class EnvironmentUpdateStatusParams(TypedDict, total=False):
    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    environment_id: Annotated[str, PropertyInfo(alias="environmentId")]
    """The environment's ID"""

    runner_id: Annotated[str, PropertyInfo(alias="runnerId")]
    """The runner's identity"""

    status: Status
    """EnvironmentStatus describes an environment status"""

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""


class StatusActivitySignal(TypedDict, total=False):
    source: str
    """
    source of the activity signal, such as "VS Code", "SSH", or "Automations". It
    should be a human-readable string that describes the source of the activity
    signal.
    """

    timestamp: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
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


class StatusAutomationsFile(TypedDict, total=False):
    automations_file_path: Annotated[str, PropertyInfo(alias="automationsFilePath")]
    """
    automations_file_path is the path to the automations file relative to the repo
    root.
    """

    automations_file_presence: Annotated[
        Literal["PRESENCE_UNSPECIFIED", "PRESENCE_ABSENT", "PRESENCE_DISCOVERED", "PRESENCE_SPECIFIED"],
        PropertyInfo(alias="automationsFilePresence"),
    ]
    """
    automations_file_presence indicates how an automations file is present in the
    environment.
    """

    failure_message: Annotated[str, PropertyInfo(alias="failureMessage")]
    """
    failure_message contains the reason the automations file failed to be applied.
    This is only set if the phase is FAILED.
    """

    phase: Literal[
        "CONTENT_PHASE_UNSPECIFIED",
        "CONTENT_PHASE_CREATING",
        "CONTENT_PHASE_INITIALIZING",
        "CONTENT_PHASE_READY",
        "CONTENT_PHASE_UPDATING",
        "CONTENT_PHASE_FAILED",
    ]
    """phase is the current phase of the automations file."""

    session: str
    """
    session is the automations file session that is currently applied in the
    environment.
    """


class StatusContentGitChangedFile(TypedDict, total=False):
    change_type: Annotated[
        Literal[
            "CHANGE_TYPE_UNSPECIFIED",
            "CHANGE_TYPE_ADDED",
            "CHANGE_TYPE_MODIFIED",
            "CHANGE_TYPE_DELETED",
            "CHANGE_TYPE_RENAMED",
            "CHANGE_TYPE_COPIED",
            "CHANGE_TYPE_UPDATED_BUT_UNMERGED",
            "CHANGE_TYPE_UNTRACKED",
        ],
        PropertyInfo(alias="changeType"),
    ]
    """ChangeType is the type of change that happened to the file"""

    path: str
    """path is the path of the file"""


class StatusContentGit(TypedDict, total=False):
    branch: str
    """branch is branch we're currently on"""

    changed_files: Annotated[Iterable[StatusContentGitChangedFile], PropertyInfo(alias="changedFiles")]
    """
    changed_files is an array of changed files in the environment, possibly
    truncated
    """

    clone_url: Annotated[str, PropertyInfo(alias="cloneUrl")]
    """
    clone_url is the repository url as you would pass it to "git clone". Only HTTPS
    clone URLs are supported.
    """

    latest_commit: Annotated[str, PropertyInfo(alias="latestCommit")]
    """latest_commit is the most recent commit on the current branch"""

    total_changed_files: Annotated[int, PropertyInfo(alias="totalChangedFiles")]

    total_unpushed_commits: Annotated[int, PropertyInfo(alias="totalUnpushedCommits")]
    """the total number of unpushed changes"""

    unpushed_commits: Annotated[List[str], PropertyInfo(alias="unpushedCommits")]
    """
    unpushed_commits is an array of unpushed changes in the environment, possibly
    truncated
    """


class StatusContent(TypedDict, total=False):
    content_location_in_machine: Annotated[str, PropertyInfo(alias="contentLocationInMachine")]
    """content_location_in_machine is the location of the content in the machine"""

    failure_message: Annotated[str, PropertyInfo(alias="failureMessage")]
    """failure_message contains the reason the content initialization failed."""

    git: StatusContentGit
    """
    git is the Git working copy status of the environment. Note: this is a
    best-effort field and more often than not will not be present. Its absence does
    not indicate the absence of a working copy.
    """

    phase: Literal[
        "CONTENT_PHASE_UNSPECIFIED",
        "CONTENT_PHASE_CREATING",
        "CONTENT_PHASE_INITIALIZING",
        "CONTENT_PHASE_READY",
        "CONTENT_PHASE_UPDATING",
        "CONTENT_PHASE_FAILED",
    ]
    """phase is the current phase of the environment content"""

    session: str
    """session is the session that is currently active in the environment."""

    warning_message: Annotated[str, PropertyInfo(alias="warningMessage")]
    """warning_message contains warnings, e.g.

    when the content is present but not in the expected state.
    """


class StatusDevcontainer(TypedDict, total=False):
    container_id: Annotated[str, PropertyInfo(alias="containerId")]
    """container_id is the ID of the container."""

    container_name: Annotated[str, PropertyInfo(alias="containerName")]
    """
    container_name is the name of the container that is used to connect to the
    devcontainer
    """

    devcontainerconfig_in_sync: Annotated[bool, PropertyInfo(alias="devcontainerconfigInSync")]
    """devcontainerconfig_in_sync indicates if the devcontainer is up to date w.r.t.

    the devcontainer config file.
    """

    devcontainer_file_path: Annotated[str, PropertyInfo(alias="devcontainerFilePath")]
    """
    devcontainer_file_path is the path to the devcontainer file relative to the repo
    root
    """

    devcontainer_file_presence: Annotated[
        Literal["PRESENCE_UNSPECIFIED", "PRESENCE_GENERATED", "PRESENCE_DISCOVERED", "PRESENCE_SPECIFIED"],
        PropertyInfo(alias="devcontainerFilePresence"),
    ]
    """
    devcontainer_file_presence indicates how the devcontainer file is present in the
    repo.
    """

    failure_message: Annotated[str, PropertyInfo(alias="failureMessage")]
    """failure_message contains the reason the devcontainer failed to operate."""

    phase: Literal["PHASE_UNSPECIFIED", "PHASE_CREATING", "PHASE_RUNNING", "PHASE_STOPPED", "PHASE_FAILED"]
    """phase is the current phase of the devcontainer"""

    remote_user: Annotated[str, PropertyInfo(alias="remoteUser")]
    """remote_user is the user that is used to connect to the devcontainer"""

    remote_workspace_folder: Annotated[str, PropertyInfo(alias="remoteWorkspaceFolder")]
    """
    remote_workspace_folder is the folder that is used to connect to the
    devcontainer
    """

    secrets_in_sync: Annotated[bool, PropertyInfo(alias="secretsInSync")]
    """secrets_in_sync indicates if the secrets are up to date w.r.t.

    the running devcontainer.
    """

    session: str
    """session is the session that is currently active in the devcontainer."""

    warning_message: Annotated[str, PropertyInfo(alias="warningMessage")]
    """warning_message contains warnings, e.g.

    when the devcontainer is present but not in the expected state.
    """


class StatusEnvironmentURLsPort(TypedDict, total=False):
    port: int
    """port is the port number of the environment port"""

    url: str
    """url is the URL at which the environment port can be accessed"""


class StatusEnvironmentURLsSSH(TypedDict, total=False):
    url: str


class StatusEnvironmentURLs(TypedDict, total=False):
    logs: str
    """logs is the URL at which the environment logs can be accessed."""

    ports: Iterable[StatusEnvironmentURLsPort]

    ssh: StatusEnvironmentURLsSSH
    """SSH is the URL at which the environment can be accessed via SSH."""


class StatusMachineVersions(TypedDict, total=False):
    supervisor_commit: Annotated[str, PropertyInfo(alias="supervisorCommit")]

    supervisor_version: Annotated[str, PropertyInfo(alias="supervisorVersion")]


class StatusMachine(TypedDict, total=False):
    failure_message: Annotated[str, PropertyInfo(alias="failureMessage")]
    """failure_message contains the reason the machine failed to operate."""

    phase: Literal[
        "PHASE_UNSPECIFIED",
        "PHASE_CREATING",
        "PHASE_STARTING",
        "PHASE_RUNNING",
        "PHASE_STOPPING",
        "PHASE_STOPPED",
        "PHASE_DELETING",
        "PHASE_DELETED",
    ]
    """phase is the current phase of the environment machine"""

    session: str
    """session is the session that is currently active in the machine."""

    timeout: str
    """timeout contains the reason the environment has timed out.

    If this field is empty, the environment has not timed out.
    """

    versions: StatusMachineVersions
    """versions contains the versions of components in the machine."""

    warning_message: Annotated[str, PropertyInfo(alias="warningMessage")]
    """warning_message contains warnings, e.g.

    when the machine is present but not in the expected state.
    """


class StatusRunnerAck(TypedDict, total=False):
    message: str

    spec_version: Annotated[Union[int, str], PropertyInfo(alias="specVersion")]

    status_code: Annotated[
        Literal[
            "STATUS_CODE_UNSPECIFIED",
            "STATUS_CODE_OK",
            "STATUS_CODE_INVALID_RESOURCE",
            "STATUS_CODE_FAILED_PRECONDITION",
        ],
        PropertyInfo(alias="statusCode"),
    ]


class StatusSecret(TypedDict, total=False):
    failure_message: Annotated[str, PropertyInfo(alias="failureMessage")]
    """failure_message contains the reason the secret failed to be materialize."""

    phase: Literal[
        "CONTENT_PHASE_UNSPECIFIED",
        "CONTENT_PHASE_CREATING",
        "CONTENT_PHASE_INITIALIZING",
        "CONTENT_PHASE_READY",
        "CONTENT_PHASE_UPDATING",
        "CONTENT_PHASE_FAILED",
    ]

    secret_name: Annotated[str, PropertyInfo(alias="secretName")]

    session: str
    """session is the session that is currently active in the environment."""

    warning_message: Annotated[str, PropertyInfo(alias="warningMessage")]
    """warning_message contains warnings, e.g.

    when the secret is present but not in the expected state.
    """


class StatusSSHPublicKey(TypedDict, total=False):
    id: str
    """id is the unique identifier of the public key"""

    phase: Literal[
        "CONTENT_PHASE_UNSPECIFIED",
        "CONTENT_PHASE_CREATING",
        "CONTENT_PHASE_INITIALIZING",
        "CONTENT_PHASE_READY",
        "CONTENT_PHASE_UPDATING",
        "CONTENT_PHASE_FAILED",
    ]
    """phase is the current phase of the public key"""


class Status(TypedDict, total=False):
    activity_signal: Annotated[StatusActivitySignal, PropertyInfo(alias="activitySignal")]
    """EnvironmentActivitySignal used to signal activity for an environment."""

    automations_file: Annotated[StatusAutomationsFile, PropertyInfo(alias="automationsFile")]
    """automations_file contains the status of the automations file."""

    content: StatusContent
    """content contains the status of the environment content."""

    devcontainer: StatusDevcontainer
    """devcontainer contains the status of the devcontainer."""

    environment_urls: Annotated[StatusEnvironmentURLs, PropertyInfo(alias="environmentUrls")]
    """
    environment_url contains the URL at which the environment can be accessed. This
    field is only set if the environment is running.
    """

    failure_message: Annotated[List[str], PropertyInfo(alias="failureMessage")]
    """failure_message summarises why the environment failed to operate.

    If this is non-empty the environment has failed to operate and will likely
    transition to a stopped state.
    """

    machine: StatusMachine
    """machine contains the status of the environment machine"""

    phase: Literal[
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
    """
    the phase of an environment is a simple, high-level summary of where the
    environment is in its lifecycle
    """

    runner_ack: Annotated[StatusRunnerAck, PropertyInfo(alias="runnerAck")]
    """
    RunnerACK is the acknowledgement from the runner that is has received the
    environment spec.
    """

    secrets: Iterable[StatusSecret]
    """secrets contains the status of the environment secrets"""

    ssh_public_keys: Annotated[Iterable[StatusSSHPublicKey], PropertyInfo(alias="sshPublicKeys")]
    """ssh_public_keys contains the status of the environment ssh public keys"""

    status_version: Annotated[Union[int, str], PropertyInfo(alias="statusVersion")]
    """version of the status update.

    Environment instances themselves are unversioned, but their status has different
    versions. The value of this field has no semantic meaning (e.g. don't interpret
    it as as a timestamp), but it can be used to impose a partial order. If
    a.status_version < b.status_version then a was the status before b.
    """

    warning_message: Annotated[List[str], PropertyInfo(alias="warningMessage")]
    """warning_message contains warnings, e.g.

    when the environment is present but not in the expected state.
    """
