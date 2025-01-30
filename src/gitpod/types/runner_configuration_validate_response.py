# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "RunnerConfigurationValidateResponse",
    "EnvironmentClass",
    "EnvironmentClassEnvironmentClass",
    "EnvironmentClassEnvironmentClassDescriptionError",
    "EnvironmentClassEnvironmentClassDisplayNameError",
    "ScmIntegration",
    "ScmIntegrationScmIntegration",
    "ScmIntegrationScmIntegrationHostError",
    "ScmIntegrationScmIntegrationOAuthError",
    "ScmIntegrationScmIntegrationPatError",
    "ScmIntegrationScmIntegrationScmIDError",
]


class EnvironmentClassEnvironmentClassDescriptionError(BaseModel):
    description_error: str = FieldInfo(alias="descriptionError")


class EnvironmentClassEnvironmentClassDisplayNameError(BaseModel):
    display_name_error: str = FieldInfo(alias="displayNameError")


EnvironmentClassEnvironmentClass: TypeAlias = Union[
    EnvironmentClassEnvironmentClassDescriptionError, EnvironmentClassEnvironmentClassDisplayNameError
]


class EnvironmentClass(BaseModel):
    environment_class: EnvironmentClassEnvironmentClass = FieldInfo(alias="environmentClass")


class ScmIntegrationScmIntegrationHostError(BaseModel):
    host_error: str = FieldInfo(alias="hostError")


class ScmIntegrationScmIntegrationOAuthError(BaseModel):
    oauth_error: str = FieldInfo(alias="oauthError")


class ScmIntegrationScmIntegrationPatError(BaseModel):
    pat_error: str = FieldInfo(alias="patError")


class ScmIntegrationScmIntegrationScmIDError(BaseModel):
    scm_id_error: str = FieldInfo(alias="scmIdError")


ScmIntegrationScmIntegration: TypeAlias = Union[
    ScmIntegrationScmIntegrationHostError,
    ScmIntegrationScmIntegrationOAuthError,
    ScmIntegrationScmIntegrationPatError,
    ScmIntegrationScmIntegrationScmIDError,
]


class ScmIntegration(BaseModel):
    scm_integration: ScmIntegrationScmIntegration = FieldInfo(alias="scmIntegration")


RunnerConfigurationValidateResponse: TypeAlias = Union[EnvironmentClass, ScmIntegration]
