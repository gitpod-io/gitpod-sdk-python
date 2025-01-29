# Services

Types:

```python
from gitpod.types import (
    ServiceUpdateResponse,
    ServiceDeleteResponse,
    ServiceStartResponse,
    ServiceStopResponse,
)
```

Methods:

- <code title="post /gitpod.v1.EnvironmentAutomationService/UpdateService">client.services.<a href="./src/gitpod/resources/services.py">update</a>(\*\*<a href="src/gitpod/types/service_update_params.py">params</a>) -> <a href="./src/gitpod/types/service_update_response.py">object</a></code>
- <code title="post /gitpod.v1.EnvironmentAutomationService/DeleteService">client.services.<a href="./src/gitpod/resources/services.py">delete</a>(\*\*<a href="src/gitpod/types/service_delete_params.py">params</a>) -> <a href="./src/gitpod/types/service_delete_response.py">object</a></code>
- <code title="post /gitpod.v1.EnvironmentAutomationService/StartService">client.services.<a href="./src/gitpod/resources/services.py">start</a>(\*\*<a href="src/gitpod/types/service_start_params.py">params</a>) -> <a href="./src/gitpod/types/service_start_response.py">object</a></code>
- <code title="post /gitpod.v1.EnvironmentAutomationService/StopService">client.services.<a href="./src/gitpod/resources/services.py">stop</a>(\*\*<a href="src/gitpod/types/service_stop_params.py">params</a>) -> <a href="./src/gitpod/types/service_stop_response.py">object</a></code>

# AutomationsFiles

Types:

```python
from gitpod.types import AutomationsFileUpsertResponse
```

Methods:

- <code title="post /gitpod.v1.EnvironmentAutomationService/UpsertAutomationsFile">client.automations_files.<a href="./src/gitpod/resources/automations_files.py">upsert</a>(\*\*<a href="src/gitpod/types/automations_file_upsert_params.py">params</a>) -> <a href="./src/gitpod/types/automations_file_upsert_response.py">AutomationsFileUpsertResponse</a></code>

# Tasks

Types:

```python
from gitpod.types import TaskCreateResponse, TaskRetrieveCreateResponse
```

Methods:

- <code title="post /gitpod.v1.EnvironmentAutomationService/CreateTask">client.tasks.<a href="./src/gitpod/resources/tasks.py">create</a>(\*\*<a href="src/gitpod/types/task_create_params.py">params</a>) -> <a href="./src/gitpod/types/task_create_response.py">TaskCreateResponse</a></code>
- <code title="post /gitpod.v1.EnvironmentAutomationService/GetTask">client.tasks.<a href="./src/gitpod/resources/tasks.py">retrieve_create</a>(\*\*<a href="src/gitpod/types/task_retrieve_create_params.py">params</a>) -> <a href="./src/gitpod/types/task_retrieve_create_response.py">TaskRetrieveCreateResponse</a></code>

# Editors

Types:

```python
from gitpod.types import EditorRetrieveResponse, EditorListResponse, EditorResolveEditorURLResponse
```

Methods:

- <code title="post /gitpod.v1.EditorService/GetEditor">client.editors.<a href="./src/gitpod/resources/editors.py">retrieve</a>(\*\*<a href="src/gitpod/types/editor_retrieve_params.py">params</a>) -> <a href="./src/gitpod/types/editor_retrieve_response.py">EditorRetrieveResponse</a></code>
- <code title="post /gitpod.v1.EditorService/ListEditors">client.editors.<a href="./src/gitpod/resources/editors.py">list</a>(\*\*<a href="src/gitpod/types/editor_list_params.py">params</a>) -> <a href="./src/gitpod/types/editor_list_response.py">EditorListResponse</a></code>
- <code title="post /gitpod.v1.EditorService/ResolveEditorURL">client.editors.<a href="./src/gitpod/resources/editors.py">resolve_editor_url</a>(\*\*<a href="src/gitpod/types/editor_resolve_editor_url_params.py">params</a>) -> <a href="./src/gitpod/types/editor_resolve_editor_url_response.py">EditorResolveEditorURLResponse</a></code>

# EnvironmentAutomations

## Tasks

Types:

```python
from gitpod.types.environment_automations import (
    TaskUpdateResponse,
    TaskListResponse,
    TaskDeleteResponse,
    TaskStartResponse,
)
```

Methods:

