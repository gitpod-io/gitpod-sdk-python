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
    "SchemaEnvironmentClassUnionMember0Display",
    "SchemaEnvironmentClassUnionMember0Enum",
    "SchemaEnvironmentClassUnionMember0Int",
    "SchemaEnvironmentClassUnionMember0String",
    "SchemaEnvironmentClassUnionMember1",
    "SchemaEnvironmentClassUnionMember1Display",
    "SchemaEnvironmentClassUnionMember1Bool",
    "SchemaEnvironmentClassUnionMember1Enum",
    "SchemaEnvironmentClassUnionMember1Int",
    "SchemaEnvironmentClassUnionMember1String",
    "SchemaEnvironmentClassUnionMember2",
    "SchemaEnvironmentClassUnionMember2Enum",
    "SchemaEnvironmentClassUnionMember2Bool",
    "SchemaEnvironmentClassUnionMember2Display",
    "SchemaEnvironmentClassUnionMember2Int",
    "SchemaEnvironmentClassUnionMember2String",
    "SchemaEnvironmentClassUnionMember3",
    "SchemaEnvironmentClassUnionMember3Int",
    "SchemaEnvironmentClassUnionMember3Bool",
    "SchemaEnvironmentClassUnionMember3Display",
    "SchemaEnvironmentClassUnionMember3Enum",
    "SchemaEnvironmentClassUnionMember3String",
    "SchemaEnvironmentClassUnionMember4",
    "SchemaEnvironmentClassUnionMember4String",
    "SchemaEnvironmentClassUnionMember4Bool",
    "SchemaEnvironmentClassUnionMember4Display",
    "SchemaEnvironmentClassUnionMember4Enum",
    "SchemaEnvironmentClassUnionMember4Int",
    "SchemaEnvironmentClassUnionMember5",
    "SchemaEnvironmentClassUnionMember5Bool",
    "SchemaEnvironmentClassUnionMember5Display",
    "SchemaEnvironmentClassUnionMember5Enum",
    "SchemaEnvironmentClassUnionMember5Int",
    "SchemaEnvironmentClassUnionMember5String",
    "SchemaRunnerConfig",
    "SchemaRunnerConfigUnionMember0",
    "SchemaRunnerConfigUnionMember0Bool",
    "SchemaRunnerConfigUnionMember0Display",
    "SchemaRunnerConfigUnionMember0Enum",
    "SchemaRunnerConfigUnionMember0Int",
    "SchemaRunnerConfigUnionMember0String",
    "SchemaRunnerConfigUnionMember1",
    "SchemaRunnerConfigUnionMember1Display",
    "SchemaRunnerConfigUnionMember1Bool",
    "SchemaRunnerConfigUnionMember1Enum",
    "SchemaRunnerConfigUnionMember1Int",
    "SchemaRunnerConfigUnionMember1String",
    "SchemaRunnerConfigUnionMember2",
    "SchemaRunnerConfigUnionMember2Enum",
    "SchemaRunnerConfigUnionMember2Bool",
    "SchemaRunnerConfigUnionMember2Display",
    "SchemaRunnerConfigUnionMember2Int",
    "SchemaRunnerConfigUnionMember2String",
    "SchemaRunnerConfigUnionMember3",
    "SchemaRunnerConfigUnionMember3Int",
    "SchemaRunnerConfigUnionMember3Bool",
    "SchemaRunnerConfigUnionMember3Display",
    "SchemaRunnerConfigUnionMember3Enum",
    "SchemaRunnerConfigUnionMember3String",
    "SchemaRunnerConfigUnionMember4",
    "SchemaRunnerConfigUnionMember4String",
    "SchemaRunnerConfigUnionMember4Bool",
    "SchemaRunnerConfigUnionMember4Display",
    "SchemaRunnerConfigUnionMember4Enum",
    "SchemaRunnerConfigUnionMember4Int",
    "SchemaRunnerConfigUnionMember5",
    "SchemaRunnerConfigUnionMember5Bool",
    "SchemaRunnerConfigUnionMember5Display",
    "SchemaRunnerConfigUnionMember5Enum",
    "SchemaRunnerConfigUnionMember5Int",
    "SchemaRunnerConfigUnionMember5String",
    "SchemaScm",
    "SchemaScmOAuth",
    "SchemaScmPat",
]


