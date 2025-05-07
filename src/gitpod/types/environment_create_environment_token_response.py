# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EnvironmentCreateEnvironmentTokenResponse"]


class EnvironmentCreateEnvironmentTokenResponse(BaseModel):
    access_token: str = FieldInfo(alias="accessToken")
    """access_token is the token that can be used for environment authentication"""
