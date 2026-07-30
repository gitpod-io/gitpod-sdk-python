# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from .project_creation_default_environment_class_warm_pool_param import (
    ProjectCreationDefaultEnvironmentClassWarmPoolParam,
)

__all__ = ["ProjectCreationDefaultEnvironmentClassParam"]


class ProjectCreationDefaultEnvironmentClassParam(TypedDict, total=False):
    """
    ProjectCreationDefaultEnvironmentClass configures a single environment class
     in the project creation defaults.
    """

    environment_class_id: Annotated[str, PropertyInfo(alias="environmentClassId")]
    """environment_class_id is the ID of the environment class."""

    order: int
    """order is the priority of this entry (lower = higher priority)."""

    prebuild: bool
    """
    prebuild controls whether prebuilds are enabled for this environment class on
    newly created projects.
    """

    warm_pool: Annotated[ProjectCreationDefaultEnvironmentClassWarmPoolParam, PropertyInfo(alias="warmPool")]
    """
    warm_pool configures the warm pool for this environment class on newly created
    projects. Only meaningful when prebuild is true.
    """
