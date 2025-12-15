# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .prebuild_spec import PrebuildSpec
from .prebuild_status import PrebuildStatus
from .prebuild_metadata import PrebuildMetadata

__all__ = ["Prebuild"]


class Prebuild(BaseModel):
    """
    Prebuild represents a prebuild for a project that creates a snapshot
     for faster environment startup times.
    """

    metadata: PrebuildMetadata
    """metadata contains organizational and ownership information"""

    spec: PrebuildSpec
    """spec contains the configuration used to create this prebuild"""

    status: PrebuildStatus
    """status contains the current status and progress of the prebuild"""

    id: Optional[str] = None
    """id is the unique identifier for the prebuild"""
