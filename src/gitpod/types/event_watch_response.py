# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .resource_type import ResourceType
from .resource_operation import ResourceOperation

__all__ = ["EventWatchResponse"]


class EventWatchResponse(BaseModel):
    operation: Optional[ResourceOperation] = None

    resource_id: Optional[str] = FieldInfo(alias="resourceId", default=None)

    resource_type: Optional[ResourceType] = FieldInfo(alias="resourceType", default=None)
