# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .prebuild_spec_param import PrebuildSpecParam

__all__ = ["PrebuildCreateParams"]


class PrebuildCreateParams(TypedDict, total=False):
    project_id: Required[Annotated[str, PropertyInfo(alias="projectId")]]
    """project_id specifies the project to create a prebuild for"""

    spec: Required[PrebuildSpecParam]
    """spec contains the configuration for creating the prebuild"""

    environment_class_id: Annotated[Optional[str], PropertyInfo(alias="environmentClassId")]
    """
    environment_class_id specifies which environment class to use for the prebuild.
    If not specified, uses the project's default environment class.
    """
