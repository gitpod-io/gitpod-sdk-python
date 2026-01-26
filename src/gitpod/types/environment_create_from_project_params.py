# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .environment_spec_param import EnvironmentSpecParam

__all__ = ["EnvironmentCreateFromProjectParams"]


class EnvironmentCreateFromProjectParams(TypedDict, total=False):
    name: Optional[str]
    """
    name is a user-defined identifier for the environment. If not specified, the
    system will generate a name.
    """

    project_id: Annotated[str, PropertyInfo(alias="projectId")]

    spec: EnvironmentSpecParam
    """
    Spec is the configuration of the environment that's required for the runner to
    start the environment Configuration already defined in the Project will override
    parts of the spec, if set
    """
