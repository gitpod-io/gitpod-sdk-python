# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ...._utils import PropertyInfo

__all__ = [
    "ScmIntegrationCreateParams",
    "OAuthClientIDIsTheOAuthAppSClientIDIfOAuthIsConfiguredIfConfiguredOAuthPlaintextClientSecretMustAlsoBeSet",
    "OAuthPlaintextClientSecretIsTheOAuthAppSClientSecretInClearTextThisWillFirstBeEncryptedWithTheRunnerSPublicKeyBeforeBeingStored",
]


class OAuthClientIDIsTheOAuthAppSClientIDIfOAuthIsConfiguredIfConfiguredOAuthPlaintextClientSecretMustAlsoBeSet(
    TypedDict, total=False
):
    oauth_client_id: Required[Annotated[str, PropertyInfo(alias="oauthClientId")]]
    """oauth_client_id is the OAuth app's client ID, if OAuth is configured.

    If configured, oauth_plaintext_client_secret must also be set.
    """

    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""


class OAuthPlaintextClientSecretIsTheOAuthAppSClientSecretInClearTextThisWillFirstBeEncryptedWithTheRunnerSPublicKeyBeforeBeingStored(
    TypedDict, total=False
):
    oauth_plaintext_client_secret: Required[Annotated[str, PropertyInfo(alias="oauthPlaintextClientSecret")]]
    """oauth_plaintext_client_secret is the OAuth app's client secret in clear text.

    This will first be encrypted with the runner's public key before being stored.
    """

    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""


ScmIntegrationCreateParams: TypeAlias = Union[
    OAuthClientIDIsTheOAuthAppSClientIDIfOAuthIsConfiguredIfConfiguredOAuthPlaintextClientSecretMustAlsoBeSet,
    OAuthPlaintextClientSecretIsTheOAuthAppSClientSecretInClearTextThisWillFirstBeEncryptedWithTheRunnerSPublicKeyBeforeBeingStored,
]
