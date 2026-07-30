# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .project_creation_default_environment_class_warm_pool import ProjectCreationDefaultEnvironmentClassWarmPool

__all__ = ["ProjectCreationDefaultEnvironmentClass"]


class ProjectCreationDefaultEnvironmentClass(BaseModel):
    """
    ProjectCreationDefaultEnvironmentClass configures a single environment class
     in the project creation defaults.
    """

    environment_class_id: Optional[str] = FieldInfo(alias="environmentClassId", default=None)
    """environment_class_id is the ID of the environment class."""

    order: Optional[int] = None
    """order is the priority of this entry (lower = higher priority)."""

    prebuild: Optional[bool] = None
    """
    prebuild controls whether prebuilds are enabled for this environment class on
    newly created projects.
    """

    warm_pool: Optional[ProjectCreationDefaultEnvironmentClassWarmPool] = FieldInfo(alias="warmPool", default=None)
    """
    warm_pool configures the warm pool for this environment class on newly created
    projects. Only meaningful when prebuild is true.
    """
