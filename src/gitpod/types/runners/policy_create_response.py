# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .runner_policy import RunnerPolicy

__all__ = ["PolicyCreateResponse"]


class PolicyCreateResponse(BaseModel):
    policy: Optional[RunnerPolicy] = None
