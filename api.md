# Shared Types

```python
from gitpod.types import (
    AutomationTrigger,
    EnvironmentClass,
    ErrorCode,
    FieldValue,
    OrganizationRole,
    Principal,
    RunsOn,
    Subject,
    Task,
    TaskExecution,
    TaskExecutionMetadata,
    TaskExecutionPhase,
    TaskExecutionSpec,
    TaskExecutionStatus,
    TaskMetadata,
    TaskSpec,
    UserStatus,
)
```

# Accounts

Types:

```python
from gitpod.types import (
    Account,
    AccountMembership,
    JoinableOrganization,
    LoginProvider,
    AccountRetrieveResponse,
    AccountDeleteResponse,
    AccountGetSSOLoginURLResponse,
)
```

Methods:

- <code title="post /gitpod.v1.AccountService/GetAccount">client.accounts.<a href="./src/gitpod/resources/accounts.py">retrieve</a>(\*\*<a href="src/gitpod/types/account_retrieve_params.py">params</a>) -> <a href="./src/gitpod/types/account_retrieve_response.py">AccountRetrieveResponse</a></code>
- <code title="post /gitpod.v1.AccountService/DeleteAccount">client.accounts.<a href="./src/gitpod/resources/accounts.py">delete</a>(\*\*<a href="src/gitpod/types/account_delete_params.py">params</a>) -> <a href="./src/gitpod/types/account_delete_response.py">object</a></code>
- <code title="post /gitpod.v1.AccountService/GetSSOLoginURL">client.accounts.<a href="./src/gitpod/resources/accounts.py">get_sso_login_url</a>(\*\*<a href="src/gitpod/types/account_get_sso_login_url_params.py">params</a>) -> <a href="./src/gitpod/types/account_get_sso_login_url_response.py">AccountGetSSOLoginURLResponse</a></code>
- <code title="post /gitpod.v1.AccountService/ListLoginProviders">client.accounts.<a href="./src/gitpod/resources/accounts.py">list_login_providers</a>(\*\*<a href="src/gitpod/types/account_list_login_providers_params.py">params</a>) -> <a href="./src/gitpod/types/login_provider.py">SyncLoginProvidersPage[LoginProvider]</a></code>

# Editors

Types:

```python
from gitpod.types import Editor, EditorRetrieveResponse, EditorResolveURLResponse
```

Methods:

- <code title="post /gitpod.v1.EditorService/GetEditor">client.editors.<a href="./src/gitpod/resources/editors.py">retrieve</a>(\*\*<a href="src/gitpod/types/editor_retrieve_params.py">params</a>) -> <a href="./src/gitpod/types/editor_retrieve_response.py">EditorRetrieveResponse</a></code>
- <code title="post /gitpod.v1.EditorService/ListEditors">client.editors.<a href="./src/gitpod/resources/editors.py">list</a>(\*\*<a href="src/gitpod/types/editor_list_params.py">params</a>) -> <a href="./src/gitpod/types/editor.py">SyncEditorsPage[Editor]</a></code>
- <code title="post /gitpod.v1.EditorService/ResolveEditorURL">client.editors.<a href="./src/gitpod/resources/editors.py">resolve_url</a>(\*\*<a href="src/gitpod/types/editor_resolve_url_params.py">params</a>) -> <a href="./src/gitpod/types/editor_resolve_url_response.py">EditorResolveURLResponse</a></code>

# Environments

Types:

```python
from gitpod.types import (
    AdmissionLevel,
    Environment,
    EnvironmentActivitySignal,
    EnvironmentMetadata,
    EnvironmentPhase,
    EnvironmentSpec,
    EnvironmentStatus,
    EnvironmentCreateResponse,
    EnvironmentRetrieveResponse,
    EnvironmentUpdateResponse,
    EnvironmentDeleteResponse,
    EnvironmentCreateFromProjectResponse,
    EnvironmentCreateLogsTokenResponse,
    EnvironmentMarkActiveResponse,
    EnvironmentStartResponse,
    EnvironmentStopResponse,
)
```

Methods:

- <code title="post /gitpod.v1.EnvironmentService/CreateEnvironment">client.environments.<a href="./src/gitpod/resources/environments/environments.py">create</a>(\*\*<a href="src/gitpod/types/environment_create_params.py">params</a>) -> <a href="./src/gitpod/types/environment_create_response.py">EnvironmentCreateResponse</a></code>
- <code title="post /gitpod.v1.EnvironmentService/GetEnvironment">client.environments.<a href="./src/gitpod/resources/environments/environments.py">retrieve</a>(\*\*<a href="src/gitpod/types/environment_retrieve_params.py">params</a>) -> <a href="./src/gitpod/types/environment_retrieve_response.py">EnvironmentRetrieveResponse</a></code>
- <code title="post /gitpod.v1.EnvironmentService/UpdateEnvironment">client.environments.<a href="./src/gitpod/resources/environments/environments.py">update</a>(\*\*<a href="src/gitpod/types/environment_update_params.py">params</a>) -> <a href="./src/gitpod/types/environment_update_response.py">object</a></code>
- <code title="post /gitpod.v1.EnvironmentService/ListEnvironments">client.environments.<a href="./src/gitpod/resources/environments/environments.py">list</a>(\*\*<a href="src/gitpod/types/environment_list_params.py">params</a>) -> <a href="./src/gitpod/types/environment.py">SyncEnvironmentsPage[Environment]</a></code>
- <code title="post /gitpod.v1.EnvironmentService/DeleteEnvironment">client.environments.<a href="./src/gitpod/resources/environments/environments.py">delete</a>(\*\*<a href="src/gitpod/types/environment_delete_params.py">params</a>) -> <a href="./src/gitpod/types/environment_delete_response.py">object</a></code>
- <code title="post /gitpod.v1.EnvironmentService/CreateEnvironmentFromProject">client.environments.<a href="./src/gitpod/resources/environments/environments.py">create_from_project</a>(\*\*<a href="src/gitpod/types/environment_create_from_project_params.py">params</a>) -> <a href="./src/gitpod/types/environment_create_from_project_response.py">EnvironmentCreateFromProjectResponse</a></code>
- <code title="post /gitpod.v1.EnvironmentService/CreateEnvironmentLogsToken">client.environments.<a href="./src/gitpod/resources/environments/environments.py">create_logs_token</a>(\*\*<a href="src/gitpod/types/environment_create_logs_token_params.py">params</a>) -> <a href="./src/gitpod/types/environment_create_logs_token_response.py">EnvironmentCreateLogsTokenResponse</a></code>
- <code title="post /gitpod.v1.EnvironmentService/MarkEnvironmentActive">client.environments.<a href="./src/gitpod/resources/environments/environments.py">mark_active</a>(\*\*<a href="src/gitpod/types/environment_mark_active_params.py">params</a>) -> <a href="./src/gitpod/types/environment_mark_active_response.py">object</a></code>
- <code title="post /gitpod.v1.EnvironmentService/StartEnvironment">client.environments.<a href="./src/gitpod/resources/environments/environments.py">start</a>(\*\*<a href="src/gitpod/types/environment_start_params.py">params</a>) -> <a href="./src/gitpod/types/environment_start_response.py">object</a></code>
- <code title="post /gitpod.v1.EnvironmentService/StopEnvironment">client.environments.<a href="./src/gitpod/resources/environments/environments.py">stop</a>(\*\*<a href="src/gitpod/types/environment_stop_params.py">params</a>) -> <a href="./src/gitpod/types/environment_stop_response.py">object</a></code>

