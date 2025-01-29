# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ProjectCreateParams", "Initializer", "InitializerSpec"]


class ProjectCreateParams(TypedDict, total=False):
    environment_class: Required[Annotated[Union[object, object, object], PropertyInfo(alias="environmentClass")]]

    initializer: Required[Initializer]
    """EnvironmentInitializer specifies how an environment is to be initialized"""

    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    automations_file_path: Annotated[str, PropertyInfo(alias="automationsFilePath")]
    """
    automations_file_path is the path to the automations file relative to the repo
    root path must not be absolute (start with a /):

    ```
    this.matches('^$|^[^/].*')
    ```
    """

    devcontainer_file_path: Annotated[str, PropertyInfo(alias="devcontainerFilePath")]
    """
    devcontainer_file_path is the path to the devcontainer file relative to the repo
    root path must not be absolute (start with a /):

    ```
    this.matches('^$|^[^/].*')
    ```
    """

    name: str

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""


class InitializerSpec:
    pass


class Initializer(TypedDict, total=False):
    specs: Iterable[InitializerSpec]
