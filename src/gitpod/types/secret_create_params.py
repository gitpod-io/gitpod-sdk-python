# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

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

    name: str

    project_id: Annotated[str, PropertyInfo(alias="projectId")]
    """project_id is the ProjectID this Secret belongs to"""

    value: str
    """value is the plaintext value of the secret"""


class AbsolutePathToTheFileWhereTheSecretIsMounted(TypedDict, total=False):
    file_path: Required[Annotated[str, PropertyInfo(alias="filePath")]]
    """
    absolute path to the file where the secret is mounted value must be an absolute
    path (start with a /):

    ```
    this.matches('^/(?:[^/]*/)*.*$')
    ```
    """

    name: str

    project_id: Annotated[str, PropertyInfo(alias="projectId")]
    """project_id is the ProjectID this Secret belongs to"""

    value: str
    """value is the plaintext value of the secret"""


SecretCreateParams: TypeAlias = Union[
    SecretWillBeCreatedAsAnEnvironmentVariableWithTheSameNameAsTheSecret, AbsolutePathToTheFileWhereTheSecretIsMounted
]