class SchemaEnvironmentClassUnionMember0Bool(BaseModel):
    default: Optional[bool] = None


class SchemaEnvironmentClassUnionMember0Display(BaseModel):
    default: Optional[str] = None


class SchemaEnvironmentClassUnionMember0Enum(BaseModel):
    default: Optional[str] = None

    values: Optional[List[str]] = None


class SchemaEnvironmentClassUnionMember0Int(BaseModel):
    default: Optional[int] = None

    max: Optional[int] = None

    min: Optional[int] = None


class SchemaEnvironmentClassUnionMember0String(BaseModel):
    default: Optional[str] = None

    pattern: Optional[str] = None


class SchemaEnvironmentClassUnionMember0(BaseModel):
    bool: SchemaEnvironmentClassUnionMember0Bool

    id: Optional[str] = None

    description: Optional[str] = None

    display: Optional[SchemaEnvironmentClassUnionMember0Display] = None

    enum: Optional[SchemaEnvironmentClassUnionMember0Enum] = None

    int: Optional[SchemaEnvironmentClassUnionMember0Int] = None

    name: Optional[str] = None

    required: Optional[builtins.bool] = None

    secret: Optional[builtins.bool] = None

    string: Optional[SchemaEnvironmentClassUnionMember0String] = None


class SchemaEnvironmentClassUnionMember1Display(BaseModel):
    default: Optional[str] = None


class SchemaEnvironmentClassUnionMember1Bool(BaseModel):
    default: Optional[bool] = None


class SchemaEnvironmentClassUnionMember1Enum(BaseModel):
    default: Optional[str] = None

    values: Optional[List[str]] = None


class SchemaEnvironmentClassUnionMember1Int(BaseModel):
    default: Optional[int] = None

    max: Optional[int] = None

    min: Optional[int] = None


class SchemaEnvironmentClassUnionMember1String(BaseModel):
    default: Optional[str] = None

    pattern: Optional[str] = None


class SchemaEnvironmentClassUnionMember1(BaseModel):
    display: SchemaEnvironmentClassUnionMember1Display

    id: Optional[str] = None

    bool: Optional[SchemaEnvironmentClassUnionMember1Bool] = None

    description: Optional[str] = None

    enum: Optional[SchemaEnvironmentClassUnionMember1Enum] = None

    int: Optional[SchemaEnvironmentClassUnionMember1Int] = None

    name: Optional[str] = None

    required: Optional[builtins.bool] = None

    secret: Optional[builtins.bool] = None

    string: Optional[SchemaEnvironmentClassUnionMember1String] = None


class SchemaEnvironmentClassUnionMember2Enum(BaseModel):
    default: Optional[str] = None

    values: Optional[List[str]] = None


class SchemaEnvironmentClassUnionMember2Bool(BaseModel):
    default: Optional[bool] = None


class SchemaEnvironmentClassUnionMember2Display(BaseModel):
    default: Optional[str] = None


class SchemaEnvironmentClassUnionMember2Int(BaseModel):
    default: Optional[int] = None

    max: Optional[int] = None

    min: Optional[int] = None


class SchemaEnvironmentClassUnionMember2String(BaseModel):
    default: Optional[str] = None

    pattern: Optional[str] = None


class SchemaEnvironmentClassUnionMember2(BaseModel):
    enum: SchemaEnvironmentClassUnionMember2Enum

    id: Optional[str] = None

    bool: Optional[SchemaEnvironmentClassUnionMember2Bool] = None

    description: Optional[str] = None

    display: Optional[SchemaEnvironmentClassUnionMember2Display] = None

    int: Optional[SchemaEnvironmentClassUnionMember2Int] = None

    name: Optional[str] = None

    required: Optional[builtins.bool] = None

    secret: Optional[builtins.bool] = None

    string: Optional[SchemaEnvironmentClassUnionMember2String] = None


