# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from pydantic import Field as FieldInfo

from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = [
    "SyncServicesPage",
    "AsyncServicesPage",
    "SyncTasksPage",
    "AsyncTasksPage",
    "SyncTaskExecutionsPage",
    "AsyncTaskExecutionsPage",
    "SyncEnvironnmentClassesPage",
    "AsyncEnvironnmentClassesPage",
    "SyncEnvironmentsPage",
    "AsyncEnvironmentsPage",
    "SyncEntriesPage",
    "AsyncEntriesPage",
    "SyncGroupsPage",
    "AsyncGroupsPage",
    "SyncMembersPage",
    "AsyncMembersPage",
]

_T = TypeVar("_T")


class SyncServicesPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    services: List[_T]
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        services = self.services
        if not services:
            return []
        return services

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = self.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncServicesPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    services: List[_T]
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        services = self.services
        if not services:
            return []
        return services

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = self.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class SyncTasksPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    tasks: List[_T]
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        tasks = self.tasks
        if not tasks:
            return []
        return tasks

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = self.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncTasksPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    tasks: List[_T]
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        tasks = self.tasks
        if not tasks:
            return []
        return tasks

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = self.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class SyncTaskExecutionsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    task_executions: List[_T] = FieldInfo(alias="taskExecutions")
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        task_executions = self.task_executions
        if not task_executions:
            return []
        return task_executions

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = self.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncTaskExecutionsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    task_executions: List[_T] = FieldInfo(alias="taskExecutions")
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        task_executions = self.task_executions
        if not task_executions:
            return []
        return task_executions

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = self.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class SyncEnvironnmentClassesPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    environment_classes: List[_T] = FieldInfo(alias="environmentClasses")
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        environment_classes = self.environment_classes
        if not environment_classes:
            return []
        return environment_classes

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = self.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncEnvironnmentClassesPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    environment_classes: List[_T] = FieldInfo(alias="environmentClasses")
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        environment_classes = self.environment_classes
        if not environment_classes:
            return []
        return environment_classes

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = self.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class SyncEnvironmentsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    environments: List[_T]
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        environments = self.environments
        if not environments:
            return []
        return environments

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = self.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncEnvironmentsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    environments: List[_T]
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        environments = self.environments
        if not environments:
            return []
        return environments

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = self.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class SyncEntriesPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    entries: List[_T]
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        entries = self.entries
        if not entries:
            return []
        return entries

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = self.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncEntriesPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    entries: List[_T]
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        entries = self.entries
        if not entries:
            return []
        return entries

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = self.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class SyncGroupsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    groups: List[_T]
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        groups = self.groups
        if not groups:
            return []
        return groups

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = self.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncGroupsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    groups: List[_T]
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        groups = self.groups
        if not groups:
            return []
        return groups

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = self.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class SyncMembersPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    members: List[_T]
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        members = self.members
        if not members:
            return []
        return members

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = self.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncMembersPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    members: List[_T]
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        members = self.members
        if not members:
            return []
        return members

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = self.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})
