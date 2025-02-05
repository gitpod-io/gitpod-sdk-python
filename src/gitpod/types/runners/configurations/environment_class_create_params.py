# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["EnvironmentClassCreateParams", "Configuration"]


class EnvironmentClassCreateParams(TypedDict, total=False):
    configuration: Iterable[Configuration]

    description: str

    display_name: Annotated[str, PropertyInfo(alias="displayName")]

    runner_id: Annotated[str, PropertyInfo(alias="runnerId")]


class Configuration(TypedDict, total=False):
    key: str

    value: str
