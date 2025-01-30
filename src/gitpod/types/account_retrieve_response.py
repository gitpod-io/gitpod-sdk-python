# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AccountRetrieveResponse", "Account"]


class Account(BaseModel):
    organization_id: str = FieldInfo(alias="organizationId")
    """
    organization_id is the ID of the organization the account is owned by if it's
    created through custom SSO
    """


class AccountRetrieveResponse(BaseModel):
    account: Optional[Account] = None
