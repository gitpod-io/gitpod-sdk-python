# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .service import Service
from ...._models import BaseModel

__all__ = ["ServiceRetrieveResponse"]


class ServiceRetrieveResponse(BaseModel):
    service: Service
