# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EnvironmentStartParams"]


class EnvironmentStartParams(TypedDict, total=False):
    acknowledge_token: Annotated[str, PropertyInfo(alias="acknowledgeToken")]
    """
    acknowledge_token is the HMAC token from a previous
    EnvironmentMaxLifetimeEnforcementDetails response, allowing the user to start an
    environment past its max lifetime in warn mode.
    """

    environment_id: Annotated[str, PropertyInfo(alias="environmentId")]
    """environment_id specifies which environment should be started."""