- <code title="post /gitpod.v1.EnvironmentAutomationService/UpdateTask">client.environment_automations.tasks.<a href="./src/gitpod/resources/environment_automations/tasks.py">update</a>(\*\*<a href="src/gitpod/types/environment_automations/task_update_params.py">params</a>) -> <a href="./src/gitpod/types/environment_automations/task_update_response.py">object</a></code>
- <code title="post /gitpod.v1.EnvironmentAutomationService/ListTasks">client.environment_automations.tasks.<a href="./src/gitpod/resources/environment_automations/tasks.py">list</a>(\*\*<a href="src/gitpod/types/environment_automations/task_list_params.py">params</a>) -> <a href="./src/gitpod/types/environment_automations/task_list_response.py">TaskListResponse</a></code>
- <code title="post /gitpod.v1.EnvironmentAutomationService/DeleteTask">client.environment_automations.tasks.<a href="./src/gitpod/resources/environment_automations/tasks.py">delete</a>(\*\*<a href="src/gitpod/types/environment_automations/task_delete_params.py">params</a>) -> <a href="./src/gitpod/types/environment_automations/task_delete_response.py">object</a></code>
- <code title="post /gitpod.v1.EnvironmentAutomationService/StartTask">client.environment_automations.tasks.<a href="./src/gitpod/resources/environment_automations/tasks.py">start</a>(\*\*<a href="src/gitpod/types/environment_automations/task_start_params.py">params</a>) -> <a href="./src/gitpod/types/environment_automations/task_start_response.py">TaskStartResponse</a></code>

## TaskExecutions

Types:

```python
from gitpod.types.environment_automations import (
    TaskExecutionRetrieveResponse,
    TaskExecutionListResponse,
    TaskExecutionCreateRetrieveResponse,
    TaskExecutionStopResponse,
    TaskExecutionUpdateTaskExecutionStatusResponse,
)
```

Methods:

- <code title="post /gitpod.v1.EnvironmentAutomationService/GetTaskExecution">client.environment_automations.task_executions.<a href="./src/gitpod/resources/environment_automations/task_executions.py">retrieve</a>(\*\*<a href="src/gitpod/types/environment_automations/task_execution_retrieve_params.py">params</a>) -> <a href="./src/gitpod/types/environment_automations/task_execution_retrieve_response.py">TaskExecutionRetrieveResponse</a></code>
- <code title="post /gitpod.v1.EnvironmentAutomationService/ListTaskExecutions">client.environment_automations.task_executions.<a href="./src/gitpod/resources/environment_automations/task_executions.py">list</a>(\*\*<a href="src/gitpod/types/environment_automations/task_execution_list_params.py">params</a>) -> <a href="./src/gitpod/types/environment_automations/task_execution_list_response.py">TaskExecutionListResponse</a></code>
- <code title="post /gitpod.v1.EnvironmentAutomationService/GetTaskExecution">client.environment_automations.task_executions.<a href="./src/gitpod/resources/environment_automations/task_executions.py">create_retrieve</a>(\*\*<a href="src/gitpod/types/environment_automations/task_execution_create_retrieve_params.py">params</a>) -> <a href="./src/gitpod/types/environment_automations/task_execution_create_retrieve_response.py">TaskExecutionCreateRetrieveResponse</a></code>
- <code title="post /gitpod.v1.EnvironmentAutomationService/StopTaskExecution">client.environment_automations.task_executions.<a href="./src/gitpod/resources/environment_automations/task_executions.py">stop</a>(\*\*<a href="src/gitpod/types/environment_automations/task_execution_stop_params.py">params</a>) -> <a href="./src/gitpod/types/environment_automations/task_execution_stop_response.py">object</a></code>
- <code title="post /gitpod.v1.EnvironmentAutomationService/UpdateTaskExecutionStatus">client.environment_automations.task_executions.<a href="./src/gitpod/resources/environment_automations/task_executions.py">update_task_execution_status</a>(\*\*<a href="src/gitpod/types/environment_automations/task_execution_update_task_execution_status_params.py">params</a>) -> <a href="./src/gitpod/types/environment_automations/task_execution_update_task_execution_status_response.py">object</a></code>

# Environments

Types:

```python
from gitpod.types import (
    EnvironmentCreateResponse,
    EnvironmentRetrieveResponse,
    EnvironmentListResponse,
    EnvironmentCreateFromProjectResponse,
    EnvironmentStartResponse,
)
```

Methods:

