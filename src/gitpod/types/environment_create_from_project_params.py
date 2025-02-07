# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .environment_spec_param import EnvironmentSpecParam

__all__ = ["EnvironmentCreateFromProjectParams"]


class EnvironmentCreateFromProjectParams(TypedDict, total=False):
    project_id: Annotated[str, PropertyInfo(alias="projectId")]

    spec: EnvironmentSpecParam
    """
    EnvironmentSpec specifies the configuration of an environment for an environment
    start
    """
