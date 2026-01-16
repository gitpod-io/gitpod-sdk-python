# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .scim_configuration import ScimConfiguration

__all__ = ["ScimConfigurationCreateResponse"]


class ScimConfigurationCreateResponse(BaseModel):
    token: str
    """
    token is the bearer token for SCIM API authentication. This is only returned
    once during creation - store it securely.
    """

    scim_configuration: ScimConfiguration = FieldInfo(alias="scimConfiguration")
    """scim_configuration is the created SCIM configuration"""
