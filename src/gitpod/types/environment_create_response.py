# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "EnvironmentCreateResponse",
    "Environment",
    "EnvironmentMetadata",
    "EnvironmentMetadataCreator",
    "EnvironmentSpec",
    "EnvironmentSpecAutomationsFile",
    "EnvironmentSpecContent",
    "EnvironmentSpecContentInitializer",
    "EnvironmentSpecContentInitializerSpec",
    "EnvironmentSpecDevcontainer",
    "EnvironmentSpecMachine",
    "EnvironmentSpecPort",
    "EnvironmentSpecSecret",
    "EnvironmentSpecSSHPublicKey",
    "EnvironmentSpecTimeout",
    "EnvironmentStatus",
    "EnvironmentStatusAutomationsFile",
    "EnvironmentStatusContent",
    "EnvironmentStatusContentGit",
    "EnvironmentStatusContentGitChangedFile",
    "EnvironmentStatusDevcontainer",
    "EnvironmentStatusEnvironmentURLs",
    "EnvironmentStatusEnvironmentURLsPort",
    "EnvironmentStatusEnvironmentURLsSSH",
    "EnvironmentStatusMachine",
    "EnvironmentStatusMachineVersions",
    "EnvironmentStatusRunnerAck",
    "EnvironmentStatusSecret",
    "EnvironmentStatusSSHPublicKey",
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


class EnvironmentSpecContentInitializerSpec:
    pass


class EnvironmentSpecContentInitializer(BaseModel):
    specs: Optional[List[EnvironmentSpecContentInitializerSpec]] = None


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


class EnvironmentSpecSecret:
    pass


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

    secrets: Optional[List[EnvironmentSpecSecret]] = None
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


class EnvironmentStatusAutomationsFile(BaseModel):
    automations_file_path: Optional[str] = FieldInfo(alias="automationsFilePath", default=None)
    """
    automations_file_path is the path to the automations file relative to the repo
    root.
    """

    automations_file_presence: Optional[
        Literal["PRESENCE_UNSPECIFIED", "PRESENCE_ABSENT", "PRESENCE_DISCOVERED", "PRESENCE_SPECIFIED"]
    ] = FieldInfo(alias="automationsFilePresence", default=None)
    """
    automations_file_presence indicates how an automations file is present in the
    environment.
    """

    failure_message: Optional[str] = FieldInfo(alias="failureMessage", default=None)
    """
    failure_message contains the reason the automations file failed to be applied.
    This is only set if the phase is FAILED.
    """

    phase: Optional[
        Literal[
            "CONTENT_PHASE_UNSPECIFIED",
            "CONTENT_PHASE_CREATING",
            "CONTENT_PHASE_INITIALIZING",
            "CONTENT_PHASE_READY",
            "CONTENT_PHASE_UPDATING",
            "CONTENT_PHASE_FAILED",
        ]
    ] = None
    """phase is the current phase of the automations file."""

    session: Optional[str] = None
    """
    session is the automations file session that is currently applied in the
    environment.
    """


class EnvironmentStatusContentGitChangedFile(BaseModel):
    change_type: Optional[
        Literal[
            "CHANGE_TYPE_UNSPECIFIED",
            "CHANGE_TYPE_ADDED",
            "CHANGE_TYPE_MODIFIED",
            "CHANGE_TYPE_DELETED",
            "CHANGE_TYPE_RENAMED",
            "CHANGE_TYPE_COPIED",
            "CHANGE_TYPE_UPDATED_BUT_UNMERGED",
            "CHANGE_TYPE_UNTRACKED",
        ]
    ] = FieldInfo(alias="changeType", default=None)
    """ChangeType is the type of change that happened to the file"""

    path: Optional[str] = None
    """path is the path of the file"""


class EnvironmentStatusContentGit(BaseModel):
    branch: Optional[str] = None
    """branch is branch we're currently on"""

    changed_files: Optional[List[EnvironmentStatusContentGitChangedFile]] = FieldInfo(
        alias="changedFiles", default=None
    )
    """
    changed_files is an array of changed files in the environment, possibly
    truncated
    """

    clone_url: Optional[str] = FieldInfo(alias="cloneUrl", default=None)
    """
    clone_url is the repository url as you would pass it to "git clone". Only HTTPS
    clone URLs are supported.
    """

    latest_commit: Optional[str] = FieldInfo(alias="latestCommit", default=None)
    """latest_commit is the most recent commit on the current branch"""

    total_changed_files: Optional[int] = FieldInfo(alias="totalChangedFiles", default=None)

    total_unpushed_commits: Optional[int] = FieldInfo(alias="totalUnpushedCommits", default=None)
    """the total number of unpushed changes"""

    unpushed_commits: Optional[List[str]] = FieldInfo(alias="unpushedCommits", default=None)
    """
    unpushed_commits is an array of unpushed changes in the environment, possibly
    truncated
    """


