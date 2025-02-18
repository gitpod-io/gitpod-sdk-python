# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["RunnerCheckAuthenticationForHostResponse", "SupportsOauth2", "SupportsPat"]


class SupportsOauth2(BaseModel):
    auth_url: Optional[str] = FieldInfo(alias="authUrl", default=None)
    """auth_url is the URL where users can authenticate"""

    docs_url: Optional[str] = FieldInfo(alias="docsUrl", default=None)
    """docs_url is the URL to the documentation explaining this authentication method"""


class SupportsPat(BaseModel):
    create_url: Optional[str] = FieldInfo(alias="createUrl", default=None)
    """create_url is the URL where users can create a new Personal Access Token"""

    docs_url: Optional[str] = FieldInfo(alias="docsUrl", default=None)
    """docs_url is the URL to the documentation explaining PAT usage for this host"""

    example: Optional[str] = None
    """example is an example of a Personal Access Token"""

    required_scopes: Optional[List[str]] = FieldInfo(alias="requiredScopes", default=None)
    """
    required_scopes is the list of permissions required for the Personal Access
    Token
    """


class RunnerCheckAuthenticationForHostResponse(BaseModel):
    authenticated: Optional[bool] = None

    authentication_url: Optional[str] = FieldInfo(alias="authenticationUrl", default=None)

    pat_supported: Optional[bool] = FieldInfo(alias="patSupported", default=None)

    scm_id: Optional[str] = FieldInfo(alias="scmId", default=None)
    """scm_id is the unique identifier of the SCM provider"""

    scm_name: Optional[str] = FieldInfo(alias="scmName", default=None)
    """
    scm_name is the human-readable name of the SCM provider (e.g., "GitHub",
    "GitLab")
    """

    supports_oauth2: Optional[SupportsOauth2] = FieldInfo(alias="supportsOauth2", default=None)
    """supports_oauth2 indicates that the host supports OAuth2 authentication"""

    supports_pat: Optional[SupportsPat] = FieldInfo(alias="supportsPat", default=None)
    """
    supports_pat indicates that the host supports Personal Access Token
    authentication
    """
