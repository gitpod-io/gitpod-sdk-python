# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RunnerDeleteParams"]


class RunnerDeleteParams(TypedDict, total=False):
    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    force: bool
    """
    force indicates whether the runner should be deleted forcefully. When force
    deleting a Runner, all Environments on the runner are also force deleted and
    regular Runner lifecycle is not respected. Force deleting can result in data
    loss.
    """

    runner_id: Annotated[str, PropertyInfo(alias="runnerId")]

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""
