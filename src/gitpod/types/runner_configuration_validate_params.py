# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import Base64FileInput
from .._utils import PropertyInfo
from .._models import set_pydantic_config

__all__ = [
    "RunnerConfigurationValidateParams",
    "EnvironmentClass",
    "EnvironmentClassEnvironmentClass",
    "EnvironmentClassEnvironmentClassConfiguration",
    "ScmIntegration",
    "ScmIntegrationScmIntegration",
    "ScmIntegrationScmIntegrationOAuthClientID",
    "ScmIntegrationScmIntegrationOAuthEncryptedClientSecret",
    "ScmIntegrationScmIntegrationOAuthPlaintextClientSecret",
]


class EnvironmentClass(TypedDict, total=False):
    environment_class: Required[Annotated[EnvironmentClassEnvironmentClass, PropertyInfo(alias="environmentClass")]]

    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    runner_id: Annotated[str, PropertyInfo(alias="runnerId")]

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""


class EnvironmentClassEnvironmentClassConfiguration(TypedDict, total=False):
    key: str

    value: str


class EnvironmentClassEnvironmentClass(TypedDict, total=False):
    id: str
    """id is the unique identifier of the environment class"""

    configuration: Iterable[EnvironmentClassEnvironmentClassConfiguration]
    """configuration describes the configuration of the environment class"""

    description: str
    """description is a human readable description of the environment class"""

    display_name: Annotated[str, PropertyInfo(alias="displayName")]
    """display_name is the human readable name of the environment class"""

    enabled: bool
    """enabled indicates whether the environment class can be used to create

    new environments.
    """

    runner_id: Annotated[str, PropertyInfo(alias="runnerId")]
    """
    runner_id is the unique identifier of the runner the environment class belongs
    to
    """


class ScmIntegration(TypedDict, total=False):
    scm_integration: Required[Annotated[ScmIntegrationScmIntegration, PropertyInfo(alias="scmIntegration")]]

    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    runner_id: Annotated[str, PropertyInfo(alias="runnerId")]

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""


class ScmIntegrationScmIntegrationOAuthClientID(TypedDict, total=False):
    oauth_client_id: Required[Annotated[str, PropertyInfo(alias="oauthClientId")]]
    """oauth_client_id is the OAuth app's client ID, if OAuth is configured.

    If configured, oauth_client_secret must also be set.
    """


class ScmIntegrationScmIntegrationOAuthEncryptedClientSecret(TypedDict, total=False):
    oauth_encrypted_client_secret: Required[
        Annotated[Union[str, Base64FileInput], PropertyInfo(alias="oauthEncryptedClientSecret", format="base64")]
    ]
    """
    oauth_encrypted_client_secret is the OAuth app's client secret encrypted with
    the runner's public key,

    if OAuth is configured. This can be used to e.g. validate an already encrypted
    client secret of an existing SCM integration.
    """


set_pydantic_config(ScmIntegrationScmIntegrationOAuthEncryptedClientSecret, {"arbitrary_types_allowed": True})


class ScmIntegrationScmIntegrationOAuthPlaintextClientSecret(TypedDict, total=False):
    oauth_plaintext_client_secret: Required[Annotated[str, PropertyInfo(alias="oauthPlaintextClientSecret")]]
    """
    oauth_plaintext_client_secret is the OAuth app's client secret in clear text, if
    OAuth is configured.

    This can be set to validate any new client secret before it is encrypted and
    stored. This value will not be stored and get encrypted with the runner's public
    key before passing it to the runner.
    """


ScmIntegrationScmIntegration: TypeAlias = Union[
    ScmIntegrationScmIntegrationOAuthClientID,
    ScmIntegrationScmIntegrationOAuthEncryptedClientSecret,
    ScmIntegrationScmIntegrationOAuthPlaintextClientSecret,
]

RunnerConfigurationValidateParams: TypeAlias = Union[EnvironmentClass, ScmIntegration]
