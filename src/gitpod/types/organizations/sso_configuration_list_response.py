# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SSOConfigurationListResponse", "Pagination", "SSOConfiguration"]


class Pagination(BaseModel):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)
    """Token passed for retreiving the next set of results.

    Empty if there are no more results
    """


class SSOConfiguration(BaseModel):
    id: Optional[str] = None
    """id is the unique identifier of the SSO configuration"""

    claims: Optional[Dict[str, str]] = None
    """claims are key/value pairs that defines a mapping of claims issued by the IdP."""

    client_id: Optional[str] = FieldInfo(alias="clientId", default=None)
    """client_id is the client ID of the OIDC application set on the IdP"""

    email_domain: Optional[str] = FieldInfo(alias="emailDomain", default=None)

    issuer_url: Optional[str] = FieldInfo(alias="issuerUrl", default=None)
    """issuer_url is the URL of the IdP issuer"""

    organization_id: Optional[str] = FieldInfo(alias="organizationId", default=None)

    provider_type: Optional[Literal["PROVIDER_TYPE_UNSPECIFIED", "PROVIDER_TYPE_BUILTIN", "PROVIDER_TYPE_CUSTOM"]] = (
        FieldInfo(alias="providerType", default=None)
    )
    """provider_type defines the type of the SSO configuration"""

    state: Optional[
        Literal[
            "SSO_CONFIGURATION_STATE_UNSPECIFIED", "SSO_CONFIGURATION_STATE_INACTIVE", "SSO_CONFIGURATION_STATE_ACTIVE"
        ]
    ] = None
    """state is the state of the SSO configuration"""


class SSOConfigurationListResponse(BaseModel):
    pagination: Optional[Pagination] = None

    sso_configurations: Optional[List[SSOConfiguration]] = FieldInfo(alias="ssoConfigurations", default=None)
    """sso_configurations are the SSO configurations for the organization"""
