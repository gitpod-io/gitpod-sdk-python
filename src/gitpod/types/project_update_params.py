# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .environment_initializer_param import EnvironmentInitializerParam
from .project_environment_class_param import ProjectEnvironmentClassParam

__all__ = ["ProjectUpdateParams"]


class ProjectUpdateParams(TypedDict, total=False):
    automations_file_path: Annotated[Optional[str], PropertyInfo(alias="automationsFilePath")]
    """
    automations_file_path is the path to the automations file relative to the repo
    root path must not be absolute (start with a /):

    ```
    this.matches('^$|^[^/].*')
    ```
    """

    devcontainer_file_path: Annotated[Optional[str], PropertyInfo(alias="devcontainerFilePath")]
    """
    devcontainer_file_path is the path to the devcontainer file relative to the repo
    root path must not be absolute (start with a /):

    ```
    this.matches('^$|^[^/].*')
    ```
    """

    environment_class: Annotated[Optional[ProjectEnvironmentClassParam], PropertyInfo(alias="environmentClass")]

    initializer: Optional[EnvironmentInitializerParam]
    """EnvironmentInitializer specifies how an environment is to be initialized"""

    name: Optional[str]

    project_id: Annotated[str, PropertyInfo(alias="projectId")]
    """project_id specifies the project identifier"""
