# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ProjectEnvironmentClass"]


class ProjectEnvironmentClass(BaseModel):
    environment_class_id: Optional[str] = FieldInfo(alias="environmentClassId", default=None)
    """Use a fixed environment class on a given Runner.

    This cannot be a local runner's environment class.
    """

    local_runner: Optional[bool] = FieldInfo(alias="localRunner", default=None)
    """Use a local runner for the user"""
