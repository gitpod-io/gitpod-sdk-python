# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["StackFrameParam"]


class StackFrameParam(TypedDict, total=False):
    """Stack trace frame information (Sentry-compatible)"""

    colno: int
    """Column number in the line"""

    context_line: Annotated[str, PropertyInfo(alias="contextLine")]

    filename: str
    """File name or path"""

    function: str
    """Function name"""

    in_app: Annotated[bool, PropertyInfo(alias="inApp")]
    """Whether this frame is in application code (vs library/framework code)"""

    lineno: int
    """Line number in the file"""

    module: str
    """Module or package name"""

    post_context: Annotated[SequenceNotStr[str], PropertyInfo(alias="postContext")]

    pre_context: Annotated[SequenceNotStr[str], PropertyInfo(alias="preContext")]
    """Source code context around the error line"""

    vars: Dict[str, str]
    """Additional frame-specific variables/locals"""
