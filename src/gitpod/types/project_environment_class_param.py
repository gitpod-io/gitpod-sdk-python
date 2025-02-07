# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ProjectEnvironmentClassParam"]


class ProjectEnvironmentClassParam(TypedDict, total=False):
    environment_class_id: Annotated[str, PropertyInfo(alias="environmentClassId")]
    """Use a fixed environment class on a given Runner.

    This cannot be a local runner's environment class.
    """

    local_runner: Annotated[bool, PropertyInfo(alias="localRunner")]
    """Use a local runner for the user"""
