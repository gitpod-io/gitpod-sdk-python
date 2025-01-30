# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import List, Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "ConfigurationSchemaRetrieveResponse",
    "Schema",
    "SchemaEnvironmentClass",
    "SchemaEnvironmentClassBool",
    "SchemaEnvironmentClassBoolBool",
    "SchemaEnvironmentClassDisplay",
    "SchemaEnvironmentClassDisplayDisplay",
    "SchemaEnvironmentClassEnum",
    "SchemaEnvironmentClassEnumEnum",
    "SchemaEnvironmentClassInt",
    "SchemaEnvironmentClassIntInt",
    "SchemaEnvironmentClassString",
    "SchemaEnvironmentClassStringString",
    "SchemaRunnerConfig",
    "SchemaRunnerConfigBool",
    "SchemaRunnerConfigBoolBool",
    "SchemaRunnerConfigDisplay",
    "SchemaRunnerConfigDisplayDisplay",
    "SchemaRunnerConfigEnum",
    "SchemaRunnerConfigEnumEnum",
    "SchemaRunnerConfigInt",
    "SchemaRunnerConfigIntInt",
    "SchemaRunnerConfigString",
    "SchemaRunnerConfigStringString",
    "SchemaScm",
    "SchemaScmOAuth",
    "SchemaScmPat",
]


class SchemaEnvironmentClassBoolBool(BaseModel):
    default: Optional[bool] = None


class SchemaEnvironmentClassBool(BaseModel):
    bool: SchemaEnvironmentClassBoolBool

    id: Optional[str] = None

    description: Optional[str] = None

    name: Optional[str] = None

    required: Optional[builtins.bool] = None

    secret: Optional[builtins.bool] = None


class SchemaEnvironmentClassDisplayDisplay(BaseModel):
    default: Optional[str] = None


class SchemaEnvironmentClassDisplay(BaseModel):
    display: SchemaEnvironmentClassDisplayDisplay

    id: Optional[str] = None

    description: Optional[str] = None

    name: Optional[str] = None

    required: Optional[bool] = None

    secret: Optional[bool] = None


class SchemaEnvironmentClassEnumEnum(BaseModel):
    default: Optional[str] = None

    values: Optional[List[str]] = None


class SchemaEnvironmentClassEnum(BaseModel):
    enum: SchemaEnvironmentClassEnumEnum

    id: Optional[str] = None

    description: Optional[str] = None

    name: Optional[str] = None

    required: Optional[bool] = None

    secret: Optional[bool] = None


class SchemaEnvironmentClassIntInt(BaseModel):
    default: Optional[int] = None

    max: Optional[int] = None

    min: Optional[int] = None


class SchemaEnvironmentClassInt(BaseModel):
    int: SchemaEnvironmentClassIntInt

    id: Optional[str] = None

    description: Optional[str] = None

    name: Optional[str] = None

    required: Optional[bool] = None

    secret: Optional[bool] = None


class SchemaEnvironmentClassStringString(BaseModel):
    default: Optional[str] = None

    pattern: Optional[str] = None


class SchemaEnvironmentClassString(BaseModel):
    string: SchemaEnvironmentClassStringString

    id: Optional[str] = None

    description: Optional[str] = None

    name: Optional[str] = None

    required: Optional[bool] = None

    secret: Optional[bool] = None


SchemaEnvironmentClass: TypeAlias = Union[
    SchemaEnvironmentClassBool,
    SchemaEnvironmentClassDisplay,
    SchemaEnvironmentClassEnum,
    SchemaEnvironmentClassInt,
    SchemaEnvironmentClassString,
]


class SchemaRunnerConfigBoolBool(BaseModel):
    default: Optional[bool] = None


class SchemaRunnerConfigBool(BaseModel):
    bool: SchemaRunnerConfigBoolBool

    id: Optional[str] = None

    description: Optional[str] = None

    name: Optional[str] = None

    required: Optional[builtins.bool] = None

    secret: Optional[builtins.bool] = None


class SchemaRunnerConfigDisplayDisplay(BaseModel):
    default: Optional[str] = None


class SchemaRunnerConfigDisplay(BaseModel):
    display: SchemaRunnerConfigDisplayDisplay

    id: Optional[str] = None

    description: Optional[str] = None

    name: Optional[str] = None

    required: Optional[bool] = None

    secret: Optional[bool] = None


class SchemaRunnerConfigEnumEnum(BaseModel):
    default: Optional[str] = None

    values: Optional[List[str]] = None


class SchemaRunnerConfigEnum(BaseModel):
    enum: SchemaRunnerConfigEnumEnum

    id: Optional[str] = None

    description: Optional[str] = None

    name: Optional[str] = None

    required: Optional[bool] = None

    secret: Optional[bool] = None


class SchemaRunnerConfigIntInt(BaseModel):
    default: Optional[int] = None

    max: Optional[int] = None

    min: Optional[int] = None


class SchemaRunnerConfigInt(BaseModel):
    int: SchemaRunnerConfigIntInt

    id: Optional[str] = None

    description: Optional[str] = None

    name: Optional[str] = None

    required: Optional[bool] = None

    secret: Optional[bool] = None


class SchemaRunnerConfigStringString(BaseModel):
    default: Optional[str] = None

    pattern: Optional[str] = None


class SchemaRunnerConfigString(BaseModel):
    string: SchemaRunnerConfigStringString

    id: Optional[str] = None

    description: Optional[str] = None

    name: Optional[str] = None

    required: Optional[bool] = None

    secret: Optional[bool] = None


SchemaRunnerConfig: TypeAlias = Union[
    SchemaRunnerConfigBool,
    SchemaRunnerConfigDisplay,
    SchemaRunnerConfigEnum,
    SchemaRunnerConfigInt,
    SchemaRunnerConfigString,
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


class ConfigurationSchemaRetrieveResponse(BaseModel):
    schema_: Optional[Schema] = FieldInfo(alias="schema", default=None)
