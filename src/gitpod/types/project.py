# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.subject import Subject
from .project_metadata import ProjectMetadata
from .environment_initializer import EnvironmentInitializer
from .project_environment_class import ProjectEnvironmentClass

__all__ = ["Project", "UsedBy"]


class UsedBy(BaseModel):
    subjects: Optional[List[Subject]] = None
    """
    Subjects are the 10 most recent subjects who have used the project to create an
    environment
    """

    total_subjects: Optional[int] = FieldInfo(alias="totalSubjects", default=None)
    """Total number of unique subjects who have used the project"""


class Project(BaseModel):
    environment_class: ProjectEnvironmentClass = FieldInfo(alias="environmentClass")

    id: Optional[str] = None
    """id is the unique identifier for the project"""

    automations_file_path: Optional[str] = FieldInfo(alias="automationsFilePath", default=None)
    """
    automations_file_path is the path to the automations file relative to the repo
    root
    """

    devcontainer_file_path: Optional[str] = FieldInfo(alias="devcontainerFilePath", default=None)
    """
    devcontainer_file_path is the path to the devcontainer file relative to the repo
    root
    """

    initializer: Optional[EnvironmentInitializer] = None
    """EnvironmentInitializer specifies how an environment is to be initialized"""

    metadata: Optional[ProjectMetadata] = None

    used_by: Optional[UsedBy] = FieldInfo(alias="usedBy", default=None)
