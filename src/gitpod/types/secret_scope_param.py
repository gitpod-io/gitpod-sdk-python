# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SecretScopeParam"]


class SecretScopeParam(TypedDict, total=False):
    project_id: Annotated[str, PropertyInfo(alias="projectId")]
    """project_id is the Project ID this Secret belongs to"""

    user_id: Annotated[str, PropertyInfo(alias="userId")]
    """user_id is the User ID this Secret belongs to"""
