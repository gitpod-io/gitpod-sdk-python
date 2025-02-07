# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ScmIntegrationValidationResult"]


class ScmIntegrationValidationResult(BaseModel):
    host_error: Optional[str] = FieldInfo(alias="hostError", default=None)

    oauth_error: Optional[str] = FieldInfo(alias="oauthError", default=None)

    pat_error: Optional[str] = FieldInfo(alias="patError", default=None)

    scm_id_error: Optional[str] = FieldInfo(alias="scmIdError", default=None)

    valid: Optional[bool] = None