class SchemaEnvironmentClassUnionMember3Int(BaseModel):
    default: Optional[int] = None

    max: Optional[int] = None

    min: Optional[int] = None


class SchemaEnvironmentClassUnionMember3Bool(BaseModel):
    default: Optional[bool] = None


class SchemaEnvironmentClassUnionMember3Display(BaseModel):
    default: Optional[str] = None


class SchemaEnvironmentClassUnionMember3Enum(BaseModel):
    default: Optional[str] = None

    values: Optional[List[str]] = None


class SchemaEnvironmentClassUnionMember3String(BaseModel):
    default: Optional[str] = None

    pattern: Optional[str] = None


class SchemaEnvironmentClassUnionMember3(BaseModel):
    int: SchemaEnvironmentClassUnionMember3Int

    id: Optional[str] = None

    bool: Optional[SchemaEnvironmentClassUnionMember3Bool] = None

    description: Optional[str] = None

    display: Optional[SchemaEnvironmentClassUnionMember3Display] = None

    enum: Optional[SchemaEnvironmentClassUnionMember3Enum] = None

    name: Optional[str] = None

    required: Optional[builtins.bool] = None

    secret: Optional[builtins.bool] = None

    string: Optional[SchemaEnvironmentClassUnionMember3String] = None


class SchemaEnvironmentClassUnionMember4String(BaseModel):
    default: Optional[str] = None

    pattern: Optional[str] = None


class SchemaEnvironmentClassUnionMember4Bool(BaseModel):
    default: Optional[bool] = None


class SchemaEnvironmentClassUnionMember4Display(BaseModel):
    default: Optional[str] = None


class SchemaEnvironmentClassUnionMember4Enum(BaseModel):
    default: Optional[str] = None

    values: Optional[List[str]] = None


class SchemaEnvironmentClassUnionMember4Int(BaseModel):
    default: Optional[int] = None

    max: Optional[int] = None

    min: Optional[int] = None


class SchemaEnvironmentClassUnionMember4(BaseModel):
    string: SchemaEnvironmentClassUnionMember4String

    id: Optional[str] = None

    bool: Optional[SchemaEnvironmentClassUnionMember4Bool] = None

    description: Optional[str] = None

    display: Optional[SchemaEnvironmentClassUnionMember4Display] = None

    enum: Optional[SchemaEnvironmentClassUnionMember4Enum] = None

    int: Optional[SchemaEnvironmentClassUnionMember4Int] = None

    name: Optional[str] = None

    required: Optional[builtins.bool] = None

    secret: Optional[builtins.bool] = None


class SchemaEnvironmentClassUnionMember5Bool(BaseModel):
    default: Optional[bool] = None


class SchemaEnvironmentClassUnionMember5Display(BaseModel):
    default: Optional[str] = None


class SchemaEnvironmentClassUnionMember5Enum(BaseModel):
    default: Optional[str] = None

    values: Optional[List[str]] = None


class SchemaEnvironmentClassUnionMember5Int(BaseModel):
    default: Optional[int] = None

    max: Optional[int] = None

    min: Optional[int] = None


class SchemaEnvironmentClassUnionMember5String(BaseModel):
    default: Optional[str] = None

    pattern: Optional[str] = None


class SchemaEnvironmentClassUnionMember5(BaseModel):
    id: Optional[str] = None

    bool: Optional[SchemaEnvironmentClassUnionMember5Bool] = None

    description: Optional[str] = None

    display: Optional[SchemaEnvironmentClassUnionMember5Display] = None

    enum: Optional[SchemaEnvironmentClassUnionMember5Enum] = None

    int: Optional[SchemaEnvironmentClassUnionMember5Int] = None

    name: Optional[str] = None

    required: Optional[builtins.bool] = None

    secret: Optional[builtins.bool] = None

    string: Optional[SchemaEnvironmentClassUnionMember5String] = None


