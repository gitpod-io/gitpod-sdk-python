# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo
from .service_role import ServiceRole
from ...shared_params.subject import Subject
from ...shared_params.automation_trigger import AutomationTrigger

__all__ = ["ServiceMetadataParam"]


class ServiceMetadataParam(TypedDict, total=False):
    created_at: Annotated[Union[str, datetime], PropertyInfo(alias="createdAt", format="iso8601")]
    """created_at is the time the service was created."""

    creator: Subject
    """creator describes the principal who created the service."""

    description: str
    """description is a user-facing description for the service.

    It can be used to provide context and documentation for the service.
    """

    name: str
    """name is a user-facing name for the service.

    Unlike the reference, this field is not unique, and not referenced by the
    system. This is a short descriptive name for the service.
    """

    reference: str
    """
    reference is a user-facing identifier for the service which must be unique on
    the environment. It is used to express dependencies between services, and to
    identify the service in user interactions (e.g. the CLI).
    """

    role: ServiceRole
    """role specifies the intended role or purpose of the service."""

    triggered_by: Annotated[Iterable[AutomationTrigger], PropertyInfo(alias="triggeredBy")]
    """triggered_by is a list of trigger that start the service."""
