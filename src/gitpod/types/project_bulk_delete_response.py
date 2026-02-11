# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ProjectBulkDeleteResponse", "FailedProject"]


class FailedProject(BaseModel):
    error: Optional[str] = None
    """error describes why the project deletion failed"""

    index: Optional[int] = None
    """index is the position in the request array (0-based)"""

    project_id: Optional[str] = FieldInfo(alias="projectId", default=None)
    """project_id is the project ID that failed"""


class ProjectBulkDeleteResponse(BaseModel):
    deleted_project_ids: Optional[List[str]] = FieldInfo(alias="deletedProjectIds", default=None)
    """deleted_project_ids contains the IDs of successfully deleted projects"""

    failed_projects: Optional[List[FailedProject]] = FieldInfo(alias="failedProjects", default=None)
    """failed_projects contains details about projects that failed to delete"""
