# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["PolicyListResponse", "Pagination", "Policy"]


class Pagination(BaseModel):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)
    """Token passed for retreiving the next set of results. Empty if there are no

    more results
    """


class Policy(BaseModel):
    group_id: Optional[str] = FieldInfo(alias="groupId", default=None)

    role: Optional[Literal["PROJECT_ROLE_UNSPECIFIED", "PROJECT_ROLE_ADMIN", "PROJECT_ROLE_USER"]] = None
    """role is the role assigned to the group"""


class PolicyListResponse(BaseModel):
    pagination: Optional[Pagination] = None

    policies: Optional[List[Policy]] = None
