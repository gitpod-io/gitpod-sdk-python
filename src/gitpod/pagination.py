# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from pydantic import Field as FieldInfo

from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = [
    "SyncPersonalAccessTokensPage",
    "AsyncPersonalAccessTokensPage",
    "SyncOrganizationsPage",
    "AsyncOrganizationsPage",
    "SyncMembersPage",
    "AsyncMembersPage",
    "SyncSSOConfigurationsPage",
    "AsyncSSOConfigurationsPage",
    "SyncLoginProvidersPage",
    "AsyncLoginProvidersPage",
    "SyncEditorsPage",
    "AsyncEditorsPage",
    "SyncTokensPage",
    "AsyncTokensPage",
    "SyncIntegrationsPage",
    "AsyncIntegrationsPage",
    "SyncEnvironmentClassesPage",
    "AsyncEnvironmentClassesPage",
    "SyncRunnersPage",
    "AsyncRunnersPage",
    "SyncPoliciesPage",
    "AsyncPoliciesPage",
    "SyncEnvironmentsPage",
    "AsyncEnvironmentsPage",
    "SyncServicesPage",
    "AsyncServicesPage",
    "SyncTasksPage",
    "AsyncTasksPage",
    "SyncTaskExecutionsPage",
    "AsyncTaskExecutionsPage",
    "SyncEntriesPage",
    "AsyncEntriesPage",
    "SyncGroupsPage",
    "AsyncGroupsPage",
    "SyncProjectsPage",
    "AsyncProjectsPage",
    "SyncSecretsPage",
    "AsyncSecretsPage",
]

_T = TypeVar("_T")


class SyncPersonalAccessTokensPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    personal_access_tokens: List[_T]
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        personal_access_tokens = self.personal_access_tokens
        if not personal_access_tokens:
            return []
        return personal_access_tokens

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = self.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncPersonalAccessTokensPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    personal_access_tokens: List[_T]
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        personal_access_tokens = self.personal_access_tokens
        if not personal_access_tokens:
            return []
        return personal_access_tokens

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = self.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class SyncOrganizationsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    organizations: List[_T]
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        organizations = self.organizations
        if not organizations:
            return []
        return organizations

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = self.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncOrganizationsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    organizations: List[_T]
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        organizations = self.organizations
        if not organizations:
            return []
        return organizations

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


class SyncSSOConfigurationsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    sso_configurations: List[_T]
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        sso_configurations = self.sso_configurations
        if not sso_configurations:
            return []
        return sso_configurations

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = self.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncSSOConfigurationsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    sso_configurations: List[_T]
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        sso_configurations = self.sso_configurations
        if not sso_configurations:
            return []
        return sso_configurations

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = self.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class SyncLoginProvidersPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    login_providers: List[_T]
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        login_providers = self.login_providers
        if not login_providers:
            return []
        return login_providers

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = self.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncLoginProvidersPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    login_providers: List[_T]
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        login_providers = self.login_providers
        if not login_providers:
            return []
        return login_providers

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = self.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class SyncEditorsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    editors: List[_T]
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        editors = self.editors
        if not editors:
            return []
        return editors

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = self.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncEditorsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    editors: List[_T]
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        editors = self.editors
        if not editors:
            return []
        return editors

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = self.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class SyncTokensPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    tokens: List[_T]
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        tokens = self.tokens
        if not tokens:
            return []
        return tokens

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = self.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncTokensPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    tokens: List[_T]
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        tokens = self.tokens
        if not tokens:
            return []
        return tokens

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = self.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class SyncIntegrationsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    integrations: List[_T]
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        integrations = self.integrations
        if not integrations:
            return []
        return integrations

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = self.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncIntegrationsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    integrations: List[_T]
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        integrations = self.integrations
        if not integrations:
            return []
        return integrations

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = self.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class SyncEnvironmentClassesPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    environment_classes: List[_T]
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


class AsyncEnvironmentClassesPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    environment_classes: List[_T]
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


class SyncRunnersPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    runners: List[_T]
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        runners = self.runners
        if not runners:
            return []
        return runners

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = self.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncRunnersPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    runners: List[_T]
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        runners = self.runners
        if not runners:
            return []
        return runners

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = self.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class SyncPoliciesPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    policies: List[_T]
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        policies = self.policies
        if not policies:
            return []
        return policies

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = self.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncPoliciesPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    policies: List[_T]
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        policies = self.policies
        if not policies:
            return []
        return policies

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


class SyncEnvironmentClassesPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    environment_classes: List[_T]
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


class AsyncEnvironmentClassesPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    environment_classes: List[_T]
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
    task_executions: List[_T]
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
    task_executions: List[_T]
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


class SyncProjectsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    projects: List[_T]
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        projects = self.projects
        if not projects:
            return []
        return projects

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = self.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncProjectsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    projects: List[_T]
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        projects = self.projects
        if not projects:
            return []
        return projects

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = self.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class SyncPoliciesPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    policies: List[_T]
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        policies = self.policies
        if not policies:
            return []
        return policies

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = self.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncPoliciesPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    policies: List[_T]
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        policies = self.policies
        if not policies:
            return []
        return policies

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = self.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class SyncSecretsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    secrets: List[_T]
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        secrets = self.secrets
        if not secrets:
            return []
        return secrets

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = self.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncSecretsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    secrets: List[_T]
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        secrets = self.secrets
        if not secrets:
            return []
        return secrets

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = self.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})
