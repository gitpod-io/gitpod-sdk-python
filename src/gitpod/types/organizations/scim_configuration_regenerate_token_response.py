# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ScimConfigurationRegenerateTokenResponse"]


class ScimConfigurationRegenerateTokenResponse(BaseModel):
    token: str
    """
    token is the new bearer token for SCIM API authentication. This invalidates the
    previous token - store it securely.
    """

    token_expires_at: datetime = FieldInfo(alias="tokenExpiresAt")
    """token_expires_at is when the new token will expire"""
