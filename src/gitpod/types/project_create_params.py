# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .environment_initializer_param import EnvironmentInitializerParam
from .project_prebuild_configuration_param import ProjectPrebuildConfigurationParam

__all__ = ["ProjectCreateParams"]


class ProjectCreateParams(TypedDict, total=False):
    initializer: Required[EnvironmentInitializerParam]
    """initializer is the content initializer"""

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

    prebuild_configuration: Annotated[ProjectPrebuildConfigurationParam, PropertyInfo(alias="prebuildConfiguration")]
    """
    prebuild_configuration defines how prebuilds are created for this project. If
    not set, prebuilds are disabled for the project.
    """

    technical_description: Annotated[str, PropertyInfo(alias="technicalDescription")]
    """
    technical_description is a detailed technical description of the project This
    field is not returned by default in GetProject or ListProjects responses 8KB max
    """
