# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .organization import Organization

__all__ = ["OrganizationUpdateResponse"]


class OrganizationUpdateResponse(BaseModel):
    organization: Optional[Organization] = None
    """organization is the updated organization"""