SchemaEnvironmentClass: TypeAlias = Union[
    SchemaEnvironmentClassUnionMember0,
    SchemaEnvironmentClassUnionMember1,
    SchemaEnvironmentClassUnionMember2,
    SchemaEnvironmentClassUnionMember3,
    SchemaEnvironmentClassUnionMember4,
    SchemaEnvironmentClassUnionMember5,
]


class SchemaRunnerConfigUnionMember0Bool(BaseModel):
    default: Optional[bool] = None


class SchemaRunnerConfigUnionMember0Display(BaseModel):
    default: Optional[str] = None


class SchemaRunnerConfigUnionMember0Enum(BaseModel):
    default: Optional[str] = None

    values: Optional[List[str]] = None


class SchemaRunnerConfigUnionMember0Int(BaseModel):
    default: Optional[int] = None

    max: Optional[int] = None

    min: Optional[int] = None


class SchemaRunnerConfigUnionMember0String(BaseModel):
    default: Optional[str] = None

    pattern: Optional[str] = None


class SchemaRunnerConfigUnionMember0(BaseModel):
    bool: SchemaRunnerConfigUnionMember0Bool

    id: Optional[str] = None

    description: Optional[str] = None

    display: Optional[SchemaRunnerConfigUnionMember0Display] = None

    enum: Optional[SchemaRunnerConfigUnionMember0Enum] = None

    int: Optional[SchemaRunnerConfigUnionMember0Int] = None

    name: Optional[str] = None

    required: Optional[builtins.bool] = None

    secret: Optional[builtins.bool] = None

    string: Optional[SchemaRunnerConfigUnionMember0String] = None


class SchemaRunnerConfigUnionMember1Display(BaseModel):
    default: Optional[str] = None


class SchemaRunnerConfigUnionMember1Bool(BaseModel):
    default: Optional[bool] = None


class SchemaRunnerConfigUnionMember1Enum(BaseModel):
    default: Optional[str] = None

    values: Optional[List[str]] = None


class SchemaRunnerConfigUnionMember1Int(BaseModel):
    default: Optional[int] = None

    max: Optional[int] = None

    min: Optional[int] = None


class SchemaRunnerConfigUnionMember1String(BaseModel):
    default: Optional[str] = None

    pattern: Optional[str] = None


class SchemaRunnerConfigUnionMember1(BaseModel):
    display: SchemaRunnerConfigUnionMember1Display

    id: Optional[str] = None

    bool: Optional[SchemaRunnerConfigUnionMember1Bool] = None

    description: Optional[str] = None

    enum: Optional[SchemaRunnerConfigUnionMember1Enum] = None

    int: Optional[SchemaRunnerConfigUnionMember1Int] = None

    name: Optional[str] = None

    required: Optional[builtins.bool] = None

    secret: Optional[builtins.bool] = None

    string: Optional[SchemaRunnerConfigUnionMember1String] = None


class SchemaRunnerConfigUnionMember2Enum(BaseModel):
    default: Optional[str] = None

    values: Optional[List[str]] = None


class SchemaRunnerConfigUnionMember2Bool(BaseModel):
    default: Optional[bool] = None


class SchemaRunnerConfigUnionMember2Display(BaseModel):
    default: Optional[str] = None


class SchemaRunnerConfigUnionMember2Int(BaseModel):
    default: Optional[int] = None

    max: Optional[int] = None

    min: Optional[int] = None


class SchemaRunnerConfigUnionMember2String(BaseModel):
    default: Optional[str] = None

    pattern: Optional[str] = None


class SchemaRunnerConfigUnionMember2(BaseModel):
    enum: SchemaRunnerConfigUnionMember2Enum

    id: Optional[str] = None

    bool: Optional[SchemaRunnerConfigUnionMember2Bool] = None

    description: Optional[str] = None

    display: Optional[SchemaRunnerConfigUnionMember2Display] = None

    int: Optional[SchemaRunnerConfigUnionMember2Int] = None

    name: Optional[str] = None

    required: Optional[builtins.bool] = None

    secret: Optional[builtins.bool] = None

    string: Optional[SchemaRunnerConfigUnionMember2String] = None


class SchemaRunnerConfigUnionMember3Int(BaseModel):
    default: Optional[int] = None

    max: Optional[int] = None

    min: Optional[int] = None


