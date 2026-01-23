# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .announcement_banner import AnnouncementBanner

__all__ = ["AnnouncementBannerGetResponse"]


class AnnouncementBannerGetResponse(BaseModel):
    banner: AnnouncementBanner
    """banner is the announcement banner configuration"""
