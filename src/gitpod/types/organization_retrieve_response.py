# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel
from .organization import Organization

__all__ = ["OrganizationRetrieveResponse"]


class OrganizationRetrieveResponse(BaseModel):
    organization: Organization
    """organization is the requested organization"""
