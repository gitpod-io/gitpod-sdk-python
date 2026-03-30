# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .sso_configuration_state import SSOConfigurationState
from .additional_scopes_update_param import AdditionalScopesUpdateParam

__all__ = ["SSOConfigurationUpdateParams"]


class SSOConfigurationUpdateParams(TypedDict, total=False):
    sso_configuration_id: Required[Annotated[str, PropertyInfo(alias="ssoConfigurationId")]]
    """sso_configuration_id is the ID of the SSO configuration to update"""

    additional_scopes: Annotated[Optional[AdditionalScopesUpdateParam], PropertyInfo(alias="additionalScopes")]
    """
    additional_scopes replaces the configured OIDC scopes when present. When absent
    (nil), scopes are left unchanged. When present with an empty scopes list, all
    additional scopes are cleared.
    """

    claims: Dict[str, str]
    """claims are key/value pairs that defines a mapping of claims issued by the IdP."""

    claims_expression: Annotated[Optional[str], PropertyInfo(alias="claimsExpression")]
    """
    claims_expression is a CEL expression evaluated against OIDC token claims during
    login. When set, the expression must evaluate to true for the login to succeed.
    When present with an empty string, the expression is cleared.
    """

    client_id: Annotated[Optional[str], PropertyInfo(alias="clientId")]
    """client_id is the client ID of the SSO provider"""

    client_secret: Annotated[Optional[str], PropertyInfo(alias="clientSecret")]
    """client_secret is the client secret of the SSO provider"""

    display_name: Annotated[Optional[str], PropertyInfo(alias="displayName")]

    email_domain: Annotated[Optional[str], PropertyInfo(alias="emailDomain")]

    email_domains: Annotated[SequenceNotStr[str], PropertyInfo(alias="emailDomains")]

    issuer_url: Annotated[Optional[str], PropertyInfo(alias="issuerUrl")]
    """issuer_url is the URL of the IdP issuer"""

    state: Optional[SSOConfigurationState]
    """state is the state of the SSO configuration"""
