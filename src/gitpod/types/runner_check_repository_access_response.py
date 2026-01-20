# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["RunnerCheckRepositoryAccessResponse"]


class RunnerCheckRepositoryAccessResponse(BaseModel):
    error_message: Optional[str] = FieldInfo(alias="errorMessage", default=None)
    """
    error_message provides details when access check fails. Empty when has_access is
    true.
    """

    has_access: Optional[bool] = FieldInfo(alias="hasAccess", default=None)
    """has_access indicates whether the principal has read access to the repository."""
