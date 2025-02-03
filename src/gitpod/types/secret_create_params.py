# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "SecretCreateParams",
    "SecretWillBeCreatedAsAnEnvironmentVariableWithTheSameNameAsTheSecret",
    "AbsolutePathToTheFileWhereTheSecretIsMounted",
]


class SecretWillBeCreatedAsAnEnvironmentVariableWithTheSameNameAsTheSecret(TypedDict, total=False):
    environment_variable: Required[Annotated[bool, PropertyInfo(alias="environmentVariable")]]
    """
    secret will be created as an Environment Variable with the same name as the
    secret
    """

    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    name: str

    project_id: Annotated[str, PropertyInfo(alias="projectId")]
    """project_id is the ProjectID this Secret belongs to"""

    value: str
    """value is the plaintext value of the secret"""

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""


class AbsolutePathToTheFileWhereTheSecretIsMounted(TypedDict, total=False):
    file_path: Required[Annotated[str, PropertyInfo(alias="filePath")]]
    """
    absolute path to the file where the secret is mounted value must be an absolute
    path (start with a /):

    ```
    this.matches('^/(?:[^/]*/)*.*$')
    ```
    """

    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    name: str

    project_id: Annotated[str, PropertyInfo(alias="projectId")]
    """project_id is the ProjectID this Secret belongs to"""

    value: str
    """value is the plaintext value of the secret"""

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""


SecretCreateParams: TypeAlias = Union[
    SecretWillBeCreatedAsAnEnvironmentVariableWithTheSameNameAsTheSecret, AbsolutePathToTheFileWhereTheSecretIsMounted
]
