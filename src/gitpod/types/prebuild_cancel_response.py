# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .prebuild import Prebuild

__all__ = ["PrebuildCancelResponse"]


class PrebuildCancelResponse(BaseModel):
    prebuild: Prebuild
    """
    Prebuild represents a prebuild for a project that creates a snapshot for faster
    environment startup times.
    """
