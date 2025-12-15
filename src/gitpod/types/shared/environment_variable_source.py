# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .secret_ref import SecretRef

__all__ = ["EnvironmentVariableSource"]


class EnvironmentVariableSource(BaseModel):
    """EnvironmentVariableSource specifies a source for an environment variable value."""

    secret_ref: SecretRef = FieldInfo(alias="secretRef")
    """secret_ref references a secret by ID."""
