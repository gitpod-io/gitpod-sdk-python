# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["HostAuthenticationTokenListResponse", "Pagination", "Token"]


class Pagination(BaseModel):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)
    """Token passed for retreiving the next set of results.

    Empty if there are no more results
    """


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


class HostAuthenticationTokenListResponse(BaseModel):
    pagination: Optional[Pagination] = None

    tokens: Optional[List[Token]] = None
