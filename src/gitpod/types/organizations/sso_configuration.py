# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .provider_type import ProviderType
from .sso_configuration_state import SSOConfigurationState

__all__ = ["SSOConfiguration"]


class SSOConfiguration(BaseModel):
    id: str
    """id is the unique identifier of the SSO configuration"""

    issuer_url: str = FieldInfo(alias="issuerUrl")
    """issuer_url is the URL of the IdP issuer"""

    organization_id: str = FieldInfo(alias="organizationId")

    provider_type: ProviderType = FieldInfo(alias="providerType")
    """provider_type defines the type of the SSO configuration"""

    state: SSOConfigurationState
    """state is the state of the SSO configuration"""

    additional_scopes: Optional[List[str]] = FieldInfo(alias="additionalScopes", default=None)
    """
    additional_scopes are extra OIDC scopes requested from the identity provider
    during sign-in.
    """

    claims: Optional[Dict[str, str]] = None
    """claims are key/value pairs that defines a mapping of claims issued by the IdP."""

    claims_expression: Optional[str] = FieldInfo(alias="claimsExpression", default=None)
    """
    claims_expression is a CEL (Common Expression Language) expression evaluated
    against the OIDC token claims during login. When set, the expression must
    evaluate to true for the login to succeed. The expression has access to a
    `claims` variable containing all token claims as a map. Example:
    `claims.email_verified && claims.email.endsWith("@example.com")`
    """

    client_id: Optional[str] = FieldInfo(alias="clientId", default=None)
    """client_id is the client ID of the OIDC application set on the IdP"""

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)

    email_domain: Optional[str] = FieldInfo(alias="emailDomain", default=None)

    email_domains: Optional[List[str]] = FieldInfo(alias="emailDomains", default=None)