## Automations

Types:

```python
from gitpod.types.environments import AutomationsFile, AutomationUpsertResponse
```

Methods:

- <code title="post /gitpod.v1.EnvironmentAutomationService/UpsertAutomationsFile">client.environments.automations.<a href="./src/gitpod/resources/environments/automations/automations.py">upsert</a>(\*\*<a href="src/gitpod/types/environments/automation_upsert_params.py">params</a>) -> <a href="./src/gitpod/types/environments/automation_upsert_response.py">AutomationUpsertResponse</a></code>

### Services

Types:

```python
from gitpod.types.environments.automations import (
    Service,
    ServiceMetadata,
    ServicePhase,
    ServiceSpec,
    ServiceStatus,
    ServiceCreateResponse,
    ServiceRetrieveResponse,
    ServiceUpdateResponse,
    ServiceDeleteResponse,
    ServiceStartResponse,
    ServiceStopResponse,
)
```

Methods:

- <code title="post /gitpod.v1.EnvironmentAutomationService/CreateService">client.environments.automations.services.<a href="./src/gitpod/resources/environments/automations/services.py">create</a>(\*\*<a href="src/gitpod/types/environments/automations/service_create_params.py">params</a>) -> <a href="./src/gitpod/types/environments/automations/service_create_response.py">ServiceCreateResponse</a></code>
- <code title="post /gitpod.v1.EnvironmentAutomationService/GetService">client.environments.automations.services.<a href="./src/gitpod/resources/environments/automations/services.py">retrieve</a>(\*\*<a href="src/gitpod/types/environments/automations/service_retrieve_params.py">params</a>) -> <a href="./src/gitpod/types/environments/automations/service_retrieve_response.py">ServiceRetrieveResponse</a></code>
- <code title="post /gitpod.v1.EnvironmentAutomationService/UpdateService">client.environments.automations.services.<a href="./src/gitpod/resources/environments/automations/services.py">update</a>(\*\*<a href="src/gitpod/types/environments/automations/service_update_params.py">params</a>) -> <a href="./src/gitpod/types/environments/automations/service_update_response.py">object</a></code>
- <code title="post /gitpod.v1.EnvironmentAutomationService/ListServices">client.environments.automations.services.<a href="./src/gitpod/resources/environments/automations/services.py">list</a>(\*\*<a href="src/gitpod/types/environments/automations/service_list_params.py">params</a>) -> <a href="./src/gitpod/types/environments/automations/service.py">SyncServicesPage[Service]</a></code>
- <code title="post /gitpod.v1.EnvironmentAutomationService/DeleteService">client.environments.automations.services.<a href="./src/gitpod/resources/environments/automations/services.py">delete</a>(\*\*<a href="src/gitpod/types/environments/automations/service_delete_params.py">params</a>) -> <a href="./src/gitpod/types/environments/automations/service_delete_response.py">object</a></code>
- <code title="post /gitpod.v1.EnvironmentAutomationService/StartService">client.environments.automations.services.<a href="./src/gitpod/resources/environments/automations/services.py">start</a>(\*\*<a href="src/gitpod/types/environments/automations/service_start_params.py">params</a>) -> <a href="./src/gitpod/types/environments/automations/service_start_response.py">object</a></code>
- <code title="post /gitpod.v1.EnvironmentAutomationService/StopService">client.environments.automations.services.<a href="./src/gitpod/resources/environments/automations/services.py">stop</a>(\*\*<a href="src/gitpod/types/environments/automations/service_stop_params.py">params</a>) -> <a href="./src/gitpod/types/environments/automations/service_stop_response.py">object</a></code>

### Tasks

Types:

```python
from gitpod.types.environments.automations import (
    TaskCreateResponse,
    TaskRetrieveResponse,
    TaskUpdateResponse,
    TaskDeleteResponse,
    TaskStartResponse,
)
```

Methods:

