# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PrebuildCreateLogsTokenParams"]


class PrebuildCreateLogsTokenParams(TypedDict, total=False):
    prebuild_id: Required[Annotated[str, PropertyInfo(alias="prebuildId")]]
    """prebuild_id specifies the prebuild for which the logs token should be created.

    +required
    """
