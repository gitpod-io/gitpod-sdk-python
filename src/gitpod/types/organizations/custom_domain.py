# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .custom_domain_provider import CustomDomainProvider

__all__ = ["CustomDomain"]


class CustomDomain(BaseModel):
    """CustomDomain represents a custom domain configuration for an organization"""

    id: str
    """id is the unique identifier of the custom domain"""

    created_at: datetime = FieldInfo(alias="createdAt")
    """created_at is when the custom domain was created"""

    domain_name: str = FieldInfo(alias="domainName")
    """domain_name is the custom domain name"""

    organization_id: str = FieldInfo(alias="organizationId")
    """organization_id is the ID of the organization this custom domain belongs to"""

    updated_at: datetime = FieldInfo(alias="updatedAt")
    """updated_at is when the custom domain was last updated"""

    aws_account_id: Optional[str] = FieldInfo(alias="awsAccountId", default=None)
    """aws_account_id is the AWS account ID (deprecated: use cloud_account_id)"""

    cloud_account_id: Optional[str] = FieldInfo(alias="cloudAccountId", default=None)
    """
    cloud_account_id is the unified cloud account identifier (AWS Account ID or GCP
    Project ID)
    """

    provider: Optional[CustomDomainProvider] = None
    """provider is the cloud provider for this custom domain"""
