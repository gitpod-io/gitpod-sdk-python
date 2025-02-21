# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .subject import Subject
from ..._utils import PropertyInfo
from .automation_trigger import AutomationTrigger

__all__ = ["TaskMetadata"]


class TaskMetadata(TypedDict, total=False):
    created_at: Annotated[Union[str, datetime], PropertyInfo(alias="createdAt", format="iso8601")]
    """created_at is the time the task was created."""

    creator: Subject
    """creator describes the principal who created the task."""

    description: str
    """description is a user-facing description for the task.

    It can be used to provide context and documentation for the task.
    """

    name: str
    """name is a user-facing name for the task.

    Unlike the reference, this field is not unique, and not referenced by the
    system. This is a short descriptive name for the task.
    """

    reference: str
    """
    reference is a user-facing identifier for the task which must be unique on the
    environment. It is used to express dependencies between tasks, and to identify
    the task in user interactions (e.g. the CLI).
    """

    triggered_by: Annotated[Iterable[AutomationTrigger], PropertyInfo(alias="triggeredBy")]
    """triggered_by is a list of trigger that start the task."""
