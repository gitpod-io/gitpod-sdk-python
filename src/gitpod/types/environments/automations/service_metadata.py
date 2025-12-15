# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .service_role import ServiceRole
from ...shared.subject import Subject
from ...shared.automation_trigger import AutomationTrigger

__all__ = ["ServiceMetadata"]


class ServiceMetadata(BaseModel):
    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """created_at is the time the service was created."""

    creator: Optional[Subject] = None
    """creator describes the principal who created the service."""

    description: Optional[str] = None
    """description is a user-facing description for the service.

    It can be used to provide context and documentation for the service.
    """

    name: Optional[str] = None
    """name is a user-facing name for the service.

    Unlike the reference, this field is not unique, and not referenced by the
    system. This is a short descriptive name for the service.
    """

    reference: Optional[str] = None
    """
    reference is a user-facing identifier for the service which must be unique on
    the environment. It is used to express dependencies between services, and to
    identify the service in user interactions (e.g. the CLI).
    """

    role: Optional[ServiceRole] = None
    """role specifies the intended role or purpose of the service."""

    triggered_by: Optional[List[AutomationTrigger]] = FieldInfo(alias="triggeredBy", default=None)
    """triggered_by is a list of trigger that start the service."""
