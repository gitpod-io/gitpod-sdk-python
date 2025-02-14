# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .sso_configuration import SSOConfiguration

__all__ = ["SSOConfigurationCreateResponse"]


class SSOConfigurationCreateResponse(BaseModel):
    sso_configuration: SSOConfiguration = FieldInfo(alias="ssoConfiguration")
    """sso_configuration is the created SSO configuration"""
