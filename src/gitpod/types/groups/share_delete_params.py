# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from ..shared.principal import Principal
from ..shared.resource_type import ResourceType

__all__ = ["ShareDeleteParams"]


class ShareDeleteParams(TypedDict, total=False):
    principal: Principal
    """Type of principal to remove access from (user or service account)"""

    principal_id: Annotated[str, PropertyInfo(alias="principalId")]
    """ID of the principal (user or service account) to remove access from"""

    resource_id: Annotated[str, PropertyInfo(alias="resourceId")]
    """ID of the resource to unshare"""

    resource_type: Annotated[ResourceType, PropertyInfo(alias="resourceType")]
    """Type of resource to unshare"""
