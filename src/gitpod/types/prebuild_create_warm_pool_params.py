# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PrebuildCreateWarmPoolParams"]


class PrebuildCreateWarmPoolParams(TypedDict, total=False):
    environment_class_id: Required[Annotated[str, PropertyInfo(alias="environmentClassId")]]
    """
    environment_class_id specifies which environment class to warm. Must be listed
    in the project's prebuild configuration environment_class_ids.
    """

    project_id: Required[Annotated[str, PropertyInfo(alias="projectId")]]
    """
    project_id specifies the project this warm pool belongs to. The project must
    have prebuilds enabled.
    """

    desired_size: Annotated[int, PropertyInfo(alias="desiredSize")]
    """desired_size is the number of warm instances to maintain."""
