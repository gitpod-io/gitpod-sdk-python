# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import Base64FileInput
from .._utils import PropertyInfo

__all__ = ["RunnerInteractionSignupParams", "EnvironmentClass", "EnvironmentClassConfiguration"]


class RunnerInteractionSignupParams(TypedDict, total=False):
    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    environment_classes: Annotated[Iterable[EnvironmentClass], PropertyInfo(alias="environmentClasses")]
    """The environment classes this runner has to offer"""

    public_key: Annotated[Union[str, Base64FileInput], PropertyInfo(alias="publicKey", format="base64")]
    """The runner's public key.

    Must be an ECDH public key encoded in PKIX, ASN.1 DER format.
    """

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""


class EnvironmentClassConfiguration(TypedDict, total=False):
    key: str

    value: str


class EnvironmentClass(TypedDict, total=False):
    id: str
    """id is the unique identifier of the environment class"""

    configuration: Iterable[EnvironmentClassConfiguration]
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
