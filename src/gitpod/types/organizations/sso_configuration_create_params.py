# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["SSOConfigurationCreateParams"]


class SSOConfigurationCreateParams(TypedDict, total=False):
    client_id: Required[Annotated[str, PropertyInfo(alias="clientId")]]
    """client_id is the client ID of the OIDC application set on the IdP"""

    client_secret: Required[Annotated[str, PropertyInfo(alias="clientSecret")]]
    """client_secret is the client secret of the OIDC application set on the IdP"""

    issuer_url: Required[Annotated[str, PropertyInfo(alias="issuerUrl")]]
    """issuer_url is the URL of the IdP issuer"""

    organization_id: Required[Annotated[str, PropertyInfo(alias="organizationId")]]

    display_name: Annotated[str, PropertyInfo(alias="displayName")]

    email_domain: Annotated[Optional[str], PropertyInfo(alias="emailDomain")]
    """email_domain is the domain that is allowed to sign in to the organization"""

    email_domains: Annotated[SequenceNotStr[str], PropertyInfo(alias="emailDomains")]