- <code title="post /gitpod.v1.EnvironmentService/CreateEnvironment">client.environments.<a href="./src/gitpod/resources/environments.py">create</a>(\*\*<a href="src/gitpod/types/environment_create_params.py">params</a>) -> <a href="./src/gitpod/types/environment_create_response.py">EnvironmentCreateResponse</a></code>
- <code title="post /gitpod.v1.EnvironmentService/GetEnvironment">client.environments.<a href="./src/gitpod/resources/environments.py">retrieve</a>(\*\*<a href="src/gitpod/types/environment_retrieve_params.py">params</a>) -> <a href="./src/gitpod/types/environment_retrieve_response.py">EnvironmentRetrieveResponse</a></code>
- <code title="post /gitpod.v1.EnvironmentService/ListEnvironments">client.environments.<a href="./src/gitpod/resources/environments.py">list</a>(\*\*<a href="src/gitpod/types/environment_list_params.py">params</a>) -> <a href="./src/gitpod/types/environment_list_response.py">EnvironmentListResponse</a></code>
- <code title="post /gitpod.v1.EnvironmentService/CreateEnvironmentFromProject">client.environments.<a href="./src/gitpod/resources/environments.py">create_from_project</a>(\*\*<a href="src/gitpod/types/environment_create_from_project_params.py">params</a>) -> <a href="./src/gitpod/types/environment_create_from_project_response.py">EnvironmentCreateFromProjectResponse</a></code>
- <code title="post /gitpod.v1.EnvironmentService/StartEnvironment">client.environments.<a href="./src/gitpod/resources/environments.py">start</a>(\*\*<a href="src/gitpod/types/environment_start_params.py">params</a>) -> <a href="./src/gitpod/types/environment_start_response.py">object</a></code>

# EnvironmentClasses

Types:

```python
from gitpod.types import EnvironmentClassListResponse
```

Methods:

- <code title="post /gitpod.v1.EnvironmentService/ListEnvironmentClasses">client.environment_classes.<a href="./src/gitpod/resources/environment_classes.py">list</a>(\*\*<a href="src/gitpod/types/environment_class_list_params.py">params</a>) -> <a href="./src/gitpod/types/environment_class_list_response.py">EnvironmentClassListResponse</a></code>

# Organizations

Types:

```python
from gitpod.types import OrganizationLeaveResponse, OrganizationSetRoleResponse
```

Methods:

- <code title="post /gitpod.v1.OrganizationService/LeaveOrganization">client.organizations.<a href="./src/gitpod/resources/organizations/organizations.py">leave</a>(\*\*<a href="src/gitpod/types/organization_leave_params.py">params</a>) -> <a href="./src/gitpod/types/organization_leave_response.py">object</a></code>
- <code title="post /gitpod.v1.OrganizationService/SetRole">client.organizations.<a href="./src/gitpod/resources/organizations/organizations.py">set_role</a>(\*\*<a href="src/gitpod/types/organization_set_role_params.py">params</a>) -> <a href="./src/gitpod/types/organization_set_role_response.py">object</a></code>

## Members

Types:

```python
from gitpod.types.organizations import MemberListResponse
```

Methods:

- <code title="post /gitpod.v1.OrganizationService/ListMembers">client.organizations.members.<a href="./src/gitpod/resources/organizations/members.py">list</a>(\*\*<a href="src/gitpod/types/organizations/member_list_params.py">params</a>) -> <a href="./src/gitpod/types/organizations/member_list_response.py">MemberListResponse</a></code>

## Invite

Types:

```python
from gitpod.types.organizations import InviteCreateResponse, InviteRetrieveResponse
```

Methods:

- <code title="post /gitpod.v1.OrganizationService/CreateOrganizationInvite">client.organizations.invite.<a href="./src/gitpod/resources/organizations/invite/invite.py">create</a>(\*\*<a href="src/gitpod/types/organizations/invite_create_params.py">params</a>) -> <a href="./src/gitpod/types/organizations/invite_create_response.py">InviteCreateResponse</a></code>
- <code title="post /gitpod.v1.OrganizationService/GetOrganizationInvite">client.organizations.invite.<a href="./src/gitpod/resources/organizations/invite/invite.py">retrieve</a>(\*\*<a href="src/gitpod/types/organizations/invite_retrieve_params.py">params</a>) -> <a href="./src/gitpod/types/organizations/invite_retrieve_response.py">InviteRetrieveResponse</a></code>

