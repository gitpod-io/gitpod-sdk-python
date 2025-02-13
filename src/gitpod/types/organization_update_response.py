# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel
from .organization import Organization

__all__ = ["OrganizationUpdateResponse"]


class OrganizationUpdateResponse(BaseModel):
    organization: Organization
    """organization is the updated organization"""
