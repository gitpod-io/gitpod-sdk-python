# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AccountListLoginProvidersResponse", "LoginProvider", "Pagination"]


class LoginProvider(BaseModel):
    login_url: Optional[str] = FieldInfo(alias="loginUrl", default=None)
    """login_url is the URL to redirect the browser agent to for login"""

    provider: Optional[str] = None
    """provider is the provider used by this login method, e.g.

    "github", "google", "custom"
    """


class Pagination(BaseModel):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)
    """Token passed for retreiving the next set of results.

    Empty if there are no more results
    """


class AccountListLoginProvidersResponse(BaseModel):
    login_providers: Optional[List[LoginProvider]] = FieldInfo(alias="loginProviders", default=None)

    pagination: Optional[Pagination] = None
