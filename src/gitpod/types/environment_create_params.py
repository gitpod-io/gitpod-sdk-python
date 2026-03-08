# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .environment_spec_param import EnvironmentSpecParam

__all__ = ["EnvironmentCreateParams"]


class EnvironmentCreateParams(TypedDict, total=False):
    name: Optional[str]
    """
    name is a user-defined identifier for the environment. If not specified, the
    system will generate a name.
    """

    session_id: Annotated[str, PropertyInfo(alias="sessionId")]
    """
    session_id is the ID of the session this environment belongs to. If empty, a new
    session is created implicitly.
    """

    spec: EnvironmentSpecParam
    """
    spec is the configuration of the environment that's required for the to start
    the environment
    """
