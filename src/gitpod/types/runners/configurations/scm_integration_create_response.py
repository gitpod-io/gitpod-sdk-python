# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["ScmIntegrationCreateResponse"]


class ScmIntegrationCreateResponse(BaseModel):
    id: Optional[str] = None
    """id is a uniquely generated identifier for the SCM integration"""
