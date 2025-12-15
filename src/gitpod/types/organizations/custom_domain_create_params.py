# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .custom_domain_provider import CustomDomainProvider

__all__ = ["CustomDomainCreateParams"]


class CustomDomainCreateParams(TypedDict, total=False):
    domain_name: Required[Annotated[str, PropertyInfo(alias="domainName")]]
    """domain_name is the custom domain name"""

    organization_id: Required[Annotated[str, PropertyInfo(alias="organizationId")]]
    """organization_id is the ID of the organization to create the custom domain for"""

    aws_account_id: Annotated[Optional[str], PropertyInfo(alias="awsAccountId")]
    """aws_account_id is the AWS account ID (deprecated: use cloud_account_id)"""

    cloud_account_id: Annotated[Optional[str], PropertyInfo(alias="cloudAccountId")]
    """
    cloud_account_id is the unified cloud account identifier (AWS Account ID or GCP
    Project ID)
    """

    provider: CustomDomainProvider
    """provider is the cloud provider for this custom domain"""