- <code title="post /gitpod.v1.EnvironmentAutomationService/CreateTask">client.environments.automations.tasks.<a href="./src/gitpod/resources/environments/automations/tasks/tasks.py">create</a>(\*\*<a href="src/gitpod/types/environments/automations/task_create_params.py">params</a>) -> <a href="./src/gitpod/types/environments/automations/task_create_response.py">TaskCreateResponse</a></code>
- <code title="post /gitpod.v1.EnvironmentAutomationService/GetTask">client.environments.automations.tasks.<a href="./src/gitpod/resources/environments/automations/tasks/tasks.py">retrieve</a>(\*\*<a href="src/gitpod/types/environments/automations/task_retrieve_params.py">params</a>) -> <a href="./src/gitpod/types/environments/automations/task_retrieve_response.py">TaskRetrieveResponse</a></code>
- <code title="post /gitpod.v1.EnvironmentAutomationService/UpdateTask">client.environments.automations.tasks.<a href="./src/gitpod/resources/environments/automations/tasks/tasks.py">update</a>(\*\*<a href="src/gitpod/types/environments/automations/task_update_params.py">params</a>) -> <a href="./src/gitpod/types/environments/automations/task_update_response.py">object</a></code>
- <code title="post /gitpod.v1.EnvironmentAutomationService/ListTasks">client.environments.automations.tasks.<a href="./src/gitpod/resources/environments/automations/tasks/tasks.py">list</a>(\*\*<a href="src/gitpod/types/environments/automations/task_list_params.py">params</a>) -> <a href="./src/gitpod/types/shared/task.py">SyncTasksPage[Task]</a></code>
- <code title="post /gitpod.v1.EnvironmentAutomationService/DeleteTask">client.environments.automations.tasks.<a href="./src/gitpod/resources/environments/automations/tasks/tasks.py">delete</a>(\*\*<a href="src/gitpod/types/environments/automations/task_delete_params.py">params</a>) -> <a href="./src/gitpod/types/environments/automations/task_delete_response.py">object</a></code>
- <code title="post /gitpod.v1.EnvironmentAutomationService/StartTask">client.environments.automations.tasks.<a href="./src/gitpod/resources/environments/automations/tasks/tasks.py">start</a>(\*\*<a href="src/gitpod/types/environments/automations/task_start_params.py">params</a>) -> <a href="./src/gitpod/types/environments/automations/task_start_response.py">TaskStartResponse</a></code>

#### Executions

Types:

```python
from gitpod.types.environments.automations.tasks import (
    ExecutionRetrieveResponse,
    ExecutionStopResponse,
)
```

Methods:

- <code title="post /gitpod.v1.EnvironmentAutomationService/GetTaskExecution">client.environments.automations.tasks.executions.<a href="./src/gitpod/resources/environments/automations/tasks/executions.py">retrieve</a>(\*\*<a href="src/gitpod/types/environments/automations/tasks/execution_retrieve_params.py">params</a>) -> <a href="./src/gitpod/types/environments/automations/tasks/execution_retrieve_response.py">ExecutionRetrieveResponse</a></code>
- <code title="post /gitpod.v1.EnvironmentAutomationService/ListTaskExecutions">client.environments.automations.tasks.executions.<a href="./src/gitpod/resources/environments/automations/tasks/executions.py">list</a>(\*\*<a href="src/gitpod/types/environments/automations/tasks/execution_list_params.py">params</a>) -> <a href="./src/gitpod/types/shared/task_execution.py">SyncTaskExecutionsPage[TaskExecution]</a></code>
- <code title="post /gitpod.v1.EnvironmentAutomationService/StopTaskExecution">client.environments.automations.tasks.executions.<a href="./src/gitpod/resources/environments/automations/tasks/executions.py">stop</a>(\*\*<a href="src/gitpod/types/environments/automations/tasks/execution_stop_params.py">params</a>) -> <a href="./src/gitpod/types/environments/automations/tasks/execution_stop_response.py">object</a></code>

## Classes

Methods:

- <code title="post /gitpod.v1.EnvironmentService/ListEnvironmentClasses">client.environments.classes.<a href="./src/gitpod/resources/environments/classes.py">list</a>(\*\*<a href="src/gitpod/types/environments/class_list_params.py">params</a>) -> <a href="./src/gitpod/types/shared/environment_class.py">SyncEnvironmentClassesPage[EnvironmentClass]</a></code>

# Events

Types:

```python
from gitpod.types import ResourceOperation, ResourceType, EventListResponse, EventWatchResponse
```

Methods:

- <code title="post /gitpod.v1.EventService/ListAuditLogs">client.events.<a href="./src/gitpod/resources/events.py">list</a>(\*\*<a href="src/gitpod/types/event_list_params.py">params</a>) -> <a href="./src/gitpod/types/event_list_response.py">SyncEntriesPage[EventListResponse]</a></code>
- <code title="post /gitpod.v1.EventService/WatchEvents">client.events.<a href="./src/gitpod/resources/events.py">watch</a>(\*\*<a href="src/gitpod/types/event_watch_params.py">params</a>) -> <a href="./src/gitpod/types/event_watch_response.py">JSONLDecoder[EventWatchResponse]</a></code>

# Groups

Types:

```python
from gitpod.types import Group
```

Methods:

- <code title="post /gitpod.v1.GroupService/ListGroups">client.groups.<a href="./src/gitpod/resources/groups.py">list</a>(\*\*<a href="src/gitpod/types/group_list_params.py">params</a>) -> <a href="./src/gitpod/types/group.py">SyncGroupsPage[Group]</a></code>

# Identity

Types:

```python
from gitpod.types import (
    IdentityExchangeTokenResponse,
    IdentityGetAuthenticatedIdentityResponse,
    IdentityGetIDTokenResponse,
)
```

Methods:

- <code title="post /gitpod.v1.IdentityService/ExchangeToken">client.identity.<a href="./src/gitpod/resources/identity.py">exchange_token</a>(\*\*<a href="src/gitpod/types/identity_exchange_token_params.py">params</a>) -> <a href="./src/gitpod/types/identity_exchange_token_response.py">IdentityExchangeTokenResponse</a></code>
- <code title="post /gitpod.v1.IdentityService/GetAuthenticatedIdentity">client.identity.<a href="./src/gitpod/resources/identity.py">get_authenticated_identity</a>(\*\*<a href="src/gitpod/types/identity_get_authenticated_identity_params.py">params</a>) -> <a href="./src/gitpod/types/identity_get_authenticated_identity_response.py">IdentityGetAuthenticatedIdentityResponse</a></code>
- <code title="post /gitpod.v1.IdentityService/GetIDToken">client.identity.<a href="./src/gitpod/resources/identity.py">get_id_token</a>(\*\*<a href="src/gitpod/types/identity_get_id_token_params.py">params</a>) -> <a href="./src/gitpod/types/identity_get_id_token_response.py">IdentityGetIDTokenResponse</a></code>

# Organizations

Types:

```python
from gitpod.types import (
    InviteDomains,
    Organization,
    OrganizationMember,
    Scope,
    OrganizationCreateResponse,
    OrganizationRetrieveResponse,
    OrganizationUpdateResponse,
    OrganizationDeleteResponse,
    OrganizationJoinResponse,
    OrganizationLeaveResponse,
    OrganizationSetRoleResponse,
)
```

Methods:

