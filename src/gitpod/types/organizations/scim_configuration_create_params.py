# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ScimConfigurationCreateParams"]


class ScimConfigurationCreateParams(TypedDict, total=False):
    organization_id: Required[Annotated[str, PropertyInfo(alias="organizationId")]]
    """
    organization_id is the ID of the organization to create the SCIM configuration
    for
    """

    sso_configuration_id: Required[Annotated[str, PropertyInfo(alias="ssoConfigurationId")]]
    """
    sso_configuration_id is the SSO configuration to link (required for user
    provisioning)
    """

    name: Optional[str]
    """name is a human-readable name for the SCIM configuration"""
