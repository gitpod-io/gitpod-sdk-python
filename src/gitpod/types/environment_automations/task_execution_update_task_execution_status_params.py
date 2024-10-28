# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ...types.environment_automations import task_execution_update_task_execution_status_params

__all__ = ["TaskExecutionUpdateTaskExecutionStatusParams"]


class TaskExecutionUpdateTaskExecutionStatusParams(TypedDict, total=False):
    body: Required[task_execution_update_task_execution_status_params.Body]

    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""