- <code title="post /gitpod.v1.OrganizationService/CreateOrganization">client.organizations.<a href="./src/gitpod/resources/organizations/organizations.py">create</a>(\*\*<a href="src/gitpod/types/organization_create_params.py">params</a>) -> <a href="./src/gitpod/types/organization_create_response.py">OrganizationCreateResponse</a></code>
- <code title="post /gitpod.v1.OrganizationService/GetOrganization">client.organizations.<a href="./src/gitpod/resources/organizations/organizations.py">retrieve</a>(\*\*<a href="src/gitpod/types/organization_retrieve_params.py">params</a>) -> <a href="./src/gitpod/types/organization_retrieve_response.py">OrganizationRetrieveResponse</a></code>
- <code title="post /gitpod.v1.OrganizationService/UpdateOrganization">client.organizations.<a href="./src/gitpod/resources/organizations/organizations.py">update</a>(\*\*<a href="src/gitpod/types/organization_update_params.py">params</a>) -> <a href="./src/gitpod/types/organization_update_response.py">OrganizationUpdateResponse</a></code>
- <code title="post /gitpod.v1.OrganizationService/ListOrganizations">client.organizations.<a href="./src/gitpod/resources/organizations/organizations.py">list</a>(\*\*<a href="src/gitpod/types/organization_list_params.py">params</a>) -> <a href="./src/gitpod/types/organization.py">SyncOrganizationsPage[Organization]</a></code>
- <code title="post /gitpod.v1.OrganizationService/DeleteOrganization">client.organizations.<a href="./src/gitpod/resources/organizations/organizations.py">delete</a>(\*\*<a href="src/gitpod/types/organization_delete_params.py">params</a>) -> <a href="./src/gitpod/types/organization_delete_response.py">object</a></code>
- <code title="post /gitpod.v1.OrganizationService/JoinOrganization">client.organizations.<a href="./src/gitpod/resources/organizations/organizations.py">join</a>(\*\*<a href="src/gitpod/types/organization_join_params.py">params</a>) -> <a href="./src/gitpod/types/organization_join_response.py">OrganizationJoinResponse</a></code>
- <code title="post /gitpod.v1.OrganizationService/LeaveOrganization">client.organizations.<a href="./src/gitpod/resources/organizations/organizations.py">leave</a>(\*\*<a href="src/gitpod/types/organization_leave_params.py">params</a>) -> <a href="./src/gitpod/types/organization_leave_response.py">object</a></code>
- <code title="post /gitpod.v1.OrganizationService/ListMembers">client.organizations.<a href="./src/gitpod/resources/organizations/organizations.py">list_members</a>(\*\*<a href="src/gitpod/types/organization_list_members_params.py">params</a>) -> <a href="./src/gitpod/types/organization_member.py">SyncMembersPage[OrganizationMember]</a></code>
- <code title="post /gitpod.v1.OrganizationService/SetRole">client.organizations.<a href="./src/gitpod/resources/organizations/organizations.py">set_role</a>(\*\*<a href="src/gitpod/types/organization_set_role_params.py">params</a>) -> <a href="./src/gitpod/types/organization_set_role_response.py">object</a></code>

## DomainVerifications

Types:

```python
from gitpod.types.organizations import (
    DomainVerification,
    DomainVerificationState,
    DomainVerificationCreateResponse,
    DomainVerificationRetrieveResponse,
    DomainVerificationDeleteResponse,
    DomainVerificationVerifyResponse,
)
```

Methods:

- <code title="post /gitpod.v1.OrganizationService/CreateDomainVerification">client.organizations.domain_verifications.<a href="./src/gitpod/resources/organizations/domain_verifications.py">create</a>(\*\*<a href="src/gitpod/types/organizations/domain_verification_create_params.py">params</a>) -> <a href="./src/gitpod/types/organizations/domain_verification_create_response.py">DomainVerificationCreateResponse</a></code>
- <code title="post /gitpod.v1.OrganizationService/GetDomainVerification">client.organizations.domain_verifications.<a href="./src/gitpod/resources/organizations/domain_verifications.py">retrieve</a>(\*\*<a href="src/gitpod/types/organizations/domain_verification_retrieve_params.py">params</a>) -> <a href="./src/gitpod/types/organizations/domain_verification_retrieve_response.py">DomainVerificationRetrieveResponse</a></code>
- <code title="post /gitpod.v1.OrganizationService/ListDomainVerifications">client.organizations.domain_verifications.<a href="./src/gitpod/resources/organizations/domain_verifications.py">list</a>(\*\*<a href="src/gitpod/types/organizations/domain_verification_list_params.py">params</a>) -> <a href="./src/gitpod/types/organizations/domain_verification.py">SyncDomainVerificationsPage[DomainVerification]</a></code>
- <code title="post /gitpod.v1.OrganizationService/DeleteDomainVerification">client.organizations.domain_verifications.<a href="./src/gitpod/resources/organizations/domain_verifications.py">delete</a>(\*\*<a href="src/gitpod/types/organizations/domain_verification_delete_params.py">params</a>) -> <a href="./src/gitpod/types/organizations/domain_verification_delete_response.py">object</a></code>
- <code title="post /gitpod.v1.OrganizationService/VerifyDomain">client.organizations.domain_verifications.<a href="./src/gitpod/resources/organizations/domain_verifications.py">verify</a>(\*\*<a href="src/gitpod/types/organizations/domain_verification_verify_params.py">params</a>) -> <a href="./src/gitpod/types/organizations/domain_verification_verify_response.py">DomainVerificationVerifyResponse</a></code>

## Invites

Types:

```python
from gitpod.types.organizations import (
    OrganizationInvite,
    InviteCreateResponse,
    InviteRetrieveResponse,
    InviteGetSummaryResponse,
)
```

Methods:

- <code title="post /gitpod.v1.OrganizationService/CreateOrganizationInvite">client.organizations.invites.<a href="./src/gitpod/resources/organizations/invites.py">create</a>(\*\*<a href="src/gitpod/types/organizations/invite_create_params.py">params</a>) -> <a href="./src/gitpod/types/organizations/invite_create_response.py">InviteCreateResponse</a></code>
- <code title="post /gitpod.v1.OrganizationService/GetOrganizationInvite">client.organizations.invites.<a href="./src/gitpod/resources/organizations/invites.py">retrieve</a>(\*\*<a href="src/gitpod/types/organizations/invite_retrieve_params.py">params</a>) -> <a href="./src/gitpod/types/organizations/invite_retrieve_response.py">InviteRetrieveResponse</a></code>
- <code title="post /gitpod.v1.OrganizationService/GetOrganizationInviteSummary">client.organizations.invites.<a href="./src/gitpod/resources/organizations/invites.py">get_summary</a>(\*\*<a href="src/gitpod/types/organizations/invite_get_summary_params.py">params</a>) -> <a href="./src/gitpod/types/organizations/invite_get_summary_response.py">InviteGetSummaryResponse</a></code>

