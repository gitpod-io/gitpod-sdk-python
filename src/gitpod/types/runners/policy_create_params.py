# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PolicyCreateParams"]


class PolicyCreateParams(TypedDict, total=False):
    group_id: Annotated[str, PropertyInfo(alias="groupId")]
    """group_id specifies the group_id identifier"""

    role: Literal["RUNNER_ROLE_UNSPECIFIED", "RUNNER_ROLE_ADMIN", "RUNNER_ROLE_USER"]

    runner_id: Annotated[str, PropertyInfo(alias="runnerId")]
    """runner_id specifies the project identifier"""
