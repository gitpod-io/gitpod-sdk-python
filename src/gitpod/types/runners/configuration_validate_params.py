# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "ConfigurationValidateParams",
    "Variant0",
    "Variant0EnvironmentClass",
    "Variant0EnvironmentClassConfiguration",
    "Variant0ScmIntegration",
    "Variant1",
    "Variant1ScmIntegration",
    "Variant1EnvironmentClass",
    "Variant1EnvironmentClassConfiguration",
    "Variant2",
    "Variant2EnvironmentClass",
    "Variant2EnvironmentClassConfiguration",
    "Variant2ScmIntegration",
]


class Variant0(TypedDict, total=False):
    environment_class: Required[Annotated[Variant0EnvironmentClass, PropertyInfo(alias="environmentClass")]]

    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    runner_id: Annotated[str, PropertyInfo(alias="runnerId")]

    scm_integration: Annotated[Variant0ScmIntegration, PropertyInfo(alias="scmIntegration")]

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""


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
    """enabled indicates whether the environment class can be used to create

    new environments.
    """

    runner_id: Annotated[str, PropertyInfo(alias="runnerId")]
    """
    runner_id is the unique identifier of the runner the environment class belongs
    to
    """


class Variant0ScmIntegration:
    pass


class Variant1(TypedDict, total=False):
    scm_integration: Required[Annotated[Variant1ScmIntegration, PropertyInfo(alias="scmIntegration")]]

    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    environment_class: Annotated[Variant1EnvironmentClass, PropertyInfo(alias="environmentClass")]

    runner_id: Annotated[str, PropertyInfo(alias="runnerId")]

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""


class Variant1ScmIntegration:
    pass


class Variant1EnvironmentClassConfiguration(TypedDict, total=False):
    key: str

    value: str


class Variant1EnvironmentClass(TypedDict, total=False):
    id: str
    """id is the unique identifier of the environment class"""

    configuration: Iterable[Variant1EnvironmentClassConfiguration]
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


class Variant2(TypedDict, total=False):
    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    environment_class: Annotated[Variant2EnvironmentClass, PropertyInfo(alias="environmentClass")]

    runner_id: Annotated[str, PropertyInfo(alias="runnerId")]

    scm_integration: Annotated[Variant2ScmIntegration, PropertyInfo(alias="scmIntegration")]

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""


class Variant2EnvironmentClassConfiguration(TypedDict, total=False):
    key: str

    value: str


class Variant2EnvironmentClass(TypedDict, total=False):
    id: str
    """id is the unique identifier of the environment class"""

    configuration: Iterable[Variant2EnvironmentClassConfiguration]
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


class Variant2ScmIntegration:
    pass


ConfigurationValidateParams: TypeAlias = Union[Variant0, Variant1, Variant2]