## SSOConfigurations

Types:

```python
from gitpod.types.organizations import (
    ProviderType,
    SSOConfiguration,
    SSOConfigurationState,
    SSOConfigurationCreateResponse,
    SSOConfigurationRetrieveResponse,
    SSOConfigurationUpdateResponse,
    SSOConfigurationDeleteResponse,
)
```

Methods:

- <code title="post /gitpod.v1.OrganizationService/CreateSSOConfiguration">client.organizations.sso_configurations.<a href="./src/gitpod/resources/organizations/sso_configurations.py">create</a>(\*\*<a href="src/gitpod/types/organizations/sso_configuration_create_params.py">params</a>) -> <a href="./src/gitpod/types/organizations/sso_configuration_create_response.py">SSOConfigurationCreateResponse</a></code>
- <code title="post /gitpod.v1.OrganizationService/GetSSOConfiguration">client.organizations.sso_configurations.<a href="./src/gitpod/resources/organizations/sso_configurations.py">retrieve</a>(\*\*<a href="src/gitpod/types/organizations/sso_configuration_retrieve_params.py">params</a>) -> <a href="./src/gitpod/types/organizations/sso_configuration_retrieve_response.py">SSOConfigurationRetrieveResponse</a></code>
- <code title="post /gitpod.v1.OrganizationService/UpdateSSOConfiguration">client.organizations.sso_configurations.<a href="./src/gitpod/resources/organizations/sso_configurations.py">update</a>(\*\*<a href="src/gitpod/types/organizations/sso_configuration_update_params.py">params</a>) -> <a href="./src/gitpod/types/organizations/sso_configuration_update_response.py">object</a></code>
- <code title="post /gitpod.v1.OrganizationService/ListSSOConfigurations">client.organizations.sso_configurations.<a href="./src/gitpod/resources/organizations/sso_configurations.py">list</a>(\*\*<a href="src/gitpod/types/organizations/sso_configuration_list_params.py">params</a>) -> <a href="./src/gitpod/types/organizations/sso_configuration.py">SyncSSOConfigurationsPage[SSOConfiguration]</a></code>
- <code title="post /gitpod.v1.OrganizationService/DeleteSSOConfiguration">client.organizations.sso_configurations.<a href="./src/gitpod/resources/organizations/sso_configurations.py">delete</a>(\*\*<a href="src/gitpod/types/organizations/sso_configuration_delete_params.py">params</a>) -> <a href="./src/gitpod/types/organizations/sso_configuration_delete_response.py">object</a></code>

# Projects

Types:

```python
from gitpod.types import (
    EnvironmentInitializer,
    Project,
    ProjectEnvironmentClass,
    ProjectMetadata,
    ProjectCreateResponse,
    ProjectRetrieveResponse,
    ProjectUpdateResponse,
    ProjectDeleteResponse,
    ProjectCreateFromEnvironmentResponse,
)
```

Methods:

- <code title="post /gitpod.v1.ProjectService/CreateProject">client.projects.<a href="./src/gitpod/resources/projects/projects.py">create</a>(\*\*<a href="src/gitpod/types/project_create_params.py">params</a>) -> <a href="./src/gitpod/types/project_create_response.py">ProjectCreateResponse</a></code>
- <code title="post /gitpod.v1.ProjectService/GetProject">client.projects.<a href="./src/gitpod/resources/projects/projects.py">retrieve</a>(\*\*<a href="src/gitpod/types/project_retrieve_params.py">params</a>) -> <a href="./src/gitpod/types/project_retrieve_response.py">ProjectRetrieveResponse</a></code>
- <code title="post /gitpod.v1.ProjectService/UpdateProject">client.projects.<a href="./src/gitpod/resources/projects/projects.py">update</a>(\*\*<a href="src/gitpod/types/project_update_params.py">params</a>) -> <a href="./src/gitpod/types/project_update_response.py">ProjectUpdateResponse</a></code>
- <code title="post /gitpod.v1.ProjectService/ListProjects">client.projects.<a href="./src/gitpod/resources/projects/projects.py">list</a>(\*\*<a href="src/gitpod/types/project_list_params.py">params</a>) -> <a href="./src/gitpod/types/project.py">SyncProjectsPage[Project]</a></code>
- <code title="post /gitpod.v1.ProjectService/DeleteProject">client.projects.<a href="./src/gitpod/resources/projects/projects.py">delete</a>(\*\*<a href="src/gitpod/types/project_delete_params.py">params</a>) -> <a href="./src/gitpod/types/project_delete_response.py">object</a></code>
- <code title="post /gitpod.v1.ProjectService/CreateProjectFromEnvironment">client.projects.<a href="./src/gitpod/resources/projects/projects.py">create_from_environment</a>(\*\*<a href="src/gitpod/types/project_create_from_environment_params.py">params</a>) -> <a href="./src/gitpod/types/project_create_from_environment_response.py">ProjectCreateFromEnvironmentResponse</a></code>

## Policies

Types:

```python
from gitpod.types.projects import (
    ProjectPolicy,
    ProjectRole,
    PolicyCreateResponse,
    PolicyUpdateResponse,
    PolicyDeleteResponse,
)
```

Methods:

