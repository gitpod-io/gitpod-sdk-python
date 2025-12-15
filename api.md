# Shared Types

```python
from gitpod.types import (
    AutomationTrigger,
    EnvironmentClass,
    EnvironmentVariableItem,
    EnvironmentVariableSource,
    ErrorCode,
    FieldValue,
    Gateway,
    OrganizationRole,
    Principal,
    ProjectEnvironmentClass,
    ResourceType,
    RunsOn,
    SecretRef,
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
    AccountGetSSOLoginURLResponse,
    AccountListSSOLoginsResponse,
)
```

Methods:

- <code title="post /gitpod.v1.AccountService/GetAccount">client.accounts.<a href="./src/gitpod/resources/accounts.py">retrieve</a>(\*\*<a href="src/gitpod/types/account_retrieve_params.py">params</a>) -> <a href="./src/gitpod/types/account_retrieve_response.py">AccountRetrieveResponse</a></code>
- <code title="post /gitpod.v1.AccountService/DeleteAccount">client.accounts.<a href="./src/gitpod/resources/accounts.py">delete</a>(\*\*<a href="src/gitpod/types/account_delete_params.py">params</a>) -> object</code>
- <code title="post /gitpod.v1.AccountService/GetSSOLoginURL">client.accounts.<a href="./src/gitpod/resources/accounts.py">get_sso_login_url</a>(\*\*<a href="src/gitpod/types/account_get_sso_login_url_params.py">params</a>) -> <a href="./src/gitpod/types/account_get_sso_login_url_response.py">AccountGetSSOLoginURLResponse</a></code>
- <code title="post /gitpod.v1.AccountService/ListJoinableOrganizations">client.accounts.<a href="./src/gitpod/resources/accounts.py">list_joinable_organizations</a>(\*\*<a href="src/gitpod/types/account_list_joinable_organizations_params.py">params</a>) -> <a href="./src/gitpod/types/joinable_organization.py">SyncJoinableOrganizationsPage[JoinableOrganization]</a></code>
- <code title="post /gitpod.v1.AccountService/ListLoginProviders">client.accounts.<a href="./src/gitpod/resources/accounts.py">list_login_providers</a>(\*\*<a href="src/gitpod/types/account_list_login_providers_params.py">params</a>) -> <a href="./src/gitpod/types/login_provider.py">SyncLoginProvidersPage[LoginProvider]</a></code>
- <code title="post /gitpod.v1.AccountService/ListSSOLogins">client.accounts.<a href="./src/gitpod/resources/accounts.py">list_sso_logins</a>(\*\*<a href="src/gitpod/types/account_list_sso_logins_params.py">params</a>) -> <a href="./src/gitpod/types/account_list_sso_logins_response.py">SyncLoginsPage[AccountListSSOLoginsResponse]</a></code>

# Agents

Types:

```python
from gitpod.types import (
    AgentCodeContext,
    AgentExecution,
    AgentMode,
    Prompt,
    PromptMetadata,
    PromptSpec,
    UserInputBlock,
    AgentCreateExecutionConversationTokenResponse,
    AgentCreatePromptResponse,
    AgentRetrieveExecutionResponse,
    AgentRetrievePromptResponse,
    AgentStartExecutionResponse,
    AgentUpdatePromptResponse,
)
```

Methods:

- <code title="post /gitpod.v1.AgentService/CreateAgentExecutionConversationToken">client.agents.<a href="./src/gitpod/resources/agents.py">create_execution_conversation_token</a>(\*\*<a href="src/gitpod/types/agent_create_execution_conversation_token_params.py">params</a>) -> <a href="./src/gitpod/types/agent_create_execution_conversation_token_response.py">AgentCreateExecutionConversationTokenResponse</a></code>
- <code title="post /gitpod.v1.AgentService/CreatePrompt">client.agents.<a href="./src/gitpod/resources/agents.py">create_prompt</a>(\*\*<a href="src/gitpod/types/agent_create_prompt_params.py">params</a>) -> <a href="./src/gitpod/types/agent_create_prompt_response.py">AgentCreatePromptResponse</a></code>
- <code title="post /gitpod.v1.AgentService/DeleteAgentExecution">client.agents.<a href="./src/gitpod/resources/agents.py">delete_execution</a>(\*\*<a href="src/gitpod/types/agent_delete_execution_params.py">params</a>) -> object</code>
- <code title="post /gitpod.v1.AgentService/DeletePrompt">client.agents.<a href="./src/gitpod/resources/agents.py">delete_prompt</a>(\*\*<a href="src/gitpod/types/agent_delete_prompt_params.py">params</a>) -> object</code>
- <code title="post /gitpod.v1.AgentService/ListAgentExecutions">client.agents.<a href="./src/gitpod/resources/agents.py">list_executions</a>(\*\*<a href="src/gitpod/types/agent_list_executions_params.py">params</a>) -> <a href="./src/gitpod/types/agent_execution.py">SyncAgentExecutionsPage[AgentExecution]</a></code>
- <code title="post /gitpod.v1.AgentService/ListPrompts">client.agents.<a href="./src/gitpod/resources/agents.py">list_prompts</a>(\*\*<a href="src/gitpod/types/agent_list_prompts_params.py">params</a>) -> <a href="./src/gitpod/types/prompt.py">SyncPromptsPage[Prompt]</a></code>
- <code title="post /gitpod.v1.AgentService/GetAgentExecution">client.agents.<a href="./src/gitpod/resources/agents.py">retrieve_execution</a>(\*\*<a href="src/gitpod/types/agent_retrieve_execution_params.py">params</a>) -> <a href="./src/gitpod/types/agent_retrieve_execution_response.py">AgentRetrieveExecutionResponse</a></code>
- <code title="post /gitpod.v1.AgentService/GetPrompt">client.agents.<a href="./src/gitpod/resources/agents.py">retrieve_prompt</a>(\*\*<a href="src/gitpod/types/agent_retrieve_prompt_params.py">params</a>) -> <a href="./src/gitpod/types/agent_retrieve_prompt_response.py">AgentRetrievePromptResponse</a></code>
- <code title="post /gitpod.v1.AgentService/SendToAgentExecution">client.agents.<a href="./src/gitpod/resources/agents.py">send_to_execution</a>(\*\*<a href="src/gitpod/types/agent_send_to_execution_params.py">params</a>) -> object</code>
- <code title="post /gitpod.v1.AgentService/StartAgent">client.agents.<a href="./src/gitpod/resources/agents.py">start_execution</a>(\*\*<a href="src/gitpod/types/agent_start_execution_params.py">params</a>) -> <a href="./src/gitpod/types/agent_start_execution_response.py">AgentStartExecutionResponse</a></code>
- <code title="post /gitpod.v1.AgentService/StopAgentExecution">client.agents.<a href="./src/gitpod/resources/agents.py">stop_execution</a>(\*\*<a href="src/gitpod/types/agent_stop_execution_params.py">params</a>) -> object</code>
- <code title="post /gitpod.v1.AgentService/UpdatePrompt">client.agents.<a href="./src/gitpod/resources/agents.py">update_prompt</a>(\*\*<a href="src/gitpod/types/agent_update_prompt_params.py">params</a>) -> <a href="./src/gitpod/types/agent_update_prompt_response.py">AgentUpdatePromptResponse</a></code>

# Editors

Types:

