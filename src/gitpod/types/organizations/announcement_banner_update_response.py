# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .announcement_banner import AnnouncementBanner

__all__ = ["AnnouncementBannerUpdateResponse"]


class AnnouncementBannerUpdateResponse(BaseModel):
    banner: AnnouncementBanner
    """banner is the updated announcement banner configuration"""
