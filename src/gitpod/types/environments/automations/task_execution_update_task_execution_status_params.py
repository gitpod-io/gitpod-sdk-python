# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ...._utils import PropertyInfo

__all__ = ["TaskExecutionUpdateTaskExecutionStatusParams", "FailureMessage", "LogURL"]


class FailureMessage(TypedDict, total=False):
    failure_message: Required[Annotated[str, PropertyInfo(alias="failureMessage")]]
    """
    failure_message marks the task execution as failed and provides a message
    explaining the failure.

    If an individual step has failed, callers are NOT expected to set this message;
    only if the task execution as a whole has failed/cannot be started.
    """

    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""


class LogURL(TypedDict, total=False):
    log_url: Required[Annotated[str, PropertyInfo(alias="logUrl")]]
    """log_url is the URL to the logs of the task's steps.

    If this is empty, the task either has no logs or has not yet started.
    """

    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""


TaskExecutionUpdateTaskExecutionStatusParams: TypeAlias = Union[FailureMessage, LogURL]