```python
from gitpod.types import Editor, EditorVersion, EditorRetrieveResponse, EditorResolveURLResponse
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
    EnvironmentRole,
    EnvironmentSpec,
    EnvironmentStatus,
    EnvironmentCreateResponse,
    EnvironmentRetrieveResponse,
    EnvironmentCreateEnvironmentTokenResponse,
    EnvironmentCreateFromProjectResponse,
    EnvironmentCreateLogsTokenResponse,
)
```

Methods:

- <code title="post /gitpod.v1.EnvironmentService/CreateEnvironment">client.environments.<a href="./src/gitpod/resources/environments/environments.py">create</a>(\*\*<a href="src/gitpod/types/environment_create_params.py">params</a>) -> <a href="./src/gitpod/types/environment_create_response.py">EnvironmentCreateResponse</a></code>
- <code title="post /gitpod.v1.EnvironmentService/GetEnvironment">client.environments.<a href="./src/gitpod/resources/environments/environments.py">retrieve</a>(\*\*<a href="src/gitpod/types/environment_retrieve_params.py">params</a>) -> <a href="./src/gitpod/types/environment_retrieve_response.py">EnvironmentRetrieveResponse</a></code>
- <code title="post /gitpod.v1.EnvironmentService/UpdateEnvironment">client.environments.<a href="./src/gitpod/resources/environments/environments.py">update</a>(\*\*<a href="src/gitpod/types/environment_update_params.py">params</a>) -> object</code>
- <code title="post /gitpod.v1.EnvironmentService/ListEnvironments">client.environments.<a href="./src/gitpod/resources/environments/environments.py">list</a>(\*\*<a href="src/gitpod/types/environment_list_params.py">params</a>) -> <a href="./src/gitpod/types/environment.py">SyncEnvironmentsPage[Environment]</a></code>
- <code title="post /gitpod.v1.EnvironmentService/DeleteEnvironment">client.environments.<a href="./src/gitpod/resources/environments/environments.py">delete</a>(\*\*<a href="src/gitpod/types/environment_delete_params.py">params</a>) -> object</code>
- <code title="post /gitpod.v1.EnvironmentService/CreateEnvironmentAccessToken">client.environments.<a href="./src/gitpod/resources/environments/environments.py">create_environment_token</a>(\*\*<a href="src/gitpod/types/environment_create_environment_token_params.py">params</a>) -> <a href="./src/gitpod/types/environment_create_environment_token_response.py">EnvironmentCreateEnvironmentTokenResponse</a></code>
- <code title="post /gitpod.v1.EnvironmentService/CreateEnvironmentFromProject">client.environments.<a href="./src/gitpod/resources/environments/environments.py">create_from_project</a>(\*\*<a href="src/gitpod/types/environment_create_from_project_params.py">params</a>) -> <a href="./src/gitpod/types/environment_create_from_project_response.py">EnvironmentCreateFromProjectResponse</a></code>
- <code title="post /gitpod.v1.EnvironmentService/CreateEnvironmentLogsToken">client.environments.<a href="./src/gitpod/resources/environments/environments.py">create_logs_token</a>(\*\*<a href="src/gitpod/types/environment_create_logs_token_params.py">params</a>) -> <a href="./src/gitpod/types/environment_create_logs_token_response.py">EnvironmentCreateLogsTokenResponse</a></code>
- <code title="post /gitpod.v1.EnvironmentService/MarkEnvironmentActive">client.environments.<a href="./src/gitpod/resources/environments/environments.py">mark_active</a>(\*\*<a href="src/gitpod/types/environment_mark_active_params.py">params</a>) -> object</code>
- <code title="post /gitpod.v1.EnvironmentService/StartEnvironment">client.environments.<a href="./src/gitpod/resources/environments/environments.py">start</a>(\*\*<a href="src/gitpod/types/environment_start_params.py">params</a>) -> object</code>
- <code title="post /gitpod.v1.EnvironmentService/StopEnvironment">client.environments.<a href="./src/gitpod/resources/environments/environments.py">stop</a>(\*\*<a href="src/gitpod/types/environment_stop_params.py">params</a>) -> object</code>
- <code title="post /gitpod.v1.EnvironmentService/UnarchiveEnvironment">client.environments.<a href="./src/gitpod/resources/environments/environments.py">unarchive</a>(\*\*<a href="src/gitpod/types/environment_unarchive_params.py">params</a>) -> object</code>

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
    ServiceRole,
    ServiceSpec,
    ServiceStatus,
    ServiceCreateResponse,
    ServiceRetrieveResponse,
)
```

Methods:

- <code title="post /gitpod.v1.EnvironmentAutomationService/CreateService">client.environments.automations.services.<a href="./src/gitpod/resources/environments/automations/services.py">create</a>(\*\*<a href="src/gitpod/types/environments/automations/service_create_params.py">params</a>) -> <a href="./src/gitpod/types/environments/automations/service_create_response.py">ServiceCreateResponse</a></code>
- <code title="post /gitpod.v1.EnvironmentAutomationService/GetService">client.environments.automations.services.<a href="./src/gitpod/resources/environments/automations/services.py">retrieve</a>(\*\*<a href="src/gitpod/types/environments/automations/service_retrieve_params.py">params</a>) -> <a href="./src/gitpod/types/environments/automations/service_retrieve_response.py">ServiceRetrieveResponse</a></code>
- <code title="post /gitpod.v1.EnvironmentAutomationService/UpdateService">client.environments.automations.services.<a href="./src/gitpod/resources/environments/automations/services.py">update</a>(\*\*<a href="src/gitpod/types/environments/automations/service_update_params.py">params</a>) -> object</code>
- <code title="post /gitpod.v1.EnvironmentAutomationService/ListServices">client.environments.automations.services.<a href="./src/gitpod/resources/environments/automations/services.py">list</a>(\*\*<a href="src/gitpod/types/environments/automations/service_list_params.py">params</a>) -> <a href="./src/gitpod/types/environments/automations/service.py">SyncServicesPage[Service]</a></code>
- <code title="post /gitpod.v1.EnvironmentAutomationService/DeleteService">client.environments.automations.services.<a href="./src/gitpod/resources/environments/automations/services.py">delete</a>(\*\*<a href="src/gitpod/types/environments/automations/service_delete_params.py">params</a>) -> object</code>
- <code title="post /gitpod.v1.EnvironmentAutomationService/StartService">client.environments.automations.services.<a href="./src/gitpod/resources/environments/automations/services.py">start</a>(\*\*<a href="src/gitpod/types/environments/automations/service_start_params.py">params</a>) -> object</code>
- <code title="post /gitpod.v1.EnvironmentAutomationService/StopService">client.environments.automations.services.<a href="./src/gitpod/resources/environments/automations/services.py">stop</a>(\*\*<a href="src/gitpod/types/environments/automations/service_stop_params.py">params</a>) -> object</code>

### Tasks

Types:

```python
from gitpod.types.environments.automations import (
    TaskCreateResponse,
    TaskRetrieveResponse,
    TaskStartResponse,
)
```

Methods:

- <code title="post /gitpod.v1.EnvironmentAutomationService/CreateTask">client.environments.automations.tasks.<a href="./src/gitpod/resources/environments/automations/tasks/tasks.py">create</a>(\*\*<a href="src/gitpod/types/environments/automations/task_create_params.py">params</a>) -> <a href="./src/gitpod/types/environments/automations/task_create_response.py">TaskCreateResponse</a></code>
- <code title="post /gitpod.v1.EnvironmentAutomationService/GetTask">client.environments.automations.tasks.<a href="./src/gitpod/resources/environments/automations/tasks/tasks.py">retrieve</a>(\*\*<a href="src/gitpod/types/environments/automations/task_retrieve_params.py">params</a>) -> <a href="./src/gitpod/types/environments/automations/task_retrieve_response.py">TaskRetrieveResponse</a></code>
- <code title="post /gitpod.v1.EnvironmentAutomationService/UpdateTask">client.environments.automations.tasks.<a href="./src/gitpod/resources/environments/automations/tasks/tasks.py">update</a>(\*\*<a href="src/gitpod/types/environments/automations/task_update_params.py">params</a>) -> object</code>
- <code title="post /gitpod.v1.EnvironmentAutomationService/ListTasks">client.environments.automations.tasks.<a href="./src/gitpod/resources/environments/automations/tasks/tasks.py">list</a>(\*\*<a href="src/gitpod/types/environments/automations/task_list_params.py">params</a>) -> <a href="./src/gitpod/types/shared/task.py">SyncTasksPage[Task]</a></code>
- <code title="post /gitpod.v1.EnvironmentAutomationService/DeleteTask">client.environments.automations.tasks.<a href="./src/gitpod/resources/environments/automations/tasks/tasks.py">delete</a>(\*\*<a href="src/gitpod/types/environments/automations/task_delete_params.py">params</a>) -> object</code>
- <code title="post /gitpod.v1.EnvironmentAutomationService/StartTask">client.environments.automations.tasks.<a href="./src/gitpod/resources/environments/automations/tasks/tasks.py">start</a>(\*\*<a href="src/gitpod/types/environments/automations/task_start_params.py">params</a>) -> <a href="./src/gitpod/types/environments/automations/task_start_response.py">TaskStartResponse</a></code>

#### Executions

Types:

```python
from gitpod.types.environments.automations.tasks import ExecutionRetrieveResponse
```

Methods:

- <code title="post /gitpod.v1.EnvironmentAutomationService/GetTaskExecution">client.environments.automations.tasks.executions.<a href="./src/gitpod/resources/environments/automations/tasks/executions.py">retrieve</a>(\*\*<a href="src/gitpod/types/environments/automations/tasks/execution_retrieve_params.py">params</a>) -> <a href="./src/gitpod/types/environments/automations/tasks/execution_retrieve_response.py">ExecutionRetrieveResponse</a></code>
- <code title="post /gitpod.v1.EnvironmentAutomationService/ListTaskExecutions">client.environments.automations.tasks.executions.<a href="./src/gitpod/resources/environments/automations/tasks/executions.py">list</a>(\*\*<a href="src/gitpod/types/environments/automations/tasks/execution_list_params.py">params</a>) -> <a href="./src/gitpod/types/shared/task_execution.py">SyncTaskExecutionsPage[TaskExecution]</a></code>
- <code title="post /gitpod.v1.EnvironmentAutomationService/StopTaskExecution">client.environments.automations.tasks.executions.<a href="./src/gitpod/resources/environments/automations/tasks/executions.py">stop</a>(\*\*<a href="src/gitpod/types/environments/automations/tasks/execution_stop_params.py">params</a>) -> object</code>

## Classes

Methods:

- <code title="post /gitpod.v1.EnvironmentService/ListEnvironmentClasses">client.environments.classes.<a href="./src/gitpod/resources/environments/classes.py">list</a>(\*\*<a href="src/gitpod/types/environments/class_list_params.py">params</a>) -> <a href="./src/gitpod/types/shared/environment_class.py">SyncEnvironmentClassesPage[EnvironmentClass]</a></code>

# Errors

Types:

```python
from gitpod.types import (
    Breadcrumb,
    ErrorEvent,
    ErrorLevel,
    ExceptionInfo,
    ExceptionMechanism,
    RequestInfo,
    StackFrame,
)
```

Methods:

- <code title="post /gitpod.v1.ErrorsService/ReportErrors">client.errors.<a href="./src/gitpod/resources/errors.py">report_errors</a>(\*\*<a href="src/gitpod/types/error_report_errors_params.py">params</a>) -> object</code>

# Events

Types:

```python
from gitpod.types import ResourceOperation, EventListResponse, EventWatchResponse
```

Methods:

- <code title="post /gitpod.v1.EventService/ListAuditLogs">client.events.<a href="./src/gitpod/resources/events.py">list</a>(\*\*<a href="src/gitpod/types/event_list_params.py">params</a>) -> <a href="./src/gitpod/types/event_list_response.py">SyncEntriesPage[EventListResponse]</a></code>
- <code title="post /gitpod.v1.EventService/WatchEvents">client.events.<a href="./src/gitpod/resources/events.py">watch</a>(\*\*<a href="src/gitpod/types/event_watch_params.py">params</a>) -> <a href="./src/gitpod/types/event_watch_response.py">JSONLDecoder[EventWatchResponse]</a></code>

# Gateways

Methods:

- <code title="post /gitpod.v1.GatewayService/ListGateways">client.gateways.<a href="./src/gitpod/resources/gateways.py">list</a>(\*\*<a href="src/gitpod/types/gateway_list_params.py">params</a>) -> <a href="./src/gitpod/types/shared/gateway.py">SyncGatewaysPage[Gateway]</a></code>

# Groups

Types:

```python
from gitpod.types import Group, GroupCreateResponse, GroupRetrieveResponse, GroupUpdateResponse
```

Methods:

- <code title="post /gitpod.v1.GroupService/CreateGroup">client.groups.<a href="./src/gitpod/resources/groups/groups.py">create</a>(\*\*<a href="src/gitpod/types/group_create_params.py">params</a>) -> <a href="./src/gitpod/types/group_create_response.py">GroupCreateResponse</a></code>
- <code title="post /gitpod.v1.GroupService/GetGroup">client.groups.<a href="./src/gitpod/resources/groups/groups.py">retrieve</a>(\*\*<a href="src/gitpod/types/group_retrieve_params.py">params</a>) -> <a href="./src/gitpod/types/group_retrieve_response.py">GroupRetrieveResponse</a></code>
- <code title="post /gitpod.v1.GroupService/UpdateGroup">client.groups.<a href="./src/gitpod/resources/groups/groups.py">update</a>(\*\*<a href="src/gitpod/types/group_update_params.py">params</a>) -> <a href="./src/gitpod/types/group_update_response.py">GroupUpdateResponse</a></code>
- <code title="post /gitpod.v1.GroupService/ListGroups">client.groups.<a href="./src/gitpod/resources/groups/groups.py">list</a>(\*\*<a href="src/gitpod/types/group_list_params.py">params</a>) -> <a href="./src/gitpod/types/group.py">SyncGroupsPage[Group]</a></code>
- <code title="post /gitpod.v1.GroupService/DeleteGroup">client.groups.<a href="./src/gitpod/resources/groups/groups.py">delete</a>(\*\*<a href="src/gitpod/types/group_delete_params.py">params</a>) -> object</code>

## Memberships

Types:

```python
from gitpod.types.groups import GroupMembership, MembershipCreateResponse
```

Methods:

- <code title="post /gitpod.v1.GroupService/CreateMembership">client.groups.memberships.<a href="./src/gitpod/resources/groups/memberships.py">create</a>(\*\*<a href="src/gitpod/types/groups/membership_create_params.py">params</a>) -> <a href="./src/gitpod/types/groups/membership_create_response.py">MembershipCreateResponse</a></code>
- <code title="post /gitpod.v1.GroupService/ListMemberships">client.groups.memberships.<a href="./src/gitpod/resources/groups/memberships.py">list</a>(\*\*<a href="src/gitpod/types/groups/membership_list_params.py">params</a>) -> <a href="./src/gitpod/types/groups/group_membership.py">SyncMembersPage[GroupMembership]</a></code>
- <code title="post /gitpod.v1.GroupService/DeleteMembership">client.groups.memberships.<a href="./src/gitpod/resources/groups/memberships.py">delete</a>(\*\*<a href="src/gitpod/types/groups/membership_delete_params.py">params</a>) -> object</code>

## RoleAssignments

Types:

```python
from gitpod.types.groups import ResourceRole, RoleAssignment, RoleAssignmentCreateResponse
```

Methods:

- <code title="post /gitpod.v1.GroupService/CreateRoleAssignment">client.groups.role_assignments.<a href="./src/gitpod/resources/groups/role_assignments.py">create</a>(\*\*<a href="src/gitpod/types/groups/role_assignment_create_params.py">params</a>) -> <a href="./src/gitpod/types/groups/role_assignment_create_response.py">RoleAssignmentCreateResponse</a></code>
- <code title="post /gitpod.v1.GroupService/ListRoleAssignments">client.groups.role_assignments.<a href="./src/gitpod/resources/groups/role_assignments.py">list</a>(\*\*<a href="src/gitpod/types/groups/role_assignment_list_params.py">params</a>) -> <a href="./src/gitpod/types/groups/role_assignment.py">SyncAssignmentsPage[RoleAssignment]</a></code>
- <code title="post /gitpod.v1.GroupService/DeleteRoleAssignment">client.groups.role_assignments.<a href="./src/gitpod/resources/groups/role_assignments.py">delete</a>(\*\*<a href="src/gitpod/types/groups/role_assignment_delete_params.py">params</a>) -> object</code>

# Identity

Types:

```python
from gitpod.types import (
    IDTokenVersion,
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
    OrganizationTier,
    OrganizationCreateResponse,
    OrganizationRetrieveResponse,
    OrganizationUpdateResponse,
    OrganizationJoinResponse,
)
```

Methods:

- <code title="post /gitpod.v1.OrganizationService/CreateOrganization">client.organizations.<a href="./src/gitpod/resources/organizations/organizations.py">create</a>(\*\*<a href="src/gitpod/types/organization_create_params.py">params</a>) -> <a href="./src/gitpod/types/organization_create_response.py">OrganizationCreateResponse</a></code>
- <code title="post /gitpod.v1.OrganizationService/GetOrganization">client.organizations.<a href="./src/gitpod/resources/organizations/organizations.py">retrieve</a>(\*\*<a href="src/gitpod/types/organization_retrieve_params.py">params</a>) -> <a href="./src/gitpod/types/organization_retrieve_response.py">OrganizationRetrieveResponse</a></code>
- <code title="post /gitpod.v1.OrganizationService/UpdateOrganization">client.organizations.<a href="./src/gitpod/resources/organizations/organizations.py">update</a>(\*\*<a href="src/gitpod/types/organization_update_params.py">params</a>) -> <a href="./src/gitpod/types/organization_update_response.py">OrganizationUpdateResponse</a></code>
- <code title="post /gitpod.v1.OrganizationService/DeleteOrganization">client.organizations.<a href="./src/gitpod/resources/organizations/organizations.py">delete</a>(\*\*<a href="src/gitpod/types/organization_delete_params.py">params</a>) -> object</code>
- <code title="post /gitpod.v1.OrganizationService/JoinOrganization">client.organizations.<a href="./src/gitpod/resources/organizations/organizations.py">join</a>(\*\*<a href="src/gitpod/types/organization_join_params.py">params</a>) -> <a href="./src/gitpod/types/organization_join_response.py">OrganizationJoinResponse</a></code>
- <code title="post /gitpod.v1.OrganizationService/LeaveOrganization">client.organizations.<a href="./src/gitpod/resources/organizations/organizations.py">leave</a>(\*\*<a href="src/gitpod/types/organization_leave_params.py">params</a>) -> object</code>
- <code title="post /gitpod.v1.OrganizationService/ListMembers">client.organizations.<a href="./src/gitpod/resources/organizations/organizations.py">list_members</a>(\*\*<a href="src/gitpod/types/organization_list_members_params.py">params</a>) -> <a href="./src/gitpod/types/organization_member.py">SyncMembersPage[OrganizationMember]</a></code>
- <code title="post /gitpod.v1.OrganizationService/SetRole">client.organizations.<a href="./src/gitpod/resources/organizations/organizations.py">set_role</a>(\*\*<a href="src/gitpod/types/organization_set_role_params.py">params</a>) -> object</code>

## CustomDomains

Types:

```python
from gitpod.types.organizations import (
    CustomDomain,
    CustomDomainProvider,
    CustomDomainCreateResponse,
    CustomDomainRetrieveResponse,
    CustomDomainUpdateResponse,
)
```

Methods:

- <code title="post /gitpod.v1.OrganizationService/CreateCustomDomain">client.organizations.custom_domains.<a href="./src/gitpod/resources/organizations/custom_domains.py">create</a>(\*\*<a href="src/gitpod/types/organizations/custom_domain_create_params.py">params</a>) -> <a href="./src/gitpod/types/organizations/custom_domain_create_response.py">CustomDomainCreateResponse</a></code>
- <code title="post /gitpod.v1.OrganizationService/GetCustomDomain">client.organizations.custom_domains.<a href="./src/gitpod/resources/organizations/custom_domains.py">retrieve</a>(\*\*<a href="src/gitpod/types/organizations/custom_domain_retrieve_params.py">params</a>) -> <a href="./src/gitpod/types/organizations/custom_domain_retrieve_response.py">CustomDomainRetrieveResponse</a></code>
- <code title="post /gitpod.v1.OrganizationService/UpdateCustomDomain">client.organizations.custom_domains.<a href="./src/gitpod/resources/organizations/custom_domains.py">update</a>(\*\*<a href="src/gitpod/types/organizations/custom_domain_update_params.py">params</a>) -> <a href="./src/gitpod/types/organizations/custom_domain_update_response.py">CustomDomainUpdateResponse</a></code>
- <code title="post /gitpod.v1.OrganizationService/DeleteCustomDomain">client.organizations.custom_domains.<a href="./src/gitpod/resources/organizations/custom_domains.py">delete</a>(\*\*<a href="src/gitpod/types/organizations/custom_domain_delete_params.py">params</a>) -> object</code>

## DomainVerifications

Types:

```python
from gitpod.types.organizations import (
    DomainVerification,
    DomainVerificationState,
    DomainVerificationCreateResponse,
    DomainVerificationRetrieveResponse,
    DomainVerificationVerifyResponse,
)
```

Methods:

- <code title="post /gitpod.v1.OrganizationService/CreateDomainVerification">client.organizations.domain_verifications.<a href="./src/gitpod/resources/organizations/domain_verifications.py">create</a>(\*\*<a href="src/gitpod/types/organizations/domain_verification_create_params.py">params</a>) -> <a href="./src/gitpod/types/organizations/domain_verification_create_response.py">DomainVerificationCreateResponse</a></code>
- <code title="post /gitpod.v1.OrganizationService/GetDomainVerification">client.organizations.domain_verifications.<a href="./src/gitpod/resources/organizations/domain_verifications.py">retrieve</a>(\*\*<a href="src/gitpod/types/organizations/domain_verification_retrieve_params.py">params</a>) -> <a href="./src/gitpod/types/organizations/domain_verification_retrieve_response.py">DomainVerificationRetrieveResponse</a></code>
- <code title="post /gitpod.v1.OrganizationService/ListDomainVerifications">client.organizations.domain_verifications.<a href="./src/gitpod/resources/organizations/domain_verifications.py">list</a>(\*\*<a href="src/gitpod/types/organizations/domain_verification_list_params.py">params</a>) -> <a href="./src/gitpod/types/organizations/domain_verification.py">SyncDomainVerificationsPage[DomainVerification]</a></code>
- <code title="post /gitpod.v1.OrganizationService/DeleteDomainVerification">client.organizations.domain_verifications.<a href="./src/gitpod/resources/organizations/domain_verifications.py">delete</a>(\*\*<a href="src/gitpod/types/organizations/domain_verification_delete_params.py">params</a>) -> object</code>
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

## Policies

Types:

```python
from gitpod.types.organizations import (
    AgentPolicy,
    CrowdStrikeConfig,
    OrganizationPolicies,
    SecurityAgentPolicy,
    PolicyRetrieveResponse,
)
```

Methods:

- <code title="post /gitpod.v1.OrganizationService/GetOrganizationPolicies">client.organizations.policies.<a href="./src/gitpod/resources/organizations/policies.py">retrieve</a>(\*\*<a href="src/gitpod/types/organizations/policy_retrieve_params.py">params</a>) -> <a href="./src/gitpod/types/organizations/policy_retrieve_response.py">PolicyRetrieveResponse</a></code>
- <code title="post /gitpod.v1.OrganizationService/UpdateOrganizationPolicies">client.organizations.policies.<a href="./src/gitpod/resources/organizations/policies.py">update</a>(\*\*<a href="src/gitpod/types/organizations/policy_update_params.py">params</a>) -> object</code>

## SSOConfigurations

Types:

```python
from gitpod.types.organizations import (
    ProviderType,
    SSOConfiguration,
    SSOConfigurationState,
    SSOConfigurationCreateResponse,
    SSOConfigurationRetrieveResponse,
)
```

Methods:

- <code title="post /gitpod.v1.OrganizationService/CreateSSOConfiguration">client.organizations.sso_configurations.<a href="./src/gitpod/resources/organizations/sso_configurations.py">create</a>(\*\*<a href="src/gitpod/types/organizations/sso_configuration_create_params.py">params</a>) -> <a href="./src/gitpod/types/organizations/sso_configuration_create_response.py">SSOConfigurationCreateResponse</a></code>
- <code title="post /gitpod.v1.OrganizationService/GetSSOConfiguration">client.organizations.sso_configurations.<a href="./src/gitpod/resources/organizations/sso_configurations.py">retrieve</a>(\*\*<a href="src/gitpod/types/organizations/sso_configuration_retrieve_params.py">params</a>) -> <a href="./src/gitpod/types/organizations/sso_configuration_retrieve_response.py">SSOConfigurationRetrieveResponse</a></code>
- <code title="post /gitpod.v1.OrganizationService/UpdateSSOConfiguration">client.organizations.sso_configurations.<a href="./src/gitpod/resources/organizations/sso_configurations.py">update</a>(\*\*<a href="src/gitpod/types/organizations/sso_configuration_update_params.py">params</a>) -> object</code>
- <code title="post /gitpod.v1.OrganizationService/ListSSOConfigurations">client.organizations.sso_configurations.<a href="./src/gitpod/resources/organizations/sso_configurations.py">list</a>(\*\*<a href="src/gitpod/types/organizations/sso_configuration_list_params.py">params</a>) -> <a href="./src/gitpod/types/organizations/sso_configuration.py">SyncSSOConfigurationsPage[SSOConfiguration]</a></code>
- <code title="post /gitpod.v1.OrganizationService/DeleteSSOConfiguration">client.organizations.sso_configurations.<a href="./src/gitpod/resources/organizations/sso_configurations.py">delete</a>(\*\*<a href="src/gitpod/types/organizations/sso_configuration_delete_params.py">params</a>) -> object</code>

# Prebuilds

Types:

```python
from gitpod.types import (
    Prebuild,
    PrebuildMetadata,
    PrebuildPhase,
    PrebuildSpec,
    PrebuildStatus,
    PrebuildTrigger,
    PrebuildCreateResponse,
    PrebuildRetrieveResponse,
    PrebuildCancelResponse,
    PrebuildCreateLogsTokenResponse,
)
```

Methods:

- <code title="post /gitpod.v1.PrebuildService/CreatePrebuild">client.prebuilds.<a href="./src/gitpod/resources/prebuilds.py">create</a>(\*\*<a href="src/gitpod/types/prebuild_create_params.py">params</a>) -> <a href="./src/gitpod/types/prebuild_create_response.py">PrebuildCreateResponse</a></code>
- <code title="post /gitpod.v1.PrebuildService/GetPrebuild">client.prebuilds.<a href="./src/gitpod/resources/prebuilds.py">retrieve</a>(\*\*<a href="src/gitpod/types/prebuild_retrieve_params.py">params</a>) -> <a href="./src/gitpod/types/prebuild_retrieve_response.py">PrebuildRetrieveResponse</a></code>
- <code title="post /gitpod.v1.PrebuildService/ListPrebuilds">client.prebuilds.<a href="./src/gitpod/resources/prebuilds.py">list</a>(\*\*<a href="src/gitpod/types/prebuild_list_params.py">params</a>) -> <a href="./src/gitpod/types/prebuild.py">SyncPrebuildsPage[Prebuild]</a></code>
- <code title="post /gitpod.v1.PrebuildService/DeletePrebuild">client.prebuilds.<a href="./src/gitpod/resources/prebuilds.py">delete</a>(\*\*<a href="src/gitpod/types/prebuild_delete_params.py">params</a>) -> object</code>
- <code title="post /gitpod.v1.PrebuildService/CancelPrebuild">client.prebuilds.<a href="./src/gitpod/resources/prebuilds.py">cancel</a>(\*\*<a href="src/gitpod/types/prebuild_cancel_params.py">params</a>) -> <a href="./src/gitpod/types/prebuild_cancel_response.py">PrebuildCancelResponse</a></code>
- <code title="post /gitpod.v1.PrebuildService/CreatePrebuildLogsToken">client.prebuilds.<a href="./src/gitpod/resources/prebuilds.py">create_logs_token</a>(\*\*<a href="src/gitpod/types/prebuild_create_logs_token_params.py">params</a>) -> <a href="./src/gitpod/types/prebuild_create_logs_token_response.py">PrebuildCreateLogsTokenResponse</a></code>

# Projects

Types:

```python
from gitpod.types import (
    EnvironmentInitializer,
    Project,
    ProjectMetadata,
    ProjectPhase,
    ProjectPrebuildConfiguration,
    ProjectCreateResponse,
    ProjectRetrieveResponse,
    ProjectUpdateResponse,
    ProjectCreateFromEnvironmentResponse,
)
```

Methods:

- <code title="post /gitpod.v1.ProjectService/CreateProject">client.projects.<a href="./src/gitpod/resources/projects/projects.py">create</a>(\*\*<a href="src/gitpod/types/project_create_params.py">params</a>) -> <a href="./src/gitpod/types/project_create_response.py">ProjectCreateResponse</a></code>
- <code title="post /gitpod.v1.ProjectService/GetProject">client.projects.<a href="./src/gitpod/resources/projects/projects.py">retrieve</a>(\*\*<a href="src/gitpod/types/project_retrieve_params.py">params</a>) -> <a href="./src/gitpod/types/project_retrieve_response.py">ProjectRetrieveResponse</a></code>
- <code title="post /gitpod.v1.ProjectService/UpdateProject">client.projects.<a href="./src/gitpod/resources/projects/projects.py">update</a>(\*\*<a href="src/gitpod/types/project_update_params.py">params</a>) -> <a href="./src/gitpod/types/project_update_response.py">ProjectUpdateResponse</a></code>
- <code title="post /gitpod.v1.ProjectService/ListProjects">client.projects.<a href="./src/gitpod/resources/projects/projects.py">list</a>(\*\*<a href="src/gitpod/types/project_list_params.py">params</a>) -> <a href="./src/gitpod/types/project.py">SyncProjectsPage[Project]</a></code>
- <code title="post /gitpod.v1.ProjectService/DeleteProject">client.projects.<a href="./src/gitpod/resources/projects/projects.py">delete</a>(\*\*<a href="src/gitpod/types/project_delete_params.py">params</a>) -> object</code>
- <code title="post /gitpod.v1.ProjectService/CreateProjectFromEnvironment">client.projects.<a href="./src/gitpod/resources/projects/projects.py">create_from_environment</a>(\*\*<a href="src/gitpod/types/project_create_from_environment_params.py">params</a>) -> <a href="./src/gitpod/types/project_create_from_environment_response.py">ProjectCreateFromEnvironmentResponse</a></code>

## EnvironmentClases

Methods:

- <code title="post /gitpod.v1.ProjectService/UpdateProjectEnvironmentClasses">client.projects.environment_clases.<a href="./src/gitpod/resources/projects/environment_clases.py">update</a>(\*\*<a href="src/gitpod/types/projects/environment_clase_update_params.py">params</a>) -> object</code>
- <code title="post /gitpod.v1.ProjectService/ListProjectEnvironmentClasses">client.projects.environment_clases.<a href="./src/gitpod/resources/projects/environment_clases.py">list</a>(\*\*<a href="src/gitpod/types/projects/environment_clase_list_params.py">params</a>) -> <a href="./src/gitpod/types/shared/project_environment_class.py">SyncProjectEnvironmentClassesPage[ProjectEnvironmentClass]</a></code>

## Policies

Types:

```python
from gitpod.types.projects import (
    ProjectPolicy,
    ProjectRole,
    PolicyCreateResponse,
    PolicyUpdateResponse,
)
```

Methods:

- <code title="post /gitpod.v1.ProjectService/CreateProjectPolicy">client.projects.policies.<a href="./src/gitpod/resources/projects/policies.py">create</a>(\*\*<a href="src/gitpod/types/projects/policy_create_params.py">params</a>) -> <a href="./src/gitpod/types/projects/policy_create_response.py">PolicyCreateResponse</a></code>
- <code title="post /gitpod.v1.ProjectService/UpdateProjectPolicy">client.projects.policies.<a href="./src/gitpod/resources/projects/policies.py">update</a>(\*\*<a href="src/gitpod/types/projects/policy_update_params.py">params</a>) -> <a href="./src/gitpod/types/projects/policy_update_response.py">PolicyUpdateResponse</a></code>
- <code title="post /gitpod.v1.ProjectService/ListProjectPolicies">client.projects.policies.<a href="./src/gitpod/resources/projects/policies.py">list</a>(\*\*<a href="src/gitpod/types/projects/policy_list_params.py">params</a>) -> <a href="./src/gitpod/types/projects/project_policy.py">SyncPoliciesPage[ProjectPolicy]</a></code>
- <code title="post /gitpod.v1.ProjectService/DeleteProjectPolicy">client.projects.policies.<a href="./src/gitpod/resources/projects/policies.py">delete</a>(\*\*<a href="src/gitpod/types/projects/policy_delete_params.py">params</a>) -> object</code>

# Runners

Types:

```python
from gitpod.types import (
    GatewayInfo,
    LogLevel,
    MetricsConfiguration,
    Runner,
    RunnerCapability,
    RunnerConfiguration,
    RunnerKind,
    RunnerPhase,
    RunnerProvider,
    RunnerReleaseChannel,
    RunnerSpec,
    RunnerStatus,
    RunnerVariant,
    SearchMode,
    RunnerCreateResponse,
    RunnerRetrieveResponse,
    RunnerCheckAuthenticationForHostResponse,
    RunnerCreateLogsTokenResponse,
    RunnerCreateRunnerTokenResponse,
    RunnerParseContextURLResponse,
    RunnerSearchRepositoriesResponse,
)
```

Methods:

- <code title="post /gitpod.v1.RunnerService/CreateRunner">client.runners.<a href="./src/gitpod/resources/runners/runners.py">create</a>(\*\*<a href="src/gitpod/types/runner_create_params.py">params</a>) -> <a href="./src/gitpod/types/runner_create_response.py">RunnerCreateResponse</a></code>
- <code title="post /gitpod.v1.RunnerService/GetRunner">client.runners.<a href="./src/gitpod/resources/runners/runners.py">retrieve</a>(\*\*<a href="src/gitpod/types/runner_retrieve_params.py">params</a>) -> <a href="./src/gitpod/types/runner_retrieve_response.py">RunnerRetrieveResponse</a></code>
- <code title="post /gitpod.v1.RunnerService/UpdateRunner">client.runners.<a href="./src/gitpod/resources/runners/runners.py">update</a>(\*\*<a href="src/gitpod/types/runner_update_params.py">params</a>) -> object</code>
- <code title="post /gitpod.v1.RunnerService/ListRunners">client.runners.<a href="./src/gitpod/resources/runners/runners.py">list</a>(\*\*<a href="src/gitpod/types/runner_list_params.py">params</a>) -> <a href="./src/gitpod/types/runner.py">SyncRunnersPage[Runner]</a></code>
- <code title="post /gitpod.v1.RunnerService/DeleteRunner">client.runners.<a href="./src/gitpod/resources/runners/runners.py">delete</a>(\*\*<a href="src/gitpod/types/runner_delete_params.py">params</a>) -> object</code>
- <code title="post /gitpod.v1.RunnerService/CheckAuthenticationForHost">client.runners.<a href="./src/gitpod/resources/runners/runners.py">check_authentication_for_host</a>(\*\*<a href="src/gitpod/types/runner_check_authentication_for_host_params.py">params</a>) -> <a href="./src/gitpod/types/runner_check_authentication_for_host_response.py">RunnerCheckAuthenticationForHostResponse</a></code>
- <code title="post /gitpod.v1.RunnerService/CreateRunnerLogsToken">client.runners.<a href="./src/gitpod/resources/runners/runners.py">create_logs_token</a>(\*\*<a href="src/gitpod/types/runner_create_logs_token_params.py">params</a>) -> <a href="./src/gitpod/types/runner_create_logs_token_response.py">RunnerCreateLogsTokenResponse</a></code>
- <code title="post /gitpod.v1.RunnerService/CreateRunnerToken">client.runners.<a href="./src/gitpod/resources/runners/runners.py">create_runner_token</a>(\*\*<a href="src/gitpod/types/runner_create_runner_token_params.py">params</a>) -> <a href="./src/gitpod/types/runner_create_runner_token_response.py">RunnerCreateRunnerTokenResponse</a></code>
- <code title="post /gitpod.v1.RunnerService/ParseContextURL">client.runners.<a href="./src/gitpod/resources/runners/runners.py">parse_context_url</a>(\*\*<a href="src/gitpod/types/runner_parse_context_url_params.py">params</a>) -> <a href="./src/gitpod/types/runner_parse_context_url_response.py">RunnerParseContextURLResponse</a></code>
- <code title="post /gitpod.v1.RunnerService/SearchRepositories">client.runners.<a href="./src/gitpod/resources/runners/runners.py">search_repositories</a>(\*\*<a href="src/gitpod/types/runner_search_repositories_params.py">params</a>) -> <a href="./src/gitpod/types/runner_search_repositories_response.py">RunnerSearchRepositoriesResponse</a></code>

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
)
```

