# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ScimConfiguration"]


class ScimConfiguration(BaseModel):
    """SCIMConfiguration represents a SCIM 2.0 provisioning configuration"""

    id: str
    """id is the unique identifier of the SCIM configuration"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """created_at is when the SCIM configuration was created"""

    organization_id: str = FieldInfo(alias="organizationId")
    """
    organization_id is the ID of the organization this SCIM configuration belongs to
    """

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """updated_at is when the SCIM configuration was last updated"""

    enabled: Optional[bool] = None
    """enabled indicates if SCIM provisioning is active"""

    name: Optional[str] = None
    """name is a human-readable name for the SCIM configuration"""

    sso_configuration_id: Optional[str] = FieldInfo(alias="ssoConfigurationId", default=None)
    """sso_configuration_id is the linked SSO configuration (optional)"""
