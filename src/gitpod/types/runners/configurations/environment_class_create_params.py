# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["EnvironmentClassCreateParams", "Configuration"]


class EnvironmentClassCreateParams(TypedDict, total=False):
    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    configuration: Iterable[Configuration]

    description: str

    display_name: Annotated[str, PropertyInfo(alias="displayName")]

    runner_id: Annotated[str, PropertyInfo(alias="runnerId")]

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""


class Configuration(TypedDict, total=False):
    key: str

    value: str
