# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from pydantic import Field as FieldInfo

from ._models import GenericModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = [
    "PersonalAccessTokensPagePagination",
    "SyncPersonalAccessTokensPage",
    "AsyncPersonalAccessTokensPage",
    "OrganizationsPagePagination",
    "SyncOrganizationsPage",
    "AsyncOrganizationsPage",
    "MembersPagePagination",
    "SyncMembersPage",
    "AsyncMembersPage",
    "SSOConfigurationsPagePagination",
    "SyncSSOConfigurationsPage",
    "AsyncSSOConfigurationsPage",
    "LoginProvidersPagePagination",
    "SyncLoginProvidersPage",
    "AsyncLoginProvidersPage",
    "EditorsPagePagination",
    "SyncEditorsPage",
    "AsyncEditorsPage",
    "TokensPagePagination",
    "SyncTokensPage",
    "AsyncTokensPage",
    "IntegrationsPagePagination",
    "SyncIntegrationsPage",
    "AsyncIntegrationsPage",
    "EnvironmentClassesPagePagination",
    "SyncEnvironmentClassesPage",
    "AsyncEnvironmentClassesPage",
    "RunnersPagePagination",
    "SyncRunnersPage",
    "AsyncRunnersPage",
    "PoliciesPagePagination",
    "SyncPoliciesPage",
    "AsyncPoliciesPage",
    "EnvironmentsPagePagination",
    "SyncEnvironmentsPage",
    "AsyncEnvironmentsPage",
    "ServicesPagePagination",
    "SyncServicesPage",
    "AsyncServicesPage",
    "TasksPagePagination",
    "SyncTasksPage",
    "AsyncTasksPage",
    "TaskExecutionsPagePagination",
    "SyncTaskExecutionsPage",
    "AsyncTaskExecutionsPage",
    "EntriesPagePagination",
    "SyncEntriesPage",
    "AsyncEntriesPage",
    "GroupsPagePagination",
    "SyncGroupsPage",
    "AsyncGroupsPage",
    "ProjectsPagePagination",
    "SyncProjectsPage",
    "AsyncProjectsPage",
    "SecretsPagePagination",
    "SyncSecretsPage",
    "AsyncSecretsPage",
]

_T = TypeVar("_T")


class PersonalAccessTokensPagePagination(GenericModel, Generic[_T]):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    personal_access_tokens: Optional[List[_T]] = None


class SyncPersonalAccessTokensPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[PersonalAccessTokensPagePagination[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        personal_access_tokens = None
        if self.pagination is not None:
            if self.pagination.personal_access_tokens is not None:
                personal_access_tokens = self.pagination.personal_access_tokens
        if not personal_access_tokens:
            return []
        return personal_access_tokens

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncPersonalAccessTokensPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[PersonalAccessTokensPagePagination[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        personal_access_tokens = None
        if self.pagination is not None:
            if self.pagination.personal_access_tokens is not None:
                personal_access_tokens = self.pagination.personal_access_tokens
        if not personal_access_tokens:
            return []
        return personal_access_tokens

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class OrganizationsPagePagination(GenericModel, Generic[_T]):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    organizations: Optional[List[_T]] = None


class SyncOrganizationsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[OrganizationsPagePagination[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        organizations = None
        if self.pagination is not None:
            if self.pagination.organizations is not None:
                organizations = self.pagination.organizations
        if not organizations:
            return []
        return organizations

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncOrganizationsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[OrganizationsPagePagination[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        organizations = None
        if self.pagination is not None:
            if self.pagination.organizations is not None:
                organizations = self.pagination.organizations
        if not organizations:
            return []
        return organizations

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class MembersPagePagination(GenericModel, Generic[_T]):
    members: Optional[List[_T]] = None

    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)


class SyncMembersPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[MembersPagePagination[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        members = None
        if self.pagination is not None:
            if self.pagination.members is not None:
                members = self.pagination.members
        if not members:
            return []
        return members

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncMembersPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[MembersPagePagination[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        members = None
        if self.pagination is not None:
            if self.pagination.members is not None:
                members = self.pagination.members
        if not members:
            return []
        return members

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class SSOConfigurationsPagePagination(GenericModel, Generic[_T]):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    sso_configurations: Optional[List[_T]] = None


class SyncSSOConfigurationsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[SSOConfigurationsPagePagination[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        sso_configurations = None
        if self.pagination is not None:
            if self.pagination.sso_configurations is not None:
                sso_configurations = self.pagination.sso_configurations
        if not sso_configurations:
            return []
        return sso_configurations

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncSSOConfigurationsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[SSOConfigurationsPagePagination[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        sso_configurations = None
        if self.pagination is not None:
            if self.pagination.sso_configurations is not None:
                sso_configurations = self.pagination.sso_configurations
        if not sso_configurations:
            return []
        return sso_configurations

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class LoginProvidersPagePagination(GenericModel, Generic[_T]):
    login_providers: Optional[List[_T]] = None

    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)


class SyncLoginProvidersPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[LoginProvidersPagePagination[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        login_providers = None
        if self.pagination is not None:
            if self.pagination.login_providers is not None:
                login_providers = self.pagination.login_providers
        if not login_providers:
            return []
        return login_providers

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncLoginProvidersPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[LoginProvidersPagePagination[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        login_providers = None
        if self.pagination is not None:
            if self.pagination.login_providers is not None:
                login_providers = self.pagination.login_providers
        if not login_providers:
            return []
        return login_providers

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class EditorsPagePagination(GenericModel, Generic[_T]):
    editors: Optional[List[_T]] = None

    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)


class SyncEditorsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[EditorsPagePagination[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        editors = None
        if self.pagination is not None:
            if self.pagination.editors is not None:
                editors = self.pagination.editors
        if not editors:
            return []
        return editors

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncEditorsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[EditorsPagePagination[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        editors = None
        if self.pagination is not None:
            if self.pagination.editors is not None:
                editors = self.pagination.editors
        if not editors:
            return []
        return editors

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class TokensPagePagination(GenericModel, Generic[_T]):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    tokens: Optional[List[_T]] = None


class SyncTokensPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[TokensPagePagination[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        tokens = None
        if self.pagination is not None:
            if self.pagination.tokens is not None:
                tokens = self.pagination.tokens
        if not tokens:
            return []
        return tokens

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncTokensPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[TokensPagePagination[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        tokens = None
        if self.pagination is not None:
            if self.pagination.tokens is not None:
                tokens = self.pagination.tokens
        if not tokens:
            return []
        return tokens

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class IntegrationsPagePagination(GenericModel, Generic[_T]):
    integrations: Optional[List[_T]] = None

    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)


class SyncIntegrationsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[IntegrationsPagePagination[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        integrations = None
        if self.pagination is not None:
            if self.pagination.integrations is not None:
                integrations = self.pagination.integrations
        if not integrations:
            return []
        return integrations

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncIntegrationsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[IntegrationsPagePagination[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        integrations = None
        if self.pagination is not None:
            if self.pagination.integrations is not None:
                integrations = self.pagination.integrations
        if not integrations:
            return []
        return integrations

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class EnvironmentClassesPagePagination(GenericModel, Generic[_T]):
    environment_classes: Optional[List[_T]] = None

    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)


class SyncEnvironmentClassesPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[EnvironmentClassesPagePagination[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        environment_classes = None
        if self.pagination is not None:
            if self.pagination.environment_classes is not None:
                environment_classes = self.pagination.environment_classes
        if not environment_classes:
            return []
        return environment_classes

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncEnvironmentClassesPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[EnvironmentClassesPagePagination[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        environment_classes = None
        if self.pagination is not None:
            if self.pagination.environment_classes is not None:
                environment_classes = self.pagination.environment_classes
        if not environment_classes:
            return []
        return environment_classes

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class RunnersPagePagination(GenericModel, Generic[_T]):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    runners: Optional[List[_T]] = None


class SyncRunnersPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[RunnersPagePagination[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        runners = None
        if self.pagination is not None:
            if self.pagination.runners is not None:
                runners = self.pagination.runners
        if not runners:
            return []
        return runners

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncRunnersPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[RunnersPagePagination[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        runners = None
        if self.pagination is not None:
            if self.pagination.runners is not None:
                runners = self.pagination.runners
        if not runners:
            return []
        return runners

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class PoliciesPagePagination(GenericModel, Generic[_T]):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    policies: Optional[List[_T]] = None


class SyncPoliciesPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[PoliciesPagePagination[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        policies = None
        if self.pagination is not None:
            if self.pagination.policies is not None:
                policies = self.pagination.policies
        if not policies:
            return []
        return policies

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncPoliciesPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[PoliciesPagePagination[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        policies = None
        if self.pagination is not None:
            if self.pagination.policies is not None:
                policies = self.pagination.policies
        if not policies:
            return []
        return policies

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class EnvironmentsPagePagination(GenericModel, Generic[_T]):
    environments: Optional[List[_T]] = None

    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)


class SyncEnvironmentsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[EnvironmentsPagePagination[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        environments = None
        if self.pagination is not None:
            if self.pagination.environments is not None:
                environments = self.pagination.environments
        if not environments:
            return []
        return environments

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncEnvironmentsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[EnvironmentsPagePagination[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        environments = None
        if self.pagination is not None:
            if self.pagination.environments is not None:
                environments = self.pagination.environments
        if not environments:
            return []
        return environments

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class ServicesPagePagination(GenericModel, Generic[_T]):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    services: Optional[List[_T]] = None


class SyncServicesPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[ServicesPagePagination[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        services = None
        if self.pagination is not None:
            if self.pagination.services is not None:
                services = self.pagination.services
        if not services:
            return []
        return services

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncServicesPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[ServicesPagePagination[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        services = None
        if self.pagination is not None:
            if self.pagination.services is not None:
                services = self.pagination.services
        if not services:
            return []
        return services

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class TasksPagePagination(GenericModel, Generic[_T]):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    tasks: Optional[List[_T]] = None


class SyncTasksPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[TasksPagePagination[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        tasks = None
        if self.pagination is not None:
            if self.pagination.tasks is not None:
                tasks = self.pagination.tasks
        if not tasks:
            return []
        return tasks

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncTasksPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[TasksPagePagination[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        tasks = None
        if self.pagination is not None:
            if self.pagination.tasks is not None:
                tasks = self.pagination.tasks
        if not tasks:
            return []
        return tasks

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class TaskExecutionsPagePagination(GenericModel, Generic[_T]):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    task_executions: Optional[List[_T]] = None


class SyncTaskExecutionsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[TaskExecutionsPagePagination[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        task_executions = None
        if self.pagination is not None:
            if self.pagination.task_executions is not None:
                task_executions = self.pagination.task_executions
        if not task_executions:
            return []
        return task_executions

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncTaskExecutionsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[TaskExecutionsPagePagination[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        task_executions = None
        if self.pagination is not None:
            if self.pagination.task_executions is not None:
                task_executions = self.pagination.task_executions
        if not task_executions:
            return []
        return task_executions

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class EntriesPagePagination(GenericModel, Generic[_T]):
    entries: Optional[List[_T]] = None

    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)


class SyncEntriesPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[EntriesPagePagination[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        entries = None
        if self.pagination is not None:
            if self.pagination.entries is not None:
                entries = self.pagination.entries
        if not entries:
            return []
        return entries

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncEntriesPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[EntriesPagePagination[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        entries = None
        if self.pagination is not None:
            if self.pagination.entries is not None:
                entries = self.pagination.entries
        if not entries:
            return []
        return entries

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class GroupsPagePagination(GenericModel, Generic[_T]):
    groups: Optional[List[_T]] = None

    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)


class SyncGroupsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[GroupsPagePagination[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        groups = None
        if self.pagination is not None:
            if self.pagination.groups is not None:
                groups = self.pagination.groups
        if not groups:
            return []
        return groups

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncGroupsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[GroupsPagePagination[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        groups = None
        if self.pagination is not None:
            if self.pagination.groups is not None:
                groups = self.pagination.groups
        if not groups:
            return []
        return groups

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class ProjectsPagePagination(GenericModel, Generic[_T]):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    projects: Optional[List[_T]] = None


class SyncProjectsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[ProjectsPagePagination[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        projects = None
        if self.pagination is not None:
            if self.pagination.projects is not None:
                projects = self.pagination.projects
        if not projects:
            return []
        return projects

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncProjectsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[ProjectsPagePagination[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        projects = None
        if self.pagination is not None:
            if self.pagination.projects is not None:
                projects = self.pagination.projects
        if not projects:
            return []
        return projects

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class SecretsPagePagination(GenericModel, Generic[_T]):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)

    secrets: Optional[List[_T]] = None


class SyncSecretsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[SecretsPagePagination[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        secrets = None
        if self.pagination is not None:
            if self.pagination.secrets is not None:
                secrets = self.pagination.secrets
        if not secrets:
            return []
        return secrets

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncSecretsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[SecretsPagePagination[_T]] = None

    @override
    def _get_page_items(self) -> List[_T]:
        secrets = None
        if self.pagination is not None:
            if self.pagination.secrets is not None:
                secrets = self.pagination.secrets
        if not secrets:
            return []
        return secrets

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})
