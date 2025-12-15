# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .stack_frame_param import StackFrameParam
from .exception_mechanism_param import ExceptionMechanismParam

__all__ = ["ExceptionInfoParam"]


class ExceptionInfoParam(TypedDict, total=False):
    """Exception information (Sentry-compatible)"""

    mechanism: ExceptionMechanismParam
    """Exception mechanism"""

    module: str
    """Module or package where the exception type is defined"""

    stacktrace: Iterable[StackFrameParam]
    """Stack trace frames"""

    thread_id: Annotated[str, PropertyInfo(alias="threadId")]
    """Thread ID if applicable"""

    type: str
    """Exception type/class name"""

    value: str
    """Exception message/value"""