### Summary

Types:

```python
from gitpod.types.organizations.invite import SummaryRetrieveResponse
```

Methods:

- <code title="post /gitpod.v1.OrganizationService/GetOrganizationInviteSummary">client.organizations.invite.summary.<a href="./src/gitpod/resources/organizations/invite/summary.py">retrieve</a>(\*\*<a href="src/gitpod/types/organizations/invite/summary_retrieve_params.py">params</a>) -> <a href="./src/gitpod/types/organizations/invite/summary_retrieve_response.py">SummaryRetrieveResponse</a></code>

# Projects

Types:

```python
from gitpod.types import ProjectCreateResponse, ProjectCreateFromEnvironmentResponse
```

Methods:

- <code title="post /gitpod.v1.ProjectService/CreateProject">client.projects.<a href="./src/gitpod/resources/projects.py">create</a>(\*\*<a href="src/gitpod/types/project_create_params.py">params</a>) -> <a href="./src/gitpod/types/project_create_response.py">ProjectCreateResponse</a></code>
- <code title="post /gitpod.v1.ProjectService/CreateProjectFromEnvironment">client.projects.<a href="./src/gitpod/resources/projects.py">create_from_environment</a>(\*\*<a href="src/gitpod/types/project_create_from_environment_params.py">params</a>) -> <a href="./src/gitpod/types/project_create_from_environment_response.py">ProjectCreateFromEnvironmentResponse</a></code>

# RunnerConfigurations

Types:

```python
from gitpod.types import RunnerConfigurationValidateResponse
```

Methods:

- <code title="post /gitpod.v1.RunnerConfigurationService/ValidateRunnerConfiguration">client.runner_configurations.<a href="./src/gitpod/resources/runner_configurations/runner_configurations.py">validate</a>(\*\*<a href="src/gitpod/types/runner_configuration_validate_params.py">params</a>) -> <a href="./src/gitpod/types/runner_configuration_validate_response.py">RunnerConfigurationValidateResponse</a></code>

## HostAuthenticationTokens

Types:

```python
from gitpod.types.runner_configurations import (
    HostAuthenticationTokenCreateResponse,
    HostAuthenticationTokenUpdateResponse,
    HostAuthenticationTokenListResponse,
    HostAuthenticationTokenDeleteResponse,
)
```

Methods:

- <code title="post /gitpod.v1.RunnerConfigurationService/GetHostAuthenticationToken">client.runner_configurations.host_authentication_tokens.<a href="./src/gitpod/resources/runner_configurations/host_authentication_tokens.py">create</a>(\*\*<a href="src/gitpod/types/runner_configurations/host_authentication_token_create_params.py">params</a>) -> <a href="./src/gitpod/types/runner_configurations/host_authentication_token_create_response.py">HostAuthenticationTokenCreateResponse</a></code>
- <code title="post /gitpod.v1.RunnerConfigurationService/UpdateHostAuthenticationToken">client.runner_configurations.host_authentication_tokens.<a href="./src/gitpod/resources/runner_configurations/host_authentication_tokens.py">update</a>(\*\*<a href="src/gitpod/types/runner_configurations/host_authentication_token_update_params.py">params</a>) -> <a href="./src/gitpod/types/runner_configurations/host_authentication_token_update_response.py">object</a></code>
- <code title="post /gitpod.v1.RunnerConfigurationService/ListHostAuthenticationTokens">client.runner_configurations.host_authentication_tokens.<a href="./src/gitpod/resources/runner_configurations/host_authentication_tokens.py">list</a>(\*\*<a href="src/gitpod/types/runner_configurations/host_authentication_token_list_params.py">params</a>) -> <a href="./src/gitpod/types/runner_configurations/host_authentication_token_list_response.py">HostAuthenticationTokenListResponse</a></code>
- <code title="post /gitpod.v1.RunnerConfigurationService/DeleteHostAuthenticationToken">client.runner_configurations.host_authentication_tokens.<a href="./src/gitpod/resources/runner_configurations/host_authentication_tokens.py">delete</a>(\*\*<a href="src/gitpod/types/runner_configurations/host_authentication_token_delete_params.py">params</a>) -> <a href="./src/gitpod/types/runner_configurations/host_authentication_token_delete_response.py">object</a></code>

## ConfigurationSchema

Types:

```python
from gitpod.types.runner_configurations import ConfigurationSchemaCreateResponse
```

