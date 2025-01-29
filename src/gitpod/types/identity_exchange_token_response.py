# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["IdentityExchangeTokenResponse"]


class IdentityExchangeTokenResponse(BaseModel):
    access_token: Optional[str] = FieldInfo(alias="accessToken", default=None)
    """access_token is the new access token"""
