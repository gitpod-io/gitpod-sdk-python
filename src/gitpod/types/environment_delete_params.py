# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EnvironmentDeleteParams"]


class EnvironmentDeleteParams(TypedDict, total=False):
    environment_id: Annotated[str, PropertyInfo(alias="environmentId")]
    """environment_id specifies the environment that is going to delete.

    +required
    """

    force: bool
    """
    force indicates whether the environment should be deleted forcefully When force
    deleting an Environment, the Environment is removed immediately and environment
    lifecycle is not respected. Force deleting can result in data loss on the
    environment.
    """
