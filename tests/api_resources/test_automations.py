# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from gitpod import Gitpod, AsyncGitpod
from tests.utils import assert_matches_type
from gitpod.types import (
    Workflow,
    WorkflowExecution,
    WorkflowExecutionAction,
    AutomationCreateResponse,
    AutomationUpdateResponse,
    AutomationRetrieveResponse,
    AutomationStartExecutionResponse,
    AutomationRetrieveExecutionResponse,
    AutomationListExecutionOutputsResponse,
    AutomationRetrieveExecutionActionResponse,
)
from gitpod._utils import parse_datetime
from gitpod.pagination import (
    SyncOutputsPage,
    AsyncOutputsPage,
    SyncWorkflowsPage,
    AsyncWorkflowsPage,
    SyncWorkflowExecutionsPage,
    AsyncWorkflowExecutionsPage,
    SyncWorkflowExecutionActionsPage,
    AsyncWorkflowExecutionActionsPage,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAutomations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Gitpod) -> None:
        automation = client.automations.create(
            action={"limits": {}},
        )
        assert_matches_type(AutomationCreateResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Gitpod) -> None:
        automation = client.automations.create(
            action={
                "limits": {
                    "max_parallel": 0,
                    "max_total": 0,
                    "per_execution": {"max_time": "+9125115.360s"},
                },
                "steps": [
                    {
                        "agent": {"prompt": "prompt"},
                        "pull_request": {
                            "branch": "branch",
                            "description": "description",
                            "draft": True,
                            "title": "title",
                        },
                        "report": {
                            "outputs": [
                                {
                                    "acceptance_criteria": "acceptanceCriteria",
                                    "boolean": {},
                                    "command": "command",
                                    "float": {
                                        "max": 0,
                                        "min": 0,
                                    },
                                    "integer": {
                                        "max": 0,
                                        "min": 0,
                                    },
                                    "key": "key",
                                    "prompt": "prompt",
                                    "string": {"pattern": "pattern"},
                                    "title": "title",
                                }
                            ]
                        },
                        "task": {"command": "command"},
                    }
                ],
            },
            description="description",
            executor={
                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "principal": "PRINCIPAL_UNSPECIFIED",
            },
            name="name",
            report={
                "limits": {
                    "max_parallel": 0,
                    "max_total": 0,
                    "per_execution": {"max_time": "+9125115.360s"},
                },
                "steps": [
                    {
                        "agent": {"prompt": "prompt"},
                        "pull_request": {
                            "branch": "branch",
                            "description": "description",
                            "draft": True,
                            "title": "title",
                        },
                        "report": {
                            "outputs": [
                                {
                                    "acceptance_criteria": "acceptanceCriteria",
                                    "boolean": {},
                                    "command": "command",
                                    "float": {
                                        "max": 0,
                                        "min": 0,
                                    },
                                    "integer": {
                                        "max": 0,
                                        "min": 0,
                                    },
                                    "key": "key",
                                    "prompt": "prompt",
                                    "string": {"pattern": "pattern"},
                                    "title": "title",
                                }
                            ]
                        },
                        "task": {"command": "command"},
                    }
                ],
            },
            triggers=[
                {
                    "context": {
                        "agent": {"prompt": "prompt"},
                        "from_trigger": {},
                        "projects": {"project_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"]},
                        "repositories": {
                            "environment_class_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "repo_selector": {
                                "repo_search_string": "x",
                                "scm_host": "x",
                            },
                            "repository_urls": {"repo_urls": ["x"]},
                        },
                    },
                    "manual": {},
                    "pull_request": {
                        "events": ["PULL_REQUEST_EVENT_UNSPECIFIED"],
                        "webhook_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "time": {"cron_expression": "cronExpression"},
                }
            ],
        )
        assert_matches_type(AutomationCreateResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Gitpod) -> None:
        response = client.automations.with_raw_response.create(
            action={"limits": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = response.parse()
        assert_matches_type(AutomationCreateResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Gitpod) -> None:
        with client.automations.with_streaming_response.create(
            action={"limits": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = response.parse()
            assert_matches_type(AutomationCreateResponse, automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Gitpod) -> None:
        automation = client.automations.retrieve()
        assert_matches_type(AutomationRetrieveResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Gitpod) -> None:
        automation = client.automations.retrieve(
            workflow_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(AutomationRetrieveResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Gitpod) -> None:
        response = client.automations.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = response.parse()
        assert_matches_type(AutomationRetrieveResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Gitpod) -> None:
        with client.automations.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = response.parse()
            assert_matches_type(AutomationRetrieveResponse, automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Gitpod) -> None:
        automation = client.automations.update()
        assert_matches_type(AutomationUpdateResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Gitpod) -> None:
        automation = client.automations.update(
            action={
                "limits": {
                    "max_parallel": 0,
                    "max_total": 0,
                    "per_execution": {"max_time": "+9125115.360s"},
                },
                "steps": [
                    {
                        "agent": {"prompt": "prompt"},
                        "pull_request": {
                            "branch": "branch",
                            "description": "description",
                            "draft": True,
                            "title": "title",
                        },
                        "report": {
                            "outputs": [
                                {
                                    "acceptance_criteria": "acceptanceCriteria",
                                    "boolean": {},
                                    "command": "command",
                                    "float": {
                                        "max": 0,
                                        "min": 0,
                                    },
                                    "integer": {
                                        "max": 0,
                                        "min": 0,
                                    },
                                    "key": "key",
                                    "prompt": "prompt",
                                    "string": {"pattern": "pattern"},
                                    "title": "title",
                                }
                            ]
                        },
                        "task": {"command": "command"},
                    }
                ],
            },
            description="description",
            executor={
                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "principal": "PRINCIPAL_UNSPECIFIED",
            },
            name="name",
            report={
                "limits": {
                    "max_parallel": 0,
                    "max_total": 0,
                    "per_execution": {"max_time": "+9125115.360s"},
                },
                "steps": [
                    {
                        "agent": {"prompt": "prompt"},
                        "pull_request": {
                            "branch": "branch",
                            "description": "description",
                            "draft": True,
                            "title": "title",
                        },
                        "report": {
                            "outputs": [
                                {
                                    "acceptance_criteria": "acceptanceCriteria",
                                    "boolean": {},
                                    "command": "command",
                                    "float": {
                                        "max": 0,
                                        "min": 0,
                                    },
                                    "integer": {
                                        "max": 0,
                                        "min": 0,
                                    },
                                    "key": "key",
                                    "prompt": "prompt",
                                    "string": {"pattern": "pattern"},
                                    "title": "title",
                                }
                            ]
                        },
                        "task": {"command": "command"},
                    }
                ],
            },
            triggers=[
                {
                    "context": {
                        "agent": {"prompt": "prompt"},
                        "from_trigger": {},
                        "projects": {"project_ids": ["new-project-id"]},
                        "repositories": {
                            "environment_class_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "repo_selector": {
                                "repo_search_string": "x",
                                "scm_host": "x",
                            },
                            "repository_urls": {"repo_urls": ["x"]},
                        },
                    },
                    "manual": {},
                    "pull_request": {
                        "events": ["PULL_REQUEST_EVENT_UNSPECIFIED"],
                        "webhook_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "time": {"cron_expression": "cronExpression"},
                }
            ],
            workflow_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(AutomationUpdateResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Gitpod) -> None:
        response = client.automations.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = response.parse()
        assert_matches_type(AutomationUpdateResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Gitpod) -> None:
        with client.automations.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = response.parse()
            assert_matches_type(AutomationUpdateResponse, automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Gitpod) -> None:
        automation = client.automations.list()
        assert_matches_type(SyncWorkflowsPage[Workflow], automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Gitpod) -> None:
        automation = client.automations.list(
            token="token",
            page_size=0,
            filter={
                "creator_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "has_failed_execution_since": parse_datetime("2019-12-27T18:11:19.117Z"),
                "search": "search",
                "status_phases": ["WORKFLOW_EXECUTION_PHASE_UNSPECIFIED"],
                "workflow_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            },
            pagination={
                "token": "token",
                "page_size": 100,
            },
            sort={
                "field": "SORT_FIELD_UNSPECIFIED",
                "order": "SORT_ORDER_UNSPECIFIED",
            },
        )
        assert_matches_type(SyncWorkflowsPage[Workflow], automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Gitpod) -> None:
        response = client.automations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = response.parse()
        assert_matches_type(SyncWorkflowsPage[Workflow], automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Gitpod) -> None:
        with client.automations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = response.parse()
            assert_matches_type(SyncWorkflowsPage[Workflow], automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Gitpod) -> None:
        automation = client.automations.delete()
        assert_matches_type(object, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Gitpod) -> None:
        automation = client.automations.delete(
            force=True,
            workflow_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(object, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Gitpod) -> None:
        response = client.automations.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = response.parse()
        assert_matches_type(object, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Gitpod) -> None:
        with client.automations.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = response.parse()
            assert_matches_type(object, automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel_execution(self, client: Gitpod) -> None:
        automation = client.automations.cancel_execution()
        assert_matches_type(object, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel_execution_with_all_params(self, client: Gitpod) -> None:
        automation = client.automations.cancel_execution(
            workflow_execution_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(object, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_cancel_execution(self, client: Gitpod) -> None:
        response = client.automations.with_raw_response.cancel_execution()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = response.parse()
        assert_matches_type(object, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_cancel_execution(self, client: Gitpod) -> None:
        with client.automations.with_streaming_response.cancel_execution() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = response.parse()
            assert_matches_type(object, automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel_execution_action(self, client: Gitpod) -> None:
        automation = client.automations.cancel_execution_action()
        assert_matches_type(object, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel_execution_action_with_all_params(self, client: Gitpod) -> None:
        automation = client.automations.cancel_execution_action(
            workflow_execution_action_id="a1b2c3d4-5e6f-7890-abcd-ef1234567890",
        )
        assert_matches_type(object, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_cancel_execution_action(self, client: Gitpod) -> None:
        response = client.automations.with_raw_response.cancel_execution_action()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = response.parse()
        assert_matches_type(object, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_cancel_execution_action(self, client: Gitpod) -> None:
        with client.automations.with_streaming_response.cancel_execution_action() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = response.parse()
            assert_matches_type(object, automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_execution_actions(self, client: Gitpod) -> None:
        automation = client.automations.list_execution_actions()
        assert_matches_type(SyncWorkflowExecutionActionsPage[WorkflowExecutionAction], automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_execution_actions_with_all_params(self, client: Gitpod) -> None:
        automation = client.automations.list_execution_actions(
            token="token",
            page_size=0,
            filter={
                "phases": ["WORKFLOW_EXECUTION_ACTION_PHASE_UNSPECIFIED"],
                "workflow_execution_action_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "workflow_execution_ids": ["d2c94c27-3b76-4a42-b88c-95a85e392c68"],
                "workflow_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            },
            pagination={
                "token": "token",
                "page_size": 20,
            },
        )
        assert_matches_type(SyncWorkflowExecutionActionsPage[WorkflowExecutionAction], automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_execution_actions(self, client: Gitpod) -> None:
        response = client.automations.with_raw_response.list_execution_actions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = response.parse()
        assert_matches_type(SyncWorkflowExecutionActionsPage[WorkflowExecutionAction], automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_execution_actions(self, client: Gitpod) -> None:
        with client.automations.with_streaming_response.list_execution_actions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = response.parse()
            assert_matches_type(
                SyncWorkflowExecutionActionsPage[WorkflowExecutionAction], automation, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_execution_outputs(self, client: Gitpod) -> None:
        automation = client.automations.list_execution_outputs()
        assert_matches_type(SyncOutputsPage[AutomationListExecutionOutputsResponse], automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_execution_outputs_with_all_params(self, client: Gitpod) -> None:
        automation = client.automations.list_execution_outputs(
            token="token",
            page_size=0,
            filter={"workflow_execution_ids": ["d2c94c27-3b76-4a42-b88c-95a85e392c68"]},
            pagination={
                "token": "token",
                "page_size": 50,
            },
        )
        assert_matches_type(SyncOutputsPage[AutomationListExecutionOutputsResponse], automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_execution_outputs(self, client: Gitpod) -> None:
        response = client.automations.with_raw_response.list_execution_outputs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = response.parse()
        assert_matches_type(SyncOutputsPage[AutomationListExecutionOutputsResponse], automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_execution_outputs(self, client: Gitpod) -> None:
        with client.automations.with_streaming_response.list_execution_outputs() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = response.parse()
            assert_matches_type(SyncOutputsPage[AutomationListExecutionOutputsResponse], automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_executions(self, client: Gitpod) -> None:
        automation = client.automations.list_executions()
        assert_matches_type(SyncWorkflowExecutionsPage[WorkflowExecution], automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_executions_with_all_params(self, client: Gitpod) -> None:
        automation = client.automations.list_executions(
            token="token",
            page_size=0,
            filter={
                "has_failed_actions": True,
                "search": "search",
                "status_phases": ["WORKFLOW_EXECUTION_PHASE_UNSPECIFIED"],
                "workflow_execution_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "workflow_ids": ["b0e12f6c-4c67-429d-a4a6-d9838b5da047"],
            },
            pagination={
                "token": "token",
                "page_size": 20,
            },
            sort={
                "field": "field",
                "order": "SORT_ORDER_UNSPECIFIED",
            },
        )
        assert_matches_type(SyncWorkflowExecutionsPage[WorkflowExecution], automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_executions(self, client: Gitpod) -> None:
        response = client.automations.with_raw_response.list_executions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = response.parse()
        assert_matches_type(SyncWorkflowExecutionsPage[WorkflowExecution], automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_executions(self, client: Gitpod) -> None:
        with client.automations.with_streaming_response.list_executions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = response.parse()
            assert_matches_type(SyncWorkflowExecutionsPage[WorkflowExecution], automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_execution(self, client: Gitpod) -> None:
        automation = client.automations.retrieve_execution()
        assert_matches_type(AutomationRetrieveExecutionResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_execution_with_all_params(self, client: Gitpod) -> None:
        automation = client.automations.retrieve_execution(
            workflow_execution_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(AutomationRetrieveExecutionResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_execution(self, client: Gitpod) -> None:
        response = client.automations.with_raw_response.retrieve_execution()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = response.parse()
        assert_matches_type(AutomationRetrieveExecutionResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_execution(self, client: Gitpod) -> None:
        with client.automations.with_streaming_response.retrieve_execution() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = response.parse()
            assert_matches_type(AutomationRetrieveExecutionResponse, automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_execution_action(self, client: Gitpod) -> None:
        automation = client.automations.retrieve_execution_action()
        assert_matches_type(AutomationRetrieveExecutionActionResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_execution_action_with_all_params(self, client: Gitpod) -> None:
        automation = client.automations.retrieve_execution_action(
            workflow_execution_action_id="a1b2c3d4-5e6f-7890-abcd-ef1234567890",
        )
        assert_matches_type(AutomationRetrieveExecutionActionResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_execution_action(self, client: Gitpod) -> None:
        response = client.automations.with_raw_response.retrieve_execution_action()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = response.parse()
        assert_matches_type(AutomationRetrieveExecutionActionResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_execution_action(self, client: Gitpod) -> None:
        with client.automations.with_streaming_response.retrieve_execution_action() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = response.parse()
            assert_matches_type(AutomationRetrieveExecutionActionResponse, automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_start_execution(self, client: Gitpod) -> None:
        automation = client.automations.start_execution()
        assert_matches_type(AutomationStartExecutionResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_start_execution_with_all_params(self, client: Gitpod) -> None:
        automation = client.automations.start_execution(
            context_override={
                "agent": {"prompt": "prompt"},
                "from_trigger": {},
                "projects": {"project_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"]},
                "repositories": {
                    "environment_class_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "repo_selector": {
                        "repo_search_string": "x",
                        "scm_host": "x",
                    },
                    "repository_urls": {"repo_urls": ["x"]},
                },
            },
            parameters={"foo": "string"},
            workflow_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(AutomationStartExecutionResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_start_execution(self, client: Gitpod) -> None:
        response = client.automations.with_raw_response.start_execution()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = response.parse()
        assert_matches_type(AutomationStartExecutionResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_start_execution(self, client: Gitpod) -> None:
        with client.automations.with_streaming_response.start_execution() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = response.parse()
            assert_matches_type(AutomationStartExecutionResponse, automation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAutomations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncGitpod) -> None:
        automation = await async_client.automations.create(
            action={"limits": {}},
        )
        assert_matches_type(AutomationCreateResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncGitpod) -> None:
        automation = await async_client.automations.create(
            action={
                "limits": {
                    "max_parallel": 0,
                    "max_total": 0,
                    "per_execution": {"max_time": "+9125115.360s"},
                },
                "steps": [
                    {
                        "agent": {"prompt": "prompt"},
                        "pull_request": {
                            "branch": "branch",
                            "description": "description",
                            "draft": True,
                            "title": "title",
                        },
                        "report": {
                            "outputs": [
                                {
                                    "acceptance_criteria": "acceptanceCriteria",
                                    "boolean": {},
                                    "command": "command",
                                    "float": {
                                        "max": 0,
                                        "min": 0,
                                    },
                                    "integer": {
                                        "max": 0,
                                        "min": 0,
                                    },
                                    "key": "key",
                                    "prompt": "prompt",
                                    "string": {"pattern": "pattern"},
                                    "title": "title",
                                }
                            ]
                        },
                        "task": {"command": "command"},
                    }
                ],
            },
            description="description",
            executor={
                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "principal": "PRINCIPAL_UNSPECIFIED",
            },
            name="name",
            report={
                "limits": {
                    "max_parallel": 0,
                    "max_total": 0,
                    "per_execution": {"max_time": "+9125115.360s"},
                },
                "steps": [
                    {
                        "agent": {"prompt": "prompt"},
                        "pull_request": {
                            "branch": "branch",
                            "description": "description",
                            "draft": True,
                            "title": "title",
                        },
                        "report": {
                            "outputs": [
                                {
                                    "acceptance_criteria": "acceptanceCriteria",
                                    "boolean": {},
                                    "command": "command",
                                    "float": {
                                        "max": 0,
                                        "min": 0,
                                    },
                                    "integer": {
                                        "max": 0,
                                        "min": 0,
                                    },
                                    "key": "key",
                                    "prompt": "prompt",
                                    "string": {"pattern": "pattern"},
                                    "title": "title",
                                }
                            ]
                        },
                        "task": {"command": "command"},
                    }
                ],
            },
            triggers=[
                {
                    "context": {
                        "agent": {"prompt": "prompt"},
                        "from_trigger": {},
                        "projects": {"project_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"]},
                        "repositories": {
                            "environment_class_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "repo_selector": {
                                "repo_search_string": "x",
                                "scm_host": "x",
                            },
                            "repository_urls": {"repo_urls": ["x"]},
                        },
                    },
                    "manual": {},
                    "pull_request": {
                        "events": ["PULL_REQUEST_EVENT_UNSPECIFIED"],
                        "webhook_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "time": {"cron_expression": "cronExpression"},
                }
            ],
        )
        assert_matches_type(AutomationCreateResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncGitpod) -> None:
        response = await async_client.automations.with_raw_response.create(
            action={"limits": {}},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = await response.parse()
        assert_matches_type(AutomationCreateResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncGitpod) -> None:
        async with async_client.automations.with_streaming_response.create(
            action={"limits": {}},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = await response.parse()
            assert_matches_type(AutomationCreateResponse, automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGitpod) -> None:
        automation = await async_client.automations.retrieve()
        assert_matches_type(AutomationRetrieveResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncGitpod) -> None:
        automation = await async_client.automations.retrieve(
            workflow_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(AutomationRetrieveResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGitpod) -> None:
        response = await async_client.automations.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = await response.parse()
        assert_matches_type(AutomationRetrieveResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGitpod) -> None:
        async with async_client.automations.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = await response.parse()
            assert_matches_type(AutomationRetrieveResponse, automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncGitpod) -> None:
        automation = await async_client.automations.update()
        assert_matches_type(AutomationUpdateResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncGitpod) -> None:
        automation = await async_client.automations.update(
            action={
                "limits": {
                    "max_parallel": 0,
                    "max_total": 0,
                    "per_execution": {"max_time": "+9125115.360s"},
                },
                "steps": [
                    {
                        "agent": {"prompt": "prompt"},
                        "pull_request": {
                            "branch": "branch",
                            "description": "description",
                            "draft": True,
                            "title": "title",
                        },
                        "report": {
                            "outputs": [
                                {
                                    "acceptance_criteria": "acceptanceCriteria",
                                    "boolean": {},
                                    "command": "command",
                                    "float": {
                                        "max": 0,
                                        "min": 0,
                                    },
                                    "integer": {
                                        "max": 0,
                                        "min": 0,
                                    },
                                    "key": "key",
                                    "prompt": "prompt",
                                    "string": {"pattern": "pattern"},
                                    "title": "title",
                                }
                            ]
                        },
                        "task": {"command": "command"},
                    }
                ],
            },
            description="description",
            executor={
                "id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "principal": "PRINCIPAL_UNSPECIFIED",
            },
            name="name",
            report={
                "limits": {
                    "max_parallel": 0,
                    "max_total": 0,
                    "per_execution": {"max_time": "+9125115.360s"},
                },
                "steps": [
                    {
                        "agent": {"prompt": "prompt"},
                        "pull_request": {
                            "branch": "branch",
                            "description": "description",
                            "draft": True,
                            "title": "title",
                        },
                        "report": {
                            "outputs": [
                                {
                                    "acceptance_criteria": "acceptanceCriteria",
                                    "boolean": {},
                                    "command": "command",
                                    "float": {
                                        "max": 0,
                                        "min": 0,
                                    },
                                    "integer": {
                                        "max": 0,
                                        "min": 0,
                                    },
                                    "key": "key",
                                    "prompt": "prompt",
                                    "string": {"pattern": "pattern"},
                                    "title": "title",
                                }
                            ]
                        },
                        "task": {"command": "command"},
                    }
                ],
            },
            triggers=[
                {
                    "context": {
                        "agent": {"prompt": "prompt"},
                        "from_trigger": {},
                        "projects": {"project_ids": ["new-project-id"]},
                        "repositories": {
                            "environment_class_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                            "repo_selector": {
                                "repo_search_string": "x",
                                "scm_host": "x",
                            },
                            "repository_urls": {"repo_urls": ["x"]},
                        },
                    },
                    "manual": {},
                    "pull_request": {
                        "events": ["PULL_REQUEST_EVENT_UNSPECIFIED"],
                        "webhook_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                    "time": {"cron_expression": "cronExpression"},
                }
            ],
            workflow_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(AutomationUpdateResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncGitpod) -> None:
        response = await async_client.automations.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = await response.parse()
        assert_matches_type(AutomationUpdateResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncGitpod) -> None:
        async with async_client.automations.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = await response.parse()
            assert_matches_type(AutomationUpdateResponse, automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncGitpod) -> None:
        automation = await async_client.automations.list()
        assert_matches_type(AsyncWorkflowsPage[Workflow], automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGitpod) -> None:
        automation = await async_client.automations.list(
            token="token",
            page_size=0,
            filter={
                "creator_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "has_failed_execution_since": parse_datetime("2019-12-27T18:11:19.117Z"),
                "search": "search",
                "status_phases": ["WORKFLOW_EXECUTION_PHASE_UNSPECIFIED"],
                "workflow_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            },
            pagination={
                "token": "token",
                "page_size": 100,
            },
            sort={
                "field": "SORT_FIELD_UNSPECIFIED",
                "order": "SORT_ORDER_UNSPECIFIED",
            },
        )
        assert_matches_type(AsyncWorkflowsPage[Workflow], automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGitpod) -> None:
        response = await async_client.automations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = await response.parse()
        assert_matches_type(AsyncWorkflowsPage[Workflow], automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGitpod) -> None:
        async with async_client.automations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = await response.parse()
            assert_matches_type(AsyncWorkflowsPage[Workflow], automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncGitpod) -> None:
        automation = await async_client.automations.delete()
        assert_matches_type(object, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncGitpod) -> None:
        automation = await async_client.automations.delete(
            force=True,
            workflow_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(object, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncGitpod) -> None:
        response = await async_client.automations.with_raw_response.delete()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = await response.parse()
        assert_matches_type(object, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncGitpod) -> None:
        async with async_client.automations.with_streaming_response.delete() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = await response.parse()
            assert_matches_type(object, automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel_execution(self, async_client: AsyncGitpod) -> None:
        automation = await async_client.automations.cancel_execution()
        assert_matches_type(object, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel_execution_with_all_params(self, async_client: AsyncGitpod) -> None:
        automation = await async_client.automations.cancel_execution(
            workflow_execution_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(object, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_cancel_execution(self, async_client: AsyncGitpod) -> None:
        response = await async_client.automations.with_raw_response.cancel_execution()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = await response.parse()
        assert_matches_type(object, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_cancel_execution(self, async_client: AsyncGitpod) -> None:
        async with async_client.automations.with_streaming_response.cancel_execution() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = await response.parse()
            assert_matches_type(object, automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel_execution_action(self, async_client: AsyncGitpod) -> None:
        automation = await async_client.automations.cancel_execution_action()
        assert_matches_type(object, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel_execution_action_with_all_params(self, async_client: AsyncGitpod) -> None:
        automation = await async_client.automations.cancel_execution_action(
            workflow_execution_action_id="a1b2c3d4-5e6f-7890-abcd-ef1234567890",
        )
        assert_matches_type(object, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_cancel_execution_action(self, async_client: AsyncGitpod) -> None:
        response = await async_client.automations.with_raw_response.cancel_execution_action()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = await response.parse()
        assert_matches_type(object, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_cancel_execution_action(self, async_client: AsyncGitpod) -> None:
        async with async_client.automations.with_streaming_response.cancel_execution_action() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = await response.parse()
            assert_matches_type(object, automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_execution_actions(self, async_client: AsyncGitpod) -> None:
        automation = await async_client.automations.list_execution_actions()
        assert_matches_type(AsyncWorkflowExecutionActionsPage[WorkflowExecutionAction], automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_execution_actions_with_all_params(self, async_client: AsyncGitpod) -> None:
        automation = await async_client.automations.list_execution_actions(
            token="token",
            page_size=0,
            filter={
                "phases": ["WORKFLOW_EXECUTION_ACTION_PHASE_UNSPECIFIED"],
                "workflow_execution_action_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "workflow_execution_ids": ["d2c94c27-3b76-4a42-b88c-95a85e392c68"],
                "workflow_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            },
            pagination={
                "token": "token",
                "page_size": 20,
            },
        )
        assert_matches_type(AsyncWorkflowExecutionActionsPage[WorkflowExecutionAction], automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_execution_actions(self, async_client: AsyncGitpod) -> None:
        response = await async_client.automations.with_raw_response.list_execution_actions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = await response.parse()
        assert_matches_type(AsyncWorkflowExecutionActionsPage[WorkflowExecutionAction], automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_execution_actions(self, async_client: AsyncGitpod) -> None:
        async with async_client.automations.with_streaming_response.list_execution_actions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = await response.parse()
            assert_matches_type(
                AsyncWorkflowExecutionActionsPage[WorkflowExecutionAction], automation, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_execution_outputs(self, async_client: AsyncGitpod) -> None:
        automation = await async_client.automations.list_execution_outputs()
        assert_matches_type(AsyncOutputsPage[AutomationListExecutionOutputsResponse], automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_execution_outputs_with_all_params(self, async_client: AsyncGitpod) -> None:
        automation = await async_client.automations.list_execution_outputs(
            token="token",
            page_size=0,
            filter={"workflow_execution_ids": ["d2c94c27-3b76-4a42-b88c-95a85e392c68"]},
            pagination={
                "token": "token",
                "page_size": 50,
            },
        )
        assert_matches_type(AsyncOutputsPage[AutomationListExecutionOutputsResponse], automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_execution_outputs(self, async_client: AsyncGitpod) -> None:
        response = await async_client.automations.with_raw_response.list_execution_outputs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = await response.parse()
        assert_matches_type(AsyncOutputsPage[AutomationListExecutionOutputsResponse], automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_execution_outputs(self, async_client: AsyncGitpod) -> None:
        async with async_client.automations.with_streaming_response.list_execution_outputs() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = await response.parse()
            assert_matches_type(AsyncOutputsPage[AutomationListExecutionOutputsResponse], automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_executions(self, async_client: AsyncGitpod) -> None:
        automation = await async_client.automations.list_executions()
        assert_matches_type(AsyncWorkflowExecutionsPage[WorkflowExecution], automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_executions_with_all_params(self, async_client: AsyncGitpod) -> None:
        automation = await async_client.automations.list_executions(
            token="token",
            page_size=0,
            filter={
                "has_failed_actions": True,
                "search": "search",
                "status_phases": ["WORKFLOW_EXECUTION_PHASE_UNSPECIFIED"],
                "workflow_execution_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                "workflow_ids": ["b0e12f6c-4c67-429d-a4a6-d9838b5da047"],
            },
            pagination={
                "token": "token",
                "page_size": 20,
            },
            sort={
                "field": "field",
                "order": "SORT_ORDER_UNSPECIFIED",
            },
        )
        assert_matches_type(AsyncWorkflowExecutionsPage[WorkflowExecution], automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_executions(self, async_client: AsyncGitpod) -> None:
        response = await async_client.automations.with_raw_response.list_executions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = await response.parse()
        assert_matches_type(AsyncWorkflowExecutionsPage[WorkflowExecution], automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_executions(self, async_client: AsyncGitpod) -> None:
        async with async_client.automations.with_streaming_response.list_executions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = await response.parse()
            assert_matches_type(AsyncWorkflowExecutionsPage[WorkflowExecution], automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_execution(self, async_client: AsyncGitpod) -> None:
        automation = await async_client.automations.retrieve_execution()
        assert_matches_type(AutomationRetrieveExecutionResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_execution_with_all_params(self, async_client: AsyncGitpod) -> None:
        automation = await async_client.automations.retrieve_execution(
            workflow_execution_id="d2c94c27-3b76-4a42-b88c-95a85e392c68",
        )
        assert_matches_type(AutomationRetrieveExecutionResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_execution(self, async_client: AsyncGitpod) -> None:
        response = await async_client.automations.with_raw_response.retrieve_execution()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = await response.parse()
        assert_matches_type(AutomationRetrieveExecutionResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_execution(self, async_client: AsyncGitpod) -> None:
        async with async_client.automations.with_streaming_response.retrieve_execution() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = await response.parse()
            assert_matches_type(AutomationRetrieveExecutionResponse, automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_execution_action(self, async_client: AsyncGitpod) -> None:
        automation = await async_client.automations.retrieve_execution_action()
        assert_matches_type(AutomationRetrieveExecutionActionResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_execution_action_with_all_params(self, async_client: AsyncGitpod) -> None:
        automation = await async_client.automations.retrieve_execution_action(
            workflow_execution_action_id="a1b2c3d4-5e6f-7890-abcd-ef1234567890",
        )
        assert_matches_type(AutomationRetrieveExecutionActionResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_execution_action(self, async_client: AsyncGitpod) -> None:
        response = await async_client.automations.with_raw_response.retrieve_execution_action()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = await response.parse()
        assert_matches_type(AutomationRetrieveExecutionActionResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_execution_action(self, async_client: AsyncGitpod) -> None:
        async with async_client.automations.with_streaming_response.retrieve_execution_action() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = await response.parse()
            assert_matches_type(AutomationRetrieveExecutionActionResponse, automation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_start_execution(self, async_client: AsyncGitpod) -> None:
        automation = await async_client.automations.start_execution()
        assert_matches_type(AutomationStartExecutionResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_start_execution_with_all_params(self, async_client: AsyncGitpod) -> None:
        automation = await async_client.automations.start_execution(
            context_override={
                "agent": {"prompt": "prompt"},
                "from_trigger": {},
                "projects": {"project_ids": ["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"]},
                "repositories": {
                    "environment_class_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "repo_selector": {
                        "repo_search_string": "x",
                        "scm_host": "x",
                    },
                    "repository_urls": {"repo_urls": ["x"]},
                },
            },
            parameters={"foo": "string"},
            workflow_id="b0e12f6c-4c67-429d-a4a6-d9838b5da047",
        )
        assert_matches_type(AutomationStartExecutionResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_start_execution(self, async_client: AsyncGitpod) -> None:
        response = await async_client.automations.with_raw_response.start_execution()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        automation = await response.parse()
        assert_matches_type(AutomationStartExecutionResponse, automation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_start_execution(self, async_client: AsyncGitpod) -> None:
        async with async_client.automations.with_streaming_response.start_execution() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            automation = await response.parse()
            assert_matches_type(AutomationStartExecutionResponse, automation, path=["response"])

        assert cast(Any, response.is_closed) is True