- <code title="post /gitpod.v1.ProjectService/CreateProjectPolicy">client.projects.policies.<a href="./src/gitpod/resources/projects/policies.py">create</a>(\*\*<a href="src/gitpod/types/projects/policy_create_params.py">params</a>) -> <a href="./src/gitpod/types/projects/policy_create_response.py">PolicyCreateResponse</a></code>
- <code title="post /gitpod.v1.ProjectService/UpdateProjectPolicy">client.projects.policies.<a href="./src/gitpod/resources/projects/policies.py">update</a>(\*\*<a href="src/gitpod/types/projects/policy_update_params.py">params</a>) -> <a href="./src/gitpod/types/projects/policy_update_response.py">PolicyUpdateResponse</a></code>
- <code title="post /gitpod.v1.ProjectService/ListProjectPolicies">client.projects.policies.<a href="./src/gitpod/resources/projects/policies.py">list</a>(\*\*<a href="src/gitpod/types/projects/policy_list_params.py">params</a>) -> <a href="./src/gitpod/types/projects/project_policy.py">SyncPoliciesPage[ProjectPolicy]</a></code>
- <code title="post /gitpod.v1.ProjectService/DeleteProjectPolicy">client.projects.policies.<a href="./src/gitpod/resources/projects/policies.py">delete</a>(\*\*<a href="src/gitpod/types/projects/policy_delete_params.py">params</a>) -> <a href="./src/gitpod/types/projects/policy_delete_response.py">object</a></code>

# Runners

Types:

```python
from gitpod.types import (
    Runner,
    RunnerCapability,
    RunnerConfiguration,
    RunnerKind,
    RunnerPhase,
    RunnerProvider,
    RunnerReleaseChannel,
    RunnerSpec,
    RunnerStatus,
    RunnerCreateResponse,
    RunnerRetrieveResponse,
    RunnerUpdateResponse,
    RunnerDeleteResponse,
    RunnerCheckAuthenticationForHostResponse,
    RunnerCreateRunnerTokenResponse,
    RunnerParseContextURLResponse,
)
```

Methods:

- <code title="post /gitpod.v1.RunnerService/CreateRunner">client.runners.<a href="./src/gitpod/resources/runners/runners.py">create</a>(\*\*<a href="src/gitpod/types/runner_create_params.py">params</a>) -> <a href="./src/gitpod/types/runner_create_response.py">RunnerCreateResponse</a></code>
- <code title="post /gitpod.v1.RunnerService/GetRunner">client.runners.<a href="./src/gitpod/resources/runners/runners.py">retrieve</a>(\*\*<a href="src/gitpod/types/runner_retrieve_params.py">params</a>) -> <a href="./src/gitpod/types/runner_retrieve_response.py">RunnerRetrieveResponse</a></code>
- <code title="post /gitpod.v1.RunnerService/UpdateRunner">client.runners.<a href="./src/gitpod/resources/runners/runners.py">update</a>(\*\*<a href="src/gitpod/types/runner_update_params.py">params</a>) -> <a href="./src/gitpod/types/runner_update_response.py">object</a></code>
- <code title="post /gitpod.v1.RunnerService/ListRunners">client.runners.<a href="./src/gitpod/resources/runners/runners.py">list</a>(\*\*<a href="src/gitpod/types/runner_list_params.py">params</a>) -> <a href="./src/gitpod/types/runner.py">SyncRunnersPage[Runner]</a></code>
- <code title="post /gitpod.v1.RunnerService/DeleteRunner">client.runners.<a href="./src/gitpod/resources/runners/runners.py">delete</a>(\*\*<a href="src/gitpod/types/runner_delete_params.py">params</a>) -> <a href="./src/gitpod/types/runner_delete_response.py">object</a></code>
- <code title="post /gitpod.v1.RunnerService/CheckAuthenticationForHost">client.runners.<a href="./src/gitpod/resources/runners/runners.py">check_authentication_for_host</a>(\*\*<a href="src/gitpod/types/runner_check_authentication_for_host_params.py">params</a>) -> <a href="./src/gitpod/types/runner_check_authentication_for_host_response.py">RunnerCheckAuthenticationForHostResponse</a></code>
- <code title="post /gitpod.v1.RunnerService/CreateRunnerToken">client.runners.<a href="./src/gitpod/resources/runners/runners.py">create_runner_token</a>(\*\*<a href="src/gitpod/types/runner_create_runner_token_params.py">params</a>) -> <a href="./src/gitpod/types/runner_create_runner_token_response.py">RunnerCreateRunnerTokenResponse</a></code>
- <code title="post /gitpod.v1.RunnerService/ParseContextURL">client.runners.<a href="./src/gitpod/resources/runners/runners.py">parse_context_url</a>(\*\*<a href="src/gitpod/types/runner_parse_context_url_params.py">params</a>) -> <a href="./src/gitpod/types/runner_parse_context_url_response.py">RunnerParseContextURLResponse</a></code>

## Configurations

Types:

```python
from gitpod.types.runners import (
    EnvironmentClassValidationResult,
    FieldValidationError,
    ScmIntegrationValidationResult,
    ConfigurationValidateResponse,
)
```

Methods:

- <code title="post /gitpod.v1.RunnerConfigurationService/ValidateRunnerConfiguration">client.runners.configurations.<a href="./src/gitpod/resources/runners/configurations/configurations.py">validate</a>(\*\*<a href="src/gitpod/types/runners/configuration_validate_params.py">params</a>) -> <a href="./src/gitpod/types/runners/configuration_validate_response.py">ConfigurationValidateResponse</a></code>

### EnvironmentClasses

Types:

```python
from gitpod.types.runners.configurations import (
    EnvironmentClassCreateResponse,
    EnvironmentClassRetrieveResponse,
    EnvironmentClassUpdateResponse,
)
```

Methods:

- <code title="post /gitpod.v1.RunnerConfigurationService/CreateEnvironmentClass">client.runners.configurations.environment_classes.<a href="./src/gitpod/resources/runners/configurations/environment_classes.py">create</a>(\*\*<a href="src/gitpod/types/runners/configurations/environment_class_create_params.py">params</a>) -> <a href="./src/gitpod/types/runners/configurations/environment_class_create_response.py">EnvironmentClassCreateResponse</a></code>
- <code title="post /gitpod.v1.RunnerConfigurationService/GetEnvironmentClass">client.runners.configurations.environment_classes.<a href="./src/gitpod/resources/runners/configurations/environment_classes.py">retrieve</a>(\*\*<a href="src/gitpod/types/runners/configurations/environment_class_retrieve_params.py">params</a>) -> <a href="./src/gitpod/types/runners/configurations/environment_class_retrieve_response.py">EnvironmentClassRetrieveResponse</a></code>
- <code title="post /gitpod.v1.RunnerConfigurationService/UpdateEnvironmentClass">client.runners.configurations.environment_classes.<a href="./src/gitpod/resources/runners/configurations/environment_classes.py">update</a>(\*\*<a href="src/gitpod/types/runners/configurations/environment_class_update_params.py">params</a>) -> <a href="./src/gitpod/types/runners/configurations/environment_class_update_response.py">object</a></code>
- <code title="post /gitpod.v1.RunnerConfigurationService/ListEnvironmentClasses">client.runners.configurations.environment_classes.<a href="./src/gitpod/resources/runners/configurations/environment_classes.py">list</a>(\*\*<a href="src/gitpod/types/runners/configurations/environment_class_list_params.py">params</a>) -> <a href="./src/gitpod/types/shared/environment_class.py">SyncEnvironmentClassesPage[EnvironmentClass]</a></code>