class EnvironmentStatusContent(BaseModel):
    content_location_in_machine: Optional[str] = FieldInfo(alias="contentLocationInMachine", default=None)
    """content_location_in_machine is the location of the content in the machine"""

    failure_message: Optional[str] = FieldInfo(alias="failureMessage", default=None)
    """failure_message contains the reason the content initialization failed."""

    git: Optional[EnvironmentStatusContentGit] = None
    """
    git is the Git working copy status of the environment. Note: this is a
    best-effort field and more often than not will not be present. Its absence does
    not indicate the absence of a working copy.
    """

    phase: Optional[
        Literal[
            "CONTENT_PHASE_UNSPECIFIED",
            "CONTENT_PHASE_CREATING",
            "CONTENT_PHASE_INITIALIZING",
            "CONTENT_PHASE_READY",
            "CONTENT_PHASE_UPDATING",
            "CONTENT_PHASE_FAILED",
        ]
    ] = None
    """phase is the current phase of the environment content"""

    session: Optional[str] = None
    """session is the session that is currently active in the environment."""

    warning_message: Optional[str] = FieldInfo(alias="warningMessage", default=None)
    """warning_message contains warnings, e.g.

    when the content is present but not in the expected state.
    """


class EnvironmentStatusDevcontainer(BaseModel):
    container_id: Optional[str] = FieldInfo(alias="containerId", default=None)
    """container_id is the ID of the container."""

    container_name: Optional[str] = FieldInfo(alias="containerName", default=None)
    """
    container_name is the name of the container that is used to connect to the
    devcontainer
    """

    devcontainerconfig_in_sync: Optional[bool] = FieldInfo(alias="devcontainerconfigInSync", default=None)
    """devcontainerconfig_in_sync indicates if the devcontainer is up to date w.r.t.

    the devcontainer config file.
    """

    devcontainer_file_path: Optional[str] = FieldInfo(alias="devcontainerFilePath", default=None)
    """
    devcontainer_file_path is the path to the devcontainer file relative to the repo
    root
    """

    devcontainer_file_presence: Optional[
        Literal["PRESENCE_UNSPECIFIED", "PRESENCE_GENERATED", "PRESENCE_DISCOVERED", "PRESENCE_SPECIFIED"]
    ] = FieldInfo(alias="devcontainerFilePresence", default=None)
    """
    devcontainer_file_presence indicates how the devcontainer file is present in the
    repo.
    """

    failure_message: Optional[str] = FieldInfo(alias="failureMessage", default=None)
    """failure_message contains the reason the devcontainer failed to operate."""

    phase: Optional[
        Literal["PHASE_UNSPECIFIED", "PHASE_CREATING", "PHASE_RUNNING", "PHASE_STOPPED", "PHASE_FAILED"]
    ] = None
    """phase is the current phase of the devcontainer"""

    remote_user: Optional[str] = FieldInfo(alias="remoteUser", default=None)
    """remote_user is the user that is used to connect to the devcontainer"""

    remote_workspace_folder: Optional[str] = FieldInfo(alias="remoteWorkspaceFolder", default=None)
    """
    remote_workspace_folder is the folder that is used to connect to the
    devcontainer
    """

    secrets_in_sync: Optional[bool] = FieldInfo(alias="secretsInSync", default=None)
    """secrets_in_sync indicates if the secrets are up to date w.r.t.

    the running devcontainer.
    """

    session: Optional[str] = None
    """session is the session that is currently active in the devcontainer."""

    warning_message: Optional[str] = FieldInfo(alias="warningMessage", default=None)
    """warning_message contains warnings, e.g.

    when the devcontainer is present but not in the expected state.
    """


class EnvironmentStatusEnvironmentURLsPort(BaseModel):
    port: Optional[int] = None
    """port is the port number of the environment port"""

    url: Optional[str] = None
    """url is the URL at which the environment port can be accessed"""


class EnvironmentStatusEnvironmentURLsSSH(BaseModel):
    url: Optional[str] = None


class EnvironmentStatusEnvironmentURLs(BaseModel):
    logs: Optional[str] = None
    """logs is the URL at which the environment logs can be accessed."""

    ports: Optional[List[EnvironmentStatusEnvironmentURLsPort]] = None

    ssh: Optional[EnvironmentStatusEnvironmentURLsSSH] = None
    """SSH is the URL at which the environment can be accessed via SSH."""


class EnvironmentStatusMachineVersions(BaseModel):
    supervisor_commit: Optional[str] = FieldInfo(alias="supervisorCommit", default=None)

    supervisor_version: Optional[str] = FieldInfo(alias="supervisorVersion", default=None)


class EnvironmentStatusMachine(BaseModel):
    failure_message: Optional[str] = FieldInfo(alias="failureMessage", default=None)
    """failure_message contains the reason the machine failed to operate."""

    phase: Optional[
        Literal[
            "PHASE_UNSPECIFIED",
            "PHASE_CREATING",
            "PHASE_STARTING",
            "PHASE_RUNNING",
            "PHASE_STOPPING",
            "PHASE_STOPPED",
            "PHASE_DELETING",
            "PHASE_DELETED",
        ]
    ] = None
    """phase is the current phase of the environment machine"""

    session: Optional[str] = None
    """session is the session that is currently active in the machine."""

    timeout: Optional[str] = None
    """timeout contains the reason the environment has timed out.

    If this field is empty, the environment has not timed out.
    """

    versions: Optional[EnvironmentStatusMachineVersions] = None
    """versions contains the versions of components in the machine."""

    warning_message: Optional[str] = FieldInfo(alias="warningMessage", default=None)
    """warning_message contains warnings, e.g.

    when the machine is present but not in the expected state.
    """


