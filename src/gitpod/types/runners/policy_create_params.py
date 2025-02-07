# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from .runner_role import RunnerRole

__all__ = ["PolicyCreateParams"]


class PolicyCreateParams(TypedDict, total=False):
    group_id: Annotated[str, PropertyInfo(alias="groupId")]
    """group_id specifies the group_id identifier"""

    role: RunnerRole

    runner_id: Annotated[str, PropertyInfo(alias="runnerId")]
    """runner_id specifies the project identifier"""
