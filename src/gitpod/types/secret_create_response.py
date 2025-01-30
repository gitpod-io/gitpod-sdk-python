# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "SecretCreateResponse",
    "Secret",
    "SecretSecretWillBeCreatedAsAnEnvironmentVariableWithTheSameNameAsTheSecret",
    "SecretAbsolutePathToTheFileWhereTheSecretIsMounted",
]


class SecretSecretWillBeCreatedAsAnEnvironmentVariableWithTheSameNameAsTheSecret(BaseModel):
    environment_variable: bool = FieldInfo(alias="environmentVariable")
    """
    secret will be created as an Environment Variable with the same name as the
    secret
    """


class SecretAbsolutePathToTheFileWhereTheSecretIsMounted(BaseModel):
    file_path: str = FieldInfo(alias="filePath")
    """absolute path to the file where the secret is mounted"""


Secret: TypeAlias = Union[
    SecretSecretWillBeCreatedAsAnEnvironmentVariableWithTheSameNameAsTheSecret,
    SecretAbsolutePathToTheFileWhereTheSecretIsMounted,
]


class SecretCreateResponse(BaseModel):
    secret: Optional[Secret] = None
