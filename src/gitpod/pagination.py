# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from pydantic import Field as FieldInfo

from ._models import BaseModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = [
    "AgentExecutionsPagePagination",
    "SyncAgentExecutionsPage",
    "AsyncAgentExecutionsPage",
    "AssignmentsPagePagination",
    "SyncAssignmentsPage",
    "AsyncAssignmentsPage",
    "DomainVerificationsPagePagination",
    "SyncDomainVerificationsPage",
    "AsyncDomainVerificationsPage",
    "EditorsPagePagination",
    "SyncEditorsPage",
    "AsyncEditorsPage",
    "EntriesPagePagination",
    "SyncEntriesPage",
    "AsyncEntriesPage",
    "EnvironmentClassesPagePagination",
    "SyncEnvironmentClassesPage",
    "AsyncEnvironmentClassesPage",
    "EnvironmentsPagePagination",
    "SyncEnvironmentsPage",
    "AsyncEnvironmentsPage",
    "GatewaysPagePagination",
    "SyncGatewaysPage",
    "AsyncGatewaysPage",
    "GroupsPagePagination",
    "SyncGroupsPage",
    "AsyncGroupsPage",
    "IntegrationsPagePagination",
    "SyncIntegrationsPage",
    "AsyncIntegrationsPage",
    "JoinableOrganizationsPagePagination",
    "SyncJoinableOrganizationsPage",
    "AsyncJoinableOrganizationsPage",
    "LoginProvidersPagePagination",
    "SyncLoginProvidersPage",
    "AsyncLoginProvidersPage",
    "LoginsPagePagination",
    "SyncLoginsPage",
    "AsyncLoginsPage",
    "MembersPagePagination",
    "SyncMembersPage",
    "AsyncMembersPage",
    "PersonalAccessTokensPagePagination",
    "SyncPersonalAccessTokensPage",
    "AsyncPersonalAccessTokensPage",
    "PoliciesPagePagination",
    "SyncPoliciesPage",
    "AsyncPoliciesPage",
    "PrebuildsPagePagination",
    "SyncPrebuildsPage",
    "AsyncPrebuildsPage",
    "ProjectEnvironmentClassesPagePagination",
    "SyncProjectEnvironmentClassesPage",
    "AsyncProjectEnvironmentClassesPage",
    "ProjectsPagePagination",
    "SyncProjectsPage",
    "AsyncProjectsPage",
    "PromptsPagePagination",
    "SyncPromptsPage",
    "AsyncPromptsPage",
    "RecordsPagePagination",
    "SyncRecordsPage",
    "AsyncRecordsPage",
    "RepositoriesPagePagination",
    "SyncRepositoriesPage",
    "AsyncRepositoriesPage",
    "RunnersPagePagination",
    "SyncRunnersPage",
    "AsyncRunnersPage",
    "SecretsPagePagination",
    "SyncSecretsPage",
    "AsyncSecretsPage",
    "ServicesPagePagination",
    "SyncServicesPage",
    "AsyncServicesPage",
    "SSOConfigurationsPagePagination",
    "SyncSSOConfigurationsPage",
    "AsyncSSOConfigurationsPage",
    "TaskExecutionsPagePagination",
    "SyncTaskExecutionsPage",
    "AsyncTaskExecutionsPage",
    "TasksPagePagination",
    "SyncTasksPage",
    "AsyncTasksPage",
    "TokensPagePagination",
    "SyncTokensPage",
    "AsyncTokensPage",
]

_T = TypeVar("_T")


class AgentExecutionsPagePagination(BaseModel):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)


class SyncAgentExecutionsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    agent_executions: List[_T] = FieldInfo(alias="agentExecutions")
    pagination: Optional[AgentExecutionsPagePagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        agent_executions = self.agent_executions
        if not agent_executions:
            return []
        return agent_executions

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncAgentExecutionsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    agent_executions: List[_T] = FieldInfo(alias="agentExecutions")
    pagination: Optional[AgentExecutionsPagePagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        agent_executions = self.agent_executions
        if not agent_executions:
            return []
        return agent_executions

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AssignmentsPagePagination(BaseModel):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)


class SyncAssignmentsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    assignments: List[_T]
    pagination: Optional[AssignmentsPagePagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        assignments = self.assignments
        if not assignments:
            return []
        return assignments

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncAssignmentsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    assignments: List[_T]
    pagination: Optional[AssignmentsPagePagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        assignments = self.assignments
        if not assignments:
            return []
        return assignments

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class DomainVerificationsPagePagination(BaseModel):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)


class SyncDomainVerificationsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    domain_verifications: List[_T] = FieldInfo(alias="domainVerifications")
    pagination: Optional[DomainVerificationsPagePagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        domain_verifications = self.domain_verifications
        if not domain_verifications:
            return []
        return domain_verifications

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncDomainVerificationsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    domain_verifications: List[_T] = FieldInfo(alias="domainVerifications")
    pagination: Optional[DomainVerificationsPagePagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        domain_verifications = self.domain_verifications
        if not domain_verifications:
            return []
        return domain_verifications

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class EditorsPagePagination(BaseModel):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)


class SyncEditorsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    editors: List[_T]
    pagination: Optional[EditorsPagePagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        editors = self.editors
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
    editors: List[_T]
    pagination: Optional[EditorsPagePagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        editors = self.editors
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


class EntriesPagePagination(BaseModel):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)


class SyncEntriesPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    entries: List[_T]
    pagination: Optional[EntriesPagePagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        entries = self.entries
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
    entries: List[_T]
    pagination: Optional[EntriesPagePagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        entries = self.entries
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


class EnvironmentClassesPagePagination(BaseModel):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)


class SyncEnvironmentClassesPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    environment_classes: List[_T] = FieldInfo(alias="environmentClasses")
    pagination: Optional[EnvironmentClassesPagePagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        environment_classes = self.environment_classes
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
    environment_classes: List[_T] = FieldInfo(alias="environmentClasses")
    pagination: Optional[EnvironmentClassesPagePagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        environment_classes = self.environment_classes
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


class EnvironmentsPagePagination(BaseModel):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)


class SyncEnvironmentsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    environments: List[_T]
    pagination: Optional[EnvironmentsPagePagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        environments = self.environments
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
    environments: List[_T]
    pagination: Optional[EnvironmentsPagePagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        environments = self.environments
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


class GatewaysPagePagination(BaseModel):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)


class SyncGatewaysPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    gateways: List[_T]
    pagination: Optional[GatewaysPagePagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        gateways = self.gateways
        if not gateways:
            return []
        return gateways

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncGatewaysPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    gateways: List[_T]
    pagination: Optional[GatewaysPagePagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        gateways = self.gateways
        if not gateways:
            return []
        return gateways

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class GroupsPagePagination(BaseModel):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)


class SyncGroupsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    groups: List[_T]
    pagination: Optional[GroupsPagePagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        groups = self.groups
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
    groups: List[_T]
    pagination: Optional[GroupsPagePagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        groups = self.groups
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


class IntegrationsPagePagination(BaseModel):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)


class SyncIntegrationsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    integrations: List[_T]
    pagination: Optional[IntegrationsPagePagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        integrations = self.integrations
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
    integrations: List[_T]
    pagination: Optional[IntegrationsPagePagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        integrations = self.integrations
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


class JoinableOrganizationsPagePagination(BaseModel):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)


class SyncJoinableOrganizationsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    joinable_organizations: List[_T] = FieldInfo(alias="joinableOrganizations")
    pagination: Optional[JoinableOrganizationsPagePagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        joinable_organizations = self.joinable_organizations
        if not joinable_organizations:
            return []
        return joinable_organizations

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncJoinableOrganizationsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    joinable_organizations: List[_T] = FieldInfo(alias="joinableOrganizations")
    pagination: Optional[JoinableOrganizationsPagePagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        joinable_organizations = self.joinable_organizations
        if not joinable_organizations:
            return []
        return joinable_organizations

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class LoginProvidersPagePagination(BaseModel):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)


class SyncLoginProvidersPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    login_providers: List[_T] = FieldInfo(alias="loginProviders")
    pagination: Optional[LoginProvidersPagePagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        login_providers = self.login_providers
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
    login_providers: List[_T] = FieldInfo(alias="loginProviders")
    pagination: Optional[LoginProvidersPagePagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        login_providers = self.login_providers
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


class LoginsPagePagination(BaseModel):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)


class SyncLoginsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    logins: List[_T]
    pagination: Optional[LoginsPagePagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        logins = self.logins
        if not logins:
            return []
        return logins

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncLoginsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    logins: List[_T]
    pagination: Optional[LoginsPagePagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        logins = self.logins
        if not logins:
            return []
        return logins

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class MembersPagePagination(BaseModel):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)


class SyncMembersPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    members: List[_T]
    pagination: Optional[MembersPagePagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        members = self.members
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
    members: List[_T]
    pagination: Optional[MembersPagePagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        members = self.members
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


class PersonalAccessTokensPagePagination(BaseModel):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)


class SyncPersonalAccessTokensPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[PersonalAccessTokensPagePagination] = None
    personal_access_tokens: List[_T] = FieldInfo(alias="personalAccessTokens")

    @override
    def _get_page_items(self) -> List[_T]:
        personal_access_tokens = self.personal_access_tokens
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
    pagination: Optional[PersonalAccessTokensPagePagination] = None
    personal_access_tokens: List[_T] = FieldInfo(alias="personalAccessTokens")

    @override
    def _get_page_items(self) -> List[_T]:
        personal_access_tokens = self.personal_access_tokens
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


class PoliciesPagePagination(BaseModel):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)


class SyncPoliciesPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[PoliciesPagePagination] = None
    policies: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        policies = self.policies
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
    pagination: Optional[PoliciesPagePagination] = None
    policies: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        policies = self.policies
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


class PrebuildsPagePagination(BaseModel):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)


class SyncPrebuildsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[PrebuildsPagePagination] = None
    prebuilds: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        prebuilds = self.prebuilds
        if not prebuilds:
            return []
        return prebuilds

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncPrebuildsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[PrebuildsPagePagination] = None
    prebuilds: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        prebuilds = self.prebuilds
        if not prebuilds:
            return []
        return prebuilds

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class ProjectEnvironmentClassesPagePagination(BaseModel):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)


class SyncProjectEnvironmentClassesPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[ProjectEnvironmentClassesPagePagination] = None
    project_environment_classes: List[_T] = FieldInfo(alias="projectEnvironmentClasses")

    @override
    def _get_page_items(self) -> List[_T]:
        project_environment_classes = self.project_environment_classes
        if not project_environment_classes:
            return []
        return project_environment_classes

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncProjectEnvironmentClassesPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[ProjectEnvironmentClassesPagePagination] = None
    project_environment_classes: List[_T] = FieldInfo(alias="projectEnvironmentClasses")

    @override
    def _get_page_items(self) -> List[_T]:
        project_environment_classes = self.project_environment_classes
        if not project_environment_classes:
            return []
        return project_environment_classes

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class ProjectsPagePagination(BaseModel):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)


class SyncProjectsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[ProjectsPagePagination] = None
    projects: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        projects = self.projects
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
    pagination: Optional[ProjectsPagePagination] = None
    projects: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        projects = self.projects
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


class PromptsPagePagination(BaseModel):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)


class SyncPromptsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[PromptsPagePagination] = None
    prompts: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        prompts = self.prompts
        if not prompts:
            return []
        return prompts

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncPromptsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[PromptsPagePagination] = None
    prompts: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        prompts = self.prompts
        if not prompts:
            return []
        return prompts

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class RecordsPagePagination(BaseModel):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)


class SyncRecordsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[RecordsPagePagination] = None
    records: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        records = self.records
        if not records:
            return []
        return records

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncRecordsPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[RecordsPagePagination] = None
    records: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        records = self.records
        if not records:
            return []
        return records

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class RepositoriesPagePagination(BaseModel):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)


class SyncRepositoriesPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[RepositoriesPagePagination] = None
    repositories: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        repositories = self.repositories
        if not repositories:
            return []
        return repositories

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class AsyncRepositoriesPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[RepositoriesPagePagination] = None
    repositories: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        repositories = self.repositories
        if not repositories:
            return []
        return repositories

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_token = None
        if self.pagination is not None:
            if self.pagination.next_token is not None:
                next_token = self.pagination.next_token
        if not next_token:
            return None

        return PageInfo(params={"token": next_token})


class RunnersPagePagination(BaseModel):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)


class SyncRunnersPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[RunnersPagePagination] = None
    runners: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        runners = self.runners
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
    pagination: Optional[RunnersPagePagination] = None
    runners: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        runners = self.runners
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


class SecretsPagePagination(BaseModel):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)


class SyncSecretsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[SecretsPagePagination] = None
    secrets: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        secrets = self.secrets
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
    pagination: Optional[SecretsPagePagination] = None
    secrets: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        secrets = self.secrets
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


class ServicesPagePagination(BaseModel):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)


class SyncServicesPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[ServicesPagePagination] = None
    services: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        services = self.services
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
    pagination: Optional[ServicesPagePagination] = None
    services: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        services = self.services
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


class SSOConfigurationsPagePagination(BaseModel):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)


class SyncSSOConfigurationsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[SSOConfigurationsPagePagination] = None
    sso_configurations: List[_T] = FieldInfo(alias="ssoConfigurations")

    @override
    def _get_page_items(self) -> List[_T]:
        sso_configurations = self.sso_configurations
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
    pagination: Optional[SSOConfigurationsPagePagination] = None
    sso_configurations: List[_T] = FieldInfo(alias="ssoConfigurations")

    @override
    def _get_page_items(self) -> List[_T]:
        sso_configurations = self.sso_configurations
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


class TaskExecutionsPagePagination(BaseModel):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)


class SyncTaskExecutionsPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[TaskExecutionsPagePagination] = None
    task_executions: List[_T] = FieldInfo(alias="taskExecutions")

    @override
    def _get_page_items(self) -> List[_T]:
        task_executions = self.task_executions
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
    pagination: Optional[TaskExecutionsPagePagination] = None
    task_executions: List[_T] = FieldInfo(alias="taskExecutions")

    @override
    def _get_page_items(self) -> List[_T]:
        task_executions = self.task_executions
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


class TasksPagePagination(BaseModel):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)


class SyncTasksPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[TasksPagePagination] = None
    tasks: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        tasks = self.tasks
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
    pagination: Optional[TasksPagePagination] = None
    tasks: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        tasks = self.tasks
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


class TokensPagePagination(BaseModel):
    next_token: Optional[str] = FieldInfo(alias="nextToken", default=None)


class SyncTokensPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    pagination: Optional[TokensPagePagination] = None
    tokens: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        tokens = self.tokens
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
    pagination: Optional[TokensPagePagination] = None
    tokens: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        tokens = self.tokens
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