Methods:

- <code title="post /gitpod.v1.RunnerConfigurationService/GetRunnerConfigurationSchema">client.runner_configurations.configuration_schema.<a href="./src/gitpod/resources/runner_configurations/configuration_schema.py">create</a>(\*\*<a href="src/gitpod/types/runner_configurations/configuration_schema_create_params.py">params</a>) -> <a href="./src/gitpod/types/runner_configurations/configuration_schema_create_response.py">ConfigurationSchemaCreateResponse</a></code>

## ScmIntegration

Types:

```python
from gitpod.types.runner_configurations import ScmIntegrationCreateResponse
```

Methods:

- <code title="post /gitpod.v1.RunnerConfigurationService/CreateSCMIntegration">client.runner_configurations.scm_integration.<a href="./src/gitpod/resources/runner_configurations/scm_integration.py">create</a>(\*\*<a href="src/gitpod/types/runner_configurations/scm_integration_create_params.py">params</a>) -> <a href="./src/gitpod/types/runner_configurations/scm_integration_create_response.py">ScmIntegrationCreateResponse</a></code>

## EnvironmentClasses

Types:

```python
from gitpod.types.runner_configurations import (
    EnvironmentClassUpdateResponse,
    EnvironmentClassListResponse,
)
```

Methods:

- <code title="post /gitpod.v1.RunnerConfigurationService/UpdateEnvironmentClass">client.runner_configurations.environment_classes.<a href="./src/gitpod/resources/runner_configurations/environment_classes.py">update</a>(\*\*<a href="src/gitpod/types/runner_configurations/environment_class_update_params.py">params</a>) -> <a href="./src/gitpod/types/runner_configurations/environment_class_update_response.py">object</a></code>
- <code title="post /gitpod.v1.RunnerConfigurationService/ListEnvironmentClasses">client.runner_configurations.environment_classes.<a href="./src/gitpod/resources/runner_configurations/environment_classes.py">list</a>(\*\*<a href="src/gitpod/types/runner_configurations/environment_class_list_params.py">params</a>) -> <a href="./src/gitpod/types/runner_configurations/environment_class_list_response.py">EnvironmentClassListResponse</a></code>

# RunnerInteractions

Types:

```python
from gitpod.types import (
    RunnerInteractionGetHostAuthenticationTokenValueResponse,
    RunnerInteractionGetLatestVersionResponse,
    RunnerInteractionListRunnerEnvironmentClassesResponse,
    RunnerInteractionListRunnerScmIntegrationsResponse,
    RunnerInteractionMarkActiveResponse,
    RunnerInteractionSendResponseResponse,
    RunnerInteractionSignupResponse,
    RunnerInteractionUpdateRunnerConfigurationSchemaResponse,
    RunnerInteractionUpdateStatusResponse,
)
```

Methods:

