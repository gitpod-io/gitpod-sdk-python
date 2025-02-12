# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from ...shared.task import Task

__all__ = ["TaskCreateResponse"]


class TaskCreateResponse(BaseModel):
    task: Optional[Task] = None
