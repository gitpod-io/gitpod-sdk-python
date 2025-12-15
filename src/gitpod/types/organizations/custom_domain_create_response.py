# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .custom_domain import CustomDomain

__all__ = ["CustomDomainCreateResponse"]


class CustomDomainCreateResponse(BaseModel):
    """CreateCustomDomainResponse is the response message for creating a custom domain"""

    custom_domain: CustomDomain = FieldInfo(alias="customDomain")
    """custom_domain is the created custom domain"""
