# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .project_policy import ProjectPolicy

__all__ = ["PolicyCreateResponse"]


class PolicyCreateResponse(BaseModel):
    policy: Optional[ProjectPolicy] = None
