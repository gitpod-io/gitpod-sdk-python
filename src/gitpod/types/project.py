# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .project_phase import ProjectPhase
from .shared.subject import Subject
from .project_metadata import ProjectMetadata
from .environment_initializer import EnvironmentInitializer
from .project_prebuild_configuration import ProjectPrebuildConfiguration
from .shared.project_environment_class import ProjectEnvironmentClass

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
    """Use `environment_classes` instead."""

    id: Optional[str] = None
    """id is the unique identifier for the project"""

    automations_file_path: Optional[str] = FieldInfo(alias="automationsFilePath", default=None)
    """
    automations_file_path is the path to the automations file relative to the repo
    root
    """

    desired_phase: Optional[ProjectPhase] = FieldInfo(alias="desiredPhase", default=None)
    """
    desired_phase is the desired phase of the project When set to DELETED, the
    project is pending deletion
    """

    devcontainer_file_path: Optional[str] = FieldInfo(alias="devcontainerFilePath", default=None)
    """
    devcontainer_file_path is the path to the devcontainer file relative to the repo
    root
    """

    environment_classes: Optional[List[ProjectEnvironmentClass]] = FieldInfo(alias="environmentClasses", default=None)
    """environment_classes is the list of environment classes for the project"""

    initializer: Optional[EnvironmentInitializer] = None
    """initializer is the content initializer"""

    metadata: Optional[ProjectMetadata] = None

    prebuild_configuration: Optional[ProjectPrebuildConfiguration] = FieldInfo(
        alias="prebuildConfiguration", default=None
    )
    """prebuild_configuration defines how prebuilds are created for this project."""

    technical_description: Optional[str] = FieldInfo(alias="technicalDescription", default=None)
    """
    technical_description is a detailed technical description of the project This
    field is not returned by default in GetProject or ListProjects responses
    """

    used_by: Optional[UsedBy] = FieldInfo(alias="usedBy", default=None)