Methods:

- <code title="post /gitpod.v1.RunnerConfigurationService/CreateEnvironmentClass">client.runners.configurations.environment_classes.<a href="./src/gitpod/resources/runners/configurations/environment_classes.py">create</a>(\*\*<a href="src/gitpod/types/runners/configurations/environment_class_create_params.py">params</a>) -> <a href="./src/gitpod/types/runners/configurations/environment_class_create_response.py">EnvironmentClassCreateResponse</a></code>
- <code title="post /gitpod.v1.RunnerConfigurationService/GetEnvironmentClass">client.runners.configurations.environment_classes.<a href="./src/gitpod/resources/runners/configurations/environment_classes.py">retrieve</a>(\*\*<a href="src/gitpod/types/runners/configurations/environment_class_retrieve_params.py">params</a>) -> <a href="./src/gitpod/types/runners/configurations/environment_class_retrieve_response.py">EnvironmentClassRetrieveResponse</a></code>
- <code title="post /gitpod.v1.RunnerConfigurationService/UpdateEnvironmentClass">client.runners.configurations.environment_classes.<a href="./src/gitpod/resources/runners/configurations/environment_classes.py">update</a>(\*\*<a href="src/gitpod/types/runners/configurations/environment_class_update_params.py">params</a>) -> object</code>
- <code title="post /gitpod.v1.RunnerConfigurationService/ListEnvironmentClasses">client.runners.configurations.environment_classes.<a href="./src/gitpod/resources/runners/configurations/environment_classes.py">list</a>(\*\*<a href="src/gitpod/types/runners/configurations/environment_class_list_params.py">params</a>) -> <a href="./src/gitpod/types/shared/environment_class.py">SyncEnvironmentClassesPage[EnvironmentClass]</a></code>

