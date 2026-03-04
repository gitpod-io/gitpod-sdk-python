# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .shared.resource_type import ResourceType

__all__ = ["EventWatchParams", "ResourceTypeFilter"]


class EventWatchParams(TypedDict, total=False):
    environment_id: Annotated[str, PropertyInfo(alias="environmentId")]
    """
    Environment scope produces events for the environment itself, all tasks, task
    executions, and services associated with that environment.
    """

    organization: bool
    """
    Organization scope produces events for all projects, runners and environments
    the caller can see within their organization. No task, task execution or service
    events are produed.
    """

    resource_type_filters: Annotated[Iterable[ResourceTypeFilter], PropertyInfo(alias="resourceTypeFilters")]
    """
    Filters to limit which events are delivered on organization-scoped streams. When
    empty, all events for the scope are delivered. When populated, only events
    matching at least one filter entry are forwarded. Not supported for
    environment-scoped streams; setting this field returns an error.
    """


class ResourceTypeFilter(TypedDict, total=False):
    """
    ResourceTypeFilter restricts which events are delivered for a specific resource type.
    """

    creator_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="creatorIds")]
    """
    If non-empty, only events where the resource was created by one of these user
    IDs are delivered. Skipped for DELETE operations (creator info is unavailable
    after deletion). Events with no creator information are skipped when this filter
    is set (fail-closed).
    """

    resource_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="resourceIds")]
    """If non-empty, only events for these specific resource IDs are delivered."""

    resource_type: Annotated[ResourceType, PropertyInfo(alias="resourceType")]
    """The resource type to filter for."""
