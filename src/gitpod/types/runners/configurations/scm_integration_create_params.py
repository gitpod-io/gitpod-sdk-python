# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["ScmIntegrationCreateParams"]


class ScmIntegrationCreateParams(TypedDict, total=False):
    host: str

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
