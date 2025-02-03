# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "EventWatchParams",
    "EnvironmentScopeProducesEventsForTheEnvironmentItselfAllTasksTaskExecutionsAndServicesAssociatedWithThatEnvironment",
    "OrganizationScopeProducesEventsForAllProjectsRunnersAndEnvironmentsTheCallerCanSeeWithinTheirOrganizationNoTaskTaskExecutionOrServiceEventsAreProdued",
]


class EnvironmentScopeProducesEventsForTheEnvironmentItselfAllTasksTaskExecutionsAndServicesAssociatedWithThatEnvironment(
    TypedDict, total=False
):
    environment_id: Required[Annotated[str, PropertyInfo(alias="environmentId")]]
    """
    Environment scope produces events for the environment itself, all tasks, task
    executions,

    and services associated with that environment.
    """

    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""


class OrganizationScopeProducesEventsForAllProjectsRunnersAndEnvironmentsTheCallerCanSeeWithinTheirOrganizationNoTaskTaskExecutionOrServiceEventsAreProdued(
    TypedDict, total=False
):
    organization: Required[bool]
    """Organization scope produces events for all projects, runners and environments

    the caller can see within their organization. No task, task execution or service
    events are produed.
    """

    connect_protocol_version: Required[Annotated[Literal[1], PropertyInfo(alias="Connect-Protocol-Version")]]
    """Define the version of the Connect protocol"""

    connect_timeout_ms: Annotated[float, PropertyInfo(alias="Connect-Timeout-Ms")]
    """Define the timeout, in ms"""


EventWatchParams: TypeAlias = Union[
    EnvironmentScopeProducesEventsForTheEnvironmentItselfAllTasksTaskExecutionsAndServicesAssociatedWithThatEnvironment,
    OrganizationScopeProducesEventsForAllProjectsRunnersAndEnvironmentsTheCallerCanSeeWithinTheirOrganizationNoTaskTaskExecutionOrServiceEventsAreProdued,
]
