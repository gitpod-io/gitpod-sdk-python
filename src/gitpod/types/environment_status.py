# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .environment_phase import EnvironmentPhase
from .environment_activity_signal import EnvironmentActivitySignal

__all__ = [
    "EnvironmentStatus",
    "AutomationsFile",
    "Content",
    "ContentGit",
    "ContentGitChangedFile",
    "Devcontainer",
    "EnvironmentURLs",
    "EnvironmentURLsPort",
    "EnvironmentURLsSSH",
    "Machine",
    "MachineVersions",
    "RunnerAck",
    "Secret",
    "SSHPublicKey",
]


class AutomationsFile(BaseModel):
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


class ContentGitChangedFile(BaseModel):
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


class ContentGit(BaseModel):
    branch: Optional[str] = None
    """branch is branch we're currently on"""

    changed_files: Optional[List[ContentGitChangedFile]] = FieldInfo(alias="changedFiles", default=None)
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


class Content(BaseModel):
    content_location_in_machine: Optional[str] = FieldInfo(alias="contentLocationInMachine", default=None)
    """content_location_in_machine is the location of the content in the machine"""

    failure_message: Optional[str] = FieldInfo(alias="failureMessage", default=None)
    """failure_message contains the reason the content initialization failed."""

    git: Optional[ContentGit] = None
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


class Devcontainer(BaseModel):
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


class EnvironmentURLsPort(BaseModel):
    port: Optional[int] = None
    """port is the port number of the environment port"""

    url: Optional[str] = None
    """url is the URL at which the environment port can be accessed"""


class EnvironmentURLsSSH(BaseModel):
    url: Optional[str] = None


class EnvironmentURLs(BaseModel):
    logs: Optional[str] = None
    """logs is the URL at which the environment logs can be accessed."""

    ports: Optional[List[EnvironmentURLsPort]] = None

    ssh: Optional[EnvironmentURLsSSH] = None
    """SSH is the URL at which the environment can be accessed via SSH."""


class MachineVersions(BaseModel):
    supervisor_commit: Optional[str] = FieldInfo(alias="supervisorCommit", default=None)

    supervisor_version: Optional[str] = FieldInfo(alias="supervisorVersion", default=None)


class Machine(BaseModel):
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

    versions: Optional[MachineVersions] = None
    """versions contains the versions of components in the machine."""

    warning_message: Optional[str] = FieldInfo(alias="warningMessage", default=None)
    """warning_message contains warnings, e.g.

    when the machine is present but not in the expected state.
    """


class RunnerAck(BaseModel):
    message: Optional[str] = None

    spec_version: Optional[str] = FieldInfo(alias="specVersion", default=None)

    status_code: Optional[
        Literal[
            "STATUS_CODE_UNSPECIFIED",
            "STATUS_CODE_OK",
            "STATUS_CODE_INVALID_RESOURCE",
            "STATUS_CODE_FAILED_PRECONDITION",
        ]
    ] = FieldInfo(alias="statusCode", default=None)


class Secret(BaseModel):
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

    session: Optional[str] = None
    """session is the session that is currently active in the environment."""

    warning_message: Optional[str] = FieldInfo(alias="warningMessage", default=None)
    """warning_message contains warnings, e.g.

    when the secret is present but not in the expected state.
    """


class SSHPublicKey(BaseModel):
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
    activity_signal: Optional[EnvironmentActivitySignal] = FieldInfo(alias="activitySignal", default=None)
    """EnvironmentActivitySignal used to signal activity for an environment."""

    automations_file: Optional[AutomationsFile] = FieldInfo(alias="automationsFile", default=None)
    """automations_file contains the status of the automations file."""

    content: Optional[Content] = None
    """content contains the status of the environment content."""

    devcontainer: Optional[Devcontainer] = None
    """devcontainer contains the status of the devcontainer."""

    environment_urls: Optional[EnvironmentURLs] = FieldInfo(alias="environmentUrls", default=None)
    """
    environment_url contains the URL at which the environment can be accessed. This
    field is only set if the environment is running.
    """

    failure_message: Optional[List[str]] = FieldInfo(alias="failureMessage", default=None)
    """failure_message summarises why the environment failed to operate.

    If this is non-empty the environment has failed to operate and will likely
    transition to a stopped state.
    """

    machine: Optional[Machine] = None
    """machine contains the status of the environment machine"""

    phase: Optional[EnvironmentPhase] = None
    """
    the phase of an environment is a simple, high-level summary of where the
    environment is in its lifecycle
    """

    runner_ack: Optional[RunnerAck] = FieldInfo(alias="runnerAck", default=None)
    """
    RunnerACK is the acknowledgement from the runner that is has received the
    environment spec.
    """

    secrets: Optional[List[Secret]] = None
    """secrets contains the status of the environment secrets"""

    ssh_public_keys: Optional[List[SSHPublicKey]] = FieldInfo(alias="sshPublicKeys", default=None)
    """ssh_public_keys contains the status of the environment ssh public keys"""

    status_version: Optional[str] = FieldInfo(alias="statusVersion", default=None)
    """version of the status update.

    Environment instances themselves are unversioned, but their status has different
    versions. The value of this field has no semantic meaning (e.g. don't interpret
    it as as a timestamp), but it can be used to impose a partial order. If
    a.status_version < b.status_version then a was the status before b.
    """

    warning_message: Optional[List[str]] = FieldInfo(alias="warningMessage", default=None)
    """warning_message contains warnings, e.g.

    when the environment is present but not in the expected state.
    """
