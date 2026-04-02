# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional

import httpx

from ..types import (
    automation_list_params,
    automation_create_params,
    automation_delete_params,
    automation_update_params,
    automation_retrieve_params,
    automation_list_executions_params,
    automation_start_execution_params,
    automation_cancel_execution_params,
    automation_retrieve_execution_params,
    automation_list_execution_actions_params,
    automation_list_execution_outputs_params,
    automation_cancel_execution_action_params,
    automation_retrieve_execution_action_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import (
    SyncOutputsPage,
    AsyncOutputsPage,
    SyncWorkflowsPage,
    AsyncWorkflowsPage,
    SyncWorkflowExecutionsPage,
    AsyncWorkflowExecutionsPage,
    SyncWorkflowExecutionActionsPage,
    AsyncWorkflowExecutionActionsPage,
)
from .._base_client import AsyncPaginator, make_request_options
from ..types.workflow import Workflow
from ..types.shared_params.sort import Sort
from ..types.workflow_execution import WorkflowExecution
from ..types.shared_params.subject import Subject
from ..types.workflow_action_param import WorkflowActionParam
from ..types.workflow_trigger_param import WorkflowTriggerParam
from ..types.workflow_execution_action import WorkflowExecutionAction
from ..types.automation_create_response import AutomationCreateResponse
from ..types.automation_update_response import AutomationUpdateResponse
from ..types.automation_retrieve_response import AutomationRetrieveResponse
from ..types.workflow_trigger_context_param import WorkflowTriggerContextParam
from ..types.automation_start_execution_response import AutomationStartExecutionResponse
from ..types.automation_retrieve_execution_response import AutomationRetrieveExecutionResponse
from ..types.automation_list_execution_outputs_response import AutomationListExecutionOutputsResponse
from ..types.automation_retrieve_execution_action_response import AutomationRetrieveExecutionActionResponse

__all__ = ["AutomationsResource", "AsyncAutomationsResource"]


class AutomationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AutomationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AutomationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AutomationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return AutomationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        action: WorkflowActionParam,
        description: str | Omit = omit,
        executor: Optional[Subject] | Omit = omit,
        name: str | Omit = omit,
        report: WorkflowActionParam | Omit = omit,
        triggers: Iterable[WorkflowTriggerParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutomationCreateResponse:
        """
        Creates a new workflow with specified configuration.

        Use this method to:

        - Set up automated workflows
        - Configure workflow triggers
        - Define workflow actions and steps
        - Set execution limits and constraints

        Args:
          action: WorkflowAction defines the actions to be executed in a workflow.

          description:
              Description must be at most 500 characters:

              ```
              size(this) <= 500
              ```

          executor: Optional executor for the workflow. If not provided, defaults to the creator.
              Must be either the caller themselves or a service account.

          name:
              Name must be between 1 and 80 characters:

              ```
              size(this) >= 1 && size(this) <= 80
              ```

          report: WorkflowAction defines the actions to be executed in a workflow.

          triggers:
              Automation must have between 1 and 10 triggers:

              ```
              size(this) >= 1 && size(this) <= 10
              ```

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.WorkflowService/CreateWorkflow",
            body=maybe_transform(
                {
                    "action": action,
                    "description": description,
                    "executor": executor,
                    "name": name,
                    "report": report,
                    "triggers": triggers,
                },
                automation_create_params.AutomationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutomationCreateResponse,
        )

    def retrieve(
        self,
        *,
        workflow_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutomationRetrieveResponse:
        """
        Gets details about a specific workflow.

        Use this method to:

        - View workflow configuration
        - Check workflow status
        - Get workflow metadata

        ### Examples

        - Get workflow details:

          Retrieves information about a specific workflow.

          ```yaml
          workflowId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.WorkflowService/GetWorkflow",
            body=maybe_transform({"workflow_id": workflow_id}, automation_retrieve_params.AutomationRetrieveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutomationRetrieveResponse,
        )

    def update(
        self,
        *,
        action: Optional[WorkflowActionParam] | Omit = omit,
        description: Optional[str] | Omit = omit,
        disabled: Optional[bool] | Omit = omit,
        executor: Optional[Subject] | Omit = omit,
        name: Optional[str] | Omit = omit,
        report: Optional[WorkflowActionParam] | Omit = omit,
        triggers: Iterable[WorkflowTriggerParam] | Omit = omit,
        workflow_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutomationUpdateResponse:
        """
        Updates a workflow's configuration using full replacement semantics.

        Update Behavior:

        - All provided fields completely replace existing values
        - Optional fields that are not provided remain unchanged
        - Complex fields (triggers, action) are replaced entirely, not merged
        - To remove optional fields, explicitly set them to empty/default values

        Use this method to:

        - Modify workflow settings
        - Update triggers and actions
        - Change execution limits
        - Update workflow steps

        ### Examples

        - Update workflow name:

          Changes the workflow's display name.

          ```yaml
          workflowId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          name: "Updated Workflow Name"
          ```

        - Replace all triggers:

          Completely replaces the workflow's trigger configuration.

          ```yaml
          workflowId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          triggers:
            - manual: {}
              context:
                projects:
                  projectIds: ["new-project-id"]
          ```

        - Update execution limits:

          Completely replaces the workflow's action configuration.

          ```yaml
          workflowId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          action:
            limits:
              maxParallel: 10
              maxTotal: 100
            steps:
              - task:
                  command: "npm test"
          ```

        Args:
          action: WorkflowAction defines the actions to be executed in a workflow.

          description:
              Description must be at most 500 characters:

              ```
              size(this) <= 500
              ```

          disabled: When set, enables or disables the workflow. A disabled workflow will not be
              triggered by any automatic trigger and manual starts are rejected.

          name:
              Name must be between 1 and 80 characters:

              ```
              size(this) >= 1 && size(this) <= 80
              ```

          report: WorkflowAction defines the actions to be executed in a workflow.

          triggers:
              Automation can have at most 10 triggers:

              ```
              size(this) <= 10
              ```

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.WorkflowService/UpdateWorkflow",
            body=maybe_transform(
                {
                    "action": action,
                    "description": description,
                    "disabled": disabled,
                    "executor": executor,
                    "name": name,
                    "report": report,
                    "triggers": triggers,
                    "workflow_id": workflow_id,
                },
                automation_update_params.AutomationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutomationUpdateResponse,
        )

    def list(
        self,
        *,
        token: str | Omit = omit,
        page_size: int | Omit = omit,
        filter: automation_list_params.Filter | Omit = omit,
        pagination: automation_list_params.Pagination | Omit = omit,
        sort: automation_list_params.Sort | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncWorkflowsPage[Workflow]:
        """ListWorkflows

        Args:
          sort: sort specifies the order of results.

        When unspecified, results are sorted
              alphabetically by name ascending.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.WorkflowService/ListWorkflows",
            page=SyncWorkflowsPage[Workflow],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                    "sort": sort,
                },
                automation_list_params.AutomationListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "token": token,
                        "page_size": page_size,
                    },
                    automation_list_params.AutomationListParams,
                ),
            ),
            model=Workflow,
            method="post",
        )

    def delete(
        self,
        *,
        force: bool | Omit = omit,
        workflow_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Deletes a workflow permanently.

        Use this method to:

        - Remove unused workflows
        - Clean up test workflows
        - Delete obsolete configurations

        ### Examples

        - Delete workflow:

          Permanently removes a workflow.

          ```yaml
          workflowId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          ```

        Args:
          force: force indicates whether to immediately delete the workflow and all related
              resources. When true, performs cascading deletion of:

              - All workflow executions
              - All workflow execution actions
              - All environments created by workflow actions
              - All agent executions created by workflow actions
              - The workflow itself When false (default), marks workflow executions for
                deletion and relies on background reconciliation to clean up resources.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.WorkflowService/DeleteWorkflow",
            body=maybe_transform(
                {
                    "force": force,
                    "workflow_id": workflow_id,
                },
                automation_delete_params.AutomationDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def cancel_execution(
        self,
        *,
        workflow_execution_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Cancels a running workflow execution.

        Use this method to:

        - Stop long-running executions
        - Cancel failed executions
        - Manage resource usage

        ### Examples

        - Cancel execution:

          Stops a running workflow execution.

          ```yaml
          workflowExecutionId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.WorkflowService/CancelWorkflowExecution",
            body=maybe_transform(
                {"workflow_execution_id": workflow_execution_id},
                automation_cancel_execution_params.AutomationCancelExecutionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def cancel_execution_action(
        self,
        *,
        workflow_execution_action_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Cancels a running workflow execution action.

        Use this method to:

        - Stop long-running actions
        - Cancel failed actions
        - Manage resource usage

        ### Examples

        - Cancel execution action:

          Stops a running workflow execution action.

          ```yaml
          workflowExecutionActionId: "a1b2c3d4-5e6f-7890-abcd-ef1234567890"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.WorkflowService/CancelWorkflowExecutionAction",
            body=maybe_transform(
                {"workflow_execution_action_id": workflow_execution_action_id},
                automation_cancel_execution_action_params.AutomationCancelExecutionActionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def list_execution_actions(
        self,
        *,
        token: str | Omit = omit,
        page_size: int | Omit = omit,
        filter: automation_list_execution_actions_params.Filter | Omit = omit,
        pagination: automation_list_execution_actions_params.Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncWorkflowExecutionActionsPage[WorkflowExecutionAction]:
        """
        Lists workflow execution actions with optional filtering.

        Use this method to:

        - Monitor individual action execution status
        - Debug action failures
        - Track resource usage per action

        ### Examples

        - List execution actions for workflow execution:

          Shows all execution actions for a specific workflow execution.

          ```yaml
          filter:
            workflowExecutionIds: ["d2c94c27-3b76-4a42-b88c-95a85e392c68"]
          pagination:
            pageSize: 20
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.WorkflowService/ListWorkflowExecutionActions",
            page=SyncWorkflowExecutionActionsPage[WorkflowExecutionAction],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                automation_list_execution_actions_params.AutomationListExecutionActionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "token": token,
                        "page_size": page_size,
                    },
                    automation_list_execution_actions_params.AutomationListExecutionActionsParams,
                ),
            ),
            model=WorkflowExecutionAction,
            method="post",
        )

    def list_execution_outputs(
        self,
        *,
        token: str | Omit = omit,
        page_size: int | Omit = omit,
        filter: automation_list_execution_outputs_params.Filter | Omit = omit,
        pagination: automation_list_execution_outputs_params.Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncOutputsPage[AutomationListExecutionOutputsResponse]:
        """
        Lists outputs produced by workflow execution actions.

        Use this method to:

        - Retrieve test results, coverage metrics, or other structured data from
          executions
        - Aggregate outputs across multiple workflow executions
        - Build dashboards or reports from execution data

        ### Examples

        - List outputs for a workflow execution:

          Retrieves all outputs produced by actions in the specified execution.

          ```yaml
          filter:
            workflowExecutionIds: ["d2c94c27-3b76-4a42-b88c-95a85e392c68"]
          pagination:
            pageSize: 50
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.WorkflowService/ListWorkflowExecutionOutputs",
            page=SyncOutputsPage[AutomationListExecutionOutputsResponse],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                automation_list_execution_outputs_params.AutomationListExecutionOutputsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "token": token,
                        "page_size": page_size,
                    },
                    automation_list_execution_outputs_params.AutomationListExecutionOutputsParams,
                ),
            ),
            model=AutomationListExecutionOutputsResponse,
            method="post",
        )

    def list_executions(
        self,
        *,
        token: str | Omit = omit,
        page_size: int | Omit = omit,
        filter: automation_list_executions_params.Filter | Omit = omit,
        pagination: automation_list_executions_params.Pagination | Omit = omit,
        sort: Sort | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncWorkflowExecutionsPage[WorkflowExecution]:
        """
        Lists workflow executions with optional filtering.

        Use this method to:

        - Monitor workflow execution history
        - Track execution status
        - Debug workflow issues

        ### Examples

        - List executions for workflow:

          Shows all executions for a specific workflow.

          ```yaml
          filter:
            workflowIds: ["b0e12f6c-4c67-429d-a4a6-d9838b5da047"]
          pagination:
            pageSize: 20
          ```

        Args:
          sort: sort specifies the order of results. When unspecified, results are sorted by
              operational priority (running first, then failed, then completed, then others).
              Supported sort fields: startedAt, finishedAt, createdAt.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.WorkflowService/ListWorkflowExecutions",
            page=SyncWorkflowExecutionsPage[WorkflowExecution],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                    "sort": sort,
                },
                automation_list_executions_params.AutomationListExecutionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "token": token,
                        "page_size": page_size,
                    },
                    automation_list_executions_params.AutomationListExecutionsParams,
                ),
            ),
            model=WorkflowExecution,
            method="post",
        )

    def retrieve_execution(
        self,
        *,
        workflow_execution_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutomationRetrieveExecutionResponse:
        """
        Gets details about a specific workflow execution.

        Use this method to:

        - Check execution status
        - View execution results
        - Monitor execution progress

        ### Examples

        - Get execution details:

          Retrieves information about a specific execution.

          ```yaml
          workflowExecutionId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.WorkflowService/GetWorkflowExecution",
            body=maybe_transform(
                {"workflow_execution_id": workflow_execution_id},
                automation_retrieve_execution_params.AutomationRetrieveExecutionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutomationRetrieveExecutionResponse,
        )

    def retrieve_execution_action(
        self,
        *,
        workflow_execution_action_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutomationRetrieveExecutionActionResponse:
        """
        Gets details about a specific workflow execution action.

        Use this method to:

        - Check execution action status
        - View execution action results
        - Monitor execution action progress

        ### Examples

        - Get execution action details:

          Retrieves information about a specific execution action.

          ```yaml
          workflowExecutionActionId: "a1b2c3d4-5e6f-7890-abcd-ef1234567890"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.WorkflowService/GetWorkflowExecutionAction",
            body=maybe_transform(
                {"workflow_execution_action_id": workflow_execution_action_id},
                automation_retrieve_execution_action_params.AutomationRetrieveExecutionActionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutomationRetrieveExecutionActionResponse,
        )

    def start_execution(
        self,
        *,
        context_override: Optional[WorkflowTriggerContextParam] | Omit = omit,
        parameters: Dict[str, str] | Omit = omit,
        workflow_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutomationStartExecutionResponse:
        """
        Starts a workflow execution.

        Use this method to:

        - Start workflow execution on demand
        - Test workflow configurations
        - Run workflows outside of automatic triggers

        ### Examples

        - Start workflow:

          Starts a workflow execution manually.

          ```yaml
          workflowId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          ```

        Args:
          context_override: Optional context override for the execution. When provided, replaces the
              workflow's default trigger context. User must have appropriate permissions on
              the overridden resources. Supports Projects, Repositories, and Agent context
              types. FromTrigger context type is not supported for manual overrides.

          parameters: Parameters to substitute into workflow steps using Go template syntax. Use
              {{ .Parameters.key_name }} in templatable fields (task.command, agent.prompt,
              pull*request.title/description/branch, trigger context agent.prompt). Keys must
              match pattern ^[a-zA-Z*][a-zA-Z0-9_]\\**$ Maximum 10 parameters allowed. Empty map
              is treated as no parameters provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.WorkflowService/StartWorkflow",
            body=maybe_transform(
                {
                    "context_override": context_override,
                    "parameters": parameters,
                    "workflow_id": workflow_id,
                },
                automation_start_execution_params.AutomationStartExecutionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutomationStartExecutionResponse,
        )


class AsyncAutomationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAutomationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAutomationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAutomationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return AsyncAutomationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        action: WorkflowActionParam,
        description: str | Omit = omit,
        executor: Optional[Subject] | Omit = omit,
        name: str | Omit = omit,
        report: WorkflowActionParam | Omit = omit,
        triggers: Iterable[WorkflowTriggerParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutomationCreateResponse:
        """
        Creates a new workflow with specified configuration.

        Use this method to:

        - Set up automated workflows
        - Configure workflow triggers
        - Define workflow actions and steps
        - Set execution limits and constraints

        Args:
          action: WorkflowAction defines the actions to be executed in a workflow.

          description:
              Description must be at most 500 characters:

              ```
              size(this) <= 500
              ```

          executor: Optional executor for the workflow. If not provided, defaults to the creator.
              Must be either the caller themselves or a service account.

          name:
              Name must be between 1 and 80 characters:

              ```
              size(this) >= 1 && size(this) <= 80
              ```

          report: WorkflowAction defines the actions to be executed in a workflow.

          triggers:
              Automation must have between 1 and 10 triggers:

              ```
              size(this) >= 1 && size(this) <= 10
              ```

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.WorkflowService/CreateWorkflow",
            body=await async_maybe_transform(
                {
                    "action": action,
                    "description": description,
                    "executor": executor,
                    "name": name,
                    "report": report,
                    "triggers": triggers,
                },
                automation_create_params.AutomationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutomationCreateResponse,
        )

    async def retrieve(
        self,
        *,
        workflow_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutomationRetrieveResponse:
        """
        Gets details about a specific workflow.

        Use this method to:

        - View workflow configuration
        - Check workflow status
        - Get workflow metadata

        ### Examples

        - Get workflow details:

          Retrieves information about a specific workflow.

          ```yaml
          workflowId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.WorkflowService/GetWorkflow",
            body=await async_maybe_transform(
                {"workflow_id": workflow_id}, automation_retrieve_params.AutomationRetrieveParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutomationRetrieveResponse,
        )

    async def update(
        self,
        *,
        action: Optional[WorkflowActionParam] | Omit = omit,
        description: Optional[str] | Omit = omit,
        disabled: Optional[bool] | Omit = omit,
        executor: Optional[Subject] | Omit = omit,
        name: Optional[str] | Omit = omit,
        report: Optional[WorkflowActionParam] | Omit = omit,
        triggers: Iterable[WorkflowTriggerParam] | Omit = omit,
        workflow_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutomationUpdateResponse:
        """
        Updates a workflow's configuration using full replacement semantics.

        Update Behavior:

        - All provided fields completely replace existing values
        - Optional fields that are not provided remain unchanged
        - Complex fields (triggers, action) are replaced entirely, not merged
        - To remove optional fields, explicitly set them to empty/default values

        Use this method to:

        - Modify workflow settings
        - Update triggers and actions
        - Change execution limits
        - Update workflow steps

        ### Examples

        - Update workflow name:

          Changes the workflow's display name.

          ```yaml
          workflowId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          name: "Updated Workflow Name"
          ```

        - Replace all triggers:

          Completely replaces the workflow's trigger configuration.

          ```yaml
          workflowId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          triggers:
            - manual: {}
              context:
                projects:
                  projectIds: ["new-project-id"]
          ```

        - Update execution limits:

          Completely replaces the workflow's action configuration.

          ```yaml
          workflowId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          action:
            limits:
              maxParallel: 10
              maxTotal: 100
            steps:
              - task:
                  command: "npm test"
          ```

        Args:
          action: WorkflowAction defines the actions to be executed in a workflow.

          description:
              Description must be at most 500 characters:

              ```
              size(this) <= 500
              ```

          disabled: When set, enables or disables the workflow. A disabled workflow will not be
              triggered by any automatic trigger and manual starts are rejected.

          name:
              Name must be between 1 and 80 characters:

              ```
              size(this) >= 1 && size(this) <= 80
              ```

          report: WorkflowAction defines the actions to be executed in a workflow.

          triggers:
              Automation can have at most 10 triggers:

              ```
              size(this) <= 10
              ```

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.WorkflowService/UpdateWorkflow",
            body=await async_maybe_transform(
                {
                    "action": action,
                    "description": description,
                    "disabled": disabled,
                    "executor": executor,
                    "name": name,
                    "report": report,
                    "triggers": triggers,
                    "workflow_id": workflow_id,
                },
                automation_update_params.AutomationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutomationUpdateResponse,
        )

    def list(
        self,
        *,
        token: str | Omit = omit,
        page_size: int | Omit = omit,
        filter: automation_list_params.Filter | Omit = omit,
        pagination: automation_list_params.Pagination | Omit = omit,
        sort: automation_list_params.Sort | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Workflow, AsyncWorkflowsPage[Workflow]]:
        """ListWorkflows

        Args:
          sort: sort specifies the order of results.

        When unspecified, results are sorted
              alphabetically by name ascending.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.WorkflowService/ListWorkflows",
            page=AsyncWorkflowsPage[Workflow],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                    "sort": sort,
                },
                automation_list_params.AutomationListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "token": token,
                        "page_size": page_size,
                    },
                    automation_list_params.AutomationListParams,
                ),
            ),
            model=Workflow,
            method="post",
        )

    async def delete(
        self,
        *,
        force: bool | Omit = omit,
        workflow_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Deletes a workflow permanently.

        Use this method to:

        - Remove unused workflows
        - Clean up test workflows
        - Delete obsolete configurations

        ### Examples

        - Delete workflow:

          Permanently removes a workflow.

          ```yaml
          workflowId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          ```

        Args:
          force: force indicates whether to immediately delete the workflow and all related
              resources. When true, performs cascading deletion of:

              - All workflow executions
              - All workflow execution actions
              - All environments created by workflow actions
              - All agent executions created by workflow actions
              - The workflow itself When false (default), marks workflow executions for
                deletion and relies on background reconciliation to clean up resources.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.WorkflowService/DeleteWorkflow",
            body=await async_maybe_transform(
                {
                    "force": force,
                    "workflow_id": workflow_id,
                },
                automation_delete_params.AutomationDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def cancel_execution(
        self,
        *,
        workflow_execution_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Cancels a running workflow execution.

        Use this method to:

        - Stop long-running executions
        - Cancel failed executions
        - Manage resource usage

        ### Examples

        - Cancel execution:

          Stops a running workflow execution.

          ```yaml
          workflowExecutionId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.WorkflowService/CancelWorkflowExecution",
            body=await async_maybe_transform(
                {"workflow_execution_id": workflow_execution_id},
                automation_cancel_execution_params.AutomationCancelExecutionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def cancel_execution_action(
        self,
        *,
        workflow_execution_action_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Cancels a running workflow execution action.

        Use this method to:

        - Stop long-running actions
        - Cancel failed actions
        - Manage resource usage

        ### Examples

        - Cancel execution action:

          Stops a running workflow execution action.

          ```yaml
          workflowExecutionActionId: "a1b2c3d4-5e6f-7890-abcd-ef1234567890"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.WorkflowService/CancelWorkflowExecutionAction",
            body=await async_maybe_transform(
                {"workflow_execution_action_id": workflow_execution_action_id},
                automation_cancel_execution_action_params.AutomationCancelExecutionActionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def list_execution_actions(
        self,
        *,
        token: str | Omit = omit,
        page_size: int | Omit = omit,
        filter: automation_list_execution_actions_params.Filter | Omit = omit,
        pagination: automation_list_execution_actions_params.Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[WorkflowExecutionAction, AsyncWorkflowExecutionActionsPage[WorkflowExecutionAction]]:
        """
        Lists workflow execution actions with optional filtering.

        Use this method to:

        - Monitor individual action execution status
        - Debug action failures
        - Track resource usage per action

        ### Examples

        - List execution actions for workflow execution:

          Shows all execution actions for a specific workflow execution.

          ```yaml
          filter:
            workflowExecutionIds: ["d2c94c27-3b76-4a42-b88c-95a85e392c68"]
          pagination:
            pageSize: 20
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.WorkflowService/ListWorkflowExecutionActions",
            page=AsyncWorkflowExecutionActionsPage[WorkflowExecutionAction],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                automation_list_execution_actions_params.AutomationListExecutionActionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "token": token,
                        "page_size": page_size,
                    },
                    automation_list_execution_actions_params.AutomationListExecutionActionsParams,
                ),
            ),
            model=WorkflowExecutionAction,
            method="post",
        )

    def list_execution_outputs(
        self,
        *,
        token: str | Omit = omit,
        page_size: int | Omit = omit,
        filter: automation_list_execution_outputs_params.Filter | Omit = omit,
        pagination: automation_list_execution_outputs_params.Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[
        AutomationListExecutionOutputsResponse, AsyncOutputsPage[AutomationListExecutionOutputsResponse]
    ]:
        """
        Lists outputs produced by workflow execution actions.

        Use this method to:

        - Retrieve test results, coverage metrics, or other structured data from
          executions
        - Aggregate outputs across multiple workflow executions
        - Build dashboards or reports from execution data

        ### Examples

        - List outputs for a workflow execution:

          Retrieves all outputs produced by actions in the specified execution.

          ```yaml
          filter:
            workflowExecutionIds: ["d2c94c27-3b76-4a42-b88c-95a85e392c68"]
          pagination:
            pageSize: 50
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.WorkflowService/ListWorkflowExecutionOutputs",
            page=AsyncOutputsPage[AutomationListExecutionOutputsResponse],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                automation_list_execution_outputs_params.AutomationListExecutionOutputsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "token": token,
                        "page_size": page_size,
                    },
                    automation_list_execution_outputs_params.AutomationListExecutionOutputsParams,
                ),
            ),
            model=AutomationListExecutionOutputsResponse,
            method="post",
        )

    def list_executions(
        self,
        *,
        token: str | Omit = omit,
        page_size: int | Omit = omit,
        filter: automation_list_executions_params.Filter | Omit = omit,
        pagination: automation_list_executions_params.Pagination | Omit = omit,
        sort: Sort | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[WorkflowExecution, AsyncWorkflowExecutionsPage[WorkflowExecution]]:
        """
        Lists workflow executions with optional filtering.

        Use this method to:

        - Monitor workflow execution history
        - Track execution status
        - Debug workflow issues

        ### Examples

        - List executions for workflow:

          Shows all executions for a specific workflow.

          ```yaml
          filter:
            workflowIds: ["b0e12f6c-4c67-429d-a4a6-d9838b5da047"]
          pagination:
            pageSize: 20
          ```

        Args:
          sort: sort specifies the order of results. When unspecified, results are sorted by
              operational priority (running first, then failed, then completed, then others).
              Supported sort fields: startedAt, finishedAt, createdAt.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.WorkflowService/ListWorkflowExecutions",
            page=AsyncWorkflowExecutionsPage[WorkflowExecution],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                    "sort": sort,
                },
                automation_list_executions_params.AutomationListExecutionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "token": token,
                        "page_size": page_size,
                    },
                    automation_list_executions_params.AutomationListExecutionsParams,
                ),
            ),
            model=WorkflowExecution,
            method="post",
        )

    async def retrieve_execution(
        self,
        *,
        workflow_execution_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutomationRetrieveExecutionResponse:
        """
        Gets details about a specific workflow execution.

        Use this method to:

        - Check execution status
        - View execution results
        - Monitor execution progress

        ### Examples

        - Get execution details:

          Retrieves information about a specific execution.

          ```yaml
          workflowExecutionId: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.WorkflowService/GetWorkflowExecution",
            body=await async_maybe_transform(
                {"workflow_execution_id": workflow_execution_id},
                automation_retrieve_execution_params.AutomationRetrieveExecutionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutomationRetrieveExecutionResponse,
        )

    async def retrieve_execution_action(
        self,
        *,
        workflow_execution_action_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutomationRetrieveExecutionActionResponse:
        """
        Gets details about a specific workflow execution action.

        Use this method to:

        - Check execution action status
        - View execution action results
        - Monitor execution action progress

        ### Examples

        - Get execution action details:

          Retrieves information about a specific execution action.

          ```yaml
          workflowExecutionActionId: "a1b2c3d4-5e6f-7890-abcd-ef1234567890"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.WorkflowService/GetWorkflowExecutionAction",
            body=await async_maybe_transform(
                {"workflow_execution_action_id": workflow_execution_action_id},
                automation_retrieve_execution_action_params.AutomationRetrieveExecutionActionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutomationRetrieveExecutionActionResponse,
        )

    async def start_execution(
        self,
        *,
        context_override: Optional[WorkflowTriggerContextParam] | Omit = omit,
        parameters: Dict[str, str] | Omit = omit,
        workflow_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AutomationStartExecutionResponse:
        """
        Starts a workflow execution.

        Use this method to:

        - Start workflow execution on demand
        - Test workflow configurations
        - Run workflows outside of automatic triggers

        ### Examples

        - Start workflow:

          Starts a workflow execution manually.

          ```yaml
          workflowId: "b0e12f6c-4c67-429d-a4a6-d9838b5da047"
          ```

        Args:
          context_override: Optional context override for the execution. When provided, replaces the
              workflow's default trigger context. User must have appropriate permissions on
              the overridden resources. Supports Projects, Repositories, and Agent context
              types. FromTrigger context type is not supported for manual overrides.

          parameters: Parameters to substitute into workflow steps using Go template syntax. Use
              {{ .Parameters.key_name }} in templatable fields (task.command, agent.prompt,
              pull*request.title/description/branch, trigger context agent.prompt). Keys must
              match pattern ^[a-zA-Z*][a-zA-Z0-9_]\\**$ Maximum 10 parameters allowed. Empty map
              is treated as no parameters provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.WorkflowService/StartWorkflow",
            body=await async_maybe_transform(
                {
                    "context_override": context_override,
                    "parameters": parameters,
                    "workflow_id": workflow_id,
                },
                automation_start_execution_params.AutomationStartExecutionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AutomationStartExecutionResponse,
        )


class AutomationsResourceWithRawResponse:
    def __init__(self, automations: AutomationsResource) -> None:
        self._automations = automations

        self.create = to_raw_response_wrapper(
            automations.create,
        )
        self.retrieve = to_raw_response_wrapper(
            automations.retrieve,
        )
        self.update = to_raw_response_wrapper(
            automations.update,
        )
        self.list = to_raw_response_wrapper(
            automations.list,
        )
        self.delete = to_raw_response_wrapper(
            automations.delete,
        )
        self.cancel_execution = to_raw_response_wrapper(
            automations.cancel_execution,
        )
        self.cancel_execution_action = to_raw_response_wrapper(
            automations.cancel_execution_action,
        )
        self.list_execution_actions = to_raw_response_wrapper(
            automations.list_execution_actions,
        )
        self.list_execution_outputs = to_raw_response_wrapper(
            automations.list_execution_outputs,
        )
        self.list_executions = to_raw_response_wrapper(
            automations.list_executions,
        )
        self.retrieve_execution = to_raw_response_wrapper(
            automations.retrieve_execution,
        )
        self.retrieve_execution_action = to_raw_response_wrapper(
            automations.retrieve_execution_action,
        )
        self.start_execution = to_raw_response_wrapper(
            automations.start_execution,
        )


class AsyncAutomationsResourceWithRawResponse:
    def __init__(self, automations: AsyncAutomationsResource) -> None:
        self._automations = automations

        self.create = async_to_raw_response_wrapper(
            automations.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            automations.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            automations.update,
        )
        self.list = async_to_raw_response_wrapper(
            automations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            automations.delete,
        )
        self.cancel_execution = async_to_raw_response_wrapper(
            automations.cancel_execution,
        )
        self.cancel_execution_action = async_to_raw_response_wrapper(
            automations.cancel_execution_action,
        )
        self.list_execution_actions = async_to_raw_response_wrapper(
            automations.list_execution_actions,
        )
        self.list_execution_outputs = async_to_raw_response_wrapper(
            automations.list_execution_outputs,
        )
        self.list_executions = async_to_raw_response_wrapper(
            automations.list_executions,
        )
        self.retrieve_execution = async_to_raw_response_wrapper(
            automations.retrieve_execution,
        )
        self.retrieve_execution_action = async_to_raw_response_wrapper(
            automations.retrieve_execution_action,
        )
        self.start_execution = async_to_raw_response_wrapper(
            automations.start_execution,
        )


class AutomationsResourceWithStreamingResponse:
    def __init__(self, automations: AutomationsResource) -> None:
        self._automations = automations

        self.create = to_streamed_response_wrapper(
            automations.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            automations.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            automations.update,
        )
        self.list = to_streamed_response_wrapper(
            automations.list,
        )
        self.delete = to_streamed_response_wrapper(
            automations.delete,
        )
        self.cancel_execution = to_streamed_response_wrapper(
            automations.cancel_execution,
        )
        self.cancel_execution_action = to_streamed_response_wrapper(
            automations.cancel_execution_action,
        )
        self.list_execution_actions = to_streamed_response_wrapper(
            automations.list_execution_actions,
        )
        self.list_execution_outputs = to_streamed_response_wrapper(
            automations.list_execution_outputs,
        )
        self.list_executions = to_streamed_response_wrapper(
            automations.list_executions,
        )
        self.retrieve_execution = to_streamed_response_wrapper(
            automations.retrieve_execution,
        )
        self.retrieve_execution_action = to_streamed_response_wrapper(
            automations.retrieve_execution_action,
        )
        self.start_execution = to_streamed_response_wrapper(
            automations.start_execution,
        )


class AsyncAutomationsResourceWithStreamingResponse:
    def __init__(self, automations: AsyncAutomationsResource) -> None:
        self._automations = automations

        self.create = async_to_streamed_response_wrapper(
            automations.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            automations.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            automations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            automations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            automations.delete,
        )
        self.cancel_execution = async_to_streamed_response_wrapper(
            automations.cancel_execution,
        )
        self.cancel_execution_action = async_to_streamed_response_wrapper(
            automations.cancel_execution_action,
        )
        self.list_execution_actions = async_to_streamed_response_wrapper(
            automations.list_execution_actions,
        )
        self.list_execution_outputs = async_to_streamed_response_wrapper(
            automations.list_execution_outputs,
        )
        self.list_executions = async_to_streamed_response_wrapper(
            automations.list_executions,
        )
        self.retrieve_execution = async_to_streamed_response_wrapper(
            automations.retrieve_execution,
        )
        self.retrieve_execution_action = async_to_streamed_response_wrapper(
            automations.retrieve_execution_action,
        )
        self.start_execution = async_to_streamed_response_wrapper(
            automations.start_execution,
        )
