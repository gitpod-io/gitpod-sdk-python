# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..shared_params.runs_on import RunsOn

__all__ = ["AutomationsFileParam", "Services", "ServicesCommands", "Tasks"]


class ServicesCommands(TypedDict, total=False):
    ready: str
    """
    ready is an optional command that is run repeatedly until it exits with a zero
    exit code. If set, the service will first go into a Starting phase, and then
    into a Running phase once the ready command exits with a zero exit code.
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
    """
    stop is an optional command that runs when the service is requested to stop. If
    set, instead of sending a SIGTERM signal to the start command, the stop command
    will be run. Once the stop command exits, the start command will receive a
    SIGKILL signal. If the stop command exits with a non-zero exit code, the service
    will transition to the Failed phase. If the stop command does not exit within 2
    minutes, a SIGKILL signal will be sent to both the start and stop commands.
    """


class Services(TypedDict, total=False):
    commands: ServicesCommands

    description: str

    name: str

    runs_on: Annotated[RunsOn, PropertyInfo(alias="runsOn")]

    triggered_by: Annotated[
        List[Literal["manual", "postEnvironmentStart", "postDevcontainerStart"]], PropertyInfo(alias="triggeredBy")
    ]


class Tasks(TypedDict, total=False):
    command: str

    depends_on: Annotated[List[str], PropertyInfo(alias="dependsOn")]

    description: str

    name: str

    runs_on: Annotated[RunsOn, PropertyInfo(alias="runsOn")]

    triggered_by: Annotated[
        List[Literal["manual", "postEnvironmentStart", "postDevcontainerStart"]], PropertyInfo(alias="triggeredBy")
    ]


class AutomationsFileParam(TypedDict, total=False):
    services: Dict[str, Services]

    tasks: Dict[str, Tasks]
