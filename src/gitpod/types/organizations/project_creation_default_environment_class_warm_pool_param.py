# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ProjectCreationDefaultEnvironmentClassWarmPoolParam"]


class ProjectCreationDefaultEnvironmentClassWarmPoolParam(TypedDict, total=False):
    """
    ProjectCreationDefaultEnvironmentClassWarmPool configures warm pool defaults
     for an environment class in the project creation defaults.
    """

    enabled: bool
    """enabled controls whether a warm pool is created for this environment class."""

    max_size: Annotated[int, PropertyInfo(alias="maxSize")]
    """max_size is the maximum number of warm instances.

    Must be >= min_size and <= 20.
    """

    min_size: Annotated[int, PropertyInfo(alias="minSize")]
    """min_size is the minimum number of warm instances. Must be >= 0 and <= max_size."""
