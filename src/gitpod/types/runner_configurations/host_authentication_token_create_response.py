# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["HostAuthenticationTokenCreateResponse", "Token"]


class Token(BaseModel):
    id: Optional[str] = None

    host: Optional[str] = None

    runner_id: Optional[str] = FieldInfo(alias="runnerId", default=None)

    source: Optional[
        Literal[
            "HOST_AUTHENTICATION_TOKEN_SOURCE_UNSPECIFIED",
            "HOST_AUTHENTICATION_TOKEN_SOURCE_OAUTH",
            "HOST_AUTHENTICATION_TOKEN_SOURCE_PAT",
        ]
    ] = None

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)


class HostAuthenticationTokenCreateResponse(BaseModel):
    token: Optional[Token] = None
