# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

from .error_event_param import ErrorEventParam

__all__ = ["ErrorReportErrorsParams"]


class ErrorReportErrorsParams(TypedDict, total=False):
    events: Iterable[ErrorEventParam]
    """Error events to be reported (batch) - now using Sentry-compatible structure"""
