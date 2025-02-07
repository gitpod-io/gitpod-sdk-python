# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .runner import Runner
from .._models import BaseModel

__all__ = ["RunnerRetrieveResponse"]


class RunnerRetrieveResponse(BaseModel):
    runner: Optional[Runner] = None
