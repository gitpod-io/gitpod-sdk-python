# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .joinable_organization import JoinableOrganization

__all__ = ["AccountListJoinableOrganizationsResponse"]


class AccountListJoinableOrganizationsResponse(BaseModel):
    joinable_organizations: Optional[List[JoinableOrganization]] = FieldInfo(
        alias="joinableOrganizations", default=None
    )
