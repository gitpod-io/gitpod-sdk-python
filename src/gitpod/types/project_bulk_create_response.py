# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .project import Project
from .._models import BaseModel

__all__ = ["ProjectBulkCreateResponse", "FailedProject"]


class FailedProject(BaseModel):
    error: Optional[str] = None
    """error describes why the project creation failed"""

    index: Optional[int] = None
    """index is the position in the request array (0-based)"""

    name: Optional[str] = None
    """name is the project name that failed"""


class ProjectBulkCreateResponse(BaseModel):
    created_projects: Optional[List[Project]] = FieldInfo(alias="createdProjects", default=None)
    """created_projects contains the successfully created projects"""

    failed_projects: Optional[List[FailedProject]] = FieldInfo(alias="failedProjects", default=None)
    """failed_projects contains details about projects that failed to create"""
