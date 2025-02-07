# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .environment_initializer_param import EnvironmentInitializerParam
from .project_environment_class_param import ProjectEnvironmentClassParam

__all__ = ["ProjectCreateParams"]


class ProjectCreateParams(TypedDict, total=False):
    environment_class: Required[Annotated[ProjectEnvironmentClassParam, PropertyInfo(alias="environmentClass")]]

    initializer: Required[EnvironmentInitializerParam]
    """EnvironmentInitializer specifies how an environment is to be initialized"""

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
