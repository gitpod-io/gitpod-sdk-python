# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ProjectCreationDefaultEnvironmentClassWarmPool"]


class ProjectCreationDefaultEnvironmentClassWarmPool(BaseModel):
    """
    ProjectCreationDefaultEnvironmentClassWarmPool configures warm pool defaults
     for an environment class in the project creation defaults.
    """

    enabled: Optional[bool] = None
    """enabled controls whether a warm pool is created for this environment class."""

    max_size: Optional[int] = FieldInfo(alias="maxSize", default=None)
    """max_size is the maximum number of warm instances.

    Must be >= min_size and <= 20.
    """

    min_size: Optional[int] = FieldInfo(alias="minSize", default=None)
    """min_size is the minimum number of warm instances. Must be >= 0 and <= max_size."""
