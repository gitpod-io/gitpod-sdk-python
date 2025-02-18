# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ...._models import BaseModel
from .host_authentication_token import HostAuthenticationToken

__all__ = ["HostAuthenticationTokenRetrieveResponse"]


class HostAuthenticationTokenRetrieveResponse(BaseModel):
    token: HostAuthenticationToken
