# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "AutomationUpsertParams",
    "AutomationsFile",
    "AutomationsFileServices",
    "AutomationsFileServicesCommands",
    "AutomationsFileServicesRunsOn",
    "AutomationsFileServicesRunsOnDocker",
    "AutomationsFileServicesRunsOnDockerDocker",
    "AutomationsFileTasks",
    "AutomationsFileTasksRunsOn",
    "AutomationsFileTasksRunsOnDocker",
    "AutomationsFileTasksRunsOnDockerDocker",
]


class AutomationUpsertParams(TypedDict, total=False):
    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    automations_file: Annotated[AutomationsFile, PropertyInfo(alias="automationsFile")]
    """
    WARN: Do not remove any field here, as it will break reading automation yaml
    files. We error if there are any

    unknown fields in the yaml (to ensure the yaml is correct), but would break if
    we removed any fields. This includes marking a field as "reserved" in the proto
    file, this will also break reading the yaml.
    """

    environment_id: Annotated[str, PropertyInfo(alias="environmentId")]

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""


class AutomationsFileServicesCommands(TypedDict, total=False):
    ready: str
    """
    ready is an optional command that is run repeatedly until it exits with a zero
    exit code.

    If set, the service will first go into a Starting phase, and then into a Running
    phase once the ready command exits with a zero exit code.
    """

    start: str
    """
    start is the command to start and run the service. If start exits, the service
    will transition to the following phase:

    - Stopped: if the exit code is 0
    - Failed: if the exit code is not 0 If the stop command is not set, the start
      command will receive a SIGTERM signal when the service is requested to stop.
      If it does not exit within 2 minutes, it will receive a SIGKILL signal.
    """

    stop: str
    """stop is an optional command that runs when the service is requested to stop.

    If set, instead of sending a SIGTERM signal to the start command, the stop
    command will be run. Once the stop command exits, the start command will receive
    a SIGKILL signal. If the stop command exits with a non-zero exit code, the
    service will transition to the Failed phase. If the stop command does not exit
    within 2 minutes, a SIGKILL signal will be sent to both the start and stop
    commands.
    """


class AutomationsFileServicesRunsOnDockerDocker(TypedDict, total=False):
    environment: List[str]

    image: str


class AutomationsFileServicesRunsOnDocker(TypedDict, total=False):
    docker: Required[AutomationsFileServicesRunsOnDockerDocker]


AutomationsFileServicesRunsOn: TypeAlias = Union[
    AutomationsFileServicesRunsOnDocker, AutomationsFileServicesRunsOnDocker
]


class AutomationsFileServices(TypedDict, total=False):
    commands: AutomationsFileServicesCommands

    description: str

    name: str

    runs_on: Annotated[AutomationsFileServicesRunsOn, PropertyInfo(alias="runsOn")]

    triggered_by: Annotated[List[str], PropertyInfo(alias="triggeredBy")]


class AutomationsFileTasksRunsOnDockerDocker(TypedDict, total=False):
    environment: List[str]

    image: str


class AutomationsFileTasksRunsOnDocker(TypedDict, total=False):
    docker: Required[AutomationsFileTasksRunsOnDockerDocker]


AutomationsFileTasksRunsOn: TypeAlias = Union[AutomationsFileTasksRunsOnDocker, AutomationsFileTasksRunsOnDocker]


class AutomationsFileTasks(TypedDict, total=False):
    command: str

    depends_on: Annotated[List[str], PropertyInfo(alias="dependsOn")]

    description: str

    name: str

    runs_on: Annotated[AutomationsFileTasksRunsOn, PropertyInfo(alias="runsOn")]

    triggered_by: Annotated[List[str], PropertyInfo(alias="triggeredBy")]


class AutomationsFile(TypedDict, total=False):
    services: Dict[str, AutomationsFileServices]

    tasks: Dict[str, AutomationsFileTasks]
