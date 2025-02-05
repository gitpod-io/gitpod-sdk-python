# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from ..._types import Base64FileInput
from ..._utils import PropertyInfo
from ..._models import set_pydantic_config

__all__ = [
    "ConfigurationValidateParams",
    "Variant0",
    "Variant0EnvironmentClass",
    "Variant0EnvironmentClassConfiguration",
    "Variant1",
    "Variant1ScmIntegration",
    "Variant1ScmIntegrationOAuthClientIDIsTheOAuthAppSClientIDIfOAuthIsConfiguredIfConfiguredOAuthClientSecretMustAlsoBeSet",
    "Variant1ScmIntegrationOAuthEncryptedClientSecretIsTheOAuthAppSClientSecretEncryptedWithTheRunnerSPublicKeyIfOAuthIsConfiguredThisCanBeUsedToEGValidateAnAlreadyEncryptedClientSecretOfAnExistingScmIntegration",
    "Variant1ScmIntegrationOAuthPlaintextClientSecretIsTheOAuthAppSClientSecretInClearTextIfOAuthIsConfiguredThisCanBeSetToValidateAnyNewClientSecretBeforeItIsEncryptedAndStoredThisValueWillNotBeStoredAndGetEncryptedWithTheRunnerSPublicKeyBeforePassingItToTheRunner",
]


class Variant0(TypedDict, total=False):
    environment_class: Required[Annotated[Variant0EnvironmentClass, PropertyInfo(alias="environmentClass")]]

    runner_id: Annotated[str, PropertyInfo(alias="runnerId")]


class Variant0EnvironmentClassConfiguration(TypedDict, total=False):
    key: str

    value: str


class Variant0EnvironmentClass(TypedDict, total=False):
    id: str
    """id is the unique identifier of the environment class"""

    configuration: Iterable[Variant0EnvironmentClassConfiguration]
    """configuration describes the configuration of the environment class"""

    description: str
    """description is a human readable description of the environment class"""

    display_name: Annotated[str, PropertyInfo(alias="displayName")]
    """display_name is the human readable name of the environment class"""

    enabled: bool
    """
    enabled indicates whether the environment class can be used to create new
    environments.
    """

    runner_id: Annotated[str, PropertyInfo(alias="runnerId")]
    """
    runner_id is the unique identifier of the runner the environment class belongs
    to
    """


class Variant1(TypedDict, total=False):
    scm_integration: Required[Annotated[Variant1ScmIntegration, PropertyInfo(alias="scmIntegration")]]

    runner_id: Annotated[str, PropertyInfo(alias="runnerId")]


class Variant1ScmIntegrationOAuthClientIDIsTheOAuthAppSClientIDIfOAuthIsConfiguredIfConfiguredOAuthClientSecretMustAlsoBeSet(
    TypedDict, total=False
):
    oauth_client_id: Required[Annotated[str, PropertyInfo(alias="oauthClientId")]]
    """
    oauth_client_id is the OAuth app's client ID, if OAuth is configured. If
    configured, oauth_client_secret must also be set.
    """


class Variant1ScmIntegrationOAuthEncryptedClientSecretIsTheOAuthAppSClientSecretEncryptedWithTheRunnerSPublicKeyIfOAuthIsConfiguredThisCanBeUsedToEGValidateAnAlreadyEncryptedClientSecretOfAnExistingScmIntegration(
    TypedDict, total=False
):
    oauth_encrypted_client_secret: Required[
        Annotated[Union[str, Base64FileInput], PropertyInfo(alias="oauthEncryptedClientSecret", format="base64")]
    ]
    """
    oauth_encrypted_client_secret is the OAuth app's client secret encrypted with
    the runner's public key, if OAuth is configured. This can be used to e.g.
    validate an already encrypted client secret of an existing SCM integration.
    """


set_pydantic_config(
    Variant1ScmIntegrationOAuthEncryptedClientSecretIsTheOAuthAppSClientSecretEncryptedWithTheRunnerSPublicKeyIfOAuthIsConfiguredThisCanBeUsedToEGValidateAnAlreadyEncryptedClientSecretOfAnExistingScmIntegration,
    {"arbitrary_types_allowed": True},
)


class Variant1ScmIntegrationOAuthPlaintextClientSecretIsTheOAuthAppSClientSecretInClearTextIfOAuthIsConfiguredThisCanBeSetToValidateAnyNewClientSecretBeforeItIsEncryptedAndStoredThisValueWillNotBeStoredAndGetEncryptedWithTheRunnerSPublicKeyBeforePassingItToTheRunner(
    TypedDict, total=False
):
    oauth_plaintext_client_secret: Required[Annotated[str, PropertyInfo(alias="oauthPlaintextClientSecret")]]
    """
    oauth_plaintext_client_secret is the OAuth app's client secret in clear text, if
    OAuth is configured. This can be set to validate any new client secret before it
    is encrypted and stored. This value will not be stored and get encrypted with
    the runner's public key before passing it to the runner.
    """


Variant1ScmIntegration: TypeAlias = Union[
    Variant1ScmIntegrationOAuthClientIDIsTheOAuthAppSClientIDIfOAuthIsConfiguredIfConfiguredOAuthClientSecretMustAlsoBeSet,
    Variant1ScmIntegrationOAuthEncryptedClientSecretIsTheOAuthAppSClientSecretEncryptedWithTheRunnerSPublicKeyIfOAuthIsConfiguredThisCanBeUsedToEGValidateAnAlreadyEncryptedClientSecretOfAnExistingScmIntegration,
    Variant1ScmIntegrationOAuthPlaintextClientSecretIsTheOAuthAppSClientSecretInClearTextIfOAuthIsConfiguredThisCanBeSetToValidateAnyNewClientSecretBeforeItIsEncryptedAndStoredThisValueWillNotBeStoredAndGetEncryptedWithTheRunnerSPublicKeyBeforePassingItToTheRunner,
]

ConfigurationValidateParams: TypeAlias = Union[Variant0, Variant1]
