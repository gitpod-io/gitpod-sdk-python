# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EditorResolveURLParams"]


class EditorResolveURLParams(TypedDict, total=False):
    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    editor_id: Annotated[str, PropertyInfo(alias="editorId")]
    """editorId is the ID of the editor to resolve the URL for"""

    environment_id: Annotated[str, PropertyInfo(alias="environmentId")]
    """environmentId is the ID of the environment to resolve the URL for"""

    organization_id: Annotated[str, PropertyInfo(alias="organizationId")]
    """organizationId is the ID of the organization to resolve the URL for"""

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""