### HostAuthenticationTokens

Types:

```python
from gitpod.types.runners.configurations import (
    HostAuthenticationToken,
    HostAuthenticationTokenSource,
    HostAuthenticationTokenCreateResponse,
    HostAuthenticationTokenRetrieveResponse,
    HostAuthenticationTokenUpdateResponse,
    HostAuthenticationTokenDeleteResponse,
)
```

Methods:

- <code title="post /gitpod.v1.RunnerConfigurationService/CreateHostAuthenticationToken">client.runners.configurations.host_authentication_tokens.<a href="./src/gitpod/resources/runners/configurations/host_authentication_tokens.py">create</a>(\*\*<a href="src/gitpod/types/runners/configurations/host_authentication_token_create_params.py">params</a>) -> <a href="./src/gitpod/types/runners/configurations/host_authentication_token_create_response.py">HostAuthenticationTokenCreateResponse</a></code>
- <code title="post /gitpod.v1.RunnerConfigurationService/GetHostAuthenticationToken">client.runners.configurations.host_authentication_tokens.<a href="./src/gitpod/resources/runners/configurations/host_authentication_tokens.py">retrieve</a>(\*\*<a href="src/gitpod/types/runners/configurations/host_authentication_token_retrieve_params.py">params</a>) -> <a href="./src/gitpod/types/runners/configurations/host_authentication_token_retrieve_response.py">HostAuthenticationTokenRetrieveResponse</a></code>
- <code title="post /gitpod.v1.RunnerConfigurationService/UpdateHostAuthenticationToken">client.runners.configurations.host_authentication_tokens.<a href="./src/gitpod/resources/runners/configurations/host_authentication_tokens.py">update</a>(\*\*<a href="src/gitpod/types/runners/configurations/host_authentication_token_update_params.py">params</a>) -> <a href="./src/gitpod/types/runners/configurations/host_authentication_token_update_response.py">object</a></code>
- <code title="post /gitpod.v1.RunnerConfigurationService/ListHostAuthenticationTokens">client.runners.configurations.host_authentication_tokens.<a href="./src/gitpod/resources/runners/configurations/host_authentication_tokens.py">list</a>(\*\*<a href="src/gitpod/types/runners/configurations/host_authentication_token_list_params.py">params</a>) -> <a href="./src/gitpod/types/runners/configurations/host_authentication_token.py">SyncTokensPage[HostAuthenticationToken]</a></code>
- <code title="post /gitpod.v1.RunnerConfigurationService/DeleteHostAuthenticationToken">client.runners.configurations.host_authentication_tokens.<a href="./src/gitpod/resources/runners/configurations/host_authentication_tokens.py">delete</a>(\*\*<a href="src/gitpod/types/runners/configurations/host_authentication_token_delete_params.py">params</a>) -> <a href="./src/gitpod/types/runners/configurations/host_authentication_token_delete_response.py">object</a></code>

### Schema

Types:

```python
from gitpod.types.runners.configurations import RunnerConfigurationSchema, SchemaRetrieveResponse
```

Methods:

- <code title="post /gitpod.v1.RunnerConfigurationService/GetRunnerConfigurationSchema">client.runners.configurations.schema.<a href="./src/gitpod/resources/runners/configurations/schema.py">retrieve</a>(\*\*<a href="src/gitpod/types/runners/configurations/schema_retrieve_params.py">params</a>) -> <a href="./src/gitpod/types/runners/configurations/schema_retrieve_response.py">SchemaRetrieveResponse</a></code>

### ScmIntegrations

Types:

```python
from gitpod.types.runners.configurations import (
    ScmIntegration,
    ScmIntegrationOAuthConfig,
    ScmIntegrationCreateResponse,
    ScmIntegrationRetrieveResponse,
    ScmIntegrationUpdateResponse,
    ScmIntegrationDeleteResponse,
)
```

Methods:

- <code title="post /gitpod.v1.RunnerConfigurationService/CreateSCMIntegration">client.runners.configurations.scm_integrations.<a href="./src/gitpod/resources/runners/configurations/scm_integrations.py">create</a>(\*\*<a href="src/gitpod/types/runners/configurations/scm_integration_create_params.py">params</a>) -> <a href="./src/gitpod/types/runners/configurations/scm_integration_create_response.py">ScmIntegrationCreateResponse</a></code>
- <code title="post /gitpod.v1.RunnerConfigurationService/GetSCMIntegration">client.runners.configurations.scm_integrations.<a href="./src/gitpod/resources/runners/configurations/scm_integrations.py">retrieve</a>(\*\*<a href="src/gitpod/types/runners/configurations/scm_integration_retrieve_params.py">params</a>) -> <a href="./src/gitpod/types/runners/configurations/scm_integration_retrieve_response.py">ScmIntegrationRetrieveResponse</a></code>
- <code title="post /gitpod.v1.RunnerConfigurationService/UpdateSCMIntegration">client.runners.configurations.scm_integrations.<a href="./src/gitpod/resources/runners/configurations/scm_integrations.py">update</a>(\*\*<a href="src/gitpod/types/runners/configurations/scm_integration_update_params.py">params</a>) -> <a href="./src/gitpod/types/runners/configurations/scm_integration_update_response.py">object</a></code>
- <code title="post /gitpod.v1.RunnerConfigurationService/ListSCMIntegrations">client.runners.configurations.scm_integrations.<a href="./src/gitpod/resources/runners/configurations/scm_integrations.py">list</a>(\*\*<a href="src/gitpod/types/runners/configurations/scm_integration_list_params.py">params</a>) -> <a href="./src/gitpod/types/runners/configurations/scm_integration.py">SyncIntegrationsPage[ScmIntegration]</a></code>
- <code title="post /gitpod.v1.RunnerConfigurationService/DeleteSCMIntegration">client.runners.configurations.scm_integrations.<a href="./src/gitpod/resources/runners/configurations/scm_integrations.py">delete</a>(\*\*<a href="src/gitpod/types/runners/configurations/scm_integration_delete_params.py">params</a>) -> <a href="./src/gitpod/types/runners/configurations/scm_integration_delete_response.py">object</a></code>

