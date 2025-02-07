# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .principal import Principal

__all__ = ["Subject"]


class Subject(BaseModel):
    id: Optional[str] = None
    """id is the UUID of the subject"""

    principal: Optional[Principal] = None
    """Principal is the principal of the subject"""
