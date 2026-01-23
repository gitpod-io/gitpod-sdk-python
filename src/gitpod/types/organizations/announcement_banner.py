# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AnnouncementBanner"]


class AnnouncementBanner(BaseModel):
    organization_id: str = FieldInfo(alias="organizationId")
    """organization_id is the ID of the organization"""

    enabled: Optional[bool] = None
    """enabled controls whether the banner is displayed"""

    message: Optional[str] = None
    """message is the banner message displayed to users. Supports basic Markdown."""
