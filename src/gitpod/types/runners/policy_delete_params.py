# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PolicyDeleteParams"]


class PolicyDeleteParams(TypedDict, total=False):
    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    group_id: Annotated[str, PropertyInfo(alias="groupId")]
    """group_id specifies the group_id identifier"""

    runner_id: Annotated[str, PropertyInfo(alias="runnerId")]
    """runner_id specifies the project identifier"""

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""
