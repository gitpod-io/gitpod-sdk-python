# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from ..shared_params.project_environment_class import ProjectEnvironmentClass

__all__ = ["EnvironmentClaseUpdateParams"]


class EnvironmentClaseUpdateParams(TypedDict, total=False):
    project_environment_classes: Annotated[
        Iterable[ProjectEnvironmentClass], PropertyInfo(alias="projectEnvironmentClasses")
    ]

    project_id: Annotated[str, PropertyInfo(alias="projectId")]
    """project_id specifies the project identifier"""
