# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .account import Account
from .._models import BaseModel

__all__ = ["AccountRetrieveResponse"]


class AccountRetrieveResponse(BaseModel):
    account: Optional[Account] = None
