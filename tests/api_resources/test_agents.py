# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.types import (
    Prompt,
    AgentExecution,
    AgentCreatePromptResponse,
    AgentUpdatePromptResponse,
    AgentRetrievePromptResponse,
    AgentStartExecutionResponse,
    AgentRetrieveExecutionResponse,
    AgentCreateExecutionConversationTokenResponse,
)
from gitpod._utils import parse_datetime
from gitpod.pagination import SyncPromptsPage, AsyncPromptsPage, SyncAgentExecutionsPage, AsyncAgentExecutionsPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_execution_conversation_token(self, client: Gitpod) -> None:
        agent = client.agents.create_execution_conversation_token()
        assert_matches_type(AgentCreateExecutionConversationTokenResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_execution_conversation_token_with_all_params(self, client: Gitpod) -> None:
        agent = client.agents.create_execution_conversation_token(
            agent_execution_id="6fa1a3c7-fbb7-49d1-ba56-1890dc7c4c35",
        )
        assert_matches_type(AgentCreateExecutionConversationTokenResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_execution_conversation_token(self, client: Gitpod) -> None:
        response = client.agents.with_raw_response.create_execution_conversation_token()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentCreateExecutionConversationTokenResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_execution_conversation_token(self, client: Gitpod) -> None:
        with client.agents.with_streaming_response.create_execution_conversation_token() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentCreateExecutionConversationTokenResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_prompt(self, client: Gitpod) -> None:
        agent = client.agents.create_prompt()
        assert_matches_type(AgentCreatePromptResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_prompt_with_all_params(self, client: Gitpod) -> None:
        agent = client.agents.create_prompt(
            command="command",
            description="x",
            is_command=True,
            is_template=True,
            name="x",
            prompt="x",
        )
        assert_matches_type(AgentCreatePromptResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_prompt(self, client: Gitpod) -> None:
        response = client.agents.with_raw_response.create_prompt()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentCreatePromptResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_prompt(self, client: Gitpod) -> None:
        with client.agents.with_streaming_response.create_prompt() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentCreatePromptResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_execution(self, client: Gitpod) -> None:
        agent = client.agents.delete_execution()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_execution_with_all_params(self, client: Gitpod) -> None:
        agent = client.agents.delete_execution(
            agent_execution_id="6fa1a3c7-fbb7-49d1-ba56-1890dc7c4c35",
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_execution(self, client: Gitpod) -> None:
        response = client.agents.with_raw_response.delete_execution()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_execution(self, client: Gitpod) -> None:
        with client.agents.with_streaming_response.delete_execution() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_prompt(self, client: Gitpod) -> None:
        agent = client.agents.delete_prompt()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_prompt_with_all_params(self, client: Gitpod) -> None:
        agent = client.agents.delete_prompt(
            prompt_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete_prompt(self, client: Gitpod) -> None:
        response = client.agents.with_raw_response.delete_prompt()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete_prompt(self, client: Gitpod) -> None:
        with client.agents.with_streaming_response.delete_prompt() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_executions(self, client: Gitpod) -> None:
        agent = client.agents.list_executions()
        assert_matches_type(SyncAgentExecutionsPage[AgentExecution], agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_executions_with_all_params(self, client: Gitpod) -> None:
        agent = client.agents.list_executions(
            token="token",
            page_size=0,
            filter={
                "agent_ids": ["b8a64cfa-43e2-4b9d-9fb3-07edc63f5971"],
                "creator_ids": ["string"],
                "environment_ids": ["string"],
                "project_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "roles": ["AGENT_EXECUTION_ROLE_UNSPECIFIED"],
                "status_phases": ["PHASE_UNSPECIFIED"],
            },
            pagination={
                "token": "token",
                "page_size": 10,
            },
        )
        assert_matches_type(SyncAgentExecutionsPage[AgentExecution], agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_executions(self, client: Gitpod) -> None:
        response = client.agents.with_raw_response.list_executions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(SyncAgentExecutionsPage[AgentExecution], agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_executions(self, client: Gitpod) -> None:
        with client.agents.with_streaming_response.list_executions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(SyncAgentExecutionsPage[AgentExecution], agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_prompts(self, client: Gitpod) -> None:
        agent = client.agents.list_prompts()
        assert_matches_type(SyncPromptsPage[Prompt], agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_prompts_with_all_params(self, client: Gitpod) -> None:
        agent = client.agents.list_prompts(
            token="token",
            page_size=0,
            filter={
                "command": "command",
                "command_prefix": "commandPrefix",
                "is_command": True,
                "is_template": True,
            },
            pagination={
                "token": "token",
                "page_size": 10,
            },
        )
        assert_matches_type(SyncPromptsPage[Prompt], agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_prompts(self, client: Gitpod) -> None:
        response = client.agents.with_raw_response.list_prompts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(SyncPromptsPage[Prompt], agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_prompts(self, client: Gitpod) -> None:
        with client.agents.with_streaming_response.list_prompts() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(SyncPromptsPage[Prompt], agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_execution(self, client: Gitpod) -> None:
        agent = client.agents.retrieve_execution()
        assert_matches_type(AgentRetrieveExecutionResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_execution_with_all_params(self, client: Gitpod) -> None:
        agent = client.agents.retrieve_execution(
            agent_execution_id="6fa1a3c7-fbb7-49d1-ba56-1890dc7c4c35",
        )
        assert_matches_type(AgentRetrieveExecutionResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_execution(self, client: Gitpod) -> None:
        response = client.agents.with_raw_response.retrieve_execution()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentRetrieveExecutionResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_execution(self, client: Gitpod) -> None:
        with client.agents.with_streaming_response.retrieve_execution() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentRetrieveExecutionResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_prompt(self, client: Gitpod) -> None:
        agent = client.agents.retrieve_prompt()
        assert_matches_type(AgentRetrievePromptResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_prompt_with_all_params(self, client: Gitpod) -> None:
        agent = client.agents.retrieve_prompt(
            prompt_id="07e03a28-65a5-4d98-b532-8ea67b188048",
        )
        assert_matches_type(AgentRetrievePromptResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_prompt(self, client: Gitpod) -> None:
        response = client.agents.with_raw_response.retrieve_prompt()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentRetrievePromptResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_prompt(self, client: Gitpod) -> None:
        with client.agents.with_streaming_response.retrieve_prompt() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentRetrievePromptResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_to_execution(self, client: Gitpod) -> None:
        agent = client.agents.send_to_execution()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_to_execution_with_all_params(self, client: Gitpod) -> None:
        agent = client.agents.send_to_execution(
            agent_execution_id="6fa1a3c7-fbb7-49d1-ba56-1890dc7c4c35",
            user_input={
                "text": {"content": "Generate a report based on the latest logs."},
                "id": "id",
                "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_send_to_execution(self, client: Gitpod) -> None:
        response = client.agents.with_raw_response.send_to_execution()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_send_to_execution(self, client: Gitpod) -> None:
        with client.agents.with_streaming_response.send_to_execution() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_start_execution(self, client: Gitpod) -> None:
        agent = client.agents.start_execution()
        assert_matches_type(AgentStartExecutionResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_start_execution_with_all_params(self, client: Gitpod) -> None:
        agent = client.agents.start_execution(
            agent_id="b8a64cfa-43e2-4b9d-9fb3-07edc63f5971",
            code_context={
                "context_url": {
                    "environment_class_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "url": "https://example.com",
                },
                "environment_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "project_id": "2d22e4eb-31da-467f-882c-27e21550992f",
                "pull_request": {
                    "id": "id",
                    "author": "author",
                    "from_branch": "fromBranch",
                    "repository": {
                        "clone_url": "cloneUrl",
                        "host": "host",
                        "name": "name",
                        "owner": "owner",
                    },
                    "title": "title",
                    "to_branch": "toBranch",
                    "url": "url",
                },
            },
            mode="AGENT_MODE_UNSPECIFIED",
            name="name",
            workflow_action_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AgentStartExecutionResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_start_execution(self, client: Gitpod) -> None:
        response = client.agents.with_raw_response.start_execution()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentStartExecutionResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_start_execution(self, client: Gitpod) -> None:
        with client.agents.with_streaming_response.start_execution() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentStartExecutionResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_stop_execution(self, client: Gitpod) -> None:
        agent = client.agents.stop_execution()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_stop_execution_with_all_params(self, client: Gitpod) -> None:
        agent = client.agents.stop_execution(
            agent_execution_id="6fa1a3c7-fbb7-49d1-ba56-1890dc7c4c35",
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_stop_execution(self, client: Gitpod) -> None:
        response = client.agents.with_raw_response.stop_execution()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_stop_execution(self, client: Gitpod) -> None:
        with client.agents.with_streaming_response.stop_execution() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_prompt(self, client: Gitpod) -> None:
        agent = client.agents.update_prompt()
        assert_matches_type(AgentUpdatePromptResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_prompt_with_all_params(self, client: Gitpod) -> None:
        agent = client.agents.update_prompt(
            metadata={
                "description": "x",
                "name": "name",
            },
            prompt_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            spec={
                "command": "command",
                "is_command": True,
                "is_template": True,
                "prompt": "prompt",
            },
        )
        assert_matches_type(AgentUpdatePromptResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_prompt(self, client: Gitpod) -> None:
        response = client.agents.with_raw_response.update_prompt()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentUpdatePromptResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_prompt(self, client: Gitpod) -> None:
        with client.agents.with_streaming_response.update_prompt() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentUpdatePromptResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAgents:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_execution_conversation_token(self, async_client: AsyncGitpod) -> None:
        agent = await async_client.agents.create_execution_conversation_token()
        assert_matches_type(AgentCreateExecutionConversationTokenResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_execution_conversation_token_with_all_params(self, async_client: AsyncGitpod) -> None:
        agent = await async_client.agents.create_execution_conversation_token(
            agent_execution_id="6fa1a3c7-fbb7-49d1-ba56-1890dc7c4c35",
        )
        assert_matches_type(AgentCreateExecutionConversationTokenResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_execution_conversation_token(self, async_client: AsyncGitpod) -> None:
        response = await async_client.agents.with_raw_response.create_execution_conversation_token()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentCreateExecutionConversationTokenResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_execution_conversation_token(self, async_client: AsyncGitpod) -> None:
        async with async_client.agents.with_streaming_response.create_execution_conversation_token() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentCreateExecutionConversationTokenResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_prompt(self, async_client: AsyncGitpod) -> None:
        agent = await async_client.agents.create_prompt()
        assert_matches_type(AgentCreatePromptResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_prompt_with_all_params(self, async_client: AsyncGitpod) -> None:
        agent = await async_client.agents.create_prompt(
            command="command",
            description="x",
            is_command=True,
            is_template=True,
            name="x",
            prompt="x",
        )
        assert_matches_type(AgentCreatePromptResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_prompt(self, async_client: AsyncGitpod) -> None:
        response = await async_client.agents.with_raw_response.create_prompt()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentCreatePromptResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_prompt(self, async_client: AsyncGitpod) -> None:
        async with async_client.agents.with_streaming_response.create_prompt() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentCreatePromptResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_execution(self, async_client: AsyncGitpod) -> None:
        agent = await async_client.agents.delete_execution()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_execution_with_all_params(self, async_client: AsyncGitpod) -> None:
        agent = await async_client.agents.delete_execution(
            agent_execution_id="6fa1a3c7-fbb7-49d1-ba56-1890dc7c4c35",
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_execution(self, async_client: AsyncGitpod) -> None:
        response = await async_client.agents.with_raw_response.delete_execution()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_execution(self, async_client: AsyncGitpod) -> None:
        async with async_client.agents.with_streaming_response.delete_execution() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_prompt(self, async_client: AsyncGitpod) -> None:
        agent = await async_client.agents.delete_prompt()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_prompt_with_all_params(self, async_client: AsyncGitpod) -> None:
        agent = await async_client.agents.delete_prompt(
            prompt_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete_prompt(self, async_client: AsyncGitpod) -> None:
        response = await async_client.agents.with_raw_response.delete_prompt()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete_prompt(self, async_client: AsyncGitpod) -> None:
        async with async_client.agents.with_streaming_response.delete_prompt() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_executions(self, async_client: AsyncGitpod) -> None:
        agent = await async_client.agents.list_executions()
        assert_matches_type(AsyncAgentExecutionsPage[AgentExecution], agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_executions_with_all_params(self, async_client: AsyncGitpod) -> None:
        agent = await async_client.agents.list_executions(
            token="token",
            page_size=0,
            filter={
                "agent_ids": ["b8a64cfa-43e2-4b9d-9fb3-07edc63f5971"],
                "creator_ids": ["string"],
                "environment_ids": ["string"],
                "project_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "roles": ["AGENT_EXECUTION_ROLE_UNSPECIFIED"],
                "status_phases": ["PHASE_UNSPECIFIED"],
            },
            pagination={
                "token": "token",
                "page_size": 10,
            },
        )
        assert_matches_type(AsyncAgentExecutionsPage[AgentExecution], agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_executions(self, async_client: AsyncGitpod) -> None:
        response = await async_client.agents.with_raw_response.list_executions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AsyncAgentExecutionsPage[AgentExecution], agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_executions(self, async_client: AsyncGitpod) -> None:
        async with async_client.agents.with_streaming_response.list_executions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AsyncAgentExecutionsPage[AgentExecution], agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_prompts(self, async_client: AsyncGitpod) -> None:
        agent = await async_client.agents.list_prompts()
        assert_matches_type(AsyncPromptsPage[Prompt], agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_prompts_with_all_params(self, async_client: AsyncGitpod) -> None:
        agent = await async_client.agents.list_prompts(
            token="token",
            page_size=0,
            filter={
                "command": "command",
                "command_prefix": "commandPrefix",
                "is_command": True,
                "is_template": True,
            },
            pagination={
                "token": "token",
                "page_size": 10,
            },
        )
        assert_matches_type(AsyncPromptsPage[Prompt], agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_prompts(self, async_client: AsyncGitpod) -> None:
        response = await async_client.agents.with_raw_response.list_prompts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AsyncPromptsPage[Prompt], agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_prompts(self, async_client: AsyncGitpod) -> None:
        async with async_client.agents.with_streaming_response.list_prompts() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AsyncPromptsPage[Prompt], agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_execution(self, async_client: AsyncGitpod) -> None:
        agent = await async_client.agents.retrieve_execution()
        assert_matches_type(AgentRetrieveExecutionResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_execution_with_all_params(self, async_client: AsyncGitpod) -> None:
        agent = await async_client.agents.retrieve_execution(
            agent_execution_id="6fa1a3c7-fbb7-49d1-ba56-1890dc7c4c35",
        )
        assert_matches_type(AgentRetrieveExecutionResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_execution(self, async_client: AsyncGitpod) -> None:
        response = await async_client.agents.with_raw_response.retrieve_execution()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentRetrieveExecutionResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_execution(self, async_client: AsyncGitpod) -> None:
        async with async_client.agents.with_streaming_response.retrieve_execution() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentRetrieveExecutionResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_prompt(self, async_client: AsyncGitpod) -> None:
        agent = await async_client.agents.retrieve_prompt()
        assert_matches_type(AgentRetrievePromptResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_prompt_with_all_params(self, async_client: AsyncGitpod) -> None:
        agent = await async_client.agents.retrieve_prompt(
            prompt_id="07e03a28-65a5-4d98-b532-8ea67b188048",
        )
        assert_matches_type(AgentRetrievePromptResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_prompt(self, async_client: AsyncGitpod) -> None:
        response = await async_client.agents.with_raw_response.retrieve_prompt()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentRetrievePromptResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_prompt(self, async_client: AsyncGitpod) -> None:
        async with async_client.agents.with_streaming_response.retrieve_prompt() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentRetrievePromptResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_to_execution(self, async_client: AsyncGitpod) -> None:
        agent = await async_client.agents.send_to_execution()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_to_execution_with_all_params(self, async_client: AsyncGitpod) -> None:
        agent = await async_client.agents.send_to_execution(
            agent_execution_id="6fa1a3c7-fbb7-49d1-ba56-1890dc7c4c35",
            user_input={
                "text": {"content": "Generate a report based on the latest logs."},
                "id": "id",
                "created_at": parse_datetime("2019-12-27T18:11:19.117Z"),
            },
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_send_to_execution(self, async_client: AsyncGitpod) -> None:
        response = await async_client.agents.with_raw_response.send_to_execution()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_send_to_execution(self, async_client: AsyncGitpod) -> None:
        async with async_client.agents.with_streaming_response.send_to_execution() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_start_execution(self, async_client: AsyncGitpod) -> None:
        agent = await async_client.agents.start_execution()
        assert_matches_type(AgentStartExecutionResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_start_execution_with_all_params(self, async_client: AsyncGitpod) -> None:
        agent = await async_client.agents.start_execution(
            agent_id="b8a64cfa-43e2-4b9d-9fb3-07edc63f5971",
            code_context={
                "context_url": {
                    "environment_class_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "url": "https://example.com",
                },
                "environment_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "project_id": "2d22e4eb-31da-467f-882c-27e21550992f",
                "pull_request": {
                    "id": "id",
                    "author": "author",
                    "from_branch": "fromBranch",
                    "repository": {
                        "clone_url": "cloneUrl",
                        "host": "host",
                        "name": "name",
                        "owner": "owner",
                    },
                    "title": "title",
                    "to_branch": "toBranch",
                    "url": "url",
                },
            },
            mode="AGENT_MODE_UNSPECIFIED",
            name="name",
            workflow_action_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AgentStartExecutionResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_start_execution(self, async_client: AsyncGitpod) -> None:
        response = await async_client.agents.with_raw_response.start_execution()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentStartExecutionResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_start_execution(self, async_client: AsyncGitpod) -> None:
        async with async_client.agents.with_streaming_response.start_execution() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentStartExecutionResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_stop_execution(self, async_client: AsyncGitpod) -> None:
        agent = await async_client.agents.stop_execution()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_stop_execution_with_all_params(self, async_client: AsyncGitpod) -> None:
        agent = await async_client.agents.stop_execution(
            agent_execution_id="6fa1a3c7-fbb7-49d1-ba56-1890dc7c4c35",
        )
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_stop_execution(self, async_client: AsyncGitpod) -> None:
        response = await async_client.agents.with_raw_response.stop_execution()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(object, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_stop_execution(self, async_client: AsyncGitpod) -> None:
        async with async_client.agents.with_streaming_response.stop_execution() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(object, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_prompt(self, async_client: AsyncGitpod) -> None:
        agent = await async_client.agents.update_prompt()
        assert_matches_type(AgentUpdatePromptResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_prompt_with_all_params(self, async_client: AsyncGitpod) -> None:
        agent = await async_client.agents.update_prompt(
            metadata={
                "description": "x",
                "name": "name",
            },
            prompt_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            spec={
                "command": "command",
                "is_command": True,
                "is_template": True,
                "prompt": "prompt",
            },
        )
        assert_matches_type(AgentUpdatePromptResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_prompt(self, async_client: AsyncGitpod) -> None:
        response = await async_client.agents.with_raw_response.update_prompt()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentUpdatePromptResponse, agent, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_prompt(self, async_client: AsyncGitpod) -> None:
        async with async_client.agents.with_streaming_response.update_prompt() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentUpdatePromptResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True
