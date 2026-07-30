# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .security_policy import SecurityPolicy

__all__ = ["SecurityPolicyCreateResponse"]


class SecurityPolicyCreateResponse(BaseModel):
    security_policy: SecurityPolicy = FieldInfo(alias="securityPolicy")
