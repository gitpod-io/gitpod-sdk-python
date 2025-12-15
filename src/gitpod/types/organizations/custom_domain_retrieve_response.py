# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .custom_domain import CustomDomain

__all__ = ["CustomDomainRetrieveResponse"]


class CustomDomainRetrieveResponse(BaseModel):
    custom_domain: CustomDomain = FieldInfo(alias="customDomain")
    """CustomDomain represents a custom domain configuration for an organization"""