class EnvironmentStatusRunnerAck(BaseModel):
    message: Optional[str] = None

    spec_version: Union[str, float, None] = FieldInfo(alias="specVersion", default=None)

    status_code: Optional[
        Literal[
            "STATUS_CODE_UNSPECIFIED",
            "STATUS_CODE_OK",
            "STATUS_CODE_INVALID_RESOURCE",
            "STATUS_CODE_FAILED_PRECONDITION",
        ]
    ] = FieldInfo(alias="statusCode", default=None)


class EnvironmentStatusSecret(BaseModel):
    failure_message: Optional[str] = FieldInfo(alias="failureMessage", default=None)
    """failure_message contains the reason the secret failed to be materialize."""

    phase: Optional[
        Literal[
            "CONTENT_PHASE_UNSPECIFIED",
            "CONTENT_PHASE_CREATING",
            "CONTENT_PHASE_INITIALIZING",
            "CONTENT_PHASE_READY",
            "CONTENT_PHASE_UPDATING",
            "CONTENT_PHASE_FAILED",
        ]
    ] = None

    secret_name: Optional[str] = FieldInfo(alias="secretName", default=None)

    warning_message: Optional[str] = FieldInfo(alias="warningMessage", default=None)
    """warning_message contains warnings, e.g.

    when the secret is present but not in the expected state.
    """


class EnvironmentStatusSSHPublicKey(BaseModel):
    id: Optional[str] = None
    """id is the unique identifier of the public key"""

    phase: Optional[
        Literal[
            "CONTENT_PHASE_UNSPECIFIED",
            "CONTENT_PHASE_CREATING",
            "CONTENT_PHASE_INITIALIZING",
            "CONTENT_PHASE_READY",
            "CONTENT_PHASE_UPDATING",
            "CONTENT_PHASE_FAILED",
        ]
    ] = None
    """phase is the current phase of the public key"""


class EnvironmentStatus(BaseModel):
    automations_file: Optional[EnvironmentStatusAutomationsFile] = FieldInfo(alias="automationsFile", default=None)
    """automations_file contains the status of the automations file."""

    content: Optional[EnvironmentStatusContent] = None
    """content contains the status of the environment content."""

    devcontainer: Optional[EnvironmentStatusDevcontainer] = None
    """devcontainer contains the status of the devcontainer."""

    environment_urls: Optional[EnvironmentStatusEnvironmentURLs] = FieldInfo(alias="environmentUrls", default=None)
    """
    environment_url contains the URL at which the environment can be accessed. This
    field is only set if the environment is running.
    """

    failure_message: Optional[List[str]] = FieldInfo(alias="failureMessage", default=None)
    """failure_message summarises why the environment failed to operate.

    If this is non-empty the environment has failed to operate and will likely
    transition to a stopped state.
    """

    machine: Optional[EnvironmentStatusMachine] = None
    """machine contains the status of the environment machine"""

    phase: Optional[
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
    ] = None
    """
    the phase of an environment is a simple, high-level summary of where the
    environment is in its lifecycle
    """

    runner_ack: Optional[EnvironmentStatusRunnerAck] = FieldInfo(alias="runnerAck", default=None)
    """
    RunnerACK is the acknowledgement from the runner that is has received the
    environment spec.
    """

    secrets: Optional[List[EnvironmentStatusSecret]] = None
    """secrets contains the status of the environment secrets"""

    ssh_public_keys: Optional[List[EnvironmentStatusSSHPublicKey]] = FieldInfo(alias="sshPublicKeys", default=None)
    """ssh_public_keys contains the status of the environment ssh public keys"""

    status_version: Union[str, float, None] = FieldInfo(alias="statusVersion", default=None)
    """version of the status update.

    Environment instances themselves are unversioned, but their statuus has
    different versions. The value of this field has no semantic meaning (e.g. don't
    interpret it as as a timestemp), but it can be used to impose a partial order.
    If a.status_version < b.status_version then a was the status before b.
    """

    warning_message: Optional[List[str]] = FieldInfo(alias="warningMessage", default=None)
    """warning_message contains warnings, e.g.

    when the environment is present but not in the expected state.
    """


class Environment(BaseModel):
    id: Optional[str] = None
    """ID is a unique identifier of this environment.

    No other environment with the same name must be managed by this environment
    manager
    """

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

    status: Optional[EnvironmentStatus] = None
    """EnvironmentStatus describes an environment status"""


class EnvironmentCreateResponse(BaseModel):
    environment: Optional[Environment] = None
    """+resource get environment"""
