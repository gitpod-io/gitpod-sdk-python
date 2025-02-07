# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.subject import Subject

__all__ = ["IdentityGetAuthenticatedIdentityResponse"]


class IdentityGetAuthenticatedIdentityResponse(BaseModel):
    organization_id: Optional[str] = FieldInfo(alias="organizationId", default=None)

    subject: Optional[Subject] = None
    """subject is the identity of the current user"""
