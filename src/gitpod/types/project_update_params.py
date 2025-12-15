# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .environment_initializer_param import EnvironmentInitializerParam
from .project_prebuild_configuration_param import ProjectPrebuildConfigurationParam

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

    initializer: Optional[EnvironmentInitializerParam]
    """initializer is the content initializer"""

    name: Optional[str]

    prebuild_configuration: Annotated[
        Optional[ProjectPrebuildConfigurationParam], PropertyInfo(alias="prebuildConfiguration")
    ]
    """
    prebuild_configuration defines how prebuilds are created for this project. If
    not provided, the existing prebuild configuration is not modified. To disable
    prebuilds, set enabled to false.
    """

    project_id: Annotated[str, PropertyInfo(alias="projectId")]
    """project_id specifies the project identifier"""

    technical_description: Annotated[Optional[str], PropertyInfo(alias="technicalDescription")]
    """
    technical_description is a detailed technical description of the project This
    field is not returned by default in GetProject or ListProjects responses 8KB max
    """
