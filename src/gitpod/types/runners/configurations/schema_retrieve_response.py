# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import List, Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "SchemaRetrieveResponse",
    "Schema",
    "SchemaEnvironmentClass",
    "SchemaEnvironmentClassUnionMember0",
    "SchemaEnvironmentClassUnionMember0Bool",
    "SchemaEnvironmentClassUnionMember1",
    "SchemaEnvironmentClassUnionMember1Display",
    "SchemaEnvironmentClassUnionMember2",
    "SchemaEnvironmentClassUnionMember2Enum",
    "SchemaEnvironmentClassUnionMember3",
    "SchemaEnvironmentClassUnionMember3Int",
    "SchemaEnvironmentClassUnionMember4",
    "SchemaEnvironmentClassUnionMember4String",
    "SchemaRunnerConfig",
    "SchemaRunnerConfigUnionMember0",
    "SchemaRunnerConfigUnionMember0Bool",
    "SchemaRunnerConfigUnionMember1",
    "SchemaRunnerConfigUnionMember1Display",
    "SchemaRunnerConfigUnionMember2",
    "SchemaRunnerConfigUnionMember2Enum",
    "SchemaRunnerConfigUnionMember3",
    "SchemaRunnerConfigUnionMember3Int",
    "SchemaRunnerConfigUnionMember4",
    "SchemaRunnerConfigUnionMember4String",
    "SchemaScm",
    "SchemaScmOAuth",
    "SchemaScmPat",
]


class SchemaEnvironmentClassUnionMember0Bool(BaseModel):
    default: Optional[bool] = None


class SchemaEnvironmentClassUnionMember0(BaseModel):
    bool: SchemaEnvironmentClassUnionMember0Bool

    id: Optional[str] = None

    description: Optional[str] = None

    name: Optional[str] = None

    required: Optional[builtins.bool] = None

    secret: Optional[builtins.bool] = None


class SchemaEnvironmentClassUnionMember1Display(BaseModel):
    default: Optional[str] = None


class SchemaEnvironmentClassUnionMember1(BaseModel):
    display: SchemaEnvironmentClassUnionMember1Display

    id: Optional[str] = None

    description: Optional[str] = None

    name: Optional[str] = None

    required: Optional[bool] = None

    secret: Optional[bool] = None


class SchemaEnvironmentClassUnionMember2Enum(BaseModel):
    default: Optional[str] = None

    values: Optional[List[str]] = None


class SchemaEnvironmentClassUnionMember2(BaseModel):
    enum: SchemaEnvironmentClassUnionMember2Enum

    id: Optional[str] = None

    description: Optional[str] = None

    name: Optional[str] = None

    required: Optional[bool] = None

    secret: Optional[bool] = None


class SchemaEnvironmentClassUnionMember3Int(BaseModel):
    default: Optional[int] = None

    max: Optional[int] = None

    min: Optional[int] = None


class SchemaEnvironmentClassUnionMember3(BaseModel):
    int: SchemaEnvironmentClassUnionMember3Int

    id: Optional[str] = None

    description: Optional[str] = None

    name: Optional[str] = None

    required: Optional[bool] = None

    secret: Optional[bool] = None


class SchemaEnvironmentClassUnionMember4String(BaseModel):
    default: Optional[str] = None

    pattern: Optional[str] = None


class SchemaEnvironmentClassUnionMember4(BaseModel):
    string: SchemaEnvironmentClassUnionMember4String

    id: Optional[str] = None

    description: Optional[str] = None

    name: Optional[str] = None

    required: Optional[bool] = None

    secret: Optional[bool] = None


SchemaEnvironmentClass: TypeAlias = Union[
    SchemaEnvironmentClassUnionMember0,
    SchemaEnvironmentClassUnionMember1,
    SchemaEnvironmentClassUnionMember2,
    SchemaEnvironmentClassUnionMember3,
    SchemaEnvironmentClassUnionMember4,
]


class SchemaRunnerConfigUnionMember0Bool(BaseModel):
    default: Optional[bool] = None


class SchemaRunnerConfigUnionMember0(BaseModel):
    bool: SchemaRunnerConfigUnionMember0Bool

    id: Optional[str] = None

    description: Optional[str] = None

    name: Optional[str] = None

    required: Optional[builtins.bool] = None

    secret: Optional[builtins.bool] = None


class SchemaRunnerConfigUnionMember1Display(BaseModel):
    default: Optional[str] = None


class SchemaRunnerConfigUnionMember1(BaseModel):
    display: SchemaRunnerConfigUnionMember1Display

    id: Optional[str] = None

    description: Optional[str] = None

    name: Optional[str] = None

    required: Optional[bool] = None

    secret: Optional[bool] = None


class SchemaRunnerConfigUnionMember2Enum(BaseModel):
    default: Optional[str] = None

    values: Optional[List[str]] = None


class SchemaRunnerConfigUnionMember2(BaseModel):
    enum: SchemaRunnerConfigUnionMember2Enum

    id: Optional[str] = None

    description: Optional[str] = None

    name: Optional[str] = None

    required: Optional[bool] = None

    secret: Optional[bool] = None


class SchemaRunnerConfigUnionMember3Int(BaseModel):
    default: Optional[int] = None

    max: Optional[int] = None

    min: Optional[int] = None


class SchemaRunnerConfigUnionMember3(BaseModel):
    int: SchemaRunnerConfigUnionMember3Int

    id: Optional[str] = None

    description: Optional[str] = None

    name: Optional[str] = None

    required: Optional[bool] = None

    secret: Optional[bool] = None


class SchemaRunnerConfigUnionMember4String(BaseModel):
    default: Optional[str] = None

    pattern: Optional[str] = None


class SchemaRunnerConfigUnionMember4(BaseModel):
    string: SchemaRunnerConfigUnionMember4String

    id: Optional[str] = None

    description: Optional[str] = None

    name: Optional[str] = None

    required: Optional[bool] = None

    secret: Optional[bool] = None


SchemaRunnerConfig: TypeAlias = Union[
    SchemaRunnerConfigUnionMember0,
    SchemaRunnerConfigUnionMember1,
    SchemaRunnerConfigUnionMember2,
    SchemaRunnerConfigUnionMember3,
    SchemaRunnerConfigUnionMember4,
]


class SchemaScmOAuth(BaseModel):
    callback_url: Optional[str] = FieldInfo(alias="callbackUrl", default=None)
    """
    callback_url is the URL the OAuth app will redirect to after the user has
    authenticated.
    """


class SchemaScmPat(BaseModel):
    description: Optional[str] = None
    """description is a human-readable description of the PAT."""

    docs_link: Optional[str] = FieldInfo(alias="docsLink", default=None)
    """
    docs_link is a link to the documentation on how to create a PAT for this SCM
    system.
    """


class SchemaScm(BaseModel):
    default_hosts: Optional[List[str]] = FieldInfo(alias="defaultHosts", default=None)

    name: Optional[str] = None

    oauth: Optional[SchemaScmOAuth] = None

    pat: Optional[SchemaScmPat] = None

    scm_id: Optional[str] = FieldInfo(alias="scmId", default=None)


class Schema(BaseModel):
    environment_classes: Optional[List[SchemaEnvironmentClass]] = FieldInfo(alias="environmentClasses", default=None)

    runner_config: Optional[List[SchemaRunnerConfig]] = FieldInfo(alias="runnerConfig", default=None)

    scm: Optional[List[SchemaScm]] = None

    version: Optional[str] = None
    """The schema version"""


class SchemaRetrieveResponse(BaseModel):
    schema_: Optional[Schema] = FieldInfo(alias="schema", default=None)