class SchemaRunnerConfigUnionMember3Bool(BaseModel):
    default: Optional[bool] = None


class SchemaRunnerConfigUnionMember3Display(BaseModel):
    default: Optional[str] = None


class SchemaRunnerConfigUnionMember3Enum(BaseModel):
    default: Optional[str] = None

    values: Optional[List[str]] = None


class SchemaRunnerConfigUnionMember3String(BaseModel):
    default: Optional[str] = None

    pattern: Optional[str] = None


class SchemaRunnerConfigUnionMember3(BaseModel):
    int: SchemaRunnerConfigUnionMember3Int

    id: Optional[str] = None

    bool: Optional[SchemaRunnerConfigUnionMember3Bool] = None

    description: Optional[str] = None

    display: Optional[SchemaRunnerConfigUnionMember3Display] = None

    enum: Optional[SchemaRunnerConfigUnionMember3Enum] = None

    name: Optional[str] = None

    required: Optional[builtins.bool] = None

    secret: Optional[builtins.bool] = None

    string: Optional[SchemaRunnerConfigUnionMember3String] = None


class SchemaRunnerConfigUnionMember4String(BaseModel):
    default: Optional[str] = None

    pattern: Optional[str] = None


class SchemaRunnerConfigUnionMember4Bool(BaseModel):
    default: Optional[bool] = None


class SchemaRunnerConfigUnionMember4Display(BaseModel):
    default: Optional[str] = None


class SchemaRunnerConfigUnionMember4Enum(BaseModel):
    default: Optional[str] = None

    values: Optional[List[str]] = None


class SchemaRunnerConfigUnionMember4Int(BaseModel):
    default: Optional[int] = None

    max: Optional[int] = None

    min: Optional[int] = None


class SchemaRunnerConfigUnionMember4(BaseModel):
    string: SchemaRunnerConfigUnionMember4String

    id: Optional[str] = None

    bool: Optional[SchemaRunnerConfigUnionMember4Bool] = None

    description: Optional[str] = None

    display: Optional[SchemaRunnerConfigUnionMember4Display] = None

    enum: Optional[SchemaRunnerConfigUnionMember4Enum] = None

    int: Optional[SchemaRunnerConfigUnionMember4Int] = None

    name: Optional[str] = None

    required: Optional[builtins.bool] = None

    secret: Optional[builtins.bool] = None


class SchemaRunnerConfigUnionMember5Bool(BaseModel):
    default: Optional[bool] = None


class SchemaRunnerConfigUnionMember5Display(BaseModel):
    default: Optional[str] = None


class SchemaRunnerConfigUnionMember5Enum(BaseModel):
    default: Optional[str] = None

    values: Optional[List[str]] = None


class SchemaRunnerConfigUnionMember5Int(BaseModel):
    default: Optional[int] = None

    max: Optional[int] = None

    min: Optional[int] = None


class SchemaRunnerConfigUnionMember5String(BaseModel):
    default: Optional[str] = None

    pattern: Optional[str] = None


class SchemaRunnerConfigUnionMember5(BaseModel):
    id: Optional[str] = None

    bool: Optional[SchemaRunnerConfigUnionMember5Bool] = None

    description: Optional[str] = None

    display: Optional[SchemaRunnerConfigUnionMember5Display] = None

    enum: Optional[SchemaRunnerConfigUnionMember5Enum] = None

    int: Optional[SchemaRunnerConfigUnionMember5Int] = None

    name: Optional[str] = None

    required: Optional[builtins.bool] = None

    secret: Optional[builtins.bool] = None

    string: Optional[SchemaRunnerConfigUnionMember5String] = None


SchemaRunnerConfig: TypeAlias = Union[
    SchemaRunnerConfigUnionMember0,
    SchemaRunnerConfigUnionMember1,
    SchemaRunnerConfigUnionMember2,
    SchemaRunnerConfigUnionMember3,
    SchemaRunnerConfigUnionMember4,
    SchemaRunnerConfigUnionMember5,
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
