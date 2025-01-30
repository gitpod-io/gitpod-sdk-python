# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PolicyCreateResponse", "Policy"]


class Policy(BaseModel):
    group_id: Optional[str] = FieldInfo(alias="groupId", default=None)

    role: Optional[Literal["RUNNER_ROLE_UNSPECIFIED", "RUNNER_ROLE_ADMIN", "RUNNER_ROLE_USER"]] = None
    """role is the role assigned to the group"""


class PolicyCreateResponse(BaseModel):
    policy: Optional[Policy] = None
