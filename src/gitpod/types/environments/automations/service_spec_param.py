# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo
from .service_phase import ServicePhase
from ...shared_params.runs_on import RunsOn

__all__ = ["ServiceSpecParam", "Commands"]


class Commands(TypedDict, total=False):
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


class ServiceSpecParam(TypedDict, total=False):
    commands: Commands
    """
    commands contains the commands to start, stop and check the readiness of the
    service
    """

    desired_phase: Annotated[ServicePhase, PropertyInfo(alias="desiredPhase")]
    """desired_phase is the phase the service should be in.

    Used to start or stop the service.
    """

    runs_on: Annotated[RunsOn, PropertyInfo(alias="runsOn")]
    """runs_on specifies the environment the service should run on."""

    session: str
    """session should be changed to trigger a restart of the service.

    If a service exits it will not be restarted until the session is changed.
    """

    spec_version: Annotated[str, PropertyInfo(alias="specVersion")]
    """version of the spec.

    The value of this field has no semantic meaning (e.g. don't interpret it as as a
    timestamp), but it can be used to impose a partial order. If a.spec_version <
    b.spec_version then a was the spec before b.
    """
