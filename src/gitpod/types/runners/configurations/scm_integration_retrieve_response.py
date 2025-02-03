# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "ScmIntegrationRetrieveResponse",
    "Integration",
    "IntegrationUnionMember0",
    "IntegrationUnionMember0OAuth",
    "IntegrationUnionMember1",
    "IntegrationUnionMember1OAuth",
]


class IntegrationUnionMember0OAuth(BaseModel):
    client_id: Optional[str] = FieldInfo(alias="clientId", default=None)
    """client_id is the OAuth app's client ID in clear text."""

    encrypted_client_secret: Optional[str] = FieldInfo(alias="encryptedClientSecret", default=None)
    """
    encrypted_client_secret is the OAuth app's secret encrypted with the runner's
    public key.
    """


class IntegrationUnionMember0(BaseModel):
    oauth: IntegrationUnionMember0OAuth

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


class IntegrationUnionMember1OAuth(BaseModel):
    client_id: Optional[str] = FieldInfo(alias="clientId", default=None)
    """client_id is the OAuth app's client ID in clear text."""

    encrypted_client_secret: Optional[str] = FieldInfo(alias="encryptedClientSecret", default=None)
    """
    encrypted_client_secret is the OAuth app's secret encrypted with the runner's
    public key.
    """


class IntegrationUnionMember1(BaseModel):
    id: Optional[str] = None
    """id is the unique identifier of the SCM integration"""

    host: Optional[str] = None

    oauth: Optional[IntegrationUnionMember1OAuth] = None

    pat: Optional[bool] = None

    runner_id: Optional[str] = FieldInfo(alias="runnerId", default=None)

    scm_id: Optional[str] = FieldInfo(alias="scmId", default=None)
    """
    scm_id references the scm_id in the runner's configuration schema that this
    integration is for
    """


Integration: TypeAlias = Union[IntegrationUnionMember0, IntegrationUnionMember1]


class ScmIntegrationRetrieveResponse(BaseModel):
    integration: Optional[Integration] = None
