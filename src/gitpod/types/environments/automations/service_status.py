# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .service_phase import ServicePhase

__all__ = ["ServiceStatus"]


class ServiceStatus(BaseModel):
    failure_message: Optional[str] = FieldInfo(alias="failureMessage", default=None)
    """failure_message summarises why the service failed to operate.

    If this is non-empty the service has failed to operate and will likely
    transition to a failed state.
    """

    log_url: Optional[str] = FieldInfo(alias="logUrl", default=None)
    """log_url contains the URL at which the service logs can be accessed."""

    phase: Optional[ServicePhase] = None
    """phase is the current phase of the service."""

    session: Optional[str] = None
    """session is the current session of the service."""

    status_version: Optional[str] = FieldInfo(alias="statusVersion", default=None)
    """version of the status update.

    Service instances themselves are unversioned, but their status has different
    versions. The value of this field has no semantic meaning (e.g. don't interpret
    it as as a timestamp), but it can be used to impose a partial order. If
    a.status_version < b.status_version then a was the status before b.
    """
