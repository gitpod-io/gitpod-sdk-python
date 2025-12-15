# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .error_level import ErrorLevel
from .breadcrumb_param import BreadcrumbParam
from .request_info_param import RequestInfoParam
from .exception_info_param import ExceptionInfoParam

__all__ = ["ErrorEventParam"]


class ErrorEventParam(TypedDict, total=False):
    """ErrorEvent contains comprehensive error information (Sentry-compatible)"""

    breadcrumbs: Iterable[BreadcrumbParam]
    """Breadcrumbs leading up to the error"""

    environment: str
    """Environment (e.g., "production", "staging", "development")"""

    event_id: Annotated[str, PropertyInfo(alias="eventId")]
    """Unique event identifier (required by Sentry)"""

    exceptions: Iterable[ExceptionInfoParam]
    """Exception information (primary error data)"""

    extra: Dict[str, str]
    """Additional arbitrary metadata"""

    fingerprint: SequenceNotStr[str]
    """Custom fingerprint for grouping"""

    identity_id: Annotated[str, PropertyInfo(alias="identityId")]
    """Identity ID of the user (UUID)"""

    level: ErrorLevel
    """Error severity level"""

    logger: str
    """Logger name"""

    modules: Dict[str, str]
    """Modules/dependencies information"""

    platform: str
    """Platform identifier (required by Sentry)"""

    release: str
    """Release version"""

    request: RequestInfoParam
    """Request information"""

    sdk: Dict[str, str]
    """SDK information"""

    server_name: Annotated[str, PropertyInfo(alias="serverName")]
    """Server/host name"""

    tags: Dict[str, str]
    """Tags for filtering and grouping"""

    timestamp: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """When the event occurred (required by Sentry)"""

    transaction: str
    """Transaction name (e.g., route name, function name)"""
