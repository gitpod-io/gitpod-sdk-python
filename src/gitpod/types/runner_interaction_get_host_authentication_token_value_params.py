# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RunnerInteractionGetHostAuthenticationTokenValueParams"]


class RunnerInteractionGetHostAuthenticationTokenValueParams(TypedDict, total=False):
    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    host: str
    """The host to get the authentication token for"""

    principal_id: Annotated[str, PropertyInfo(alias="principalId")]
    """The principal's ID to get the authentication token for"""

    runner_id: Annotated[str, PropertyInfo(alias="runnerId")]
    """The runner's identity"""

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""
