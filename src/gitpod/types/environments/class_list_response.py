# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ClassListResponse", "Configuration"]


class Configuration(BaseModel):
    key: Optional[str] = None

    value: Optional[str] = None


class ClassListResponse(BaseModel):
    id: Optional[str] = None
    """id is the unique identifier of the environment class"""

    configuration: Optional[List[Configuration]] = None
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

    runner_id: Optional[str] = FieldInfo(alias="runnerId", default=None)
    """
    runner_id is the unique identifier of the runner the environment class belongs
    to
    """
