# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "ConfigurationValidateResponse",
    "UnionMember0",
    "UnionMember0EnvironmentClass",
    "UnionMember0ScmIntegration",
    "UnionMember1",
    "UnionMember1ScmIntegration",
    "UnionMember1EnvironmentClass",
    "UnionMember2",
    "UnionMember2EnvironmentClass",
    "UnionMember2ScmIntegration",
]


class UnionMember0EnvironmentClass:
    pass


class UnionMember0ScmIntegration:
    pass


class UnionMember0(BaseModel):
    environment_class: UnionMember0EnvironmentClass = FieldInfo(alias="environmentClass")

    scm_integration: Optional[UnionMember0ScmIntegration] = FieldInfo(alias="scmIntegration", default=None)


class UnionMember1ScmIntegration:
    pass


class UnionMember1EnvironmentClass:
    pass


class UnionMember1(BaseModel):
    scm_integration: UnionMember1ScmIntegration = FieldInfo(alias="scmIntegration")

    environment_class: Optional[UnionMember1EnvironmentClass] = FieldInfo(alias="environmentClass", default=None)


class UnionMember2EnvironmentClass:
    pass


class UnionMember2ScmIntegration:
    pass


class UnionMember2(BaseModel):
    environment_class: Optional[UnionMember2EnvironmentClass] = FieldInfo(alias="environmentClass", default=None)

    scm_integration: Optional[UnionMember2ScmIntegration] = FieldInfo(alias="scmIntegration", default=None)


ConfigurationValidateResponse: TypeAlias = Union[UnionMember0, UnionMember1, UnionMember2]
