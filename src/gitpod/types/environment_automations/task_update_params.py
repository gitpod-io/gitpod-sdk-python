# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ...types.environment_automations import task_update_params

__all__ = ["TaskUpdateParams"]


class TaskUpdateParams(TypedDict, total=False):
    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    id: str

    depends_on: Annotated[List[str], PropertyInfo(alias="dependsOn")]
    """dependencies specifies the IDs of the automations this task depends on."""

    metadata: task_update_params.Metadata

    spec: Union[object, object]

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""