- <code title="post /gitpod.v1.RunnerInteractionService/GetHostAuthenticationTokenValue">client.runner_interactions.<a href="./src/gitpod/resources/runner_interactions/runner_interactions.py">get_host_authentication_token_value</a>(\*\*<a href="src/gitpod/types/runner_interaction_get_host_authentication_token_value_params.py">params</a>) -> <a href="./src/gitpod/types/runner_interaction_get_host_authentication_token_value_response.py">RunnerInteractionGetHostAuthenticationTokenValueResponse</a></code>
- <code title="post /gitpod.v1.RunnerInteractionService/GetLatestVersion">client.runner_interactions.<a href="./src/gitpod/resources/runner_interactions/runner_interactions.py">get_latest_version</a>(\*\*<a href="src/gitpod/types/runner_interaction_get_latest_version_params.py">params</a>) -> <a href="./src/gitpod/types/runner_interaction_get_latest_version_response.py">RunnerInteractionGetLatestVersionResponse</a></code>
- <code title="post /gitpod.v1.RunnerInteractionService/ListRunnerEnvironmentClasses">client.runner_interactions.<a href="./src/gitpod/resources/runner_interactions/runner_interactions.py">list_runner_environment_classes</a>(\*\*<a href="src/gitpod/types/runner_interaction_list_runner_environment_classes_params.py">params</a>) -> <a href="./src/gitpod/types/runner_interaction_list_runner_environment_classes_response.py">RunnerInteractionListRunnerEnvironmentClassesResponse</a></code>
- <code title="post /gitpod.v1.RunnerInteractionService/ListRunnerSCMIntegrations">client.runner_interactions.<a href="./src/gitpod/resources/runner_interactions/runner_interactions.py">list_runner_scm_integrations</a>(\*\*<a href="src/gitpod/types/runner_interaction_list_runner_scm_integrations_params.py">params</a>) -> <a href="./src/gitpod/types/runner_interaction_list_runner_scm_integrations_response.py">RunnerInteractionListRunnerScmIntegrationsResponse</a></code>
- <code title="post /gitpod.v1.RunnerInteractionService/MarkRunnerActive">client.runner_interactions.<a href="./src/gitpod/resources/runner_interactions/runner_interactions.py">mark_active</a>(\*\*<a href="src/gitpod/types/runner_interaction_mark_active_params.py">params</a>) -> <a href="./src/gitpod/types/runner_interaction_mark_active_response.py">object</a></code>
- <code title="post /gitpod.v1.RunnerInteractionService/SendResponse">client.runner_interactions.<a href="./src/gitpod/resources/runner_interactions/runner_interactions.py">send_response</a>(\*\*<a href="src/gitpod/types/runner_interaction_send_response_params.py">params</a>) -> <a href="./src/gitpod/types/runner_interaction_send_response_response.py">object</a></code>
- <code title="post /gitpod.v1.RunnerInteractionService/Signup">client.runner_interactions.<a href="./src/gitpod/resources/runner_interactions/runner_interactions.py">signup</a>(\*\*<a href="src/gitpod/types/runner_interaction_signup_params.py">params</a>) -> <a href="./src/gitpod/types/runner_interaction_signup_response.py">RunnerInteractionSignupResponse</a></code>
- <code title="post /gitpod.v1.RunnerInteractionService/UpdateRunnerConfigurationSchema">client.runner_interactions.<a href="./src/gitpod/resources/runner_interactions/runner_interactions.py">update_runner_configuration_schema</a>(\*\*<a href="src/gitpod/types/runner_interaction_update_runner_configuration_schema_params.py">params</a>) -> <a href="./src/gitpod/types/runner_interaction_update_runner_configuration_schema_response.py">object</a></code>
- <code title="post /gitpod.v1.RunnerInteractionService/UpdateRunnerStatus">client.runner_interactions.<a href="./src/gitpod/resources/runner_interactions/runner_interactions.py">update_status</a>(\*\*<a href="src/gitpod/types/runner_interaction_update_status_params.py">params</a>) -> <a href="./src/gitpod/types/runner_interaction_update_status_response.py">object</a></code>

## Environments

Types:

```python
from gitpod.types.runner_interactions import (
    EnvironmentRetrieveResponse,
    EnvironmentListResponse,
    EnvironmentUpdateStatusResponse,
)
```

Methods:

- <code title="post /gitpod.v1.RunnerInteractionService/GetRunnerEnvironment">client.runner_interactions.environments.<a href="./src/gitpod/resources/runner_interactions/environments.py">retrieve</a>(\*\*<a href="src/gitpod/types/runner_interactions/environment_retrieve_params.py">params</a>) -> <a href="./src/gitpod/types/runner_interactions/environment_retrieve_response.py">EnvironmentRetrieveResponse</a></code>
- <code title="post /gitpod.v1.RunnerInteractionService/ListRunnerEnvironments">client.runner_interactions.environments.<a href="./src/gitpod/resources/runner_interactions/environments.py">list</a>(\*\*<a href="src/gitpod/types/runner_interactions/environment_list_params.py">params</a>) -> <a href="./src/gitpod/types/runner_interactions/environment_list_response.py">EnvironmentListResponse</a></code>
- <code title="post /gitpod.v1.RunnerInteractionService/UpdateRunnerEnvironmentStatus">client.runner_interactions.environments.<a href="./src/gitpod/resources/runner_interactions/environments.py">update_status</a>(\*\*<a href="src/gitpod/types/runner_interactions/environment_update_status_params.py">params</a>) -> <a href="./src/gitpod/types/runner_interactions/environment_update_status_response.py">object</a></code>

# Runners

Types:

```python
from gitpod.types import (
    RunnerCreateResponse,
    RunnerListResponse,
    RunnerCheckAuthenticationForHostResponse,
    RunnerCreateRunnerTokenResponse,
    RunnerDeleteRunnerResponse,
    RunnerGetRunnerResponse,
    RunnerParseContextURLResponse,
    RunnerUpdateRunnerResponse,
)
```

