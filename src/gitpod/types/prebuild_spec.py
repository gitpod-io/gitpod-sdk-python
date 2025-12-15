# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .prebuild_phase import PrebuildPhase

__all__ = ["PrebuildSpec"]


class PrebuildSpec(BaseModel):
    """PrebuildSpec contains the configuration used to create a prebuild"""

    desired_phase: Optional[PrebuildPhase] = FieldInfo(alias="desiredPhase", default=None)
    """
    desired_phase is the desired phase of the prebuild. Used to signal cancellation
    or other state changes. This field is managed by the API and reconciler.
    """

    spec_version: Optional[str] = FieldInfo(alias="specVersion", default=None)
    """
    spec_version is incremented each time the spec is updated. Used for optimistic
    concurrency control.
    """

    timeout: Optional[str] = None
    """
    timeout is the maximum time allowed for the prebuild to complete. Defaults to 60
    minutes if not specified. Maximum allowed timeout is 2 hours.
    """
