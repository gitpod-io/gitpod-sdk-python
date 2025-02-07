# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ScmIntegrationOAuthConfig"]


class ScmIntegrationOAuthConfig(BaseModel):
    client_id: Optional[str] = FieldInfo(alias="clientId", default=None)
    """client_id is the OAuth app's client ID in clear text."""

    encrypted_client_secret: Optional[str] = FieldInfo(alias="encryptedClientSecret", default=None)
    """
    encrypted_client_secret is the OAuth app's secret encrypted with the runner's
    public key.
    """
