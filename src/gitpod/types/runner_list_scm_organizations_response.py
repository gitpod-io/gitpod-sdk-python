# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["RunnerListScmOrganizationsResponse", "Organization"]


class Organization(BaseModel):
    is_admin: Optional[bool] = FieldInfo(alias="isAdmin", default=None)
    """
    Deprecated: this field is unused by all known consumers and is scheduled for
    removal in a future release. Do not read it.

    Originally intended to gate organization-level webhook creation in the
    dashboard, but that gating was never implemented. Populating this field on the
    GitLab path requires a second fully-paginated ListGroups call, which is the main
    reason we are deprecating it.
    """

    name: Optional[str] = None
    """Organization name/slug (e.g., "gitpod-io")"""

    url: Optional[str] = None
    """Organization URL (e.g., "https://github.com/gitpod-io")"""


class RunnerListScmOrganizationsResponse(BaseModel):
    organizations: Optional[List[Organization]] = None
    """List of organizations the user belongs to"""
