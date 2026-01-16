# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .scim_configuration import ScimConfiguration

__all__ = ["ScimConfigurationUpdateResponse"]


class ScimConfigurationUpdateResponse(BaseModel):
    scim_configuration: ScimConfiguration = FieldInfo(alias="scimConfiguration")
    """scim_configuration is the updated SCIM configuration"""
