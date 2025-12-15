# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import (
    AgentMode,
    agent_list_prompts_params,
    agent_create_prompt_params,
    agent_delete_prompt_params,
    agent_update_prompt_params,
    agent_stop_execution_params,
    agent_list_executions_params,
    agent_retrieve_prompt_params,
    agent_start_execution_params,
    agent_delete_execution_params,
    agent_send_to_execution_params,
    agent_retrieve_execution_params,
    agent_create_execution_conversation_token_params,
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
from ..pagination import SyncPromptsPage, AsyncPromptsPage, SyncAgentExecutionsPage, AsyncAgentExecutionsPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.prompt import Prompt
from ..types.agent_mode import AgentMode
from ..types.agent_execution import AgentExecution
from ..types.user_input_block_param import UserInputBlockParam
from ..types.agent_code_context_param import AgentCodeContextParam
from ..types.agent_create_prompt_response import AgentCreatePromptResponse
from ..types.agent_update_prompt_response import AgentUpdatePromptResponse
from ..types.agent_retrieve_prompt_response import AgentRetrievePromptResponse
from ..types.agent_start_execution_response import AgentStartExecutionResponse
from ..types.agent_retrieve_execution_response import AgentRetrieveExecutionResponse
from ..types.agent_create_execution_conversation_token_response import AgentCreateExecutionConversationTokenResponse

__all__ = ["AgentsResource", "AsyncAgentsResource"]


class AgentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return AgentsResourceWithStreamingResponse(self)

    def create_execution_conversation_token(
        self,
        *,
        agent_execution_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentCreateExecutionConversationTokenResponse:
        """
        Creates a token for conversation access with a specific agent run.

        This method generates a temporary token that can be used to securely connect to
        an ongoing agent conversation, for example in a web UI.

        ### Examples

        - Create a token to join an agent run conversation in a front-end application:

          ```yaml
          agentExecutionId: "6fa1a3c7-fbb7-49d1-ba56-1890dc7c4c35"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.AgentService/CreateAgentExecutionConversationToken",
            body=maybe_transform(
                {"agent_execution_id": agent_execution_id},
                agent_create_execution_conversation_token_params.AgentCreateExecutionConversationTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentCreateExecutionConversationTokenResponse,
        )

    def create_prompt(
        self,
        *,
        command: str | Omit = omit,
        description: str | Omit = omit,
        is_command: bool | Omit = omit,
        is_template: bool | Omit = omit,
        name: str | Omit = omit,
        prompt: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentCreatePromptResponse:
        """
        Creates a new prompt.

        Use this method to:

        - Define new prompts for templates or commands
        - Set up organization-wide prompt libraries

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.AgentService/CreatePrompt",
            body=maybe_transform(
                {
                    "command": command,
                    "description": description,
                    "is_command": is_command,
                    "is_template": is_template,
                    "name": name,
                    "prompt": prompt,
                },
                agent_create_prompt_params.AgentCreatePromptParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentCreatePromptResponse,
        )

    def delete_execution(
        self,
        *,
        agent_execution_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Deletes an agent run.

        Use this method to:

        - Clean up agent runs that are no longer needed

        ### Examples

        - Delete an agent run by ID:

          ```yaml
          agentExecutionId: "6fa1a3c7-fbb7-49d1-ba56-1890dc7c4c35"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.AgentService/DeleteAgentExecution",
            body=maybe_transform(
                {"agent_execution_id": agent_execution_id}, agent_delete_execution_params.AgentDeleteExecutionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def delete_prompt(
        self,
        *,
        prompt_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Deletes a prompt.

        Use this method to:

        - Remove unused prompts

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.AgentService/DeletePrompt",
            body=maybe_transform({"prompt_id": prompt_id}, agent_delete_prompt_params.AgentDeletePromptParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def list_executions(
        self,
        *,
        token: str | Omit = omit,
        page_size: int | Omit = omit,
        filter: agent_list_executions_params.Filter | Omit = omit,
        pagination: agent_list_executions_params.Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncAgentExecutionsPage[AgentExecution]:
        """
        Lists all agent runs matching the specified filter.

        Use this method to track multiple agent runs and their associated resources.
        Results are ordered by their creation time with the newest first.

        ### Examples

        - List agent runs by agent ID:

          ```yaml
          filter:
            agentIds: ["b8a64cfa-43e2-4b9d-9fb3-07edc63f5971"]
          pagination:
            pageSize: 10
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.AgentService/ListAgentExecutions",
            page=SyncAgentExecutionsPage[AgentExecution],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                agent_list_executions_params.AgentListExecutionsParams,
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
                    agent_list_executions_params.AgentListExecutionsParams,
                ),
            ),
            model=AgentExecution,
            method="post",
        )

    def list_prompts(
        self,
        *,
        token: str | Omit = omit,
        page_size: int | Omit = omit,
        filter: agent_list_prompts_params.Filter | Omit = omit,
        pagination: agent_list_prompts_params.Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPromptsPage[Prompt]:
        """
        Lists all prompts matching the specified criteria.

        Use this method to find and browse prompts across your organization. Results are
        ordered by their creation time with the newest first.

        ### Examples

        - List all prompts:

          Retrieves all prompts with pagination.

          ```yaml
          pagination:
            pageSize: 10
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.AgentService/ListPrompts",
            page=SyncPromptsPage[Prompt],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                agent_list_prompts_params.AgentListPromptsParams,
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
                    agent_list_prompts_params.AgentListPromptsParams,
                ),
            ),
            model=Prompt,
            method="post",
        )

    def retrieve_execution(
        self,
        *,
        agent_execution_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentRetrieveExecutionResponse:
        """
        Gets details about a specific agent run, including its metadata, specification,
        and status (phase, error messages, and usage statistics).

        Use this method to:

        - Monitor the run's progress
        - Retrieve the agent's conversation URL
        - Check if an agent run is actively producing output

        ### Examples

        - Get agent run details by ID:

          ```yaml
          agentExecutionId: "6fa1a3c7-fbb7-49d1-ba56-1890dc7c4c35"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.AgentService/GetAgentExecution",
            body=maybe_transform(
                {"agent_execution_id": agent_execution_id}, agent_retrieve_execution_params.AgentRetrieveExecutionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRetrieveExecutionResponse,
        )

    def retrieve_prompt(
        self,
        *,
        prompt_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentRetrievePromptResponse:
        """
        Gets details about a specific prompt including name, description, and prompt
        content.

        Use this method to:

        - Retrieve prompt details for editing
        - Get prompt content for execution

        ### Examples

        - Get prompt details:

          ```yaml
          promptId: "07e03a28-65a5-4d98-b532-8ea67b188048"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.AgentService/GetPrompt",
            body=maybe_transform({"prompt_id": prompt_id}, agent_retrieve_prompt_params.AgentRetrievePromptParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRetrievePromptResponse,
        )

    def send_to_execution(
        self,
        *,
        agent_execution_id: str | Omit = omit,
        user_input: UserInputBlockParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Sends user input to an active agent run.

        This method is used to provide interactive or conversation-based input to an
        agent. The agent can respond with output blocks containing text, file changes,
        or tool usage requests.

        ### Examples

        - Send a text message to an agent:

          ```yaml
          agentExecutionId: "6fa1a3c7-fbb7-49d1-ba56-1890dc7c4c35"
          userInput:
            text:
              content: "Generate a report based on the latest logs."
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.AgentService/SendToAgentExecution",
            body=maybe_transform(
                {
                    "agent_execution_id": agent_execution_id,
                    "user_input": user_input,
                },
                agent_send_to_execution_params.AgentSendToExecutionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def start_execution(
        self,
        *,
        agent_id: str | Omit = omit,
        code_context: AgentCodeContextParam | Omit = omit,
        mode: AgentMode | Omit = omit,
        name: str | Omit = omit,
        workflow_action_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentStartExecutionResponse:
        """
        Starts (or triggers) an agent run using a provided agent.

        Use this method to:

        - Launch an agent based on a known agent

        ### Examples

        - Start an agent with a project ID:

          ```yaml
          agentId: "b8a64cfa-43e2-4b9d-9fb3-07edc63f5971"
          codeContext:
            projectId: "2d22e4eb-31da-467f-882c-27e21550992f"
          ```

        Args:
          mode: mode specifies the operational mode for this agent execution If not specified,
              defaults to AGENT_MODE_EXECUTION

          workflow_action_id: workflow_action_id is an optional reference to the workflow execution action
              that created this agent execution. Used for tracking and event correlation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.AgentService/StartAgent",
            body=maybe_transform(
                {
                    "agent_id": agent_id,
                    "code_context": code_context,
                    "mode": mode,
                    "name": name,
                    "workflow_action_id": workflow_action_id,
                },
                agent_start_execution_params.AgentStartExecutionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentStartExecutionResponse,
        )

    def stop_execution(
        self,
        *,
        agent_execution_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Stops an active agent execution.

        Use this method to:

        - Stop an agent that is currently running
        - Prevent further processing or resource usage

        ### Examples

        - Stop an agent execution by ID:

          ```yaml
          agentExecutionId: "6fa1a3c7-fbb7-49d1-ba56-1890dc7c4c35"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.AgentService/StopAgentExecution",
            body=maybe_transform(
                {"agent_execution_id": agent_execution_id}, agent_stop_execution_params.AgentStopExecutionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def update_prompt(
        self,
        *,
        metadata: Optional[agent_update_prompt_params.Metadata] | Omit = omit,
        prompt_id: str | Omit = omit,
        spec: Optional[agent_update_prompt_params.Spec] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentUpdatePromptResponse:
        """
        Updates an existing prompt.

        Use this method to:

        - Modify prompt content or metadata
        - Change prompt type (template/command)

        Args:
          metadata: Metadata updates

          prompt_id: The ID of the prompt to update

          spec: Spec updates

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/gitpod.v1.AgentService/UpdatePrompt",
            body=maybe_transform(
                {
                    "metadata": metadata,
                    "prompt_id": prompt_id,
                    "spec": spec,
                },
                agent_update_prompt_params.AgentUpdatePromptParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentUpdatePromptResponse,
        )


class AsyncAgentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/gitpod-io/gitpod-sdk-python#with_streaming_response
        """
        return AsyncAgentsResourceWithStreamingResponse(self)

    async def create_execution_conversation_token(
        self,
        *,
        agent_execution_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentCreateExecutionConversationTokenResponse:
        """
        Creates a token for conversation access with a specific agent run.

        This method generates a temporary token that can be used to securely connect to
        an ongoing agent conversation, for example in a web UI.

        ### Examples

        - Create a token to join an agent run conversation in a front-end application:

          ```yaml
          agentExecutionId: "6fa1a3c7-fbb7-49d1-ba56-1890dc7c4c35"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.AgentService/CreateAgentExecutionConversationToken",
            body=await async_maybe_transform(
                {"agent_execution_id": agent_execution_id},
                agent_create_execution_conversation_token_params.AgentCreateExecutionConversationTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentCreateExecutionConversationTokenResponse,
        )

    async def create_prompt(
        self,
        *,
        command: str | Omit = omit,
        description: str | Omit = omit,
        is_command: bool | Omit = omit,
        is_template: bool | Omit = omit,
        name: str | Omit = omit,
        prompt: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentCreatePromptResponse:
        """
        Creates a new prompt.

        Use this method to:

        - Define new prompts for templates or commands
        - Set up organization-wide prompt libraries

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.AgentService/CreatePrompt",
            body=await async_maybe_transform(
                {
                    "command": command,
                    "description": description,
                    "is_command": is_command,
                    "is_template": is_template,
                    "name": name,
                    "prompt": prompt,
                },
                agent_create_prompt_params.AgentCreatePromptParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentCreatePromptResponse,
        )

    async def delete_execution(
        self,
        *,
        agent_execution_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Deletes an agent run.

        Use this method to:

        - Clean up agent runs that are no longer needed

        ### Examples

        - Delete an agent run by ID:

          ```yaml
          agentExecutionId: "6fa1a3c7-fbb7-49d1-ba56-1890dc7c4c35"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.AgentService/DeleteAgentExecution",
            body=await async_maybe_transform(
                {"agent_execution_id": agent_execution_id}, agent_delete_execution_params.AgentDeleteExecutionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def delete_prompt(
        self,
        *,
        prompt_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Deletes a prompt.

        Use this method to:

        - Remove unused prompts

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.AgentService/DeletePrompt",
            body=await async_maybe_transform(
                {"prompt_id": prompt_id}, agent_delete_prompt_params.AgentDeletePromptParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def list_executions(
        self,
        *,
        token: str | Omit = omit,
        page_size: int | Omit = omit,
        filter: agent_list_executions_params.Filter | Omit = omit,
        pagination: agent_list_executions_params.Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AgentExecution, AsyncAgentExecutionsPage[AgentExecution]]:
        """
        Lists all agent runs matching the specified filter.

        Use this method to track multiple agent runs and their associated resources.
        Results are ordered by their creation time with the newest first.

        ### Examples

        - List agent runs by agent ID:

          ```yaml
          filter:
            agentIds: ["b8a64cfa-43e2-4b9d-9fb3-07edc63f5971"]
          pagination:
            pageSize: 10
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.AgentService/ListAgentExecutions",
            page=AsyncAgentExecutionsPage[AgentExecution],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                agent_list_executions_params.AgentListExecutionsParams,
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
                    agent_list_executions_params.AgentListExecutionsParams,
                ),
            ),
            model=AgentExecution,
            method="post",
        )

    def list_prompts(
        self,
        *,
        token: str | Omit = omit,
        page_size: int | Omit = omit,
        filter: agent_list_prompts_params.Filter | Omit = omit,
        pagination: agent_list_prompts_params.Pagination | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Prompt, AsyncPromptsPage[Prompt]]:
        """
        Lists all prompts matching the specified criteria.

        Use this method to find and browse prompts across your organization. Results are
        ordered by their creation time with the newest first.

        ### Examples

        - List all prompts:

          Retrieves all prompts with pagination.

          ```yaml
          pagination:
            pageSize: 10
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/gitpod.v1.AgentService/ListPrompts",
            page=AsyncPromptsPage[Prompt],
            body=maybe_transform(
                {
                    "filter": filter,
                    "pagination": pagination,
                },
                agent_list_prompts_params.AgentListPromptsParams,
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
                    agent_list_prompts_params.AgentListPromptsParams,
                ),
            ),
            model=Prompt,
            method="post",
        )

    async def retrieve_execution(
        self,
        *,
        agent_execution_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentRetrieveExecutionResponse:
        """
        Gets details about a specific agent run, including its metadata, specification,
        and status (phase, error messages, and usage statistics).

        Use this method to:

        - Monitor the run's progress
        - Retrieve the agent's conversation URL
        - Check if an agent run is actively producing output

        ### Examples

        - Get agent run details by ID:

          ```yaml
          agentExecutionId: "6fa1a3c7-fbb7-49d1-ba56-1890dc7c4c35"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.AgentService/GetAgentExecution",
            body=await async_maybe_transform(
                {"agent_execution_id": agent_execution_id}, agent_retrieve_execution_params.AgentRetrieveExecutionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRetrieveExecutionResponse,
        )

    async def retrieve_prompt(
        self,
        *,
        prompt_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentRetrievePromptResponse:
        """
        Gets details about a specific prompt including name, description, and prompt
        content.

        Use this method to:

        - Retrieve prompt details for editing
        - Get prompt content for execution

        ### Examples

        - Get prompt details:

          ```yaml
          promptId: "07e03a28-65a5-4d98-b532-8ea67b188048"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.AgentService/GetPrompt",
            body=await async_maybe_transform(
                {"prompt_id": prompt_id}, agent_retrieve_prompt_params.AgentRetrievePromptParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRetrievePromptResponse,
        )

    async def send_to_execution(
        self,
        *,
        agent_execution_id: str | Omit = omit,
        user_input: UserInputBlockParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Sends user input to an active agent run.

        This method is used to provide interactive or conversation-based input to an
        agent. The agent can respond with output blocks containing text, file changes,
        or tool usage requests.

        ### Examples

        - Send a text message to an agent:

          ```yaml
          agentExecutionId: "6fa1a3c7-fbb7-49d1-ba56-1890dc7c4c35"
          userInput:
            text:
              content: "Generate a report based on the latest logs."
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.AgentService/SendToAgentExecution",
            body=await async_maybe_transform(
                {
                    "agent_execution_id": agent_execution_id,
                    "user_input": user_input,
                },
                agent_send_to_execution_params.AgentSendToExecutionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def start_execution(
        self,
        *,
        agent_id: str | Omit = omit,
        code_context: AgentCodeContextParam | Omit = omit,
        mode: AgentMode | Omit = omit,
        name: str | Omit = omit,
        workflow_action_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentStartExecutionResponse:
        """
        Starts (or triggers) an agent run using a provided agent.

        Use this method to:

        - Launch an agent based on a known agent

        ### Examples

        - Start an agent with a project ID:

          ```yaml
          agentId: "b8a64cfa-43e2-4b9d-9fb3-07edc63f5971"
          codeContext:
            projectId: "2d22e4eb-31da-467f-882c-27e21550992f"
          ```

        Args:
          mode: mode specifies the operational mode for this agent execution If not specified,
              defaults to AGENT_MODE_EXECUTION

          workflow_action_id: workflow_action_id is an optional reference to the workflow execution action
              that created this agent execution. Used for tracking and event correlation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.AgentService/StartAgent",
            body=await async_maybe_transform(
                {
                    "agent_id": agent_id,
                    "code_context": code_context,
                    "mode": mode,
                    "name": name,
                    "workflow_action_id": workflow_action_id,
                },
                agent_start_execution_params.AgentStartExecutionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentStartExecutionResponse,
        )

    async def stop_execution(
        self,
        *,
        agent_execution_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Stops an active agent execution.

        Use this method to:

        - Stop an agent that is currently running
        - Prevent further processing or resource usage

        ### Examples

        - Stop an agent execution by ID:

          ```yaml
          agentExecutionId: "6fa1a3c7-fbb7-49d1-ba56-1890dc7c4c35"
          ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.AgentService/StopAgentExecution",
            body=await async_maybe_transform(
                {"agent_execution_id": agent_execution_id}, agent_stop_execution_params.AgentStopExecutionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def update_prompt(
        self,
        *,
        metadata: Optional[agent_update_prompt_params.Metadata] | Omit = omit,
        prompt_id: str | Omit = omit,
        spec: Optional[agent_update_prompt_params.Spec] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentUpdatePromptResponse:
        """
        Updates an existing prompt.

        Use this method to:

        - Modify prompt content or metadata
        - Change prompt type (template/command)

        Args:
          metadata: Metadata updates

          prompt_id: The ID of the prompt to update

          spec: Spec updates

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/gitpod.v1.AgentService/UpdatePrompt",
            body=await async_maybe_transform(
                {
                    "metadata": metadata,
                    "prompt_id": prompt_id,
                    "spec": spec,
                },
                agent_update_prompt_params.AgentUpdatePromptParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentUpdatePromptResponse,
        )


class AgentsResourceWithRawResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.create_execution_conversation_token = to_raw_response_wrapper(
            agents.create_execution_conversation_token,
        )
        self.create_prompt = to_raw_response_wrapper(
            agents.create_prompt,
        )
        self.delete_execution = to_raw_response_wrapper(
            agents.delete_execution,
        )
        self.delete_prompt = to_raw_response_wrapper(
            agents.delete_prompt,
        )
        self.list_executions = to_raw_response_wrapper(
            agents.list_executions,
        )
        self.list_prompts = to_raw_response_wrapper(
            agents.list_prompts,
        )
        self.retrieve_execution = to_raw_response_wrapper(
            agents.retrieve_execution,
        )
        self.retrieve_prompt = to_raw_response_wrapper(
            agents.retrieve_prompt,
        )
        self.send_to_execution = to_raw_response_wrapper(
            agents.send_to_execution,
        )
        self.start_execution = to_raw_response_wrapper(
            agents.start_execution,
        )
        self.stop_execution = to_raw_response_wrapper(
            agents.stop_execution,
        )
        self.update_prompt = to_raw_response_wrapper(
            agents.update_prompt,
        )


class AsyncAgentsResourceWithRawResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.create_execution_conversation_token = async_to_raw_response_wrapper(
            agents.create_execution_conversation_token,
        )
        self.create_prompt = async_to_raw_response_wrapper(
            agents.create_prompt,
        )
        self.delete_execution = async_to_raw_response_wrapper(
            agents.delete_execution,
        )
        self.delete_prompt = async_to_raw_response_wrapper(
            agents.delete_prompt,
        )
        self.list_executions = async_to_raw_response_wrapper(
            agents.list_executions,
        )
        self.list_prompts = async_to_raw_response_wrapper(
            agents.list_prompts,
        )
        self.retrieve_execution = async_to_raw_response_wrapper(
            agents.retrieve_execution,
        )
        self.retrieve_prompt = async_to_raw_response_wrapper(
            agents.retrieve_prompt,
        )
        self.send_to_execution = async_to_raw_response_wrapper(
            agents.send_to_execution,
        )
        self.start_execution = async_to_raw_response_wrapper(
            agents.start_execution,
        )
        self.stop_execution = async_to_raw_response_wrapper(
            agents.stop_execution,
        )
        self.update_prompt = async_to_raw_response_wrapper(
            agents.update_prompt,
        )


class AgentsResourceWithStreamingResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.create_execution_conversation_token = to_streamed_response_wrapper(
            agents.create_execution_conversation_token,
        )
        self.create_prompt = to_streamed_response_wrapper(
            agents.create_prompt,
        )
        self.delete_execution = to_streamed_response_wrapper(
            agents.delete_execution,
        )
        self.delete_prompt = to_streamed_response_wrapper(
            agents.delete_prompt,
        )
        self.list_executions = to_streamed_response_wrapper(
            agents.list_executions,
        )
        self.list_prompts = to_streamed_response_wrapper(
            agents.list_prompts,
        )
        self.retrieve_execution = to_streamed_response_wrapper(
            agents.retrieve_execution,
        )
        self.retrieve_prompt = to_streamed_response_wrapper(
            agents.retrieve_prompt,
        )
        self.send_to_execution = to_streamed_response_wrapper(
            agents.send_to_execution,
        )
        self.start_execution = to_streamed_response_wrapper(
            agents.start_execution,
        )
        self.stop_execution = to_streamed_response_wrapper(
            agents.stop_execution,
        )
        self.update_prompt = to_streamed_response_wrapper(
            agents.update_prompt,
        )


class AsyncAgentsResourceWithStreamingResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.create_execution_conversation_token = async_to_streamed_response_wrapper(
            agents.create_execution_conversation_token,
        )
        self.create_prompt = async_to_streamed_response_wrapper(
            agents.create_prompt,
        )
        self.delete_execution = async_to_streamed_response_wrapper(
            agents.delete_execution,
        )
        self.delete_prompt = async_to_streamed_response_wrapper(
            agents.delete_prompt,
        )
        self.list_executions = async_to_streamed_response_wrapper(
            agents.list_executions,
        )
        self.list_prompts = async_to_streamed_response_wrapper(
            agents.list_prompts,
        )
        self.retrieve_execution = async_to_streamed_response_wrapper(
            agents.retrieve_execution,
        )
        self.retrieve_prompt = async_to_streamed_response_wrapper(
            agents.retrieve_prompt,
        )
        self.send_to_execution = async_to_streamed_response_wrapper(
            agents.send_to_execution,
        )
        self.start_execution = async_to_streamed_response_wrapper(
            agents.start_execution,
        )
        self.stop_execution = async_to_streamed_response_wrapper(
            agents.stop_execution,
        )
        self.update_prompt = async_to_streamed_response_wrapper(
            agents.update_prompt,
        )
