# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AnnouncementBannerUpdateParams"]


class AnnouncementBannerUpdateParams(TypedDict, total=False):
    organization_id: Required[Annotated[str, PropertyInfo(alias="organizationId")]]
    """organization_id is the ID of the organization"""

    enabled: Optional[bool]
    """enabled controls whether the banner is displayed"""

    message: Optional[str]
    """message is the banner message.

    Supports basic Markdown. Maximum 1000 characters.
    """