### HostAuthenticationTokens

Types:

```python
from gitpod.types.runners.configurations import (
    HostAuthenticationToken,
    HostAuthenticationTokenSource,
    HostAuthenticationTokenCreateResponse,
    HostAuthenticationTokenRetrieveResponse,
)
```

Methods:

- <code title="post /gitpod.v1.RunnerConfigurationService/CreateHostAuthenticationToken">client.runners.configurations.host_authentication_tokens.<a href="./src/gitpod/resources/runners/configurations/host_authentication_tokens.py">create</a>(\*\*<a href="src/gitpod/types/runners/configurations/host_authentication_token_create_params.py">params</a>) -> <a href="./src/gitpod/types/runners/configurations/host_authentication_token_create_response.py">HostAuthenticationTokenCreateResponse</a></code>
- <code title="post /gitpod.v1.RunnerConfigurationService/GetHostAuthenticationToken">client.runners.configurations.host_authentication_tokens.<a href="./src/gitpod/resources/runners/configurations/host_authentication_tokens.py">retrieve</a>(\*\*<a href="src/gitpod/types/runners/configurations/host_authentication_token_retrieve_params.py">params</a>) -> <a href="./src/gitpod/types/runners/configurations/host_authentication_token_retrieve_response.py">HostAuthenticationTokenRetrieveResponse</a></code>
- <code title="post /gitpod.v1.RunnerConfigurationService/UpdateHostAuthenticationToken">client.runners.configurations.host_authentication_tokens.<a href="./src/gitpod/resources/runners/configurations/host_authentication_tokens.py">update</a>(\*\*<a href="src/gitpod/types/runners/configurations/host_authentication_token_update_params.py">params</a>) -> object</code>
- <code title="post /gitpod.v1.RunnerConfigurationService/ListHostAuthenticationTokens">client.runners.configurations.host_authentication_tokens.<a href="./src/gitpod/resources/runners/configurations/host_authentication_tokens.py">list</a>(\*\*<a href="src/gitpod/types/runners/configurations/host_authentication_token_list_params.py">params</a>) -> <a href="./src/gitpod/types/runners/configurations/host_authentication_token.py">SyncTokensPage[HostAuthenticationToken]</a></code>
- <code title="post /gitpod.v1.RunnerConfigurationService/DeleteHostAuthenticationToken">client.runners.configurations.host_authentication_tokens.<a href="./src/gitpod/resources/runners/configurations/host_authentication_tokens.py">delete</a>(\*\*<a href="src/gitpod/types/runners/configurations/host_authentication_token_delete_params.py">params</a>) -> object</code>

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
)
```

Methods:

- <code title="post /gitpod.v1.RunnerConfigurationService/CreateSCMIntegration">client.runners.configurations.scm_integrations.<a href="./src/gitpod/resources/runners/configurations/scm_integrations.py">create</a>(\*\*<a href="src/gitpod/types/runners/configurations/scm_integration_create_params.py">params</a>) -> <a href="./src/gitpod/types/runners/configurations/scm_integration_create_response.py">ScmIntegrationCreateResponse</a></code>
- <code title="post /gitpod.v1.RunnerConfigurationService/GetSCMIntegration">client.runners.configurations.scm_integrations.<a href="./src/gitpod/resources/runners/configurations/scm_integrations.py">retrieve</a>(\*\*<a href="src/gitpod/types/runners/configurations/scm_integration_retrieve_params.py">params</a>) -> <a href="./src/gitpod/types/runners/configurations/scm_integration_retrieve_response.py">ScmIntegrationRetrieveResponse</a></code>
- <code title="post /gitpod.v1.RunnerConfigurationService/UpdateSCMIntegration">client.runners.configurations.scm_integrations.<a href="./src/gitpod/resources/runners/configurations/scm_integrations.py">update</a>(\*\*<a href="src/gitpod/types/runners/configurations/scm_integration_update_params.py">params</a>) -> object</code>
- <code title="post /gitpod.v1.RunnerConfigurationService/ListSCMIntegrations">client.runners.configurations.scm_integrations.<a href="./src/gitpod/resources/runners/configurations/scm_integrations.py">list</a>(\*\*<a href="src/gitpod/types/runners/configurations/scm_integration_list_params.py">params</a>) -> <a href="./src/gitpod/types/runners/configurations/scm_integration.py">SyncIntegrationsPage[ScmIntegration]</a></code>
- <code title="post /gitpod.v1.RunnerConfigurationService/DeleteSCMIntegration">client.runners.configurations.scm_integrations.<a href="./src/gitpod/resources/runners/configurations/scm_integrations.py">delete</a>(\*\*<a href="src/gitpod/types/runners/configurations/scm_integration_delete_params.py">params</a>) -> object</code>

## Policies

Types:

```python
from gitpod.types.runners import (
    RunnerPolicy,
    RunnerRole,
    PolicyCreateResponse,
    PolicyUpdateResponse,
)
```

Methods:

- <code title="post /gitpod.v1.RunnerService/CreateRunnerPolicy">client.runners.policies.<a href="./src/gitpod/resources/runners/policies.py">create</a>(\*\*<a href="src/gitpod/types/runners/policy_create_params.py">params</a>) -> <a href="./src/gitpod/types/runners/policy_create_response.py">PolicyCreateResponse</a></code>
- <code title="post /gitpod.v1.RunnerService/UpdateRunnerPolicy">client.runners.policies.<a href="./src/gitpod/resources/runners/policies.py">update</a>(\*\*<a href="src/gitpod/types/runners/policy_update_params.py">params</a>) -> <a href="./src/gitpod/types/runners/policy_update_response.py">PolicyUpdateResponse</a></code>
- <code title="post /gitpod.v1.RunnerService/ListRunnerPolicies">client.runners.policies.<a href="./src/gitpod/resources/runners/policies.py">list</a>(\*\*<a href="src/gitpod/types/runners/policy_list_params.py">params</a>) -> <a href="./src/gitpod/types/runners/runner_policy.py">SyncPoliciesPage[RunnerPolicy]</a></code>
- <code title="post /gitpod.v1.RunnerService/DeleteRunnerPolicy">client.runners.policies.<a href="./src/gitpod/resources/runners/policies.py">delete</a>(\*\*<a href="src/gitpod/types/runners/policy_delete_params.py">params</a>) -> object</code>

# Secrets

Types:

```python
from gitpod.types import Secret, SecretScope, SecretCreateResponse, SecretGetValueResponse
```

Methods:

- <code title="post /gitpod.v1.SecretService/CreateSecret">client.secrets.<a href="./src/gitpod/resources/secrets.py">create</a>(\*\*<a href="src/gitpod/types/secret_create_params.py">params</a>) -> <a href="./src/gitpod/types/secret_create_response.py">SecretCreateResponse</a></code>
- <code title="post /gitpod.v1.SecretService/ListSecrets">client.secrets.<a href="./src/gitpod/resources/secrets.py">list</a>(\*\*<a href="src/gitpod/types/secret_list_params.py">params</a>) -> <a href="./src/gitpod/types/secret.py">SyncSecretsPage[Secret]</a></code>
- <code title="post /gitpod.v1.SecretService/DeleteSecret">client.secrets.<a href="./src/gitpod/resources/secrets.py">delete</a>(\*\*<a href="src/gitpod/types/secret_delete_params.py">params</a>) -> object</code>
- <code title="post /gitpod.v1.SecretService/GetSecretValue">client.secrets.<a href="./src/gitpod/resources/secrets.py">get_value</a>(\*\*<a href="src/gitpod/types/secret_get_value_params.py">params</a>) -> <a href="./src/gitpod/types/secret_get_value_response.py">SecretGetValueResponse</a></code>
- <code title="post /gitpod.v1.SecretService/UpdateSecretValue">client.secrets.<a href="./src/gitpod/resources/secrets.py">update_value</a>(\*\*<a href="src/gitpod/types/secret_update_value_params.py">params</a>) -> object</code>

# Usage

Types:

```python
from gitpod.types import EnvironmentUsageRecord
```

Methods:

- <code title="post /gitpod.v1.UsageService/ListEnvironmentUsageRecords">client.usage.<a href="./src/gitpod/resources/usage.py">list_environment_runtime_records</a>(\*\*<a href="src/gitpod/types/usage_list_environment_runtime_records_params.py">params</a>) -> <a href="./src/gitpod/types/environment_usage_record.py">SyncRecordsPage[EnvironmentUsageRecord]</a></code>

# Users

Types:

```python
from gitpod.types import User, UserGetAuthenticatedUserResponse, UserGetUserResponse
```

Methods:

- <code title="post /gitpod.v1.UserService/DeleteUser">client.users.<a href="./src/gitpod/resources/users/users.py">delete_user</a>(\*\*<a href="src/gitpod/types/user_delete_user_params.py">params</a>) -> object</code>
- <code title="post /gitpod.v1.UserService/GetAuthenticatedUser">client.users.<a href="./src/gitpod/resources/users/users.py">get_authenticated_user</a>(\*\*<a href="src/gitpod/types/user_get_authenticated_user_params.py">params</a>) -> <a href="./src/gitpod/types/user_get_authenticated_user_response.py">UserGetAuthenticatedUserResponse</a></code>
- <code title="post /gitpod.v1.UserService/GetUser">client.users.<a href="./src/gitpod/resources/users/users.py">get_user</a>(\*\*<a href="src/gitpod/types/user_get_user_params.py">params</a>) -> <a href="./src/gitpod/types/user_get_user_response.py">UserGetUserResponse</a></code>
- <code title="post /gitpod.v1.UserService/SetSuspended">client.users.<a href="./src/gitpod/resources/users/users.py">set_suspended</a>(\*\*<a href="src/gitpod/types/user_set_suspended_params.py">params</a>) -> object</code>

## Dotfiles

Types:

```python
from gitpod.types.users import DotfilesConfiguration, DotfileGetResponse
```

Methods:

- <code title="post /gitpod.v1.UserService/GetDotfilesConfiguration">client.users.dotfiles.<a href="./src/gitpod/resources/users/dotfiles.py">get</a>(\*\*<a href="src/gitpod/types/users/dotfile_get_params.py">params</a>) -> <a href="./src/gitpod/types/users/dotfile_get_response.py">DotfileGetResponse</a></code>
- <code title="post /gitpod.v1.UserService/SetDotfilesConfiguration">client.users.dotfiles.<a href="./src/gitpod/resources/users/dotfiles.py">set</a>(\*\*<a href="src/gitpod/types/users/dotfile_set_params.py">params</a>) -> object</code>

## Pats

Types:

```python
from gitpod.types.users import PersonalAccessToken, PatGetResponse
```

Methods:

- <code title="post /gitpod.v1.UserService/ListPersonalAccessTokens">client.users.pats.<a href="./src/gitpod/resources/users/pats.py">list</a>(\*\*<a href="src/gitpod/types/users/pat_list_params.py">params</a>) -> <a href="./src/gitpod/types/users/personal_access_token.py">SyncPersonalAccessTokensPage[PersonalAccessToken]</a></code>
- <code title="post /gitpod.v1.UserService/DeletePersonalAccessToken">client.users.pats.<a href="./src/gitpod/resources/users/pats.py">delete</a>(\*\*<a href="src/gitpod/types/users/pat_delete_params.py">params</a>) -> object</code>
- <code title="post /gitpod.v1.UserService/GetPersonalAccessToken">client.users.pats.<a href="./src/gitpod/resources/users/pats.py">get</a>(\*\*<a href="src/gitpod/types/users/pat_get_params.py">params</a>) -> <a href="./src/gitpod/types/users/pat_get_response.py">PatGetResponse</a></code>
