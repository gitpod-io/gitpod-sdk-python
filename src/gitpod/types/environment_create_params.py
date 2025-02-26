# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .environment_spec_param import EnvironmentSpecParam

__all__ = ["EnvironmentCreateParams"]


class EnvironmentCreateParams(TypedDict, total=False):
    spec: EnvironmentSpecParam
    """
    spec is the configuration of the environment that's required for the to start
    the environment
    """
