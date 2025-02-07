# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .personal_access_token import PersonalAccessToken

__all__ = ["PatGetResponse"]


class PatGetResponse(BaseModel):
    pat: Optional[PersonalAccessToken] = None
