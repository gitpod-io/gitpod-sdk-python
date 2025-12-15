# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ScmIntegrationCreateParams"]


class ScmIntegrationCreateParams(TypedDict, total=False):
    host: str

    issuer_url: Annotated[Optional[str], PropertyInfo(alias="issuerUrl")]
    """
    issuer_url can be set to override the authentication provider URL, if it doesn't
    match the SCM host.
    """

    oauth_client_id: Annotated[Optional[str], PropertyInfo(alias="oauthClientId")]
    """
    oauth_client_id is the OAuth app's client ID, if OAuth is configured. If
    configured, oauth_plaintext_client_secret must also be set.
    """

    oauth_plaintext_client_secret: Annotated[Optional[str], PropertyInfo(alias="oauthPlaintextClientSecret")]
    """
    oauth_plaintext_client_secret is the OAuth app's client secret in clear text.
    This will first be encrypted with the runner's public key before being stored.
    """

    pat: bool

    runner_id: Annotated[str, PropertyInfo(alias="runnerId")]

    scm_id: Annotated[str, PropertyInfo(alias="scmId")]
    """
    scm_id references the scm_id in the runner's configuration schema that this
    integration is for
    """

    virtual_directory: Annotated[Optional[str], PropertyInfo(alias="virtualDirectory")]
    """
    virtual_directory is the virtual directory path for Azure DevOps Server (e.g.,
    "/tfs"). This field is only used for Azure DevOps Server SCM integrations and
    should be empty for other SCM types. Azure DevOps Server APIs work without
    collection when PAT scope is 'All accessible organizations'.
    """
