# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ScmIntegrationListResponse", "OAuth"]


class OAuth(BaseModel):
    client_id: Optional[str] = FieldInfo(alias="clientId", default=None)
    """client_id is the OAuth app's client ID in clear text."""

    encrypted_client_secret: Optional[str] = FieldInfo(alias="encryptedClientSecret", default=None)
    """
    encrypted_client_secret is the OAuth app's secret encrypted with the runner's
    public key.
    """


class ScmIntegrationListResponse(BaseModel):
    oauth: OAuth

    id: Optional[str] = None
    """id is the unique identifier of the SCM integration"""

    host: Optional[str] = None

    pat: Optional[bool] = None

    runner_id: Optional[str] = FieldInfo(alias="runnerId", default=None)

    scm_id: Optional[str] = FieldInfo(alias="scmId", default=None)
    """
    scm_id references the scm_id in the runner's configuration schema that this
    integration is for
    """
