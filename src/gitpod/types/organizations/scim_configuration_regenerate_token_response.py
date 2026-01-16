# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ScimConfigurationRegenerateTokenResponse"]


class ScimConfigurationRegenerateTokenResponse(BaseModel):
    token: str
    """
    token is the new bearer token for SCIM API authentication. This invalidates the
    previous token - store it securely.
    """
