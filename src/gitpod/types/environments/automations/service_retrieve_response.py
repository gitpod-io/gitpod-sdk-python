# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .service import Service
from ...._models import BaseModel

__all__ = ["ServiceRetrieveResponse"]


class ServiceRetrieveResponse(BaseModel):
    service: Optional[Service] = None
