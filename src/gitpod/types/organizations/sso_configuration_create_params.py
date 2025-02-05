# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SSOConfigurationCreateParams"]


class SSOConfigurationCreateParams(TypedDict, total=False):
    client_id: Annotated[str, PropertyInfo(alias="clientId")]
    """client_id is the client ID of the OIDC application set on the IdP"""

    client_secret: Annotated[str, PropertyInfo(alias="clientSecret")]
    """client_secret is the client secret of the OIDC application set on the IdP"""

    email_domain: Annotated[str, PropertyInfo(alias="emailDomain")]
    """email_domain is the domain that is allowed to sign in to the organization"""

    issuer_url: Annotated[str, PropertyInfo(alias="issuerUrl")]
    """issuer_url is the URL of the IdP issuer"""

    organization_id: Annotated[str, PropertyInfo(alias="organizationId")]
