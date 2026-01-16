# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ScimConfigurationUpdateParams"]


class ScimConfigurationUpdateParams(TypedDict, total=False):
    scim_configuration_id: Required[Annotated[str, PropertyInfo(alias="scimConfigurationId")]]
    """scim_configuration_id is the ID of the SCIM configuration to update"""

    enabled: Optional[bool]
    """enabled controls whether SCIM provisioning is active"""

    name: Optional[str]
    """name is a human-readable name for the SCIM configuration"""

    sso_configuration_id: Annotated[Optional[str], PropertyInfo(alias="ssoConfigurationId")]
    """sso_configuration_id is the SSO configuration to link"""
