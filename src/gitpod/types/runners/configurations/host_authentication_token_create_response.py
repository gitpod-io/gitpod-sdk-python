# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ...._models import BaseModel
from .host_authentication_token import HostAuthenticationToken

__all__ = ["HostAuthenticationTokenCreateResponse"]


class HostAuthenticationTokenCreateResponse(BaseModel):
    token: HostAuthenticationToken
