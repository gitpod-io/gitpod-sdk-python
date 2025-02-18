# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .service_spec import ServiceSpec
from .service_status import ServiceStatus
from .service_metadata import ServiceMetadata

__all__ = ["Service"]


class Service(BaseModel):
    id: str

    environment_id: Optional[str] = FieldInfo(alias="environmentId", default=None)

    metadata: Optional[ServiceMetadata] = None

    spec: Optional[ServiceSpec] = None

    status: Optional[ServiceStatus] = None
