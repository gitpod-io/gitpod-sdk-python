# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ScmIntegrationListResponse", "Integration", "IntegrationOAuth", "Pagination"]


class IntegrationOAuth(BaseModel):
    client_id: Optional[str] = FieldInfo(alias="clientId", default=None)
    """client_id is the OAuth app's client ID in clear text."""

    encrypted_client_secret: Optional[str] = FieldInfo(alias="encryptedClientSecret", default=None)
    """
    encrypted_client_secret is the OAuth app's secret encrypted with the runner's
    public key.
    """


class Integration(BaseModel):
    oauth: IntegrationOAuth

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


class Pagination(BaseModel):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)
    """Token passed for retreiving the next set of results.

    Empty if there are no more results
    """


class ScmIntegrationListResponse(BaseModel):
    integrations: Optional[List[Integration]] = None

    pagination: Optional[Pagination] = None
    """pagination contains the pagination options for listing scm integrations"""
