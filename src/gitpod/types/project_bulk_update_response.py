# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .project import Project
from .._models import BaseModel

__all__ = ["ProjectBulkUpdateResponse", "FailedProject"]


class FailedProject(BaseModel):
    error: Optional[str] = None
    """error describes why the project update failed"""

    index: Optional[int] = None
    """index is the position in the request array (0-based)"""

    project_id: Optional[str] = FieldInfo(alias="projectId", default=None)
    """project_id is the project ID that failed"""


class ProjectBulkUpdateResponse(BaseModel):
    failed_projects: Optional[List[FailedProject]] = FieldInfo(alias="failedProjects", default=None)
    """failed_projects contains details about projects that failed to update"""

    updated_projects: Optional[List[Project]] = FieldInfo(alias="updatedProjects", default=None)
    """updated_projects contains the successfully updated projects"""
