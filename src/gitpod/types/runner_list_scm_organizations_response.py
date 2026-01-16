# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["RunnerListScmOrganizationsResponse", "Organization"]


class Organization(BaseModel):
    is_admin: Optional[bool] = FieldInfo(alias="isAdmin", default=None)
    """
    Whether the user has admin permissions in this organization. Admin permissions
    typically allow creating organization-level webhooks.
    """

    name: Optional[str] = None
    """Organization name/slug (e.g., "gitpod-io")"""

    url: Optional[str] = None
    """Organization URL (e.g., "https://github.com/gitpod-io")"""


class RunnerListScmOrganizationsResponse(BaseModel):
    organizations: Optional[List[Organization]] = None
    """List of organizations the user belongs to"""
