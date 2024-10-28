# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..types import environment_automation_update_task_execution_status_params
from .._utils import PropertyInfo

__all__ = ["EnvironmentAutomationUpdateTaskExecutionStatusParams"]


class EnvironmentAutomationUpdateTaskExecutionStatusParams(TypedDict, total=False):
    body: Required[environment_automation_update_task_execution_status_params.Body]

    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""
