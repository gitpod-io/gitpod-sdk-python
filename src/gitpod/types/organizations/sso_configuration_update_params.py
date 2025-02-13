# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .sso_configuration_state import SSOConfigurationState

__all__ = ["SSOConfigurationUpdateParams"]


class SSOConfigurationUpdateParams(TypedDict, total=False):
    sso_configuration_id: Required[Annotated[str, PropertyInfo(alias="ssoConfigurationId")]]
    """sso_configuration_id is the ID of the SSO configuration to update"""

    claims: Dict[str, str]
    """claims are key/value pairs that defines a mapping of claims issued by the IdP."""

    client_id: Annotated[Optional[str], PropertyInfo(alias="clientId")]
    """client_id is the client ID of the SSO provider"""

    client_secret: Annotated[Optional[str], PropertyInfo(alias="clientSecret")]
    """client_secret is the client secret of the SSO provider"""

    email_domain: Annotated[Optional[str], PropertyInfo(alias="emailDomain")]

    issuer_url: Annotated[Optional[str], PropertyInfo(alias="issuerUrl")]
    """issuer_url is the URL of the IdP issuer"""

    state: Optional[SSOConfigurationState]
    """state is the state of the SSO configuration"""