## Policies

Types:

```python
from gitpod.types.runners import (
    RunnerPolicy,
    RunnerRole,
    PolicyCreateResponse,
    PolicyUpdateResponse,
    PolicyDeleteResponse,
)
```

Methods:

- <code title="post /gitpod.v1.RunnerService/CreateRunnerPolicy">client.runners.policies.<a href="./src/gitpod/resources/runners/policies.py">create</a>(\*\*<a href="src/gitpod/types/runners/policy_create_params.py">params</a>) -> <a href="./src/gitpod/types/runners/policy_create_response.py">PolicyCreateResponse</a></code>
- <code title="post /gitpod.v1.RunnerService/UpdateRunnerPolicy">client.runners.policies.<a href="./src/gitpod/resources/runners/policies.py">update</a>(\*\*<a href="src/gitpod/types/runners/policy_update_params.py">params</a>) -> <a href="./src/gitpod/types/runners/policy_update_response.py">PolicyUpdateResponse</a></code>
- <code title="post /gitpod.v1.RunnerService/ListRunnerPolicies">client.runners.policies.<a href="./src/gitpod/resources/runners/policies.py">list</a>(\*\*<a href="src/gitpod/types/runners/policy_list_params.py">params</a>) -> <a href="./src/gitpod/types/runners/runner_policy.py">SyncPoliciesPage[RunnerPolicy]</a></code>
- <code title="post /gitpod.v1.RunnerService/DeleteRunnerPolicy">client.runners.policies.<a href="./src/gitpod/resources/runners/policies.py">delete</a>(\*\*<a href="src/gitpod/types/runners/policy_delete_params.py">params</a>) -> <a href="./src/gitpod/types/runners/policy_delete_response.py">object</a></code>

# Secrets

Types:

```python
from gitpod.types import (
    Secret,
    SecretCreateResponse,
    SecretDeleteResponse,
    SecretGetValueResponse,
    SecretUpdateValueResponse,
)
```

Methods:

- <code title="post /gitpod.v1.SecretService/CreateSecret">client.secrets.<a href="./src/gitpod/resources/secrets.py">create</a>(\*\*<a href="src/gitpod/types/secret_create_params.py">params</a>) -> <a href="./src/gitpod/types/secret_create_response.py">SecretCreateResponse</a></code>
- <code title="post /gitpod.v1.SecretService/ListSecrets">client.secrets.<a href="./src/gitpod/resources/secrets.py">list</a>(\*\*<a href="src/gitpod/types/secret_list_params.py">params</a>) -> <a href="./src/gitpod/types/secret.py">SyncSecretsPage[Secret]</a></code>
- <code title="post /gitpod.v1.SecretService/DeleteSecret">client.secrets.<a href="./src/gitpod/resources/secrets.py">delete</a>(\*\*<a href="src/gitpod/types/secret_delete_params.py">params</a>) -> <a href="./src/gitpod/types/secret_delete_response.py">object</a></code>
- <code title="post /gitpod.v1.SecretService/GetSecretValue">client.secrets.<a href="./src/gitpod/resources/secrets.py">get_value</a>(\*\*<a href="src/gitpod/types/secret_get_value_params.py">params</a>) -> <a href="./src/gitpod/types/secret_get_value_response.py">SecretGetValueResponse</a></code>
- <code title="post /gitpod.v1.SecretService/UpdateSecretValue">client.secrets.<a href="./src/gitpod/resources/secrets.py">update_value</a>(\*\*<a href="src/gitpod/types/secret_update_value_params.py">params</a>) -> <a href="./src/gitpod/types/secret_update_value_response.py">object</a></code>

# Users

Types:

```python
from gitpod.types import User, UserGetAuthenticatedUserResponse, UserSetSuspendedResponse
```

Methods:

- <code title="post /gitpod.v1.UserService/GetAuthenticatedUser">client.users.<a href="./src/gitpod/resources/users/users.py">get_authenticated_user</a>(\*\*<a href="src/gitpod/types/user_get_authenticated_user_params.py">params</a>) -> <a href="./src/gitpod/types/user_get_authenticated_user_response.py">UserGetAuthenticatedUserResponse</a></code>
- <code title="post /gitpod.v1.UserService/SetSuspended">client.users.<a href="./src/gitpod/resources/users/users.py">set_suspended</a>(\*\*<a href="src/gitpod/types/user_set_suspended_params.py">params</a>) -> <a href="./src/gitpod/types/user_set_suspended_response.py">object</a></code>

## Pats

Types:

```python
from gitpod.types.users import PersonalAccessToken, PatDeleteResponse, PatGetResponse
```

Methods:

- <code title="post /gitpod.v1.UserService/ListPersonalAccessTokens">client.users.pats.<a href="./src/gitpod/resources/users/pats.py">list</a>(\*\*<a href="src/gitpod/types/users/pat_list_params.py">params</a>) -> <a href="./src/gitpod/types/users/personal_access_token.py">SyncPersonalAccessTokensPage[PersonalAccessToken]</a></code>
- <code title="post /gitpod.v1.UserService/DeletePersonalAccessToken">client.users.pats.<a href="./src/gitpod/resources/users/pats.py">delete</a>(\*\*<a href="src/gitpod/types/users/pat_delete_params.py">params</a>) -> <a href="./src/gitpod/types/users/pat_delete_response.py">object</a></code>
- <code title="post /gitpod.v1.UserService/GetPersonalAccessToken">client.users.pats.<a href="./src/gitpod/resources/users/pats.py">get</a>(\*\*<a href="src/gitpod/types/users/pat_get_params.py">params</a>) -> <a href="./src/gitpod/types/users/pat_get_response.py">PatGetResponse</a></code>
