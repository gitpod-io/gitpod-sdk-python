# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .field_value import FieldValue

__all__ = ["EnvironmentClass"]


class EnvironmentClass(BaseModel):
    id: str
    """id is the unique identifier of the environment class"""

    runner_id: str = FieldInfo(alias="runnerId")
    """
    runner_id is the unique identifier of the runner the environment class belongs
    to
    """

    configuration: Optional[List[FieldValue]] = None
    """configuration describes the configuration of the environment class"""

    description: Optional[str] = None
    """description is a human readable description of the environment class"""

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)
    """display_name is the human readable name of the environment class"""

    enabled: Optional[bool] = None
    """
    enabled indicates whether the environment class can be used to create new
    environments.
    """
