# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .group import Group
from .._models import BaseModel

__all__ = ["GroupUpdateResponse"]


class GroupUpdateResponse(BaseModel):
    group: Optional[Group] = None
