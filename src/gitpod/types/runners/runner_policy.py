# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .runner_role import RunnerRole

__all__ = ["RunnerPolicy"]


class RunnerPolicy(BaseModel):
    group_id: Optional[str] = FieldInfo(alias="groupId", default=None)

    role: Optional[RunnerRole] = None
    """role is the role assigned to the group"""