Methods:

- <code title="post /gitpod.v1.RunnerService/CreateRunner">client.runners.<a href="./src/gitpod/resources/runners/runners.py">create</a>(\*\*<a href="src/gitpod/types/runner_create_params.py">params</a>) -> <a href="./src/gitpod/types/runner_create_response.py">RunnerCreateResponse</a></code>
- <code title="post /gitpod.v1.RunnerService/ListRunners">client.runners.<a href="./src/gitpod/resources/runners/runners.py">list</a>(\*\*<a href="src/gitpod/types/runner_list_params.py">params</a>) -> <a href="./src/gitpod/types/runner_list_response.py">RunnerListResponse</a></code>
- <code title="post /gitpod.v1.RunnerService/CheckAuthenticationForHost">client.runners.<a href="./src/gitpod/resources/runners/runners.py">check_authentication_for_host</a>(\*\*<a href="src/gitpod/types/runner_check_authentication_for_host_params.py">params</a>) -> <a href="./src/gitpod/types/runner_check_authentication_for_host_response.py">RunnerCheckAuthenticationForHostResponse</a></code>
- <code title="post /gitpod.v1.RunnerService/CreateRunnerToken">client.runners.<a href="./src/gitpod/resources/runners/runners.py">create_runner_token</a>(\*\*<a href="src/gitpod/types/runner_create_runner_token_params.py">params</a>) -> <a href="./src/gitpod/types/runner_create_runner_token_response.py">RunnerCreateRunnerTokenResponse</a></code>
- <code title="post /gitpod.v1.RunnerService/DeleteRunner">client.runners.<a href="./src/gitpod/resources/runners/runners.py">delete_runner</a>(\*\*<a href="src/gitpod/types/runner_delete_runner_params.py">params</a>) -> <a href="./src/gitpod/types/runner_delete_runner_response.py">object</a></code>
- <code title="post /gitpod.v1.RunnerService/GetRunner">client.runners.<a href="./src/gitpod/resources/runners/runners.py">get_runner</a>(\*\*<a href="src/gitpod/types/runner_get_runner_params.py">params</a>) -> <a href="./src/gitpod/types/runner_get_runner_response.py">RunnerGetRunnerResponse</a></code>
- <code title="post /gitpod.v1.RunnerService/ParseContextURL">client.runners.<a href="./src/gitpod/resources/runners/runners.py">parse_context_url</a>(\*\*<a href="src/gitpod/types/runner_parse_context_url_params.py">params</a>) -> <a href="./src/gitpod/types/runner_parse_context_url_response.py">RunnerParseContextURLResponse</a></code>
- <code title="post /gitpod.v1.RunnerService/UpdateRunner">client.runners.<a href="./src/gitpod/resources/runners/runners.py">update_runner</a>(\*\*<a href="src/gitpod/types/runner_update_runner_params.py">params</a>) -> <a href="./src/gitpod/types/runner_update_runner_response.py">object</a></code>

## Policies

Types:

```python
from gitpod.types.runners import PolicyListResponse
```

Methods:

- <code title="post /gitpod.v1.RunnerService/ListRunnerPolicies">client.runners.policies.<a href="./src/gitpod/resources/runners/policies.py">list</a>(\*\*<a href="src/gitpod/types/runners/policy_list_params.py">params</a>) -> <a href="./src/gitpod/types/runners/policy_list_response.py">PolicyListResponse</a></code>

# PersonalAccessTokens

Types:

```python
from gitpod.types import PersonalAccessTokenListResponse, PersonalAccessTokenDeleteResponse
```

Methods:

- <code title="post /gitpod.v1.UserService/ListPersonalAccessTokens">client.personal_access_tokens.<a href="./src/gitpod/resources/personal_access_tokens.py">list</a>(\*\*<a href="src/gitpod/types/personal_access_token_list_params.py">params</a>) -> <a href="./src/gitpod/types/personal_access_token_list_response.py">PersonalAccessTokenListResponse</a></code>
- <code title="post /gitpod.v1.UserService/DeletePersonalAccessToken">client.personal_access_tokens.<a href="./src/gitpod/resources/personal_access_tokens.py">delete</a>(\*\*<a href="src/gitpod/types/personal_access_token_delete_params.py">params</a>) -> <a href="./src/gitpod/types/personal_access_token_delete_response.py">object</a></code>
