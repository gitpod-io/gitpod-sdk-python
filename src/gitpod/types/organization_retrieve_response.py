# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .organization import Organization

__all__ = ["OrganizationRetrieveResponse"]


class OrganizationRetrieveResponse(BaseModel):
    organization: Optional[Organization] = None
    """organization is the requested organization"""
