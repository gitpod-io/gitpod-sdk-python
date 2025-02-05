# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EnvironmentCreateLogsTokenParams"]


class EnvironmentCreateLogsTokenParams(TypedDict, total=False):
    environment_id: Annotated[str, PropertyInfo(alias="environmentId")]
    """
    environment_id specifies the environment for which the logs token should be
    created.

    +required
    """
