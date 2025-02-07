# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from .scm_integration import ScmIntegration

__all__ = ["ScmIntegrationRetrieveResponse"]


class ScmIntegrationRetrieveResponse(BaseModel):
    integration: Optional[ScmIntegration] = None
