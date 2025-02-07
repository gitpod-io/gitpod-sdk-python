# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .provider_type import ProviderType
from .sso_configuration_state import SSOConfigurationState

__all__ = ["SSOConfiguration"]


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

    provider_type: Optional[ProviderType] = FieldInfo(alias="providerType", default=None)
    """provider_type defines the type of the SSO configuration"""

    state: Optional[SSOConfigurationState] = None
    """state is the state of the SSO configuration"""
