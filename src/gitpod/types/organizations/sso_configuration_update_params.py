# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "SSOConfigurationUpdateParams",
    "ClientIDIsTheClientIDOfTheSSOProvider",
    "ClientSecretIsTheClientSecretOfTheSSOProvider",
    "Variant2",
    "IssuerURLIsTheURLOfTheIDPIssuer",
    "StateIsTheStateOfTheSSOConfiguration",
]


class ClientIDIsTheClientIDOfTheSSOProvider(TypedDict, total=False):
    client_id: Required[Annotated[str, PropertyInfo(alias="clientId")]]
    """client_id is the client ID of the SSO provider"""

    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""


class ClientSecretIsTheClientSecretOfTheSSOProvider(TypedDict, total=False):
    client_secret: Required[Annotated[str, PropertyInfo(alias="clientSecret")]]
    """client_secret is the client secret of the SSO provider"""

    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""


class Variant2(TypedDict, total=False):
    email_domain: Required[Annotated[str, PropertyInfo(alias="emailDomain")]]

    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""


class IssuerURLIsTheURLOfTheIDPIssuer(TypedDict, total=False):
    issuer_url: Required[Annotated[str, PropertyInfo(alias="issuerUrl")]]
    """issuer_url is the URL of the IdP issuer"""

    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""


class StateIsTheStateOfTheSSOConfiguration(TypedDict, total=False):
    state: Required[
        Literal[
            "SSO_CONFIGURATION_STATE_UNSPECIFIED", "SSO_CONFIGURATION_STATE_INACTIVE", "SSO_CONFIGURATION_STATE_ACTIVE"
        ]
    ]
    """state is the state of the SSO configuration"""

    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""


SSOConfigurationUpdateParams: TypeAlias = Union[
    ClientIDIsTheClientIDOfTheSSOProvider,
    ClientSecretIsTheClientSecretOfTheSSOProvider,
    Variant2,
    IssuerURLIsTheURLOfTheIDPIssuer,
    StateIsTheStateOfTheSSOConfiguration,
]
