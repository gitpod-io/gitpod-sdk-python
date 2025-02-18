# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .executions import (
    ExecutionsResource,
    AsyncExecutionsResource,
    ExecutionsResourceWithRawResponse,
    AsyncExecutionsResourceWithRawResponse,
    ExecutionsResourceWithStreamingResponse,
    AsyncExecutionsResourceWithStreamingResponse,
)
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .....pagination import SyncTasksPage, AsyncTasksPage
from ....._base_client import AsyncPaginator, make_request_options
from .....types.shared.task import Task
from .....types.shared_params.task_spec import TaskSpec
from .....types.environments.automations import (
    task_list_params,
    task_start_params,
    task_create_params,
    task_delete_params,
    task_update_params,
    task_retrieve_params,
)
from .....types.shared_params.task_metadata import TaskMetadata
from .....types.environments.automations.task_start_response import TaskStartResponse
from .....types.environments.automations.task_create_response import TaskCreateResponse
from .....types.environments.automations.task_retrieve_response import TaskRetrieveResponse

__all__ = ["TasksResource", "AsyncTasksResource"]


class TasksResource(SyncAPIResource):
    @cached_property
    def executions(self) -> ExecutionsResource:
        return ExecutionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> TasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return TasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return TasksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        depends_on: List[str] | NotGiven = NOT_GIVEN,
        environment_id: str | NotGiven = NOT_GIVEN,
        metadata: TaskMetadata | NotGiven = NOT_GIVEN,
        spec: TaskSpec | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskCreateResponse:
        """
        Creates a new automation task.

        Use this method to:

        - Define one-off or scheduled tasks
        - Set up build or test automation
        - Configure task dependencies
        - Specify execution environments

        ### Examples

        - Create basic task:

          Creates a simple build task.

          ```yaml
          environmentId: "07e03a28-65a5-4d98-b532-8ea67b188048"
          metadata:
            reference: "build"
            name: "Build Project"
            description: "Builds the project artifacts"
            triggeredBy:
              - postEnvironmentStart: true
          spec:
            command: "npm run build"
          ```

        - Create task with dependencies:

          Creates a task that depends on other services.

          ```yaml
          environmentId: "07e03a28-65a5-4d98-b532-8ea67b188048"
          metadata:
            reference: "test"
            name: "Run Tests"
            description: "Runs the test suite"
          spec:
            command: "npm test"
          dependsOn: ["d2c94c27-3b76-4a42-b88c-95a85e392c68"]
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.EnvironmentAutomationService/CreateTask",
            body=maybe_transform(
                {
                    "depends_on": depends_on,
                    "environment_id": environment_id,
                    "metadata": metadata,
                    "spec": spec,
                },
                task_create_params.TaskCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskCreateResponse,
        )

    def retrieve(
        self,
        *,
        id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskRetrieveResponse:
        """
        Gets details about a specific automation task.

        Use this method to:

        - Check task configuration
        - View task dependencies
        - Monitor task status

        ### Examples

        - Get task details:

          Retrieves information about a specific task.

          ```yaml
          id: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.EnvironmentAutomationService/GetTask",
            body=maybe_transform({"id": id}, task_retrieve_params.TaskRetrieveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskRetrieveResponse,
        )

    def update(
        self,
        *,
        id: str | NotGiven = NOT_GIVEN,
        depends_on: List[str] | NotGiven = NOT_GIVEN,
        metadata: task_update_params.Metadata | NotGiven = NOT_GIVEN,
        spec: task_update_params.Spec | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Updates an automation task configuration.

        Use this method to:

        - Modify task commands
        - Update task triggers
        - Change dependencies
        - Adjust execution settings

        ### Examples

        - Update command:

          Changes the task's command.

          ```yaml
          id: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          spec:
            command: "npm run test:coverage"
          ```

        - Update triggers:

          Modifies when the task runs.

          ```yaml
          id: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          metadata:
            triggeredBy:
              trigger:
                - postEnvironmentStart: true
          ```

        Args:
          depends_on: dependencies specifies the IDs of the automations this task depends on.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.EnvironmentAutomationService/UpdateTask",
            body=maybe_transform(
                {
                    "id": id,
                    "depends_on": depends_on,
                    "metadata": metadata,
                    "spec": spec,
                },
                task_update_params.TaskUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def list(
        self,
        *,
        token: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        filter: task_list_params.Filter | NotGiven = NOT_GIVEN,
        pagination: task_list_params.Pagination | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncTasksPage[Task]:
        """
        Lists automation tasks with optional filtering.

        Use this method to:

        - View all tasks in an environment
        - Filter tasks by reference
        - Monitor task status

        ### Examples

        - List environment tasks:

          Shows all tasks for an environment.

          ```yaml
          filter:
            environmentIds: ["07e03a28-65a5-4d98-b532-8ea67b188048"]
          pagination:
            pageSize: 20
          ```

        - Filter by reference:

          Lists tasks matching specific references.

          ```yaml
          filter:
            references: ["build", "test"]
          pagination:
            pageSize: 20
          ```

        Args:
          filter: filter contains the filter options for listing tasks

          pagination: pagination contains the pagination options for listing tasks

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.EnvironmentAutomationService/ListTasks",
            page=SyncTasksPage[Task],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                task_list_params.TaskListParams,
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
                    task_list_params.TaskListParams,
                ),
            ),
            model=Task,
            method="post",
        )

    def delete(
        self,
        *,
        id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Deletes an automation task.

        Use this method to:

        - Remove unused tasks
        - Clean up task configurations
        - Delete obsolete automations

        ### Examples

        - Delete task:

          Removes a task and its configuration.

          ```yaml
          id: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.EnvironmentAutomationService/DeleteTask",
            body=maybe_transform({"id": id}, task_delete_params.TaskDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def start(
        self,
        *,
        id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskStartResponse:
        """Starts a task by creating a new task execution.

        This call does not block until
        the task is started; the task will be started asynchronously.

        Use this method to:

        - Trigger task execution
        - Run one-off tasks
        - Start scheduled tasks immediately

        ### Examples

        - Start task:

          Creates a new execution of a task.

          ```yaml
          id: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.EnvironmentAutomationService/StartTask",
            body=maybe_transform({"id": id}, task_start_params.TaskStartParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskStartResponse,
        )


class AsyncTasksResource(AsyncAPIResource):
    @cached_property
    def executions(self) -> AsyncExecutionsResource:
        return AsyncExecutionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return AsyncTasksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        depends_on: List[str] | NotGiven = NOT_GIVEN,
        environment_id: str | NotGiven = NOT_GIVEN,
        metadata: TaskMetadata | NotGiven = NOT_GIVEN,
        spec: TaskSpec | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskCreateResponse:
        """
        Creates a new automation task.

        Use this method to:

        - Define one-off or scheduled tasks
        - Set up build or test automation
        - Configure task dependencies
        - Specify execution environments

        ### Examples

        - Create basic task:

          Creates a simple build task.

          ```yaml
          environmentId: "07e03a28-65a5-4d98-b532-8ea67b188048"
          metadata:
            reference: "build"
            name: "Build Project"
            description: "Builds the project artifacts"
            triggeredBy:
              - postEnvironmentStart: true
          spec:
            command: "npm run build"
          ```

        - Create task with dependencies:

          Creates a task that depends on other services.

          ```yaml
          environmentId: "07e03a28-65a5-4d98-b532-8ea67b188048"
          metadata:
            reference: "test"
            name: "Run Tests"
            description: "Runs the test suite"
          spec:
            command: "npm test"
          dependsOn: ["d2c94c27-3b76-4a42-b88c-95a85e392c68"]
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.EnvironmentAutomationService/CreateTask",
            body=await async_maybe_transform(
                {
                    "depends_on": depends_on,
                    "environment_id": environment_id,
                    "metadata": metadata,
                    "spec": spec,
                },
                task_create_params.TaskCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskCreateResponse,
        )

    async def retrieve(
        self,
        *,
        id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskRetrieveResponse:
        """
        Gets details about a specific automation task.

        Use this method to:

        - Check task configuration
        - View task dependencies
        - Monitor task status

        ### Examples

        - Get task details:

          Retrieves information about a specific task.

          ```yaml
          id: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.EnvironmentAutomationService/GetTask",
            body=await async_maybe_transform({"id": id}, task_retrieve_params.TaskRetrieveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskRetrieveResponse,
        )

    async def update(
        self,
        *,
        id: str | NotGiven = NOT_GIVEN,
        depends_on: List[str] | NotGiven = NOT_GIVEN,
        metadata: task_update_params.Metadata | NotGiven = NOT_GIVEN,
        spec: task_update_params.Spec | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Updates an automation task configuration.

        Use this method to:

        - Modify task commands
        - Update task triggers
        - Change dependencies
        - Adjust execution settings

        ### Examples

        - Update command:

          Changes the task's command.

          ```yaml
          id: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          spec:
            command: "npm run test:coverage"
          ```

        - Update triggers:

          Modifies when the task runs.

          ```yaml
          id: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          metadata:
            triggeredBy:
              trigger:
                - postEnvironmentStart: true
          ```

        Args:
          depends_on: dependencies specifies the IDs of the automations this task depends on.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.EnvironmentAutomationService/UpdateTask",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "depends_on": depends_on,
                    "metadata": metadata,
                    "spec": spec,
                },
                task_update_params.TaskUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def list(
        self,
        *,
        token: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        filter: task_list_params.Filter | NotGiven = NOT_GIVEN,
        pagination: task_list_params.Pagination | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Task, AsyncTasksPage[Task]]:
        """
        Lists automation tasks with optional filtering.

        Use this method to:

        - View all tasks in an environment
        - Filter tasks by reference
        - Monitor task status

        ### Examples

        - List environment tasks:

          Shows all tasks for an environment.

          ```yaml
          filter:
            environmentIds: ["07e03a28-65a5-4d98-b532-8ea67b188048"]
          pagination:
            pageSize: 20
          ```

        - Filter by reference:

          Lists tasks matching specific references.

          ```yaml
          filter:
            references: ["build", "test"]
          pagination:
            pageSize: 20
          ```

        Args:
          filter: filter contains the filter options for listing tasks

          pagination: pagination contains the pagination options for listing tasks

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.EnvironmentAutomationService/ListTasks",
            page=AsyncTasksPage[Task],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                task_list_params.TaskListParams,
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
                    task_list_params.TaskListParams,
                ),
            ),
            model=Task,
            method="post",
        )

    async def delete(
        self,
        *,
        id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Deletes an automation task.

        Use this method to:

        - Remove unused tasks
        - Clean up task configurations
        - Delete obsolete automations

        ### Examples

        - Delete task:

          Removes a task and its configuration.

          ```yaml
          id: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.EnvironmentAutomationService/DeleteTask",
            body=await async_maybe_transform({"id": id}, task_delete_params.TaskDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def start(
        self,
        *,
        id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TaskStartResponse:
        """Starts a task by creating a new task execution.

        This call does not block until
        the task is started; the task will be started asynchronously.

        Use this method to:

        - Trigger task execution
        - Run one-off tasks
        - Start scheduled tasks immediately

        ### Examples

        - Start task:

          Creates a new execution of a task.

          ```yaml
          id: "d2c94c27-3b76-4a42-b88c-95a85e392c68"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.EnvironmentAutomationService/StartTask",
            body=await async_maybe_transform({"id": id}, task_start_params.TaskStartParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TaskStartResponse,
        )


class TasksResourceWithRawResponse:
    def __init__(self, tasks: TasksResource) -> None:
        self._tasks = tasks

        self.create = to_raw_response_wrapper(
            tasks.create,
        )
        self.retrieve = to_raw_response_wrapper(
            tasks.retrieve,
        )
        self.update = to_raw_response_wrapper(
            tasks.update,
        )
        self.list = to_raw_response_wrapper(
            tasks.list,
        )
        self.delete = to_raw_response_wrapper(
            tasks.delete,
        )
        self.start = to_raw_response_wrapper(
            tasks.start,
        )

    @cached_property
    def executions(self) -> ExecutionsResourceWithRawResponse:
        return ExecutionsResourceWithRawResponse(self._tasks.executions)


class AsyncTasksResourceWithRawResponse:
    def __init__(self, tasks: AsyncTasksResource) -> None:
        self._tasks = tasks

        self.create = async_to_raw_response_wrapper(
            tasks.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            tasks.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            tasks.update,
        )
        self.list = async_to_raw_response_wrapper(
            tasks.list,
        )
        self.delete = async_to_raw_response_wrapper(
            tasks.delete,
        )
        self.start = async_to_raw_response_wrapper(
            tasks.start,
        )

    @cached_property
    def executions(self) -> AsyncExecutionsResourceWithRawResponse:
        return AsyncExecutionsResourceWithRawResponse(self._tasks.executions)


class TasksResourceWithStreamingResponse:
    def __init__(self, tasks: TasksResource) -> None:
        self._tasks = tasks

        self.create = to_streamed_response_wrapper(
            tasks.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            tasks.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            tasks.update,
        )
        self.list = to_streamed_response_wrapper(
            tasks.list,
        )
        self.delete = to_streamed_response_wrapper(
            tasks.delete,
        )
        self.start = to_streamed_response_wrapper(
            tasks.start,
        )

    @cached_property
    def executions(self) -> ExecutionsResourceWithStreamingResponse:
        return ExecutionsResourceWithStreamingResponse(self._tasks.executions)


class AsyncTasksResourceWithStreamingResponse:
    def __init__(self, tasks: AsyncTasksResource) -> None:
        self._tasks = tasks

        self.create = async_to_streamed_response_wrapper(
            tasks.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            tasks.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            tasks.update,
        )
        self.list = async_to_streamed_response_wrapper(
            tasks.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            tasks.delete,
        )
        self.start = async_to_streamed_response_wrapper(
            tasks.start,
        )

    @cached_property
    def executions(self) -> AsyncExecutionsResourceWithStreamingResponse:
        return AsyncExecutionsResourceWithStreamingResponse(self._tasks.executions)
