# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .sso_configuration import SSOConfiguration

__all__ = ["SSOConfigurationRetrieveResponse"]


class SSOConfigurationRetrieveResponse(BaseModel):
    sso_configuration: Optional[SSOConfiguration] = FieldInfo(alias="ssoConfiguration", default=None)
    """sso_configuration is the SSO configuration identified by the ID"""
