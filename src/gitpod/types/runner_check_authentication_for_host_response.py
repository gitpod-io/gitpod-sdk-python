# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["RunnerCheckAuthenticationForHostResponse"]


class RunnerCheckAuthenticationForHostResponse(BaseModel):
    authenticated: Optional[bool] = None

    authentication_url: Optional[str] = FieldInfo(alias="authenticationUrl", default=None)

    pat_supported: Optional[bool] = FieldInfo(alias="patSupported", default=None)

    scm_id: Optional[str] = FieldInfo(alias="scmId", default=None)
