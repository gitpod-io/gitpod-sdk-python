# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["InviteGetSummaryParams"]


class InviteGetSummaryParams(TypedDict, total=False):
    encoding: Required[Literal["proto", "json"]]
    """Define which encoding or 'Message-Codec' to use"""

    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    base64: bool
    """
    Specifies if the message query param is base64 encoded, which may be required
    for binary data
    """

    compression: Literal["identity", "gzip", "br"]
    """Which compression algorithm to use for this request"""

    connect: Literal["v1"]
    """Define the version of the Connect protocol"""

    message: str

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""
