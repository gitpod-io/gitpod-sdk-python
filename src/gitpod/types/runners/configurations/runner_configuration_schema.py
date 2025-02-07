# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "RunnerConfigurationSchema",
    "EnvironmentClass",
    "EnvironmentClassBool",
    "EnvironmentClassDisplay",
    "EnvironmentClassEnum",
    "EnvironmentClassInt",
    "EnvironmentClassString",
    "RunnerConfig",
    "RunnerConfigBool",
    "RunnerConfigDisplay",
    "RunnerConfigEnum",
    "RunnerConfigInt",
    "RunnerConfigString",
    "Scm",
    "ScmOAuth",
    "ScmPat",
]


class EnvironmentClassBool(BaseModel):
    default: Optional[bool] = None


class EnvironmentClassDisplay(BaseModel):
    default: Optional[str] = None


class EnvironmentClassEnum(BaseModel):
    default: Optional[str] = None

    values: Optional[List[str]] = None


class EnvironmentClassInt(BaseModel):
    default: Optional[int] = None

    max: Optional[int] = None

    min: Optional[int] = None


class EnvironmentClassString(BaseModel):
    default: Optional[str] = None

    pattern: Optional[str] = None


class EnvironmentClass(BaseModel):
    id: Optional[str] = None

    bool: Optional[EnvironmentClassBool] = None

    description: Optional[str] = None

    display: Optional[EnvironmentClassDisplay] = None

    enum: Optional[EnvironmentClassEnum] = None

    int: Optional[EnvironmentClassInt] = None

    name: Optional[str] = None

    required: Optional[builtins.bool] = None

    secret: Optional[builtins.bool] = None

    string: Optional[EnvironmentClassString] = None


class RunnerConfigBool(BaseModel):
    default: Optional[bool] = None


class RunnerConfigDisplay(BaseModel):
    default: Optional[str] = None


class RunnerConfigEnum(BaseModel):
    default: Optional[str] = None

    values: Optional[List[str]] = None


class RunnerConfigInt(BaseModel):
    default: Optional[int] = None

    max: Optional[int] = None

    min: Optional[int] = None


class RunnerConfigString(BaseModel):
    default: Optional[str] = None

    pattern: Optional[str] = None


class RunnerConfig(BaseModel):
    id: Optional[str] = None

    bool: Optional[RunnerConfigBool] = None

    description: Optional[str] = None

    display: Optional[RunnerConfigDisplay] = None

    enum: Optional[RunnerConfigEnum] = None

    int: Optional[RunnerConfigInt] = None

    name: Optional[str] = None

    required: Optional[builtins.bool] = None

    secret: Optional[builtins.bool] = None

    string: Optional[RunnerConfigString] = None


class ScmOAuth(BaseModel):
    callback_url: Optional[str] = FieldInfo(alias="callbackUrl", default=None)
    """
    callback_url is the URL the OAuth app will redirect to after the user has
    authenticated.
    """


class ScmPat(BaseModel):
    description: Optional[str] = None
    """description is a human-readable description of the PAT."""

    docs_link: Optional[str] = FieldInfo(alias="docsLink", default=None)
    """
    docs_link is a link to the documentation on how to create a PAT for this SCM
    system.
    """


class Scm(BaseModel):
    default_hosts: Optional[List[str]] = FieldInfo(alias="defaultHosts", default=None)

    name: Optional[str] = None

    oauth: Optional[ScmOAuth] = None

    pat: Optional[ScmPat] = None

    scm_id: Optional[str] = FieldInfo(alias="scmId", default=None)


class RunnerConfigurationSchema(BaseModel):
    environment_classes: Optional[List[EnvironmentClass]] = FieldInfo(alias="environmentClasses", default=None)

    runner_config: Optional[List[RunnerConfig]] = FieldInfo(alias="runnerConfig", default=None)

    scm: Optional[List[Scm]] = None

    version: Optional[str] = None
    """The schema version"""
