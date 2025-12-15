# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SecretScope"]


class SecretScope(BaseModel):
    organization_id: Optional[str] = FieldInfo(alias="organizationId", default=None)
    """organization_id is the Organization ID this Secret belongs to"""

    project_id: Optional[str] = FieldInfo(alias="projectId", default=None)
    """project_id is the Project ID this Secret belongs to"""

    user_id: Optional[str] = FieldInfo(alias="userId", default=None)
    """user_id is the User ID this Secret belongs to"""
