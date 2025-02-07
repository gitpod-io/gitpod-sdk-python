# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .project import Project
from .._models import BaseModel

__all__ = ["ProjectCreateFromEnvironmentResponse"]


class ProjectCreateFromEnvironmentResponse(BaseModel):
    project: Optional[Project] = None
