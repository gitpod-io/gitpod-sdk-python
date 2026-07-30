# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .project_creation_defaults_prebuilds import ProjectCreationDefaultsPrebuilds
from .project_creation_default_environment_class import ProjectCreationDefaultEnvironmentClass

__all__ = ["ProjectCreationDefaults"]


class ProjectCreationDefaults(BaseModel):
    """
    ProjectCreationDefaults contains default settings applied to newly created projects.
    """

    environment_classes: Optional[List[ProjectCreationDefaultEnvironmentClass]] = FieldInfo(
        alias="environmentClasses", default=None
    )
    """
    environment_classes specifies default environment classes and their per-class
    settings (order, prebuild, warm pool) for newly created projects. Each entry
    must reference an existing, enabled, non-local-runner environment class in the
    organization.
    """

    insights_enabled: Optional[bool] = FieldInfo(alias="insightsEnabled", default=None)
    """
    insights_enabled controls whether Insights (co-author attribution) is
    automatically enabled on newly created projects.
    """

    prebuilds: Optional[ProjectCreationDefaultsPrebuilds] = None
    """
    prebuilds configures default prebuild settings for newly created projects. When
    set, prebuilds can be enabled per environment class via the environment_classes
    entries. When absent, prebuilds are not enabled by default.
    """
