# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .environment import Environment

__all__ = ["EnvironmentCreateFromProjectResponse"]


class EnvironmentCreateFromProjectResponse(BaseModel):
    environment: Optional[Environment] = None
    """+resource get environment"""
