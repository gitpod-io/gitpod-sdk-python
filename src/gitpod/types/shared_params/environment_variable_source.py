# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .secret_ref import SecretRef

__all__ = ["EnvironmentVariableSource"]


class EnvironmentVariableSource(TypedDict, total=False):
    """EnvironmentVariableSource specifies a source for an environment variable value."""

    secret_ref: Required[Annotated[SecretRef, PropertyInfo(alias="secretRef")]]
    """secret_ref references a secret by ID."""
