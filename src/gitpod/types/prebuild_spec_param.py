# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .prebuild_phase import PrebuildPhase

__all__ = ["PrebuildSpecParam"]


class PrebuildSpecParam(TypedDict, total=False):
    """PrebuildSpec contains the configuration used to create a prebuild"""

    desired_phase: Annotated[PrebuildPhase, PropertyInfo(alias="desiredPhase")]
    """
    desired_phase is the desired phase of the prebuild. Used to signal cancellation
    or other state changes. This field is managed by the API and reconciler.
    """

    spec_version: Annotated[str, PropertyInfo(alias="specVersion")]
    """
    spec_version is incremented each time the spec is updated. Used for optimistic
    concurrency control.
    """

    timeout: str
    """
    timeout is the maximum time allowed for the prebuild to complete. Defaults to 60
    minutes if not specified. Maximum allowed timeout is 2 hours.
    """
