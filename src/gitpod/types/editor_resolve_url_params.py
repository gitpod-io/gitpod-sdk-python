# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EditorResolveURLParams"]


class EditorResolveURLParams(TypedDict, total=False):
    editor_id: Required[Annotated[str, PropertyInfo(alias="editorId")]]
    """editorId is the ID of the editor to resolve the URL for"""

    environment_id: Required[Annotated[str, PropertyInfo(alias="environmentId")]]
    """environmentId is the ID of the environment to resolve the URL for"""

    organization_id: Required[Annotated[str, PropertyInfo(alias="organizationId")]]
    """organizationId is the ID of the organization to resolve the URL for"""
