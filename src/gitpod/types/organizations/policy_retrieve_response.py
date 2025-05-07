# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .organization_policies import OrganizationPolicies

__all__ = ["PolicyRetrieveResponse"]


class PolicyRetrieveResponse(BaseModel):
    policies: OrganizationPolicies
