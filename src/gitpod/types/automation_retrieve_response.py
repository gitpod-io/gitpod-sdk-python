# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .workflow import Workflow

__all__ = ["AutomationRetrieveResponse"]


class AutomationRetrieveResponse(BaseModel):
    workflow: Optional[Workflow] = None
    """Workflow represents a workflow configuration."""
