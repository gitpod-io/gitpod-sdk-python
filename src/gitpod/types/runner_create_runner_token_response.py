# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["RunnerCreateRunnerTokenResponse"]


class RunnerCreateRunnerTokenResponse(BaseModel):
    exchange_token: Optional[str] = FieldInfo(alias="exchangeToken", default=None)
    """
    exchange_token is a one-time use token that should be exchanged by the runner
    for an access token, using the IdentityService.ExchangeToken rpc. The token
    expires after 24 hours.
    """
