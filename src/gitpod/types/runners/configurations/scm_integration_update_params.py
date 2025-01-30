# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ...._utils import PropertyInfo

__all__ = [
    "ScmIntegrationUpdateParams",
    "OAuthClientIDCanBeSetToUpdateTheOAuthAppSClientIDIfAnEmptyStringIsSetTheOAuthConfigurationWillBeRemovedRegardlessOfWhetherAClientSecretIsSetAndAnyExistingHostAuthenticationTokensForTheScmIntegrationSRunnerAndHostThatWereCreatedUsingTheOAuthAppWillBeDeletedThisMightLeadToUsersBeingUnableToAccessTheirRepositoriesUntilTheyReAuthenticate",
    "OAuthPlaintextClientSecretCanBeSetToUpdateTheOAuthAppSClientSecretTheCleartextSecretWillBeEncryptedWithTheRunnerSPublicKeyBeforeBeingStored",
    "PatCanBeSetToEnableOrDisablePersonalAccessTokensSupportWhenDisablingPaTsAnyExistingHostAuthenticationTokensForTheScmIntegrationSRunnerAndHostThatWereCreatedUsingAPatWillBeDeletedThisMightLeadToUsersBeingUnableToAccessTheirRepositoriesUntilTheyReAuthenticate",
]


class OAuthClientIDCanBeSetToUpdateTheOAuthAppSClientIDIfAnEmptyStringIsSetTheOAuthConfigurationWillBeRemovedRegardlessOfWhetherAClientSecretIsSetAndAnyExistingHostAuthenticationTokensForTheScmIntegrationSRunnerAndHostThatWereCreatedUsingTheOAuthAppWillBeDeletedThisMightLeadToUsersBeingUnableToAccessTheirRepositoriesUntilTheyReAuthenticate(
    TypedDict, total=False
):
    oauth_client_id: Required[Annotated[str, PropertyInfo(alias="oauthClientId")]]
    """oauth_client_id can be set to update the OAuth app's client ID.

    If an empty string is set, the OAuth configuration will be removed (regardless
    of whether a client secret is set), and any existing Host Authentication Tokens
    for the SCM integration's runner and host that were created using the OAuth app
    will be deleted. This might lead to users being unable to access their
    repositories until they re-authenticate.
    """

    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""


class OAuthPlaintextClientSecretCanBeSetToUpdateTheOAuthAppSClientSecretTheCleartextSecretWillBeEncryptedWithTheRunnerSPublicKeyBeforeBeingStored(
    TypedDict, total=False
):
    oauth_plaintext_client_secret: Required[Annotated[str, PropertyInfo(alias="oauthPlaintextClientSecret")]]
    """
    oauth_plaintext_client_secret can be set to update the OAuth app's client
    secret.

    The cleartext secret will be encrypted with the runner's public key before being
    stored.
    """

    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""


class PatCanBeSetToEnableOrDisablePersonalAccessTokensSupportWhenDisablingPaTsAnyExistingHostAuthenticationTokensForTheScmIntegrationSRunnerAndHostThatWereCreatedUsingAPatWillBeDeletedThisMightLeadToUsersBeingUnableToAccessTheirRepositoriesUntilTheyReAuthenticate(
    TypedDict, total=False
):
    pat: Required[bool]
    """pat can be set to enable or disable Personal Access Tokens support.

    When disabling PATs, any existing Host Authentication Tokens for the SCM
    integration's runner and host that were created using a PAT will be deleted.
    This might lead to users being unable to access their repositories until they
    re-authenticate.
    """

    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""


ScmIntegrationUpdateParams: TypeAlias = Union[
    OAuthClientIDCanBeSetToUpdateTheOAuthAppSClientIDIfAnEmptyStringIsSetTheOAuthConfigurationWillBeRemovedRegardlessOfWhetherAClientSecretIsSetAndAnyExistingHostAuthenticationTokensForTheScmIntegrationSRunnerAndHostThatWereCreatedUsingTheOAuthAppWillBeDeletedThisMightLeadToUsersBeingUnableToAccessTheirRepositoriesUntilTheyReAuthenticate,
    OAuthPlaintextClientSecretCanBeSetToUpdateTheOAuthAppSClientSecretTheCleartextSecretWillBeEncryptedWithTheRunnerSPublicKeyBeforeBeingStored,
    PatCanBeSetToEnableOrDisablePersonalAccessTokensSupportWhenDisablingPaTsAnyExistingHostAuthenticationTokensForTheScmIntegrationSRunnerAndHostThatWereCreatedUsingAPatWillBeDeletedThisMightLeadToUsersBeingUnableToAccessTheirRepositoriesUntilTheyReAuthenticate,
]
